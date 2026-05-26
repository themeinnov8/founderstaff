# Examples

Six walkthroughs covering the common and edge-case flows.

## Example 1 — Fresh install in a new workspace

**Goal:** turn an empty folder into a founderstaff-managed workspace.

```bash
# 1. Make a workspace folder
mkdir my-business-os && cd my-business-os
git init

# 2. Drop in the scaffolding
mkdir .platform
cp <founderstaff-repo>/scaffolding/.platform/skills.manifest.yaml .platform/
cp <founderstaff-repo>/scaffolding/.platform/platform.config.json.template .platform/platform.config.json
cp <founderstaff-repo>/scaffolding/.platform/relearn.py .platform/
cp <founderstaff-repo>/scaffolding/.platform/README.md .platform/

# 3. Fill in your tokens
notepad .platform/platform.config.json
# set BRAND, OPERATOR, HOME_CURRENCY, etc.

# 4. Run relearn
python .platform/relearn.py
```

**Expected output:**
```
[relearn] cloning https://github.com/themeinnov8/founderstaff.git
[founderstaff] syncing 13 skills into C:\...\my-business-os
  install: chief-of-staff v0.1.0 -> .github\chatmodes\chief-of-staff.chatmode.md
  install: next-best-action v0.1.0 -> .github\prompts\next-best-action.prompt.md
  ... (11 more) ...
[founderstaff] lockfile updated
[founderstaff] done.
```

**What's now in the workspace:**
```
my-business-os/
├── .platform/
│   ├── skills.manifest.yaml
│   ├── platform.config.json     ← your tokens
│   ├── skills.lock.json         ← auto-written
│   ├── relearn.py
│   └── README.md
└── .github/
    ├── chatmodes/   (5 files)
    ├── prompts/     (7 files)
    └── instructions/ (1 file)
```

Open VS Code; Copilot auto-discovers everything in `.github/`. Type `@chief-of-staff` to invoke.

---

## Example 2 — Add a new pack to an existing workspace

**Scenario:** You started with `core + research`. Now you want `content`.

```bash
cd my-business-os
python .platform/relearn.py --pack content
```

What happens:
1. `--pack content` appends `content` to the manifest's `packs:` list.
2. Manifest saved.
3. Sync runs, installs any new skills the `content` pack brings (today: zero, because `content` is a stub in v0.1).

In v0.2 once `content` ships skills, the same command will install them with no further action.

---

## Example 3 — Pull the latest from upstream

**Scenario:** founderstaff shipped a new version of `chief-of-staff` (v0.1.0 → v0.2.0). You want it.

```bash
cd my-business-os
python .platform/relearn.py
```

What happens:
1. `git pull origin main` on cache repo. Fetches new `skills/index.json` + new `chief-of-staff.chatmode.md`.
2. Resolver sees `chief-of-staff` now at v0.2.0.
3. Sync recomputes new hash. Compared to current on-disk hash → different. Compared to recorded lockfile hash → matches (you didn't edit it).
4. Prints `update: chief-of-staff v0.2.0 -> .github/chatmodes/chief-of-staff.chatmode.md`.
5. Lockfile updated with new version + new hash.

---

## Example 4 — Local edit protection

**Scenario:** You edited `.github/chatmodes/chief-of-staff.chatmode.md` to add custom rules. You forgot. Then you ran `relearn`.

```bash
python .platform/relearn.py
```

Output:
```
[founderstaff] syncing 13 skills...
  ! local edit detected at .github\chatmodes\chief-of-staff.chatmode.md — skipping (rename or remove to overwrite)
  ... other skills sync normally ...
```

Your edits are preserved. To accept the upstream version, either:
- Delete the file then re-run sync, or
- Rename the file to keep your customizations as a separate skill.

**Mechanism:** `cur_hash != recorded_hash` AND `cur_hash != new_hash` → file was modified after last sync. See [design.md](design.md) §3.

---

## Example 5 — Disable a skill you don't want

**Scenario:** `research` pack pulled in `red-team` but you find it noisy.

Edit `.platform/skills.manifest.yaml`:
```yaml
disabled_skills:
  - red-team
  - red-team-prompt
```

Run sync:
```bash
python .platform/relearn.py
```

Output:
```
[founderstaff] syncing 11 skills...
  remove: red-team (no longer in manifest) -> .github\chatmodes\red-team.chatmode.md
  remove: red-team-prompt (no longer in manifest) -> .github\prompts\red-team.prompt.md
```

The two files are removed from `.github/`, lockfile updated.

---

## Example 6 — Author a new skill (contributor flow)

**Scenario:** You want to add a `weekly-review` prompt to the `core` pack.

1. Author the file:
   ```bash
   # In founderstaff repo (not the user workspace)
   cd founderstaff
   ```

   Create `skills/prompts/weekly-review.prompt.md`:
   ```markdown
   ---
   description: One-page review of last week's outputs vs plan.
   mode: agent
   ---
   # Weekly review for {{BRAND}}

   ## Steps
   1. Read 09-meta/action-queue.md
   2. List wins, blockers, lessons
   3. Propose the top 3 actions for next week
   ```

2. Register in `skills/index.json`:
   ```json
   {
     "id": "weekly-review",
     "type": "prompt",
     "path": "skills/prompts/weekly-review.prompt.md",
     "version": "0.1.0",
     "summary": "One-page review of last week vs plan",
     "tags": ["ops", "core"],
     "depends_on": [],
     "requires_tokens": ["BRAND"],
     "min_platform_version": "0.1.0"
   }
   ```

3. Add to `packs/core.pack.json` and bump pack version:
   ```json
   {
     "id": "core",
     "version": "0.2.0",
     "skills": [
       "chief-of-staff", "next-best-action", "dashboard-generator",
       "refresh-dashboard", "agent-forge", "forge-agent",
       "weekly-review"
     ]
   }
   ```

4. Bump platform version in `version.json` (minor — additive change).

5. Add a `CHANGELOG.md` entry.

6. Smoke-test:
   ```bash
   # In a test workspace
   python <path-to-founderstaff>/scripts/sync.py --status
   # Should show 14 resolved skills.
   ```

7. PR / push.

Users get it next time they run `python .platform/relearn.py`.
