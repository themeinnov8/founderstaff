---
description: Remove an agent from the active roster. Requires operator confirmation. Disables related rhythms.
mode: agent
---

# /retire-agent

Deactivate a chatmode from {{BRAND}}'s active staff. The chatmode file is **not** deleted — it remains installed and can be re-instantiated later.

## Inputs

- `agent_id` — required (kebab-case).
- `reason` — optional, logged.

## Process

1. **Read `09-meta/roster.json`.** If agent not found → "Not on roster" and stop.
2. **Find dependent rhythms.** Scan `rhythms.json` for any entry whose `agents[]` contains `agent_id`. List them.
3. **Confirmation gate.** Print:
   ```
   Retire `{agent_id}` ({role})?
   Affected rhythms: {list or "none"}
   Type `confirm` to proceed, anything else to cancel.
   ```
   Wait for explicit `confirm`. Anything else = abort with no changes.
4. On `confirm`:
   - Remove the agent entry from `roster.json`.
   - For each affected rhythm: if the agent was the only member, set `active: false`. If the rhythm was a council (multiple agents), remove the agent from `agents[]` and keep the rhythm active. If removing leaves zero agents, set `active: false`.
   - Append to `09-meta/rhythms/runs.md`:
     ```
     ## {today ISO} — retired:{agent_id}
     - reason: {reason or "not stated"}
     - affected_rhythms: {list}
     ```
5. **Pretty-print write** both files.

## Hard rules

- Never delete chatmode files. Retirement is roster-only.
- Never bypass the confirmation gate.
- Never silently break rhythms — always log the affected list before retiring.
- One agent per invocation.

## Output

- Updated roster, list of touched rhythms, log entry path.
