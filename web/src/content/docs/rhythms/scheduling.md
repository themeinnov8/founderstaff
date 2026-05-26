---
title: Scheduling
description: Every cadence type with realistic examples.
---

import { Aside } from '@astrojs/starlight/components';

## `/schedule` syntax

```
/schedule <agents> <cadence> [day=<value>] [n=<int>] [at=HH:MM] prompt=<slash-command>
```

- `agents` — comma-separated roster IDs (e.g., `chief-of-staff` or `sales-coach,delivery-lead`)
- `cadence` — one of: `daily`, `weekdays`, `weekly`, `monthly`, `every_n_days`, `manual`
- `at` — optional `HH:MM` 24-hour. Informational only (no daemon).
- `prompt` — must start with `/` and reference an installed prompt

## Examples by cadence

### daily

The most common pattern: one driver agent, every morning.

```
/schedule chief-of-staff daily at=09:00 prompt=/next-best-action
```

Computes `next_due`: tomorrow if `last_run == today`, else today.

### weekdays

Skip weekends.

```
/schedule operations-manager weekdays prompt=/inbox-triage
```

### weekly

```
/schedule research-analyst weekly day=monday prompt="/market-research scan competitors"
/schedule delivery-lead weekly day=friday prompt="/weekly-status all clients"
/schedule operations-manager weekly day=saturday prompt=/weekly-review
```

Computes `next_due`: next occurrence of `day` after `last_run`.

### monthly

```
/schedule finance-analyst monthly day=1 prompt="/cashflow-forecast current quarter"
/schedule brand-strategist monthly day=15 prompt="/positioning-statement review"
```

<Aside type="note">
`day` is constrained to 1–28 for portability (skips the edge case of Feb 29–31).
</Aside>

### every_n_days

```
/schedule product-manager every_n_days n=14 prompt="/feature-prioritize backlog"
```

### manual

Rhythm exists but never auto-surfaces. Operator fires explicitly.

```
/schedule sales-coach manual prompt="/discovery-call-prep custom call"
# later:
/run-due --manual sales-coach-manual
```

Useful for "I want this prompt one-click ready but not on a schedule."

## How `/run-due` decides what to surface

The command reads `rhythms.json`, computes `next_due` for each active rhythm using the cadence rules above, and buckets:

| Bucket | Condition |
|---|---|
| `OVERDUE` | `next_due < today` |
| `DUE_TODAY` | `next_due == today` |
| `UPCOMING_7D` | (only with `--include-future`) `today < next_due ≤ today + 7` |

For each due/overdue, the operator answers `y` / `n` / `skip` per rhythm. On `y`:

- **Solo** → switches to `@<agent>` and runs the prompt
- **Council** → delegates to `/council <rhythm-id>`

On success: `last_run` updated to today, entry appended to `09-meta/rhythms/runs.md`.

On failure: `outcome: FAILED — <reason>` logged, `last_run` **not** advanced (so it stays in the queue).

## Edit / disable rhythms

To disable temporarily — set `active: false` in `rhythms.json`. The rhythm is preserved but `/run-due` skips it.

To remove permanently — use `/retire-agent <id>` (which cascades to rhythms containing that agent) or hand-edit `rhythms.json` (the `rhythms.instructions.md` guardrail validates the result).

To change cadence — re-run `/schedule` with the same `id`. Fields update, `last_run` is preserved.
