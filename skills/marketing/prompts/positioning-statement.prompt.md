---
description: Draft a positioning statement using the standard `For X who Y, {{BRAND}} is Z that A. Unlike B, we C.` template.
mode: agent
---

# /positioning-statement

You are `@brand-strategist`. Produce a positioning statement and supporting brief.

## Inputs (ask if missing)

1. **Primary buyer persona** — slug from `00-strategy/personas.md`.
2. **Trigger** — the moment they go looking for a solution.
3. **Alternatives** — what they would compare us against (≥ 2, including "do nothing").
4. **Unique mechanism** — the specific way we deliver value that alternatives can't.

## Output

```markdown
# Positioning — {{BRAND}} — {ISO date}

## Statement
For **{persona}** who **{trigger}**, {{BRAND}} is **{category}** that **{primary benefit}**.
Unlike **{primary alternative}**, we **{unique mechanism}**.

## Category we play in
{One sentence. Honest about who we compete with.}

## Top 3 alternatives (in buyer's mind)
1. {alternative} — why we'd lose: {…} — why we'd win: {…}
2. …
3. …

## Three claims we can defend
- {Claim} — evidence: {path in `02-research/**` or URL}
- {Claim} — evidence: {…}
- {Claim} — evidence: {…}

## Three claims to NEVER make
- {claim} — because {reason}
```

Save to `06-marketing/brand/positioning.md` (overwrite with archive of prior version into `06-marketing/brand/_archive/`).

## Hard rules

- Every claim has a citation. No unevidenced superlatives.
- The category name is what buyers Google, not what we wish they did.
- Trigger to a `red-team /red-team` pass before status flips to `accepted`.
- Log a decision record in `09-meta/decisions/` per `decision-logging.instructions.md`.
