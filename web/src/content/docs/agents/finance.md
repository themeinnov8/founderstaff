---
title: Finance pack
description: Cashflow, pricing, unit economics, invoicing. Conservative by default.
---

**Version**: `0.2.0` · **Skills**: 4 · **Requires**: `core`

## Chatmodes

| Agent | Role |
|---|---|
| `@finance-analyst` | Cashflow, runway, pricing, unit economics. Conservative by default. |

## Prompts

| Command | What it does |
|---|---|
| `/cashflow-forecast` | 12-month forecast with low/expected/high scenarios + runway |
| `/pricing-model` | Unit economics + price band (floor/anchor/stretch) for one offer |
| `/invoice-draft` | Invoice draft that reconciles to time-log + SOW |

## Typical activation

```
> /instantiate-agent finance-analyst
> /schedule finance-analyst monthly day=1 prompt="/cashflow-forecast current quarter"
```

[← Back to agents overview](/agents/)
