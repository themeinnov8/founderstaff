# Implementation map

Every file in the repo, why it exists, and where its truth lives.

## Repo root

| Path | Purpose | Owner |
|---|---|---|
| `README.md` | End-user pitch + quickstart | marketing |
| `AGENTS.md` | First-read context for AI agents | agent context |
| `LICENSE` | MIT | legal |
| `.gitignore` | Excludes `generated/`, `*-business-os/`, secrets | infra |
| `version.json` | Platform SemVer | release |
| `CHANGELOG.md` | Release notes | release |
| `CONTRIBUTING.md` | PR guidelines, agent justification | governance |

## `.github/`

| Path | Purpose |
|---|---|
| `copilot-instructions.md` | Auto-loaded by VS Code Copilot when this repo is the workspace |
| `prompts/continue-building.prompt.md` | `/continue-building` — full session resume |

## `spec/` (this folder)

| Path | Purpose |
|---|---|
| `README.md` | Index + read order |
| `requirements.md` | Functional + non-functional contract |
| `design.md` | Architecture, schemas, sync algorithm |
| `implementation.md` | THIS FILE — file map |
| `examples.md` | 6 walkthrough scenarios |
| `testing.md` | Coverage and pending test cases |

## `docs/`

| Path | Purpose |
|---|---|
| `architecture.md` | Decision log + mermaid diagrams |
| `skill-distribution.md` | Authoritative protocol spec |
| `roadmap.md` | Version plan |
| `self-evolution.md` | How new packs ship to existing users |
| `how-to-write-a-prompt.md` | Skill authoring guide |

## `skills/`

| Path | Purpose |
|---|---|
| `index.json` | Registry — every published skill |
| `chatmodes/<id>.chatmode.md` | Persistent personas (invoked via `@<id>`) |
| `prompts/<id>.prompt.md` | One-shot tasks (invoked via `/<id>`) |
| `instructions/<id>.instructions.md` | Background guardrails (auto via `applyTo`) |

Current inventory (v0.1.0): 5 chatmodes, 7 prompts, 1 instructions.

## `packs/`

| Pack | Status | Skills active |
|---|---|---|
| `core` | active | 6 (chief-of-staff, next-best-action, dashboard-generator, refresh-dashboard, agent-forge, forge-agent) |
| `research` | active | 7 (research-analyst, red-team, market-research, customer-interview, fact-check, red-team-prompt, research-quality) |
| `content` | stub | 0 active, 9 planned |
| `sales` | stub | 0 active, 9 planned |
| `delivery` | stub | 0 active, 5 planned |
| `compliance` | stub | 0 active, 7 planned |
| `n8n` | planned (v0.2) | 0 active, 5 planned |
| `video` | planned (v0.3) | 0 active, 6 planned |

## `scripts/sync.py`

The whole engine. ~200 lines, stdlib-only.

| Symbol | Role |
|---|---|
| `Manifest` (dataclass) | In-memory representation of `skills.manifest.yaml` |
| `_load_yaml`, `_mini_yaml`, `_dump_yaml` | YAML I/O (with PyYAML fallback to mini parser) |
| `ensure_upstream(url, branch)` | `git clone` or `git pull origin <branch>` on cache repo |
| `resolve_skills(repo, manifest)` | Transitive closure: packs → skills → deps |
| `substitute(text, tokens)` | Regex `{{TOKEN}}` replacement |
| `apply(workspace, repo, skills, ...)` | The write loop with hash-based local-edit detection |
| `find_workspace()` | Walks up parents from cwd to find `.platform/skills.manifest.yaml` |
| `main(argv)` | Argparse: `--status`, `--dry-run`, `--update`, `--pack` |

**Constants:**
- `DEFAULT_UPSTREAM` = `https://github.com/themeinnov8/founderstaff.git`
- `CACHE_ROOT` = `~/.founderstaff/cache/`
- `TYPE_TO_DIR` = `{chatmode: .github/chatmodes, prompt: .github/prompts, instructions: .github/instructions}`

**Gotchas to know before editing:**
1. **Bytes I/O is intentional.** `dst.write_bytes(new_bytes)` not `write_text` — avoids CRLF translation that breaks hash invariant on Windows.
2. **`_sha256(path)` reads bytes,** so hash compares are OS-agnostic.
3. **Visited set in `resolve_skills.add()`** — prevents cyclic-deps infinite recursion.
4. **Mini YAML parser** is only sufficient for the manifest schema (scalars, scalar lists, dict-of-scalars). Don't introduce nested structures unless you upgrade to PyYAML-required.
5. **`find_workspace()`** walks parents — so users can run sync from any subfolder.
6. **`prev.get("hash_after_substitution")`** may be `None` on first install — guarded with `if recorded and ...`.

## `scaffolding/.platform/`

What gets copied into a new generated OS.

| Path | Purpose |
|---|---|
| `skills.manifest.yaml` | Default manifest (packs: core, research) |
| `platform.config.json.template` | Token template — user copies to `platform.config.json` and fills in |
| `relearn.py` | Thin wrapper — clones/pulls upstream, runs sync.py |
| `README.md` | Per-workspace quickstart |

**`relearn.py` flow:**
1. Reads upstream from `<workspace>/.platform/skills.manifest.yaml`.
2. Clones or `git pull origin <branch>` on `~/.founderstaff/cache/<slug>/`.
3. `subprocess.call([python, cache/scripts/sync.py, *argv[1:]], cwd=workspace)`.

## `planner/`

4-stage idea→OS pipeline. Self-contained; not touched by sync engine.

| Stage | Folder | Output |
|---|---|---|
| 00 | `00-intake/proposal-template.md` | Filled proposal (10 sections) |
| 01 | `01-brainstorm/clarifying-questions.md` | Answered questions (12 Qs, 4 blocks) |
| 02 | `02-plan/plan-template.md` | Plan with custom-agent + generation params |
| 03 | `03-generate/{seed-prompt, generation-order, validation-checklist}.md` | Generation kit |

## Git state

- Repo initialized as `main` on 2026-05-22.
- Author: `theme.innova8@gmail.com`.
- No remote yet — user adds later.

## Cache directory (runtime)

- Path: `~/.founderstaff/cache/<slug>/` where `slug = re.sub(r'[^a-zA-Z0-9._-]+', '_', upstream_url)`.
- Created on first sync. Persists across syncs.
- Safe to delete; sync will re-clone.

## Style conventions

- 4-space indent, Python.
- Type hints on public functions.
- One file per dataclass when nontrivial; inline for trivial.
- Markdown files use H1 for title, H2 for top sections, table-heavy.
- No emojis unless user asked.
- File references in markdown use relative paths.
