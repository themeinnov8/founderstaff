# GitHub Copilot instructions for founderstaff

You are working on **founderstaff**, a platform that scaffolds Copilot-driven business OSes.

**First action in any non-trivial session: read [AGENTS.md](../AGENTS.md) for full context.** It contains the mental model, repo map, versioning rules, hard constraints, and open questions.

## Quick rules

- Stdlib-only Python for `scripts/` and `scaffolding/.platform/relearn.py`.
- No PowerShell scripts anywhere.
- All cross-machine transport uses `git pull origin <branch>` against a cache clone (see [scripts/sync.py](../scripts/sync.py)).
- Token substitution is regex `{{TOKEN}}` only.
- Never overwrite a workspace file whose hash differs from the lockfile.
- Local-only paths (`generated/`, `*-business-os/`, `*-planning/`) are git-ignored — never commit them.

## When adding a skill

Follow the checklist in [AGENTS.md](../AGENTS.md#how-to-add-a-new-skill-mechanical-checklist). Update `skills/index.json`, the relevant pack, and `CHANGELOG.md` together.

## When adding a pack category

Follow [AGENTS.md](../AGENTS.md#how-to-add-a-new-pack-category-eg-n8n). Author skills first, flip pack from `stub`/`planned` last.

## Design source of truth

[docs/skill-distribution.md](../docs/skill-distribution.md) is the authoritative spec. If code and that doc disagree, the doc wins until explicitly updated.

## Style

- Markdown lists over paragraphs.
- File links must be relative repo paths.
- No emojis unless the user asked.
- Bump versions in the same commit that changes behavior.
