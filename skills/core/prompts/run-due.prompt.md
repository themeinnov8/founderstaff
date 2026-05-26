---
description: Show which rhythms are due now (or by a given date) and offer to invoke each.
mode: agent
---

# /run-due

Surface scheduled rhythms whose `next_due` is on or before the current date. Operator decides which to fire.

## Inputs

- `as_of` — optional ISO date. Defaults to today.
- `--include-future` — optional flag to also list rhythms due within the next 7 days (preview mode).
- `--manual {rhythm-id}` — optional. Force-runs a specific rhythm regardless of due date.

## Process

1. **Read `09-meta/rhythms.json` and `09-meta/roster.json`.** If either missing → instruct operator to run `/instantiate-agent` and `/schedule` first.
2. **For each rhythm where `active: true`**, compute `next_due` (algorithm in `/schedule`).
3. **Bucket**:
   - `OVERDUE` — `next_due < as_of`
   - `DUE_TODAY` — `next_due == as_of`
   - `UPCOMING_7D` — `next_due` in (as_of, as_of+7d] (only if `--include-future`)
4. **Render as a table**:
   ```
   bucket   | id                       | agents                       | prompt                          | last_run
   ---------|--------------------------|------------------------------|---------------------------------|------------
   OVERDUE  | weekly-research-scan     | research-analyst             | /market-research scan ...       | 2026-05-10
   DUE_TODAY| daily-nba                | chief-of-staff               | /next-best-action               | 2026-05-23
   ```
5. **Offer execution.** For each due/overdue rhythm, print: `Run {id}? (y / n / skip)`. Wait for operator input per rhythm.
6. **On `y`**:
   - For `kind: solo` → invoke the prompt directly. Switch to the agent (`@{agents[0]}`) and run.
   - For `kind: council` → delegate to `/council {rhythm-id}`.
7. **After each run** (whether solo or council completes), append to `09-meta/rhythms/runs.md`:
   ```
   ## {today ISO} {HH:MM} — {rhythm-id}
   - agents: {agents-joined}
   - prompt: {prompt}
   - outcome: {one-line summary, max 120 chars}
   ```
   Then update `last_run` in `rhythms.json` to today.
8. **Summary.** After all rhythms processed, print a final count: `Ran: N · Skipped: M · Still overdue: K`.

## Hard rules

- Never run a rhythm without operator `y`. `--manual` still asks once.
- Skip rhythms with `active: false`.
- Skip rhythms whose agents are no longer on the roster (warn the operator).
- Never reorder or edit prior `runs.md` entries.
- If a rhythm fails (prompt errors, agent refuses), log `outcome: FAILED — {reason}` and do NOT advance `last_run`.

## Output

- The due-rhythms table
- Per-rhythm execution prompts and results
- Final summary line
