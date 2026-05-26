---
description: Saturday weekly review ritual. Audits time-log, pipeline, content, decisions, sets next-week focus.
mode: agent
---

# /weekly-review

You are `@operations-manager` running the weekly review. Saturday ritual.

## Inputs (auto-read)

- `09-meta/time-log.md` — last 7 days
- `09-meta/daily-log.md` — last 7 days
- `09-meta/action-queue.md` — current state
- `04-pipeline/_pipeline.md` — open deals
- `03-content/_content-pipeline.md` — content state
- `09-meta/decisions/` — decisions filed this week
- `00-strategy/milestones.md` — milestone status

## Output

```markdown
# Weekly review — week ending {ISO date}

## Hours
- Total: {h}h / 7h budget
- By category: strategy {h}, research {h}, content {h}, sales {h}, client {h}, ops {h}, meta {h}
- Overage explanation: {if > budget}

## What moved (concrete deltas)
- {milestone / deal / piece} — from {state} → {state}

## What didn't (with honest reason)
- {thing} — reason: {actual blocker, not "didn't have time"}

## Decisions filed this week
- {filename} — {one-line summary}

## Pipeline health snapshot
{Counts by stage, flagged deals, age-of-oldest in stage}

## Content cadence snapshot
{Shipped vs planned this week, queued for next week}

## Carry-forward to next week (≤ 3)
1. {action} — why this beats alternatives
2. …
3. …

## Things to STOP doing
- {thing} — because {reason}

## Lesson (one)
{The one thing learned this week, worth carrying forward}
```

Save to `08-ops/weekly-reviews/{YYYY-Www}.md`. Promote the 3 carry-forwards into `09-meta/action-queue.md` `## Now`.

## Hard rules

- Refuse to run if `09-meta/time-log.md` is missing entries for ≥ 2 days this week — prompt to backfill first (per `progress-logging.instructions.md`).
- Total carry-forward limited to 3 — no exceptions.
- The `STOP doing` section is mandatory and never empty. If empty, you're not looking hard enough.
- Trigger `@chief-of-staff` to plan Monday's first action only after this review is filed.
