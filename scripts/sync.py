#!/usr/bin/env python3
"""
founderstaff sync engine.

Pulls the latest skills from the founderstaff upstream repo and applies them
into the current workspace's `.github/` (so VS Code Copilot picks them up
natively) based on `.platform/skills.manifest.yaml`.

This script is what powers the `relearn` command. It is intentionally
dependency-light: stdlib only, except optional PyYAML if the manifest is YAML.
If PyYAML is missing it falls back to a tiny YAML subset parser.

Usage
-----
    python sync.py                 # sync to versions pinned in manifest
    python sync.py --update        # bump manifest to upstream latest, then sync
    python sync.py --dry-run       # show diff plan, no writes
    python sync.py --pack research # add a pack to the manifest, then sync
    python sync.py --status        # show what is installed and what is stale

Design contract: see `docs/skill-distribution.md` in the founderstaff repo.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

# ---------- constants ----------------------------------------------------------

DEFAULT_UPSTREAM = "https://github.com/themeinnov8/founderstaff.git"
DEFAULT_BRANCH = "main"
CACHE_ROOT = Path.home() / ".founderstaff" / "cache"
PLATFORM_DIR = ".platform"
MANIFEST_NAME = "skills.manifest.yaml"
LOCK_NAME = "skills.lock.json"
CONFIG_NAME = "platform.config.json"
TARGET_GITHUB = ".github"

# ---------- tiny YAML reader (for manifests with no nested complexity) ---------

def _load_yaml(path: Path) -> dict[str, Any]:
    try:
        import yaml  # type: ignore
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except ImportError:
        return _mini_yaml(path.read_text(encoding="utf-8"))

def _mini_yaml(text: str) -> dict[str, Any]:
    """Subset YAML: top-level scalars, lists of scalars, dict-of-scalars.
    Sufficient for our manifest schema."""
    out: dict[str, Any] = {}
    current_key: str | None = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - "):
            if current_key is None:
                continue
            out.setdefault(current_key, []).append(line[4:].strip().strip("'\""))
            continue
        if ":" in line and not line.startswith(" "):
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            if val == "":
                current_key = key
                out[key] = []
            else:
                current_key = None
                out[key] = _coerce(val.strip("'\""))
    return out

def _coerce(v: str) -> Any:
    if v.lower() in ("true", "false"):
        return v.lower() == "true"
    if v.isdigit():
        return int(v)
    return v

def _dump_yaml(data: dict[str, Any]) -> str:
    """Round-trip back to our subset format."""
    lines: list[str] = []
    for k, v in data.items():
        if isinstance(v, list):
            lines.append(f"{k}:")
            for item in v:
                lines.append(f"  - {item}")
        elif isinstance(v, bool):
            lines.append(f"{k}: {str(v).lower()}")
        else:
            lines.append(f"{k}: {v}")
    return "\n".join(lines) + "\n"

# ---------- data classes ------------------------------------------------------

@dataclass
class Manifest:
    upstream: str = DEFAULT_UPSTREAM
    branch: str = DEFAULT_BRANCH
    platform_version: str = "latest"
    packs: list[str] = field(default_factory=lambda: ["core"])
    extra_skills: list[str] = field(default_factory=list)
    disabled_skills: list[str] = field(default_factory=list)
    tokens_file: str = "platform.config.json"

    @classmethod
    def load(cls, path: Path) -> "Manifest":
        d = _load_yaml(path)
        return cls(
            upstream=d.get("upstream", DEFAULT_UPSTREAM),
            branch=d.get("branch", DEFAULT_BRANCH),
            platform_version=d.get("platform_version", "latest"),
            packs=list(d.get("packs", ["core"])),
            extra_skills=list(d.get("extra_skills", [])),
            disabled_skills=list(d.get("disabled_skills", [])),
            tokens_file=d.get("tokens_file", "platform.config.json"),
        )

    def save(self, path: Path) -> None:
        path.write_text(_dump_yaml(self.__dict__), encoding="utf-8")

# ---------- git helpers --------------------------------------------------------

def _slug(url: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._-]+", "_", url)

def _run(cmd: list[str], cwd: Path | None = None, check: bool = True) -> str:
    res = subprocess.run(cmd, cwd=str(cwd) if cwd else None,
                         capture_output=True, text=True)
    if check and res.returncode != 0:
        raise RuntimeError(f"command failed: {' '.join(cmd)}\n{res.stderr}")
    return res.stdout.strip()

def ensure_upstream(upstream: str, branch: str) -> Path:
    """Clone or `git pull origin <branch>` the upstream into the cache dir."""
    CACHE_ROOT.mkdir(parents=True, exist_ok=True)
    repo_dir = CACHE_ROOT / _slug(upstream)
    if not (repo_dir / ".git").exists():
        print(f"[founderstaff] cloning {upstream} -> {repo_dir}")
        _run(["git", "clone", "--depth", "1", "--branch", branch, upstream, str(repo_dir)])
    else:
        print(f"[founderstaff] git pull origin {branch} in {repo_dir}")
        _run(["git", "fetch", "origin", branch], cwd=repo_dir)
        _run(["git", "checkout", branch], cwd=repo_dir)
        _run(["git", "pull", "origin", branch], cwd=repo_dir)
    return repo_dir

# ---------- core sync logic ----------------------------------------------------

def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def _load_json(p: Path) -> Any:
    return json.loads(p.read_text(encoding="utf-8"))

def resolve_skills(repo: Path, manifest: Manifest) -> list[dict[str, Any]]:
    index = _load_json(repo / "skills" / "index.json")
    by_id = {s["id"]: s for s in index["skills"]}
    wanted: dict[str, dict[str, Any]] = {}

    def add(skill_id: str, reason: str) -> None:
        if skill_id in manifest.disabled_skills:
            print(f"  - skip {skill_id} (disabled in manifest)")
            return
        if skill_id not in by_id:
            print(f"  ! warning: skill '{skill_id}' ({reason}) not in upstream index", file=sys.stderr)
            return
        if skill_id in wanted:
            return
        wanted[skill_id] = by_id[skill_id]
        for dep in by_id[skill_id].get("depends_on", []):
            add(dep, f"dependency of {skill_id}")

    for pack_id in manifest.packs:
        pack_path = repo / "packs" / f"{pack_id}.pack.json"
        if not pack_path.exists():
            print(f"  ! warning: pack '{pack_id}' not found in upstream", file=sys.stderr)
            continue
        pack = _load_json(pack_path)
        for skill_id in pack.get("skills", []):
            add(skill_id, f"pack:{pack_id}")
    for sid in manifest.extra_skills:
        add(sid, "extra_skills")
    return list(wanted.values())

# ---------- token substitution ------------------------------------------------

TOKEN_RE = re.compile(r"\{\{([A-Z0-9_]+)\}\}")

def substitute(content: str, tokens: dict[str, str]) -> str:
    def repl(m: re.Match[str]) -> str:
        key = m.group(1)
        return tokens.get(key, m.group(0))
    return TOKEN_RE.sub(repl, content)

# ---------- write into workspace ----------------------------------------------

TYPE_TO_DIR = {
    "chatmode":     Path(".github") / "chatmodes",
    "prompt":       Path(".github") / "prompts",
    "instructions": Path(".github") / "instructions",
}

def apply(workspace: Path, repo: Path, skills: list[dict[str, Any]],
          tokens: dict[str, str], dry_run: bool, lockfile: dict[str, Any]) -> None:
    installed = lockfile.setdefault("installed", {})
    seen: set[str] = set()
    for s in skills:
        src = repo / s["path"]
        if not src.exists():
            print(f"  ! missing source file: {src}", file=sys.stderr)
            continue
        dst_dir = workspace / TYPE_TO_DIR[s["type"]]
        dst = dst_dir / src.name
        seen.add(str(dst.relative_to(workspace)))
        new_text = substitute(src.read_text(encoding="utf-8"), tokens)
        # Write bytes (no newline translation) so on-disk hash == recorded hash on every OS.
        new_bytes = new_text.encode("utf-8")
        new_hash = hashlib.sha256(new_bytes).hexdigest()

        prev = installed.get(s["id"])
        if dst.exists():
            cur_hash = _sha256(dst)
            recorded = prev.get("hash_after_substitution") if prev else None
            if recorded and recorded != cur_hash and cur_hash != new_hash:
                print(f"  ! local edit detected at {dst.relative_to(workspace)} — skipping (rename or remove to overwrite)")
                continue
            if cur_hash == new_hash:
                installed[s["id"]] = {"version": s["version"], "path": str(dst.relative_to(workspace)),
                                       "hash_after_substitution": new_hash}
                continue

        action = "update" if dst.exists() else "install"
        print(f"  {action}: {s['id']} v{s['version']} -> {dst.relative_to(workspace)}")
        if not dry_run:
            dst_dir.mkdir(parents=True, exist_ok=True)
            dst.write_bytes(new_bytes)
            installed[s["id"]] = {"version": s["version"], "path": str(dst.relative_to(workspace)),
                                   "hash_after_substitution": new_hash}

    # prune skills no longer wanted
    for sid in list(installed.keys()):
        if sid not in {s["id"] for s in skills}:
            old = installed[sid]
            old_path = workspace / old["path"]
            print(f"  remove: {sid} (no longer in manifest) -> {old['path']}")
            if not dry_run and old_path.exists():
                old_path.unlink()
            del installed[sid]

# ---------- entry point --------------------------------------------------------

def find_workspace() -> Path:
    cwd = Path.cwd()
    for p in [cwd, *cwd.parents]:
        if (p / PLATFORM_DIR / MANIFEST_NAME).exists():
            return p
    raise SystemExit(f"could not find {PLATFORM_DIR}/{MANIFEST_NAME} in cwd or parents. "
                     f"run `python -m founderstaff init` first (or copy scaffolding/.platform/).")

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="founderstaff-sync")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--update", action="store_true",
                    help="bump pinned versions in manifest to upstream latest")
    ap.add_argument("--pack", help="add a pack to the manifest then sync")
    ap.add_argument("--status", action="store_true")
    args = ap.parse_args(argv)

    workspace = find_workspace()
    platform_dir = workspace / PLATFORM_DIR
    manifest_path = platform_dir / MANIFEST_NAME
    lock_path = platform_dir / LOCK_NAME
    config_path = platform_dir / CONFIG_NAME

    manifest = Manifest.load(manifest_path)
    if args.pack and args.pack not in manifest.packs:
        manifest.packs.append(args.pack)
        manifest.save(manifest_path)
        print(f"[founderstaff] added pack '{args.pack}' to manifest")

    tokens = _load_json(config_path).get("tokens", {}) if config_path.exists() else {}

    repo = ensure_upstream(manifest.upstream, manifest.branch)
    skills = resolve_skills(repo, manifest)

    if args.status:
        print(f"[founderstaff] upstream: {manifest.upstream}@{manifest.branch}")
        print(f"[founderstaff] packs:    {', '.join(manifest.packs)}")
        print(f"[founderstaff] resolved {len(skills)} skills:")
        for s in skills:
            print(f"  - {s['id']:25s} v{s['version']:8s}  [{s['type']}]")
        return 0

    lockfile: dict[str, Any] = _load_json(lock_path) if lock_path.exists() else {}
    lockfile["upstream"] = manifest.upstream
    lockfile["branch"] = manifest.branch

    print(f"[founderstaff] syncing {len(skills)} skills into {workspace}")
    apply(workspace, repo, skills, tokens, args.dry_run, lockfile)

    if not args.dry_run:
        lock_path.write_text(json.dumps(lockfile, indent=2), encoding="utf-8")
        print("[founderstaff] lockfile updated")
    print("[founderstaff] done.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
