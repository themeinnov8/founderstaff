---
title: Research pack
description: Citation-disciplined research, customer interviews, fact-checking, adversarial review.
---

**Version**: `0.2.0` · **Skills**: 7 · **Requires**: `core`

## Chatmodes

| Agent | Role |
|---|---|
| `@research-analyst` | Citation-disciplined market & competitor research. Never invents numbers. |
| `@red-team` | Adversarial reviewer. Stress-tests plans, content, strategy. One verdict. |

## Prompts

| Command | What it does |
|---|---|
| `/market-research` | Structured market scan → cited research note |
| `/customer-interview` | Mom-Test-compliant discovery interview script |
| `/fact-check` | Claim-by-claim verification; blocks publish on fail |
| `/red-team` | Adversarial review of plan/SKU/content/strategy |

## Instructions

| Glob | Enforces |
|---|---|
| `02-research/**` | Citation format, confidence levels, recency, never-invent |

## Typical activation

```
> /instantiate-agent research-analyst
> /instantiate-agent red-team
> /schedule research-analyst weekly day=monday prompt="/market-research scan competitors"
```

[← Back to agents overview](/agents/)
