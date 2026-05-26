# Generation order

Batches are dependency-ordered. Later batches reference files created in earlier batches.

| Batch | Name | Files (relative to generated repo root) | Depends on |
|-------|------|-----------------------------------------|------------|
| B1 | Repo skeleton | `.gitignore`, `.gitattributes`, `.env.example`, `README.md`, `AGENTS.md`, `LICENSE`, full folder tree (00–09) | plan §1, §10 |
| B2 | Strategy core | `00-strategy/plan.md`, `milestones.md`, `do-not-contact.md`, `decisions-log.md`, `phases.md` | plan §1, §4, §5, §6 |
| B3 | Guardrails | `.github/copilot-instructions.md`, `.github/instructions/{firewall,content-voice,outreach,client-work,public-publishing,progress-logging,research-quality}.instructions.md` + custom from §9 | B2, plan §9 |
| B4 | Standard chatmodes | `.github/chatmodes/{strategist,content-creator,sales-coach,delivery,compliance-reviewer,chief-of-staff,dashboard-generator,research-analyst,red-team,agent-forge}.chatmode.md` | B3 |
| B5 | Custom chatmodes | one file per §7 chatmode entry, via `/forge-agent` | B4, plan §7 |
| B6 | Standard prompts | full prompt library in `.github/prompts/` | B3 |
| B7 | Custom prompts | one file per §7 prompt entry, via `/forge-agent` | B6, plan §7 |
| B8 | Offerings | `03-offerings/{slug}/README.md` per §3 SKU; Tier C/D scaffolded LOCKED | B2 |
| B9 | Pipeline + clients + content | `02-content/calendar.md`, `04-pipeline/_pipeline.md`, `05-clients/_template/`, `02-content/pillars.md` | B2, B8 |
| B10 | Meta | `09-meta/dashboard/{index.html,sources.md}`, `09-meta/{action-queue,time-log,compliance-log,progress-log,parking-lot}.md` | B3, B9 |
| B11 | Plan visualization | `plan.html` at repo root, populated from §1–§9 | B2, B8, B10 |
| B12 | Operating docs | `OPERATING_MANUAL.md`, `RUNBOOK_BOOTSTRAP_NEW_OS.md` (tailored), `08-automation/README.md` | all prior |
| B13 | Validation | run `validation-checklist.md`, write report to `09-meta/generation-report.md` | all prior |

## Why this order

- Strategy + guardrails before any agent/prompt — guardrails are referenced by every generated agent.
- Standard agents before custom — custom agents are forged with awareness of which standard agents already exist.
- Offerings before pipeline — pipeline templates reference SKU IDs.
- Dashboard last (before validation) — needs all source files to exist or it shows "not yet tracked".
- Operating docs last — they reference everything by path.

## Hard rules

- Never skip a batch.
- If a batch fails (validation per-batch), stop. Do not proceed to next batch.
- If a custom agent in §7 requires domain knowledge the operator hasn't provided, the `agent-forge` for that batch will ask — do not block the batch on it; defer that single file to a follow-up and continue.
