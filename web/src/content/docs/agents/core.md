---
title: Core pack
description: Chief of staff, dashboard, hiring, roster, rhythms. Always installed.
---

The **`core` pack** is required — it provides the platform's own meta-agents: the chief of staff that runs your day, the hiring manager that decides if you need a new skill, the roster manager that owns your active team, and the agent forge that creates new skills safely.

**Version**: `0.3.0` · **Skills**: 18 · **Status**: always installed

## Chatmodes

| Agent | Role |
|---|---|
| `@chief-of-staff` | Founder's-office gatekeeper. Returns ONE next action with reasoning. |
| `@dashboard-generator` | Maintains the live HTML dashboard. Read-mostly, write only to `09-meta/dashboard/`. |
| `@agent-forge` | Meta-agent. Creates new chatmodes/prompts/instructions safely. |
| `@hiring-manager` | MECE-gated triage. Refuses to forge new skills without explicit confirmation. |
| `@roster-manager` | Owns the active roster + rhythms + runs log. |

## Prompts

| Command | What it does |
|---|---|
| `/next-best-action` | "What should I do right now?" — 30/60/90 min variants |
| `/refresh-dashboard` | Regenerate `09-meta/dashboard/index.html` from markdown sources |
| `/forge-agent` | Generate a new chatmode/prompt/instructions file with correct frontmatter |
| `/hire-skill` | Produce a forge-spec — only after MECE triage + operator confirmation |
| `/instantiate-agent` | Add an installed chatmode to the active roster |
| `/retire-agent` | Deactivate an agent (confirmation-gated; disables orphaned rhythms) |
| `/schedule` | Create or update a rhythm (solo or council) |
| `/run-due` | List rhythms due now and offer to invoke each |
| `/council` | Multi-agent collaborative session with synthesis |
| `/roster-dashboard` | Generate `09-meta/dashboard/roster.html` |

## Instructions

| Glob | What it enforces |
|---|---|
| `09-meta/{roster,rhythms}.json,09-meta/rhythms/**` | Schema & edit rules for roster + rhythm files |
| `09-meta/time-log.md,09-meta/daily-log.md,09-meta/action-queue.md` | Progress logging format |
| `09-meta/decisions/**` | ADR-style decision logging |

## Typical activation

```
> /instantiate-agent chief-of-staff
> /instantiate-agent roster-manager
> /instantiate-agent dashboard-generator
> /schedule chief-of-staff daily at=09:00 prompt=/next-best-action
> /schedule dashboard-generator weekly day=monday prompt=/refresh-dashboard
```

[← Back to agents overview](/agents/)
