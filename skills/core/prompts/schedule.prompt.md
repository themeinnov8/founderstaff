---
description: Create or update a rhythm — a scheduled invocation of one agent (solo) or several (council).
mode: agent
---

# /schedule

Define when an agent (or set of agents) runs and what prompt they execute.

## Inputs (parse from natural language if needed)

- `agents` — required, one or more roster IDs.
- `cadence` — required, one of: `daily | weekdays | weekly | monthly | every_n_days | manual`.
- Cadence args: `day` (for `weekly`/`monthly`), `n` (for `every_n_days`).
- `prompt` — required. A slash-command string (e.g., `/next-best-action`, `/market-research scan competitors`, `/council pipeline-review`).
- `at` — optional, `HH:MM` 24h. Informational only (no daemon).
- `id` — optional. If omitted, derive from `{agents-joined}-{cadence}` (kebab-case, deduped with a numeric suffix if needed).

## Process

1. **Read `09-meta/roster.json` and `09-meta/rhythms.json`.** Create empty rhythms file if missing.
2. **Validate every agent** is on the roster. If any are missing → list them and stop. Suggest `/instantiate-agent` for each.
3. **Determine `kind`**: `"solo"` if `len(agents)==1`, else `"council"`. If `council` and `prompt` doesn't start with `/council`, warn the operator that council prompts coordinate multi-agent turn-taking.
4. **Validate cadence args**:
   - `weekly` → `day` ∈ {monday..sunday}
   - `monthly` → `day` ∈ 1..28 (avoid 29-31 for portability)
   - `every_n_days` → `n` ≥ 1
   - `manual` → no extra args; rhythm only fires when operator runs `/run-due --manual {id}` or invokes directly.
5. **Verify prompt exists.** Split on space; check `.github/prompts/{first-token-without-slash}.prompt.md` exists. If not → suggest creating it via `@agent-forge`.
6. **Upsert**:
   - If `id` already exists → update fields, keep `last_run`.
   - Else → append new entry with `last_run: null`, `active: true`.
7. **Pretty-print write** `rhythms.json`.
8. **Confirmation echo.** Print the rhythm as a one-line summary:
   ```
   {id}: {agents-joined} · {cadence} {args} · {prompt} · next_due={computed-iso-date}
   ```

## Computing `next_due`

- `daily` → tomorrow if `last_run == today`, else today.
- `weekdays` → next weekday after `last_run` (skip Sat/Sun).
- `weekly` → next occurrence of `day` after `last_run`.
- `monthly` → next month's `day`.
- `every_n_days` → `last_run + n days` (today if `last_run` is null).
- `manual` → no `next_due`; show `—`.

## Hard rules

- Reject agents not on roster. Never silently drop them.
- Reject a prompt that doesn't exist in `.github/prompts/`.
- Council rhythms require ≥ 2 distinct agents.
- `at` is metadata only. Never imply autonomous execution.
- One rhythm per invocation. Multi-agent council = one rhythm with multiple `agents`, not multiple rhythms.

## Output

- Path to updated `rhythms.json`
- One-line summary of the upserted rhythm
- Computed `next_due`
