---
description: ADR-style decision records for any irreversible or expensive-to-reverse choice.
applyTo: "09-meta/decisions/**"
---

# decision-logging

Every decision filed under `09-meta/decisions/` must follow this format.

## Filename

`YYYY-MM-DD-{kebab-slug}.md` — date is the day decided, not the day filed.

## Required sections

```markdown
# {Decision title — verb-first, ≤ 10 words}

**Status**: proposed | accepted | superseded by {filename} | reversed
**Decided**: {YYYY-MM-DD} by {{OPERATOR}}
**Reversibility cost**: {hours / dollars / relational}

## Context
What was true when the decision was made? 3–6 lines.

## Options considered
- A: {one-line}
- B: {one-line}
- C: {one-line}

## Decision
{One sentence. Active voice.}

## Reasoning
Why this option won. Reference source files. Honest about tradeoffs.

## Consequences
- Expected: …
- Risk: …
- Will know it's working when: {measurable signal + by-when}

## Revisit on
{date or trigger condition}
```

## Hard rules

- One decision per file. Don't bundle.
- Never edit `Decision` or `Reasoning` after `accepted` — supersede with a new file instead.
- Reversed decisions stay in the folder; mark status, link the supersedor.
- If reversibility cost > $1000 or > 8h, `red-team` must review before status flips to `accepted`.
