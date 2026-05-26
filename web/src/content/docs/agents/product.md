---
title: Product pack
description: Solo-founder product management. PRDs, user stories, prioritization. No PM theater.
---

**Version**: `0.2.0` · **Skills**: 4 · **Requires**: `core`

## Chatmodes

| Agent | Role |
|---|---|
| `@product-manager` | Solo-founder product manager. PRDs, stories, prioritization. No PM theater. |

## Prompts

| Command | What it does |
|---|---|
| `/prd-draft` | Lightweight PRD: problem, user-story, scope, non-goals, kill criterion |
| `/user-story` | Break a PRD into user-stories with observable acceptance criteria |
| `/feature-prioritize` | Rank features using impact/effort/confidence (or RICE / WSJF) |

## Typical activation

```
> /instantiate-agent product-manager
> /schedule product-manager weekly day=monday prompt="/feature-prioritize backlog"
```

[← Back to agents overview](/agents/)
