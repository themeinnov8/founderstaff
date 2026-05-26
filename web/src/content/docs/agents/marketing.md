---
title: Marketing pack
description: Positioning, launches, landing pages, paid + organic ad copy.
---

**Version**: `0.2.0` · **Skills**: 6 · **Requires**: `core`

## Chatmodes

| Agent | Role |
|---|---|
| `@brand-strategist` | Owns positioning + messaging house for the brand |
| `@growth-marketer` | Channel experiments, funnel diagnostics, growth loops |

## Prompts

| Command | What it does |
|---|---|
| `/positioning-statement` | For-Who-Is template + supporting brief |
| `/launch-playbook` | T-minus schedule + assets + success metric |
| `/landing-page` | Landing page copy (not HTML) from positioning + one offer |
| `/ad-copy` | Ad copy variants for search / LinkedIn / Meta / X |

## Typical activation

```
> /instantiate-agent brand-strategist
> /instantiate-agent growth-marketer
> /schedule brand-strategist monthly day=1 prompt="/positioning-statement review"
```

[← Back to agents overview](/agents/)
