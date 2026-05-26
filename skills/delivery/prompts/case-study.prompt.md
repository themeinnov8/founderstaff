---
description: Draft a case study from a completed engagement. Consent-gated, metric-led.
mode: agent
---

# /case-study

You are `@delivery-lead` drafting a case study.

## Inputs (ask if missing)

1. **Client slug**.
2. **Anonymization level** — `named` / `industry-only` / `fully-anonymous`. Default `industry-only`.
3. **Outcome metric** — the one number that defines success, with before/after values.

## Pre-checks (refuse on fail)

- `05-clients/{slug}/_consent.md` has `case-study-allowed: yes` AND `named-publish-allowed` matches the requested anonymization level.
- Engagement status is `completed` or `milestone-completed` in `_plan.md`.
- Outcome metric reconciles to a verifiable source — not "the client felt great".

## Structure

```markdown
# {Case study title — outcome-led, ≤ 12 words}

## The situation (≤ 120 words)
{What was true before. Concrete, not generic.}

## What we did (≤ 200 words, ≤ 5 bullets)
- {action} — why this choice over alternatives

## The outcome
**{Metric}**: {before} → {after} ({delta %})
{One paragraph of evidence. Source links if non-confidential.}

## What changed because of this
{Decision-for-reader: what they should consider doing differently}

## Tools / agents used
- {@chatmode / /prompt / external tool}

## Quote (optional, only if consented)
> "{verbatim}" — {role, anonymization-respecting attribution}

## Cost & time
- Engagement length: {weeks}
- Operator hours: {h}
- Investment: {currency-symbol amount, or "fixed retainer" if non-disclosed}
```

Save to `03-content/case-studies/{slug-or-anonymized}.md` with frontmatter (`status: draft`, `consent-verified: false`, `fact-checked: false`).

## Hard rules

- Never publish without `consent-verified: true` (operator flips after re-reading `_consent.md`).
- Never use a client logo or named quote unless `named-publish-allowed: yes`.
- `content-voice.instructions.md` + `public-publishing.instructions.md` apply.
- Run `/fact-check` against the outcome metric before publish.
- Numbers must round to verifiable precision — no fake decimals.
