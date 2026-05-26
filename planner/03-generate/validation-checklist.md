# Validation checklist — post-generation

Run after Batch 13 (or invoke `/validate-os` if that prompt exists). Each item is PASS / FAIL. Any FAIL blocks declaring the OS ready.

## Structural

- [ ] All 10 top-level folders exist (`00-strategy` … `09-meta`)
- [ ] No raw `{{TOKEN}}` placeholders in any generated file (`grep -r "{{" .` returns empty)
- [ ] `README.md` and `AGENTS.md` exist at repo root
- [ ] `.gitignore` excludes secrets, client private folders, finance invoices

## Compliance

- [ ] `.github/instructions/copilot-instructions.md` references the firewall instructions
- [ ] Firewall instructions file matches §4 strictness level
- [ ] `do-not-contact.md` seeded with §4 entries
- [ ] Anonymity rules consistent across all generated content templates
- [ ] No mention of `operator_handle` real name if §4 says anonymity required

## Agents

- [ ] All 10 standard chatmodes exist
- [ ] Every §7 custom chatmode exists with a valid frontmatter `tools:` array
- [ ] No agent has write access to scopes outside its declared boundary
- [ ] `agent-forge` chatmode is present (needed for future extensions)

## Prompts

- [ ] Standard prompts library present (count ≥ 25)
- [ ] Every §7 custom prompt exists with valid frontmatter
- [ ] Every prompt has a `description:` in frontmatter
- [ ] `/refresh-dashboard`, `/next-best-action`, `/compliance-check` all callable

## Plan + dashboard

- [ ] `plan.html` renders without console errors when opened in browser
- [ ] All §1, §3, §5, §6 values appear in `plan.html`
- [ ] `09-meta/dashboard/index.html` renders, shows "not yet tracked" for empty widgets (not blank)
- [ ] Dashboard source registry (`sources.md`) lists every widget

## Operating docs

- [ ] `OPERATING_MANUAL.md` opens with "Start here each day" section
- [ ] `RUNBOOK_BOOTSTRAP_NEW_OS.md` references the embedded `09-meta/template-os/` so the new OS can spawn its own clones if needed
- [ ] Cheatsheet of all commands exists somewhere reachable

## Health gates (red-team this)

- [ ] §5 hours × §5 timeline ≥ realistic to reach §6 endpoint goal (run a quick sanity check)
- [ ] Tier C/D offerings explicitly marked LOCKED with unlock criteria
- [ ] Time-budget guardrail card present in roadmap section of `plan.html`
- [ ] First milestone (M01) has target date within 90 days of generation date

## Run once

- [ ] Invoke `/refresh-dashboard` once — produces archived `history/{ts}.html`
- [ ] Invoke `/next-best-action` once — returns a non-empty action
- [ ] Invoke `/compliance-check` on `plan.html` — passes

## Final

- [ ] `git init` complete, initial commit made
- [ ] Operator has been shown: dashboard URL, OPERATING_MANUAL link, `/next-best-action` command
- [ ] Generation report written to `09-meta/generation-report.md` with timestamp and parameters used

When all PASS: hand off to operator with a 3-line summary:
1. What was generated (file count, custom agents)
2. Where to start (dashboard + manual links)
3. Next milestone + suggested first action
