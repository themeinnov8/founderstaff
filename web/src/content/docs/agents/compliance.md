---
title: Compliance pack
description: Pre-publish / pre-send compliance gate. Firewall, conflicts list, DNC enforcement.
---

**Version**: `0.2.0` · **Skills**: 2 · **Requires**: `core`

## Chatmodes

| Agent | Role |
|---|---|
| `@compliance-reviewer` | Pre-publish / pre-send compliance gate. Returns pass/flag. |

## Prompts

| Command | What it does |
|---|---|
| `/compliance-check` | Match artifact against firewall / conflict-list / DNC / consent rules |

## Why it matters

If you're running a venture alongside a day job, the compliance pack is non-negotiable. It enforces:

- **Day-job firewall** — won't publish anything that mentions or echoes employer-confidential material
- **Conflicts list** — refuses outreach to entities flagged as conflicts
- **DNC list** — never contacts people who've asked not to be
- **Consent gate** — case studies require recorded consent before publish

## Typical activation

```
> /instantiate-agent compliance-reviewer
```

Then every public-facing prompt automatically routes through `/compliance-check` before producing final output. You'll see it as a gate, not an extra step.

[← Back to agents overview](/agents/)
