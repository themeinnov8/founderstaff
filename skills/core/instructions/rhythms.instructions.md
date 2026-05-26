---
applyTo: "09-meta/{roster,rhythms}.json,09-meta/rhythms/**"
---

# Rhythm and roster file rules

These two JSON files are the source of truth for who is on staff and when they run. They are operator-readable, machine-readable, and version-controlled.

## Schema (frozen at `schema_version: 1`)

### `roster.json`

- Top level: `{ "schema_version": 1, "agents": [...] }`
- Each agent: `id` (string, kebab-case, MUST match `.github/chatmodes/{id}.chatmode.md`), `type` (`"chatmode"` for now), `activated` (ISO date), `role` (≤ 80 char human label), `notes` (optional, ≤ 200 char).

### `rhythms.json`

- Top level: `{ "schema_version": 1, "rhythms": [...] }`
- Each rhythm: `id` (kebab-case, unique), `agents` (non-empty string array, every ID must be on the roster), `kind` (`"solo"` if `len(agents)==1`, else `"council"`), `cadence` (one of `daily | weekdays | weekly | monthly | every_n_days | manual`), `prompt` (string starting with `/`), `last_run` (ISO date or `null`), `active` (bool).
- Cadence-specific: `weekly` requires `day` (`monday`..`sunday`); `monthly` requires `day` (int 1..28); `every_n_days` requires `n` (int ≥ 1); `at` (`"HH:MM"`, optional, informational only).

## Hard rules

1. **No invention.** Never add fields not in the schema. Add to the platform schema (PR upstream) before adding here.
2. **No orphans.** A rhythm referencing an agent not on the roster is invalid → refuse to write.
3. **No phantom roster entries.** An agent on the roster without a corresponding installed chatmode file is invalid → refuse to write; suggest `relearn.py` or `@hiring-manager`.
4. **Append-only `runs.md`.** Entries look like: `## YYYY-MM-DD HH:MM — {rhythm-id}` then a 3-bullet summary (agents, prompt, outcome). Never edit prior entries.
5. **Dates ISO 8601**, times `HH:MM` 24-hour. No timezones (operator-local).
6. **Atomic edits.** When mutating either JSON, read → mutate in memory → write the whole file. Never partial-edit.
7. **Pretty-print.** 2-space indent, trailing newline. Diffs should be human-reviewable.
8. **No secrets, no PII.** These files are committed. Treat them as public-internal.

## Never

- Never run a rhythm from these files automatically. The operator must invoke.
- Never reference a prompt that doesn't exist in `.github/prompts/`.
- Never delete `runs.md` entries to "clean up". Archive the whole file with a date suffix if it grows.
