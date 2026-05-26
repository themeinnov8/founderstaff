---
title: Operations pack
description: SOPs, meeting notes, inbox triage, weekly review.
---

**Version**: `0.2.0` · **Skills**: 6 · **Requires**: `core`

## Chatmodes

| Agent | Role |
|---|---|
| `@operations-manager` | SOPs, weekly review, hygiene. The mechanics, not the strategy. |
| `@meeting-notetaker` | Converts raw meeting input into decisions + action items + summary |

## Prompts

| Command | What it does |
|---|---|
| `/sop-author` | Standard Operating Procedure for any workflow done ≥3 times |
| `/meeting-notes` | Structured decisions + action items + summary from raw input |
| `/inbox-triage` | Triage inbox into act-now / reply-later / archive, with draft replies |
| `/weekly-review` | Saturday weekly review: hours audit, deltas, carry-forward, stop-doing |

## Typical activation

```
> /instantiate-agent operations-manager
> /instantiate-agent meeting-notetaker
> /schedule operations-manager weekly day=saturday prompt=/weekly-review
> /schedule operations-manager weekdays prompt=/inbox-triage
```

[← Back to agents overview](/agents/)
