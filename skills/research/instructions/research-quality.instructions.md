---
description: Quality guardrails for anything stored in 02-research/. Enforces citation, confidence levels, recency, and "never invent".
applyTo: "02-research/**"
---

# Research quality guardrail

Anything written to `02-research/**` is a load-bearing input for strategy and content. Hallucinated research kills the brand. Enforce these rules on every file in this scope.

## Mandatory frontmatter

```yaml
---
topic: {one-line description}
type: market | competitor | audience | pricing | trend | interview | benchmark
researcher: chief-of-staff | research-analyst | {human}
date_collected: YYYY-MM-DD
freshness: live | stale_after_YYYY-MM-DD
confidence: high | medium | low | speculative
sources_count: {n}
---
```

## Every claim must be:

1. **Cited.** Inline as `[1]`, `[2]`. Sources listed at bottom with URL + access date.
2. **Tagged with confidence.** Mark soft claims with `[low]` or `[speculative]` inline. No bare assertions.
3. **Dated.** If a number changes over time (price, market size, follower count), include the as-of date.
4. **Quantified where possible.** Replace "many" / "most" / "growing" with numbers or kill the sentence.
5. **Falsifiable.** Each claim must be checkable. "AI is exciting" is banned. "PM-tooling category grew 28% YoY [3]" is fine.

## Hard rules

- **Never invent sources.** If a URL can't be verified, drop the claim. Do not paste plausible-looking URLs.
- **Never trust a single source for a numeric claim.** Require ≥2 independent sources for any number quoted in content.
- **Mark recency.** Anything older than 12 months gets `[stale]` flag. Re-verify before citing in client-facing work.
- **Anonymize personal data.** Never store real names, emails, or company identifiers from interviews — use handles.
- **Compliance.** If research touches Microsoft or current employer's domain, flag for `/compliance-check` before write.

## Standard file structure

```markdown
---
{frontmatter}
---

# {Topic}

## TL;DR (3 bullets, all cited)
- ...

## Key findings
### Finding 1: {statement} [1][2]
- Evidence: ...
- Confidence: high — 2 primary sources + reproducible
- Counter-evidence: ...

## Open questions
- {question} — need {what} to resolve

## Implications for the OS
- For {pricing | content | offering | pipeline}: {specific action}

## Sources
1. {Author/Org}, "{Title}", {URL}, accessed {date}
2. ...

## Change log
- {date}: created
- {date}: re-verified, finding 2 updated
```

## Filename convention

`02-research/{type}/{YYYY-MM-DD}-{slug}.md`

Examples: `02-research/competitor/2026-06-12-topmate-pm-coaches.md`, `02-research/pricing/2026-07-01-pm-bootcamp-benchmark.md`
