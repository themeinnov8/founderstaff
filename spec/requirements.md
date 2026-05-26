# Requirements

## 1. Product statement

**founderstaff** is a Copilot-native platform that:

- (R1) Generates a custom business operating system folder structure from a business idea, via a 4-stage planner.
- (R2) Maintains a versioned registry of AI **skills** (chatmodes, prompts, instructions) curated into **packs** (core, research, content, sales, delivery, compliance, n8n, video, …).
- (R3) Lets any user, in any workspace, run **one command** (`python .platform/relearn.py`) to pull the latest skills they've opted into and install them under `.github/` so VS Code Copilot picks them up natively.
- (R4) Lets the platform itself grow new skill categories over time; existing users opt in by editing their manifest and re-running `relearn`.

## 2. Functional requirements

### F1 — Planner
The repo must ship a 4-stage planner under `planner/`:
- `00-intake/` — proposal template (10 sections)
- `01-brainstorm/` — clarifying questions (4 blocks)
- `02-plan/` — plan template with custom-agent and generation-params sections
- `03-generate/` — seed prompt, generation order, validation checklist

### F2 — Skill registry
`skills/index.json` lists every published skill with:
- `id` (kebab-case, unique)
- `type` (`chatmode` | `prompt` | `instructions`)
- `path` (relative to repo root)
- `version` (SemVer)
- `summary` (one line)
- `tags`, `depends_on`, `requires_tokens`, `min_platform_version`
- optional `aliases`, `deprecated`

### F3 — Packs
`packs/<id>.pack.json` declares a curated bundle:
- `id`, `name`, `summary`, `version`
- `skills` (list of skill IDs — active membership)
- `planned_skills` (list, for stub packs)
- `requires_packs`, `min_platform_version`, `always_required`, `status`

### F4 — Sync engine
`scripts/sync.py` must:
- (F4.1) Resolve the workspace manifest by walking up parents from `cwd` looking for `.platform/skills.manifest.yaml`.
- (F4.2) `git pull origin <branch>` against a cache clone at `~/.founderstaff/cache/<slug>/`.
- (F4.3) Compute the transitive closure of skills from `packs[]` + `extra_skills[]` minus `disabled_skills[]` using `depends_on`.
- (F4.4) Apply token substitution (`{{TOKEN_NAME}}` regex) using values from `.platform/platform.config.json`.
- (F4.5) Write resolved skills as **bytes** (no newline translation) into `.github/{chatmodes,prompts,instructions}/`.
- (F4.6) Detect local edits via SHA-256 comparison against `.platform/skills.lock.json`; skip overwriting and warn.
- (F4.7) Prune skills no longer wanted (and not locally edited).
- (F4.8) Persist `.platform/skills.lock.json` with `{upstream, branch, installed: {<id>: {version, path, hash_after_substitution}}}`.
- (F4.9) Support flags: `--status`, `--dry-run`, `--update`, `--pack <id>`.

### F5 — Relearn wrapper
`scaffolding/.platform/relearn.py` must:
- Read upstream + branch from local manifest.
- Clone-or-pull the cache repo.
- Re-invoke `<cache>/scripts/sync.py` with passthrough argv.

### F6 — Scaffolding
`scaffolding/.platform/` provides templates: `skills.manifest.yaml`, `platform.config.json.template`, `relearn.py`, `README.md`. These are what get copied into a new generated OS.

### F7 — Agent context
`AGENTS.md`, `.github/copilot-instructions.md`, and this `spec/` folder must give any AI agent enough context to resume work without external knowledge.

## 3. Non-functional requirements

| ID | Requirement |
|---|---|
| N1 | **Stdlib-only** Python for `scripts/sync.py` and `scaffolding/.platform/relearn.py`. Optional `import yaml` with mini-parser fallback. |
| N2 | **No PowerShell** anywhere. Python is the cross-platform contract. |
| N3 | **Cross-platform** — must work on Windows, macOS, Linux. Bytes I/O for newline-safety. |
| N4 | **Idempotent** — running sync twice produces zero file changes when state is clean. |
| N5 | **Safe** — never overwrite a user-edited skill file. Hash mismatch triggers skip + warning. |
| N6 | **Offline-tolerant** — if `git pull` fails (no network), reuse cached repo and continue with a warning. |
| N7 | **Observable** — print one line per action (`install`, `update`, `skip`, `remove`) so users can audit. |
| N8 | **No global install required** — `python sync.py` works without `pip install founderstaff`. |
| N9 | **Author identity** for platform commits: `theme.innova8@gmail.com`. |

## 4. Out of scope (v0.1)

- Telemetry.
- Private upstreams / auth.
- Version pinning per skill.
- Bisect / rollback.
- Web UI / pack browser.
- Diff preview before apply (deferred to v0.3).

## 5. Success criteria for v0.1

- ✅ Smoke test passes: fresh workspace + `python sync.py` produces 13 install lines; second run produces zero.
- ✅ `--status` lists resolved skills.
- ✅ `--dry-run` prints plan without writing.
- ✅ Manually edited `.github/chatmodes/chief-of-staff.chatmode.md` is preserved across a sync.
- ✅ Removing `research` from manifest then syncing prunes those 6 skills.
- ✅ All paths in `skills/index.json` resolve to existing files.
