# Skill distribution — the founderstaff package manager

> **Status:** design spec for v0.1. This document is the contract between the platform and every generated OS. Breaking changes require a major version bump.

## TL;DR

founderstaff distributes skills (chatmodes, prompts, instructions) to generated OSes the way npm distributes packages: a manifest the user edits, a lockfile that's auto-managed, and a sync command that reconciles them.

```
edit .platform/skills.manifest.yaml  →  run ./scripts/relearn.ps1  →  new skills available in Copilot
```

## Why not git submodules

- Submodules need users to understand git internals; founderstaff users include non-engineers.
- Copilot discovers agent files at `<workspace>/.github/{chatmodes,prompts,instructions}/`. Submodules nest content under a subdirectory — Copilot wouldn't find them without symlinks (Windows-hostile).
- Submodules conflate "what's available upstream" with "what's installed locally." A package manager separates these.

## Roles

| Role | Lives in | Authored by | Purpose |
|---|---|---|---|
| **Platform manifest** | `founderstaff/skills/index.json` | platform maintainer | machine-readable catalog of ALL available skills |
| **Pack** | `founderstaff/packs/{id}.pack.json` | platform maintainer | curated bundle of skills for a category |
| **Sync engine** | `founderstaff/scripts/sync.ps1` (+ `.sh`) | platform maintainer | reads manifests, copies skills, manages lockfile |
| **User manifest** | `{generated-os}/.platform/skills.manifest.yaml` | OS owner | declares desired packs + version pin |
| **Lockfile** | `{generated-os}/.platform/skills.lock.json` | sync engine | records exact installed versions + sha256 |
| **Platform config** | `{generated-os}/.platform/platform.config.json` | OS owner | upstream URL, brand tokens, policy flags |
| **Relearn wrapper** | `{generated-os}/scripts/relearn.ps1` | scaffolding | thin wrapper → calls platform sync |

## Schema: `skills/index.json`

```json
{
  "schema_version": 1,
  "platform_version": "0.1.0",
  "generated_at": "2026-05-22T10:30:00Z",
  "skills": [
    {
      "id": "chief-of-staff",
      "type": "chatmode",
      "path": "skills/chatmodes/chief-of-staff.chatmode.md",
      "version": "0.1.0",
      "summary": "Founder's-office gatekeeper. Recommends ONE next action.",
      "tags": ["ops", "prioritization"],
      "depends_on": [],
      "requires_tokens": ["BRAND"],
      "min_platform_version": "0.1.0",
      "aliases": [],
      "deprecated": false
    }
  ]
}
```

Field semantics:

- `id`: globally unique within founderstaff. Used as filename stem.
- `type`: one of `chatmode | prompt | instructions`.
- `path`: relative to repo root in founderstaff.
- `version`: SemVer per skill. Bumps independently of platform version.
- `depends_on`: array of skill IDs that must also be installed if this is selected.
- `requires_tokens`: token names that must exist in `platform.config.json`. Sync fails if missing.
- `aliases`: previous IDs (handles renames; old lockfiles still resolve).
- `deprecated`: still installable but emits a warning.

## Schema: `packs/{id}.pack.json`

```json
{
  "id": "research",
  "name": "Research & precision",
  "summary": "Citation-disciplined research, fact-checking, customer interviews, red-teaming.",
  "version": "0.1.0",
  "skills": [
    "research-analyst",
    "red-team",
    "market-research",
    "customer-interview",
    "fact-check",
    "research-quality"
  ],
  "requires_packs": ["core"],
  "min_platform_version": "0.1.0"
}
```

`core` is the always-installed pack. It contains: `chief-of-staff`, `next-best-action`, `dashboard-generator`, `refresh-dashboard`, `agent-forge`, `forge-agent`, `compliance-reviewer`, `progress-logging` (instructions), `firewall` (instructions).

## Schema: `.platform/skills.manifest.yaml`

```yaml
upstream: https://github.com/<you>/founderstaff.git
branch: main
pin_platform_version: ">=0.1.0,<0.2.0"

packs:
  - core
  - research
  - content
  - sales

extra_skills: []
exclude_skills: []

local_edits_policy: prompt   # prompt | overwrite | skip

token_overrides: {}          # per-skill token overrides (rare)
```

## Schema: `.platform/skills.lock.json`

```json
{
  "schema_version": 1,
  "synced_at": "2026-05-22T10:35:14Z",
  "platform_version": "0.1.0",
  "upstream_sha": "abc1234...",
  "manifest_sha256": "...",
  "installed": {
    "chief-of-staff": {
      "type": "chatmode",
      "version": "0.1.0",
      "installed_path": ".github/chatmodes/chief-of-staff.chatmode.md",
      "source_sha256": "...",
      "installed_sha256": "...",
      "tokens_resolved": {"BRAND": "outcome-stack"}
    }
  }
}
```

`source_sha256` vs `installed_sha256`:

- On sync, both are written equal.
- On next sync: if `installed_sha256` of the local file differs from the recorded `installed_sha256`, the file was edited locally. Apply `local_edits_policy`.

## Schema: `.platform/platform.config.json`

```json
{
  "schema_version": 1,
  "tokens": {
    "BRAND": "outcome-stack",
    "BRAND_SHORT": "OS",
    "BRAND_DOMAIN": "outcomestack.io",
    "BRAND_HANDLE": "@outcomestack",
    "OPERATOR": "{{ANONYMOUS}}",
    "EMPLOYER_NAME": "Microsoft",
    "EMPLOYER_FIREWALL_STRICTNESS": "max",
    "HOME_CURRENCY": "INR",
    "HOURS_PER_WEEK": 7
  },
  "platform_cache_dir": "~/.founderstaff/cache",
  "auto_reload_vscode": false
}
```

## The sync algorithm (in detail)

```
INPUT: workspace root containing .platform/

1. LOAD manifests
   a. Read .platform/skills.manifest.yaml
   b. Read .platform/skills.lock.json (if exists; else empty)
   c. Read .platform/platform.config.json
   d. Validate schemas; abort on any error

2. FETCH upstream
   a. If platform_cache_dir/{upstream-slug} exists → git fetch + checkout pin_platform_version
   b. Else → git clone --depth=1 --branch={branch} {upstream} into cache dir
   c. Record upstream_sha = git rev-parse HEAD

3. RESOLVE skills to install
   a. Read upstream skills/index.json + all packs/*.pack.json
   b. For each pack in manifest.packs:
      - Verify pack.requires_packs are also selected (auto-add core)
      - Verify pack.min_platform_version ≤ upstream platform_version
      - Add pack.skills to selected set
   c. Add manifest.extra_skills
   d. Remove manifest.exclude_skills
   e. For each selected skill, recursively add depends_on
   f. Resolve aliases (old IDs in lockfile → new IDs in index)

4. VALIDATE tokens
   a. For each selected skill with requires_tokens:
      - Verify each token exists in platform.config.json
      - Abort with clear error listing missing tokens

5. PLAN changes
   a. ADD list = selected - installed
   b. REMOVE list = installed - selected (never auto-delete; just list)
   c. UPDATE list = installed ∩ selected where lock.version < upstream.version
   d. For each in UPDATE: compute current installed_sha256, compare to lock.installed_sha256
      - Equal → clean update (proceed)
      - Different → user edited locally → apply local_edits_policy

6. APPLY (or report in dry-run mode)
   a. For each ADD: read source file → token-substitute → write to .github/{type}/
   b. For each clean UPDATE: same as ADD
   c. For each dirty UPDATE: based on policy
      - prompt: ask user [overwrite | keep local | show diff]
      - overwrite: write upstream version
      - skip: leave local, log warning
   d. For each REMOVE: prompt user; default keep

7. UPDATE lockfile
   a. Compute new source_sha256 and installed_sha256 per installed skill
   b. Write .platform/skills.lock.json atomically (write to .tmp then rename)

8. REPORT
   a. Print summary: "+3 added, ~1 updated, -0 removed, 1 skipped (local edits)"
   b. List each skill with action taken
   c. If any chatmodes/prompts changed: suggest "Reload VS Code window (Ctrl+Shift+P → Developer: Reload Window)"
```

## Token substitution

Skills can use `{{TOKEN_NAME}}` markers. During sync:

1. Sync reads the source file as text.
2. Replaces `{{TOKEN_NAME}}` with `tokens[TOKEN_NAME]` from `platform.config.json`.
3. If any unresolved `{{...}}` remains AND that token name isn't in skill's `requires_tokens` → emit warning but continue.
4. If a `requires_tokens` value isn't in config → sync aborts before any write.

Reserved token: `{{ANONYMOUS}}` — never substituted; signals "use anonymized form throughout."

## Versioning

| Component | Versioned in | Bump on |
|---|---|---|
| Platform | `version.json` top-level + `skills/index.json#platform_version` | adding/removing packs, schema changes |
| Each skill | per-entry `version` field | content changes to that skill file |
| Each pack | per-pack `version` field | adding/removing skills from the pack |
| Sync engine | `scripts/sync.ps1` header comment | algorithm changes |

User pins platform compat range via `pin_platform_version`. Skills auto-update within compat (latest patch+minor of each skill). Operator can pin a specific skill version with `extra_skills: [{ id: "chief-of-staff", version: "=0.1.0" }]`.

## Adding a new skill (maintainer)

1. Write `skills/{type}/{name}.{type}.md` following existing conventions.
2. Add entry to `skills/index.json` with version `0.1.0`.
3. Decide pack: add ID to `packs/{pack}.pack.json#skills`, OR create a new pack.
4. Bump `skills/index.json#platform_version` (patch usually).
5. Update `CHANGELOG.md`.
6. Commit + tag `v0.1.1` (or whatever).

## Adding a new pack (e.g., n8n, video)

1. Author the skill files under `skills/`.
2. Add each to `skills/index.json`.
3. Create `packs/{new-pack}.pack.json`.
4. Update `README.md` pack table.
5. Update `CHANGELOG.md`.
6. Commit + tag.

Generated OSes then opt in by adding the pack name to their `skills.manifest.yaml`.

## Self-evolution: contributing back

1. Generated OS user invokes `/forge-agent` → new skill in `.github/`.
2. If broadly useful, operator opens PR against founderstaff:
   - Drops the skill file in `skills/{type}/`
   - Adds entry to `skills/index.json`
   - Updates a pack (or creates one)
   - Adds a `docs/proposals/{date}-{name}.md` justification (see `CONTRIBUTING.md`)
3. Maintainer reviews using the existing CONTRIBUTING checklist.
4. Merge → tag → other OSes pull on next `./scripts/relearn.ps1`.

## Open questions for v0.2

- **Skill marketplace** — third-party packs (not just official ones). Probably via separate `extra_upstreams` array in manifest.
- **Skill signing** — sha256 isn't crypto-secure for "did the maintainer endorse this?" Could add GPG sig later.
- **Network-less sync** — currently requires git access on first run. Future: published tarballs on GitHub Releases for air-gapped install.
- **Cross-platform sync engine** — v0.1 has PowerShell + bash; v0.2 considers a single Node.js script for one source of truth.

## Failure modes

| Failure | Outcome |
|---|---|
| Manifest YAML malformed | Sync refuses to start; clear parse error |
| Upstream unreachable & cache missing | Sync aborts with "no upstream, no cache — `git clone` once first" |
| Upstream unreachable & cache present | Sync proceeds using cache, warns "stale by N days" |
| Required token missing | Sync aborts before any file write, lists missing tokens |
| Skill removed upstream still referenced | Sync warns "skill X was removed upstream; keeping local copy as orphan" |
| Pack version conflict (manifest pin vs upstream) | Sync aborts with version range mismatch |
| Sync interrupted mid-write | Lockfile written atomically; partial `.github/` writes are detected on next sync by sha256 mismatch and resolved per policy |
| Two skills with same filename (different packs) | Disallowed at platform level: `index.json` validation forbids duplicate IDs |

## Security considerations

- Sync executes no upstream code, only copies markdown.
- Token substitution is plain string replace, no template engine eval.
- Cache dir uses user home; never writes outside workspace or cache.
- Sync refuses to write outside `.github/` of the workspace it's run in.
- `local_edits_policy: overwrite` requires explicit configuration (default is `prompt`).
