---
description: Build a pricing model for one offer with unit economics + recommended price band.
mode: agent
---

# /pricing-model

You are `@finance-analyst` pricing one offer.

## Inputs (ask if missing)

1. **Offer** — short description + the deliverables included.
2. **Cost basis** — operator hours × loaded rate, plus direct costs.
3. **Comparables** — at least 2 from `02-research/pricing/**` or named alternatives buyers consider.
4. **Pricing model** — `fixed` / `retainer` / `hourly` / `outcome-based` / `tiered`.
5. **Target margin** — % over cost basis.

## Output

Save to `08-finance/pricing/{offer-slug}.md`.

```markdown
# Pricing — {offer name} — {ISO date}

## Assumptions
- Loaded rate: {currency/hr} — derivation: {…}
- Hours per delivery: {low / expected / high}
- Direct costs per delivery: {…}
- Target gross margin: {%}

## Unit economics
| Scenario | Hours | Cost | Margin @ price | Effective $/hr |
|---|---|---|---|---|
| Low | … | … | … | … |
| Expected | … | … | … | … |
| High | … | … | … | … |

## Market comparables
| Source | Comparable offer | Price | Notes |
|---|---|---|---|
| … | … | … | … |

## Recommended band
- Floor: {price} — never go below this; margin too thin
- Anchor: {price} — opening number in proposals
- Stretch: {price} — for higher-trust / lower-risk buyers

## What buyers compare this against
{1–3 sentences. Honest about substitution.}

## Discounting policy
{When / how / max discount before sign-off needed}
```

## Hard rules

- Floor price must clear cost basis × (1 + target margin). No exceptions.
- Stretch price requires at least one comparable above it. No untethered numbers.
- If comparables come from < 2 sources, mark `confidence: low` and recommend `/market-research` first.
- Any discount > 15% off anchor requires a `09-meta/decisions/` record.
- `@sales-coach /proposal-sow` references this file by path — do not move it after publishing.
