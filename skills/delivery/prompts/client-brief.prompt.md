---
description: Produce a one-page operator-readable brief for an existing client.
mode: agent
---

# /client-brief

You are `@delivery-lead`. Produce a current-state brief for one client.

## Inputs (ask if missing)

1. **Client slug**.
2. **Use case** — `pre-call` / `weekly-prep` / `onboarding-handoff` / `decision-doc`.

## Process

Read in order:
1. `05-clients/{slug}/README.md`
2. `05-clients/{slug}/_sow.md`
3. `05-clients/{slug}/_plan.md`
4. Most recent 3 entries in `05-clients/{slug}/_status/`
5. Most recent 3 meeting captures in `05-clients/{slug}/meetings/`
6. `_change-requests.md`

## Output

```markdown
# {slug} — Brief — {ISO date}

## At a glance
- Engagement: {type, hours/week, end date}
- Phase: {milestone N of M}
- Health: 🟢/🟡/🔴 — {one-line reason}
- Last contact: {date, channel, who}

## What we owe them right now
- {deliverable} — by {date} — status: {state}

## What they owe us
- {input / decision / payment} — by {date}

## Open change requests
- {CR} — impact: {hours/$} — status: {pending/approved/declined}

## Risks (top 3)
1. {risk} — mitigation: {…}
2. …

## Next step (one)
{What the operator should do next, with time-budget}

## Compliance flags
- {none | flag → reason}
```

Save to `05-clients/{slug}/_status/_brief-{YYYY-MM-DD}.md`.

## Hard rules

- `client-work.instructions.md` applies.
- Health 🟢 requires (a) on-track milestone AND (b) no overdue items in `_change-requests.md` AND (c) last-contact ≤ 7 days. Otherwise 🟡 or 🔴.
- Never inflate "next step" into a list — one action only.
- If compliance flag present, route the brief through `@compliance-reviewer` before sharing.
