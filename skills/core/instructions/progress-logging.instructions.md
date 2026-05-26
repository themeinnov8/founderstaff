---
description: How to log time, decisions, and progress so the dashboard and chief-of-staff have honest inputs.
applyTo: "09-meta/**"
---

# progress-logging

The dashboard, `/next-best-action`, and weekly review only work if `09-meta/**` is honest. These rules apply to every write under `09-meta/`.

## Time-log (`09-meta/time-log.md`)

- One row per work session. Columns: `date | start | end | minutes | category | tags | note`.
- Categories are fixed: `strategy`, `research`, `content`, `sales`, `client:{slug}`, `ops`, `meta`.
- No rounding up. If unsure between two buckets, pick the smaller.
- Never backfill more than 48h. If older sessions missed, log as `meta` with note `estimated`.

## Daily log (`09-meta/daily-log.md`)

- Append-only. Newest entry at top.
- Each entry: ISO date heading, 3 bullets max — `did`, `learned`, `next`.
- No emotional content here; that goes in a private journal outside the workspace.

## Decision log (`09-meta/decisions/`)

- One file per decision. Filename: `YYYY-MM-DD-{slug}.md`.
- Required sections: Context, Options considered, Decision, Reasoning, Reversibility, Revisit-on.
- Decisions that cost > 4h to reverse must list the reversibility cost explicitly.

## Action queue (`09-meta/action-queue.md`)

- Three sections only: `## Now` (≤ 3 items), `## Next` (≤ 7), `## Later` (uncapped).
- An item leaves `Now` only by being done or by an explicit decision logged in `decisions/`.
- The chief-of-staff is the only agent allowed to promote items between sections.

## Anti-patterns

- Inventing "in-progress" entries to look productive — banned.
- Logging future intentions as past work — banned.
- Deleting old daily-log entries — banned; correct via strikethrough + addendum.
