---
title: Delivery pack
description: Client scaffolding, briefs, status updates, case studies. Confidentiality and IP guardrails.
---

**Version**: `0.2.0` · **Skills**: 7 · **Requires**: `core`

## Chatmodes

| Agent | Role |
|---|---|
| `@delivery-lead` | Owns client outcomes: scope, quality, timelines |
| `@project-manager` | Lightweight planner. WBS, milestones, status. Solo-scale. |

## Prompts

| Command | What it does |
|---|---|
| `/new-client-scaffold` | Scaffold `05-clients/{slug}/` folder + files for a new engagement |
| `/client-brief` | One-page operator brief with health + next-step |
| `/weekly-status` | Weekly client status (email / doc / slack), hours-reconciled |
| `/case-study` | Case study draft from a completed engagement. Consent-gated. |

## Instructions

| Glob | Enforces |
|---|---|
| `05-clients/**` | Confidentiality, scope, deliverable guardrails |

## Typical activation

```
> /instantiate-agent delivery-lead
> /instantiate-agent project-manager
> /schedule delivery-lead weekly day=friday prompt="/weekly-status all clients"
```

[← Back to agents overview](/agents/)
