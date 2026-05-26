---
title: Rhythms overview
description: Schedule agents (solo or council) to run on a cadence. Operator-initiated, never autonomous.
---

import { Aside } from '@astrojs/starlight/components';

A **rhythm** is a scheduled invocation. One or more agents, a cadence, and a prompt to run. The system computes when each rhythm is due; the operator fires it.

<Aside type="caution" title="No daemon, no cron">
founderstaff does not run agents autonomously. "Schedule" means **the system knows what's due**. The operator runs `/run-due` (typically each morning) to see the queue and decide which rhythms to fire. This is intentional — autonomous fires would violate the platform's "operator owns the loop" principle.
</Aside>

## Two kinds

| Kind | Agents | Purpose |
|---|---|---|
| **Solo** | 1 | Recurring single-agent task (daily NBA, weekly research scan, monthly cashflow) |
| **Council** | 2–6 | Cross-functional decision (quarterly strategy, pipeline review, launch readiness) |

## Cadences (closed set)

| Cadence | Extra args | Example |
|---|---|---|
| `daily` | — | Every day |
| `weekdays` | — | Mon–Fri |
| `weekly` | `day: monday..sunday` | Every Monday |
| `monthly` | `day: 1..28` | 1st of each month |
| `every_n_days` | `n: <int>` | Every 14 days |
| `manual` | — | Only fires when operator runs `/run-due --manual <id>` |

## File contracts

Roster and rhythms live in two files in `09-meta/`:

```json
// 09-meta/roster.json
{
  "schema_version": 1,
  "agents": [
    { "id": "chief-of-staff", "type": "chatmode", "activated": "2026-05-24", "role": "Daily NBA driver" }
  ]
}
```

```json
// 09-meta/rhythms.json
{
  "schema_version": 1,
  "rhythms": [
    {
      "id": "daily-nba",
      "agents": ["chief-of-staff"],
      "kind": "solo",
      "cadence": "daily",
      "at": "09:00",
      "prompt": "/next-best-action",
      "last_run": "2026-05-23",
      "active": true
    }
  ]
}
```

Append-only log in `09-meta/rhythms/runs.md`. Every rhythm execution adds an entry. Never edited retroactively.

## Workflow

1. **Activate agents** with `/instantiate-agent`.
2. **Schedule** with `/schedule`.
3. **Check what's due** with `/run-due` (operator decides per-rhythm).
4. **Visualize** with `/roster-dashboard`.

## Deep dives

- [Scheduling cadences](/rhythms/scheduling/) — every cadence with examples
- [Councils (multi-agent)](/rhythms/councils/) — full 5-phase flow
