#!/usr/bin/env python3
"""
relearn — the one-command interface to founderstaff.

This is a thin wrapper around the upstream `scripts/sync.py`. It:

1. Locates the founderstaff cache (cloning the upstream on first run).
2. Invokes `sync.py` with the same arguments you passed.

Usage:
    python .platform/relearn.py            # sync per manifest
    python .platform/relearn.py --update   # bump pins
    python .platform/relearn.py --status   # show installed
    python .platform/relearn.py --pack n8n # add a pack

Why a wrapper? So you never have to know where founderstaff lives on disk.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

CACHE_ROOT = Path.home() / ".founderstaff" / "cache"
DEFAULT_UPSTREAM = "https://github.com/themeinnov8/founderstaff.git"
DEFAULT_BRANCH = "main"

def _slug(url: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._-]+", "_", url)

def _read_upstream_from_manifest(manifest: Path) -> tuple[str, str]:
    upstream = DEFAULT_UPSTREAM
    branch = DEFAULT_BRANCH
    if manifest.exists():
        for line in manifest.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("upstream:"):
                upstream = line.split(":", 1)[1].strip()
            elif line.startswith("branch:"):
                branch = line.split(":", 1)[1].strip()
    return upstream, branch

def _ensure_repo(upstream: str, branch: str) -> Path:
    CACHE_ROOT.mkdir(parents=True, exist_ok=True)
    repo = CACHE_ROOT / _slug(upstream)
    if not (repo / ".git").exists():
        print(f"[relearn] cloning {upstream}")
        subprocess.run(
            ["git", "clone", "--depth", "1", "--branch", branch, upstream, str(repo)],
            check=True,
        )
    else:
        print(f"[relearn] git pull origin {branch}")
        subprocess.run(["git", "fetch", "origin", branch], cwd=repo, check=True)
        subprocess.run(["git", "checkout", branch], cwd=repo, check=True)
        subprocess.run(["git", "pull", "origin", branch], cwd=repo, check=True)
    return repo

def main() -> int:
    workspace = Path(__file__).resolve().parent.parent
    manifest = workspace / ".platform" / "skills.manifest.yaml"
    if not manifest.exists():
        print(f"[relearn] no manifest at {manifest}", file=sys.stderr)
        return 1
    upstream, branch = _read_upstream_from_manifest(manifest)
    repo = _ensure_repo(upstream, branch)
    sync = repo / "scripts" / "sync.py"
    if not sync.exists():
        print(f"[relearn] sync.py missing in upstream: {sync}", file=sys.stderr)
        return 1
    cmd = [sys.executable, str(sync), *sys.argv[1:]]
    return subprocess.call(cmd, cwd=workspace)

if __name__ == "__main__":
    raise SystemExit(main())
