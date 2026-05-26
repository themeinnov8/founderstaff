---
description: One-shot prompt to resume building founderstaff from a fresh session. Pairs with AGENTS.md.
mode: agent
---
# Continue building founderstaff

You are picking up work on **founderstaff** — a platform that turns a business idea into a Copilot-native business OS via a package-manager pattern.

## Step 1 — Load context

Read these in order. Do not skip:

1. [AGENTS.md](../../AGENTS.md) — mental model, repo map, hard constraints
2. [docs/architecture.md](../../docs/architecture.md) — decisions and diagrams
3. [docs/skill-distribution.md](../../docs/skill-distribution.md) — authoritative spec
4. [docs/roadmap.md](../../docs/roadmap.md) — what's pending

Then `list_dir` on `skills/`, `packs/`, `scripts/`, `scaffolding/`, `planner/` to confirm the on-disk state matches the docs.

## Step 2 — Ask before you build

Before authoring any new skill or pack, ask the operator:

- Which pack from `docs/roadmap.md#v020` should we tackle first?
- Any new tokens needed? (would extend `platform.config.json.template`)
- Any change to the sync protocol? (would bump platform major)

## Step 3 — Build small, smoke-test often

After every change, run:

```bash
python scripts/sync.py --status
```

(in a throwaway test workspace with a `.platform/` folder).

Verify:
- No `! warning` lines
- Resolved skill count matches your manifest
- File paths under `skills/` all exist

## Step 4 — Ship discipline

Every PR-worthy change touches **at least three files**:

1. The skill or code itself
2. `skills/index.json` or relevant pack
3. `CHANGELOG.md` (under `[Unreleased]` until release)

If a change touches the sync protocol or scaffolding, also update `docs/architecture.md` and bump `version.json`.

## Step 5 — When the operator says "ship"

```bash
# bump version.json + CHANGELOG to a real version
git add .
git commit -m "Release vX.Y.Z: <one-liner>"
git tag vX.Y.Z
# operator pushes
```

## Hard rules (repeat)

- Stdlib-only Python.
- No PowerShell scripts.
- Never overwrite user-edited files (hash check in sync.py is the gate).
- Token regex stays `{{[A-Z0-9_]+}}`.
- Author identity: `theme.innova8@gmail.com`.

Begin with Step 1.
