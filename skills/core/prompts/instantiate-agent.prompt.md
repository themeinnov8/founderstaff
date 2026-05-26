---
description: Add an installed chatmode to the active roster. Refuses if the chatmode file does not exist.
mode: agent
---

# /instantiate-agent

Activate a chatmode as a member of the {{BRAND}} active staff roster.

## Inputs

- `agent_id` — required. The kebab-case id (e.g., `sales-coach`). Strip leading `@` if present.
- `role` — optional one-line label. If omitted, pull from the chatmode's frontmatter `description:` (truncated to 80 char).
- `notes` — optional.

## Process

1. **Verify installed.** Check that `.github/chatmodes/{agent_id}.chatmode.md` exists. If not → refuse with: "Not installed. Run `python .platform/relearn.py` to sync upstream skills, or run `@hiring-manager` to evaluate a new hire."
2. **Read `09-meta/roster.json`.** If file missing, create with `{ "schema_version": 1, "agents": [] }`.
3. **Check for duplicates.** If `agent_id` already in `agents[]`, report "already on roster" and stop.
4. **Parse the chatmode frontmatter** to extract the description if `role` was not provided.
5. **Append entry**:
   ```json
   {
     "id": "{agent_id}",
     "type": "chatmode",
     "activated": "{today ISO}",
     "role": "{role}",
     "notes": "{notes or empty string}"
   }
   ```
6. **Pretty-print write** to `09-meta/roster.json` (2-space indent, trailing newline).
7. **Suggest next step.** Print: "Activated `{agent_id}`. Schedule a rhythm with `/schedule {agent_id} <cadence>` or leave manual."

## Hard rules

- Refuse if chatmode file is missing. Never auto-fetch from upstream.
- Refuse to set `type` to anything other than `"chatmode"` in v1.
- One agent per invocation. Batch activation = repeat the command.
- Never modify rhythms.json from this prompt.

## Output

- Path to updated roster file
- A one-line summary table: `id · role · activated`
