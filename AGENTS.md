# Agent context for founderstaff

> **Read this file first.** It's the same context for Claude, GPT, and any future coding agent working on this repo.
> Last full audit: 2026-05-22.

## What is founderstaff?

founderstaff is a **platform that turns an idea into a working business operating system** inside VS Code, powered by GitHub Copilot's native agent customization (`.github/chatmodes/`, `.github/prompts/`, `.github/instructions/`).

A "business OS" = a folder structure + a roster of AI co-workers (chatmodes), one-shot tools (prompts), and guardrails (instructions) tailored to one venture. The generated OS becomes the founder's daily workspace.

founderstaff itself is the **upstream registry + sync engine + planner + scaffolding** that produces those OSes and keeps them up to date.

The flagship clone (private, separate repo) is `outcome-stack` — the operator's own AI-consulting OS.

## Three repos to keep straight

| Repo | Purpose | Public? |
|------|---------|---------|
| `founderstaff/` (this) | Platform: skills registry, sync engine, planner, docs | Will be public |
| `outcome-stack/` (a.k.a. `vcc`) | Operator's personal OS — generated from founderstaff | Private |
| `<client>-os/` | Per-client generated OSes | Private to client |

## Core promise

> One command — `python .platform/relearn.py` — pulls the latest skills and packs from upstream and applies them to the workspace. Skills evolve independently; users opt in by pack.

## Mental model: package manager for AI skills

| npm/pip concept | founderstaff equivalent |
|---|---|
| package | **skill** (a single `.chatmode.md`, `.prompt.md`, or `.instructions.md`) |
| meta-package | **pack** (curated bundle of skills, e.g. `core`, `research`, `n8n`) |
| `package.json` | `.platform/skills.manifest.yaml` (what the workspace wants) |
| `package-lock.json` | `.platform/skills.lock.json` (what's installed + hashes) |
| registry | `skills/index.json` in this repo |
| `npm install` | `python .platform/relearn.py` |
| `npm publish` | PR to this repo adding files under `skills/` + entries in `index.json` |

## Repository map

```
founderstaff/
├── README.md              ← marketing-style overview
├── AGENTS.md              ← THIS FILE — agent context
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE                ← MIT
├── version.json           ← platform SemVer
├── docs/
│   ├── architecture.md         ← decisions and diagrams
│   ├── skill-distribution.md   ← package-manager design spec (authoritative)
│   ├── roadmap.md              ← what's planned, what's done
│   ├── how-to-write-a-prompt.md
│   └── self-evolution.md       ← how the platform grows itself
├── skills/
│   ├── index.json              ← REGISTRY (every published skill)
│   ├── chatmodes/*.chatmode.md
│   ├── prompts/*.prompt.md
│   └── instructions/*.instructions.md
├── packs/
│   ├── core.pack.json          ← always required
│   ├── research.pack.json
│   ├── content.pack.json       ← stub (v0.2)
│   ├── sales.pack.json         ← stub (v0.2)
│   ├── delivery.pack.json      ← stub (v0.2)
│   ├── compliance.pack.json    ← stub (v0.2)
│   ├── n8n.pack.json           ← planned (v0.2)
│   └── video.pack.json         ← planned (v0.3)
├── planner/                    ← the 4-stage idea→OS pipeline
│   ├── README.md
│   ├── 00-intake/proposal-template.md
│   ├── 01-brainstorm/clarifying-questions.md
│   ├── 02-plan/plan-template.md
│   └── 03-generate/{seed-prompt,generation-order,validation-checklist}.md
├── scripts/
│   └── sync.py                 ← THE SYNC ENGINE — Python, stdlib only
└── scaffolding/                ← what gets copied into a new generated OS
    └── .platform/
        ├── skills.manifest.yaml
        ├── platform.config.json.template
        ├── relearn.py
        └── README.md
```

## Versioning rules

- **Platform** SemVer in `version.json`. Bump minor when adding new pack categories; bump major when breaking the sync protocol.
- **Each pack** has its own version (`packs/*.pack.json#version`). Bump minor when adding a skill, patch when reordering.
- **Each skill** has its own version (`skills/index.json#skills[].version`). Bump patch for prompt tweaks, minor for behavior shift, major for breaking interface.

## How to add a new skill (mechanical checklist)

1. Drop the file under `skills/{chatmodes,prompts,instructions}/<id>.<type>.md` with correct YAML frontmatter.
2. Append entry to `skills/index.json` with `id`, `type`, `path`, `version`, `summary`, `tags`, `depends_on`, `requires_tokens`.
3. (Optional) Add `id` to one or more `packs/*.pack.json#skills` arrays.
4. Bump pack version (`packs/*.pack.json#version`) — minor for additive.
5. Add a `CHANGELOG.md` entry.
6. Run smoke test: `python scripts/sync.py --status` in a test workspace.

## How to add a new pack category (e.g. n8n)

1. Author the constituent skills under `skills/`.
2. Add them to `skills/index.json` and bump platform version (`version.json`) minor.
3. Move corresponding planned-skill IDs out of `planned_skills` and into `skills` array of `packs/<id>.pack.json`.
4. Flip status from `"planned"` / `"stub"` to active. Set proper `version`.
5. CHANGELOG entry. Users opt in via `python .platform/relearn.py --pack <id>`.

## Hard constraints (do not violate)

- **Stdlib only** in `scripts/sync.py` and `scaffolding/.platform/relearn.py`. Optional `import yaml` falls back to mini-parser.
- **No PowerShell scripts.** Python only for any cross-platform tooling.
- **Git transport** via `git pull origin <branch>` against a cache clone in `~/.founderstaff/cache/<slug>/`.
- **Token substitution** is regex-only (`{{TOKEN_NAME}}`), applied to skill file contents at sync time.
- **Local edits are sacred** — if a synced file's hash differs from the lockfile's recorded post-substitution hash, the sync engine must skip it and print a warning, never overwrite.
- **Lockfile is authoritative** for "what is installed" — do not infer from filesystem state.
- **Skills auto-discovered by Copilot** must land in `<workspace>/.github/{chatmodes,prompts,instructions}/`. Do not move them.
- **Author identity** for commits: `theme.innova8@gmail.com`.

## Open questions (call these out before deciding)

1. Should the platform support **private upstreams** (auth tokens for `git pull`)? Today assumes public HTTPS.
2. Should `skills/index.json` be generated from frontmatter rather than hand-authored? (Currently hand-authored — drift risk.)
3. How do we **bisect** if a new skill version breaks a downstream OS? Today there's no automatic rollback.
4. Telemetry: do we ask users to report which packs they use, to prioritize the roadmap?
5. Should `packs/*.pack.json` allow `version_pin` per skill, not just "latest from index"?

See `docs/roadmap.md` for current sprint. See `docs/architecture.md` for decision records.

## When in doubt

- For design questions → read `docs/skill-distribution.md` first; it's the spec.
- For execution → tiny, reversible commits; smoke-test `sync.py` after every change.
- For naming → match existing patterns (`research-quality.instructions.md`, not `quality-research.md`).
- For new behavior → propose in CHANGELOG's `[Unreleased]` section before coding.
