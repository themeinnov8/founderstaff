# Design

## 1. Component map

```
┌───────────────────────────────────────────────────────────────┐
│ founderstaff repo (upstream, on GitHub or local)              │
│   ├── skills/index.json       ← registry                      │
│   ├── skills/{chatmodes,prompts,instructions}/*.md            │
│   ├── packs/*.pack.json       ← curated bundles               │
│   ├── scripts/sync.py         ← the resolver/installer        │
│   ├── scaffolding/.platform/  ← per-workspace templates       │
│   └── planner/                ← idea → OS pipeline            │
└───────────────────────────────────────────────────────────────┘
                              │
              git pull origin <branch>
                              ▼
┌───────────────────────────────────────────────────────────────┐
│ ~/.founderstaff/cache/<slug>/   (a clone of upstream)         │
└───────────────────────────────────────────────────────────────┘
                              │
                  python sync.py reads
                              ▼
┌───────────────────────────────────────────────────────────────┐
│ user workspace                                                │
│   ├── .platform/skills.manifest.yaml ← what user wants        │
│   ├── .platform/platform.config.json ← tokens                 │
│   ├── .platform/skills.lock.json     ← what's installed       │
│   └── .github/{chatmodes,prompts,instructions}/*.md ← synced  │
└───────────────────────────────────────────────────────────────┘
                              │
                Copilot auto-discovers .github/
                              ▼
                  user invokes @chief-of-staff
                          / /next-best-action
```

## 2. Data structures

### 2.1 `skills/index.json`
```json
{
  "schema_version": 1,
  "platform_version": "0.1.0",
  "generated_at": "ISO-8601",
  "skills": [
    {
      "id": "chief-of-staff",                                // required, kebab-case
      "type": "chatmode",                                    // chatmode|prompt|instructions
      "path": "skills/chatmodes/chief-of-staff.chatmode.md", // relative to repo root
      "version": "0.1.0",                                    // SemVer
      "summary": "...",                                      // one line
      "tags": ["ops", "core"],
      "depends_on": ["next-best-action"],                    // transitive close at sync
      "requires_tokens": ["BRAND"],
      "min_platform_version": "0.1.0",
      "aliases": [],                                         // optional, for renames
      "deprecated": false                                    // optional
    }
  ]
}
```

### 2.2 `packs/<id>.pack.json`
```json
{
  "id": "research",
  "name": "Research & precision",
  "summary": "...",
  "version": "0.1.0",
  "skills": ["research-analyst", "market-research", ...],
  "planned_skills": [],                  // for stub packs
  "requires_packs": ["core"],
  "min_platform_version": "0.1.0",
  "always_required": false,              // true for `core`
  "status": "active"                     // active|stub|planned
}
```

### 2.3 `.platform/skills.manifest.yaml` (workspace-side)
```yaml
upstream: https://github.com/themeinnov8/founderstaff.git
branch: main
platform_version: latest

packs:
  - core
  - research

extra_skills: []
disabled_skills: []
tokens_file: platform.config.json
```

### 2.4 `.platform/platform.config.json`
```json
{
  "tokens": {
    "BRAND": "outcome stack",
    "OPERATOR": "Theme Innov8",
    "HOME_CURRENCY": "INR",
    ...
  }
}
```

### 2.5 `.platform/skills.lock.json` (auto-written)
```json
{
  "upstream": "...",
  "branch": "main",
  "installed": {
    "chief-of-staff": {
      "version": "0.1.0",
      "path": ".github/chatmodes/chief-of-staff.chatmode.md",
      "hash_after_substitution": "<sha256 of post-token bytes>"
    }
  }
}
```

## 3. Sync algorithm (authoritative)

```
function sync(workspace, args):
    manifest      = load(workspace/.platform/skills.manifest.yaml)
    tokens        = load(workspace/.platform/platform.config.json).tokens
    lockfile      = load_or_empty(workspace/.platform/skills.lock.json)

    repo          = ensure_upstream(manifest.upstream, manifest.branch)
                    # → git clone or git fetch + checkout + pull

    index         = load(repo/skills/index.json)
    packs         = [load(repo/packs/<p>.pack.json) for p in manifest.packs]

    wanted        = transitive_closure(
                       packs.skills + manifest.extra_skills,
                       index.skills[*].depends_on,
                       exclude=manifest.disabled_skills
                    )

    for skill in wanted:
        src       = repo / skill.path
        new_text  = substitute_tokens(read(src), tokens)
        new_bytes = new_text.encode('utf-8')
        new_hash  = sha256(new_bytes)
        dst       = workspace / TYPE_TO_DIR[skill.type] / src.name

        if dst.exists():
            cur_hash = sha256(read_bytes(dst))
            recorded = lockfile.installed[skill.id]?.hash_after_substitution
            if recorded and recorded != cur_hash and cur_hash != new_hash:
                warn("local edit"); continue
            if cur_hash == new_hash:
                record_unchanged(); continue

        write_bytes(dst, new_bytes)
        record(skill.id → {version, path, new_hash})

    for sid in lockfile.installed - wanted.ids:
        old_path = workspace / lockfile.installed[sid].path
        if old_path.exists(): old_path.unlink()
        drop(sid)

    save(workspace/.platform/skills.lock.json, lockfile)
```

## 4. Key invariants

| # | Invariant | Guard |
|---|---|---|
| I1 | Local edits never overwritten | hash compare before write |
| I2 | Idempotent | bytes I/O + post-substitution hash matches |
| I3 | Acyclic resolution | memoized visited set in `add()` |
| I4 | Skill ID unique across registry | enforced at PR review (no automated check yet) |
| I5 | Every `skills.path` resolves | enforced at PR review |
| I6 | Pack only references known skill IDs | sync prints warning, doesn't crash |
| I7 | Lockfile == truth of "installed" | filesystem state is consulted only for hash compare |

## 5. Versioning

| Layer | File | Bump when |
|---|---|---|
| Platform | `version.json` | sync protocol breaks (major); new pack category (minor); fixes (patch) |
| Pack | `packs/<id>.pack.json#version` | new skill (minor); reorder (patch) |
| Skill | `skills/index.json#skills[].version` | breaking interface (major); behavior shift (minor); copy tweak (patch) |

## 6. Token system

- Pattern: `{{[A-Z0-9_]+}}` (uppercase, digits, underscores only).
- Resolved at **sync time**, not runtime — the synced file in `.github/` contains the user's literal brand name.
- Missing tokens are left literal and surfaced as warnings (not errors).
- Reserved tokens — see `requirements.md` §F4.4 and `spec/examples.md` §3.

## 7. Failure modes

| Mode | Behavior |
|---|---|
| No network | Cache reuse, warn |
| Cache repo corrupted | User deletes `~/.founderstaff/cache/`, retries |
| Manifest YAML malformed | Mini-parser returns partial dict; missing keys default |
| Skill path missing | Print `! missing source file`, continue |
| Pack id missing | Print `! warning: pack not found`, continue |
| Token unresolved | Left literal in output, no error |
| Local edit | Skip, warn |
| Cyclic deps | Visited set prevents infinite recursion |
