# business-os-planner (template)

This folder is the **bootstrapping factory**. At the maturity gate (see Tier D · D1 in `plan.html`), it gets extracted to its own public repo `business-os-planner`. Anyone — including you, on a future project — clones that repo to plan and generate a new Business OS.

## Three-stage flow

```
clone planner → 00-intake → 01-brainstorm → 02-plan → 03-generate → new OS repo
                proposal     clarifying     approved    seed         {brand}-business-os
                  .md         questions     plan.md     prompt        (separate repo)
```

| Stage | Owner | Output | Gate to next stage |
|------|-------|--------|--------------------|
| 00-intake | Prospect (alone) | `00-intake/proposal.md` | Filled & submitted |
| 01-brainstorm | Operator + prospect + `strategist` chatmode | `01-brainstorm/transcript.md` + answered `clarifying-questions.md` | Both parties sign off |
| 02-plan | Operator (with `agent-forge` if custom agents needed) | `02-plan/plan.md` + `02-plan/plan.html` | Prospect approves in writing |
| 03-generate | `agent-forge` + scripted prompts | New repo at `../{their-brand}-business-os/` | Validation checklist passes |

## Folder layout

```
09-meta/template-os/
├── README.md                       (this file)
├── 00-intake/
│   ├── proposal-template.md        copy & rename to proposal.md
│   └── README.md
├── 01-brainstorm/
│   ├── clarifying-questions.md     12 questions, asked in order
│   ├── transcript-template.md
│   └── README.md
├── 02-plan/
│   ├── plan-template.md            structured plan output
│   ├── plan-html-template.html     visual plan (mermaid + chart.js)
│   └── README.md
├── 03-generate/
│   ├── seed-prompt.md              ← paste this into a fresh agent
│   ├── generation-order.md         dependency-ordered file creation
│   ├── validation-checklist.md     post-generation healthcheck
│   └── README.md
└── extension/
    ├── adding-agents.md            how the generated OS adds new agents later
    └── adding-skills.md            same for skills/prompts/instructions
```

## Why this exists

- One-off planning conversations leak knowledge. Forcing structure into a repo means every plan is comparable, auditable, and improvable.
- Same template = same DNA. New OSes inherit guardrails (compliance, time-budget discipline, citation rules) by default.
- Public repo = lead magnet. The planner itself becomes the top-of-funnel for D1 Idea-to-Plan Bootstrapping Sprint.

## When NOT to use this

- For a one-page brainstorm — overkill. Use a note in `01-strategy/` instead.
- For internal pivots of an existing OS — use `/red-team` + `/log-decision`, don't re-spin.
- For micro-product launches (a new Topmate SKU) — handle inside the existing OS.

## Maintenance

This folder versions semantically. Breaking changes to the seed prompt or clarifying questions = major bump. Anyone running an older planner pins to a version tag.

Current version: `v0.1.0-dev`
