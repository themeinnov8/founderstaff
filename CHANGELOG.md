# Changelog

All notable changes to founderstaff documented here. Follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and [SemVer](https://semver.org/).

## [0.3.0-alpha] — 2026-05-24

### Added — Roster + Rhythms subsystem (core pack)

- **`@roster-manager`** chatmode: owns `09-meta/roster.json`, `09-meta/rhythms.json`, `09-meta/rhythms/runs.md`. Distinguishes *installed* skills from *active staff*.
- **`/instantiate-agent`**: activate an installed chatmode onto the roster. Refuses if the chatmode file is missing.
- **`/retire-agent`**: deactivate an agent with explicit `confirm` gate; auto-disables orphaned rhythms.
- **`/schedule`**: create/update a rhythm with closed-set cadences (`daily`, `weekdays`, `weekly+day`, `monthly+day`, `every_n_days`, `manual`). Validates referenced agents and prompts.
- **`/run-due`**: list rhythms whose `next_due ≤ today`, offer per-rhythm execution (operator says `y`/`n` per rhythm). Updates `last_run` and appends to runs log on success.
- **`/council`** (multi-agent session): 5-phase flow — setup → isolated round-1 → cross-read round-2 → coordinator synthesis (decisions + action items + open disagreements) → log. Disagreements are preserved, not papered over.
- **`/roster-dashboard`**: generates `09-meta/dashboard/roster.html` — agent cards with status pills (green/amber/gray), 14-day rhythm timeline, recent runs table, council index. Self-contained, archive-first.
- **`rhythms.instructions.md`** guardrail: schema lock at `schema_version: 1`, no-orphan rules, append-only `runs.md`, atomic JSON writes, ISO dates.

### Changed

- Core pack bumped to `0.3.0` (8 new skills added).
- Platform bumped to `0.3.0-alpha`.

### Design notes

- No daemon, no autonomous fires. Scheduling = the operator runs `/run-due` (or `@chief-of-staff` surfaces it). Matches platform principle: operator-initiated.
- Roster is a *subset* of installed skills. Most users will install a pack but only activate a few of its agents.
- Council coordinator is separate from participating agents — prevents synthesis capture by the loudest voice.

## [0.2.0-alpha] — 2026-05-24

### Added — full agentic roster

- **Pack-first source layout**: skills now live under `skills/{pack}/{type}/` (e.g. `skills/sales/prompts/cold-email.prompt.md`). `sync.py` still flattens to `.github/{chatmodes,prompts,instructions}/` at install time.
- **4 new packs**: `marketing`, `operations`, `finance`, `product`. All `requires_packs: ["core"]`.
- **6 new instructions guardrails**: `progress-logging`, `decision-logging`, `content-voice`, `public-publishing`, `outreach`, `client-work`.
- **11 new chatmodes** (all agentic, explicit `tools:` frontmatter): `hiring-manager` (core), `content-creator`, `blog-publisher`, `linkedin-ghostwriter` (content), `sales-coach`, `linkedin-lead-gen` (sales), `brand-strategist`, `growth-marketer` (marketing), `operations-manager`, `meeting-notetaker` (operations), `delivery-lead`, `project-manager` (delivery), `compliance-reviewer` (compliance), `finance-analyst` (finance), `product-manager` (product).
- **32 new prompts** spanning content (`blog-article`, `linkedin-post`, `linkedin-carousel`, `newsletter-issue`, `youtube-script`, `seo-optimize`, `repurpose-content`), sales (`cold-email`, `linkedin-dm`, `discovery-call-prep`, `discovery-call-recap`, `proposal-sow`, `objection-handler`), marketing (`positioning-statement`, `launch-playbook`, `landing-page`, `ad-copy`), operations (`sop-author`, `meeting-notes`, `inbox-triage`, `weekly-review`), delivery (`new-client-scaffold`, `client-brief`, `weekly-status`, `case-study`), compliance (`compliance-check`), finance (`cashflow-forecast`, `pricing-model`, `invoice-draft`), product (`prd-draft`, `user-story`, `feature-prioritize`), and core (`hire-skill`).
- **MECE-gated hiring flow**: `@hiring-manager` triages every need against the roster; only proposes a new hire when both mutually-exclusive (scope boundary) and collectively-exhaustive (composition gap) checks pass and a pattern of ≥3 occurrences is documented. `/hire-skill` refuses without prior triage log entry and demands literal `confirm forge` before producing a forge-spec.
- README install prerequisites section (Python 3.10+, Git 2.30+, VS Code, Copilot extension) with Windows / macOS / Linux commands.

### Changed

- All existing packs bumped to `0.2.0`. `status: "stub"` and `planned_skills` arrays removed where the skills now exist.
- `skills/index.json` rebuilt against pack-first paths; 67 entries.

### Notes

- `n8n.pack.json` and `video.pack.json` remain `planned` — out of scope for v0.2.
- Skill basenames are globally unique; `sync.py` flattens by basename at install time.

## [0.1.0] — 2026-05-22

### Added — initial extract from outcome-stack workspace

- 4-stage planner: `00-intake` (proposal template), `01-brainstorm` (12 clarifying questions in 4 blocks), `02-plan` (10-section plan template), `03-generate` (seed prompt + 13-batch generation order + validation checklist)
- 5 platform chatmodes: `chief-of-staff`, `dashboard-generator`, `research-analyst`, `red-team`, `agent-forge`
- Research/precision prompts: `/market-research`, `/customer-interview`, `/fact-check`, `/red-team`, `/forge-agent`
- Ops prompts: `/next-best-action`, `/refresh-dashboard`
- Research-quality guardrail instructions (citation, confidence, recency, never-invent)
- Scaffolding skeleton (00-strategy … 09-meta) with per-folder READMEs
- Architecture docs: `architecture.md`, `how-to-write-a-prompt.md`, `self-evolution.md`
- Outcome-stack reference clone pointer in `examples/`

### Known limitations

- Generated agents (`strategist`, `content-creator`, `sales-coach`, `delivery`, `compliance-reviewer`) are produced fresh per venture rather than copied — templates for these are stubbed; full content lands in v0.2.
- No automated validation script yet — validation checklist is manual.
- No webapp/intake form yet — clone-only flow.
