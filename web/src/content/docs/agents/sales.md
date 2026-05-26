---
title: Sales pack
description: Outreach, discovery, proposals, objection handling. Compliance-gated.
---

**Version**: `0.2.0` · **Skills**: 9 · **Requires**: `core`

## Chatmodes

| Agent | Role |
|---|---|
| `@sales-coach` | Pipeline-conscious sales coach. Reviews deals, preps calls, writes proposals. |
| `@linkedin-lead-gen` | LinkedIn-first prospector. Researches ICP fits, drafts first-touch DMs. |

## Prompts

| Command | What it does |
|---|---|
| `/cold-email` | Personalized cold email draft. Compliance-gated. ≤90 words first-touch. |
| `/linkedin-dm` | LinkedIn connection note or DM. Cadence-aware. Public-detail required. |
| `/discovery-call-prep` | One-page pre-call brief: questions, risks, conversation map |
| `/discovery-call-recap` | Post-call: decisions, next steps, deal-health update, pipeline edit |
| `/proposal-sow` | Proposal / SOW with explicit exclusions, milestones, compliance disclosure |
| `/objection-handler` | Honest responses to common sales objections — never manipulative |

## Instructions

| Glob | Enforces |
|---|---|
| any outbound contact | Hard rules: no fabricated detail, opt-out included, frequency caps |

## Typical activation

```
> /instantiate-agent sales-coach
> /instantiate-agent linkedin-lead-gen
> /schedule sales-coach weekly day=monday prompt="/discovery-call-prep this week's calls"
```

[← Back to agents overview](/agents/)
