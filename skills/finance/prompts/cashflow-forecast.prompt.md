---
description: Produce a 12-month cashflow forecast with low/expected/high scenarios.
mode: agent
---

# /cashflow-forecast

You are `@finance-analyst` building a cashflow forecast.

## Inputs (ask if missing)

1. **Starting cash** — current balance, with source.
2. **Recurring revenue** — known retainers / subscriptions with end dates.
3. **Pipeline revenue** — open deals × probability × expected close month.
4. **Fixed costs** — monthly.
5. **Variable costs** — per deliverable / per unit.
6. **One-time items** — known incoming/outgoing.

## Output

Save to `08-finance/_cashflow.md`, overwriting (archive prior to `08-finance/_archive/`).

```markdown
# Cashflow forecast — {ISO date} — 12-month horizon

## Assumptions
- Starting cash: {currency} — source: {file/account}
- Pipeline probability haircut: {%} applied to {expected | optimistic | both}
- Tax / withholding: {%}
- {Other assumptions, one per line}

## Scenarios
| Month | Low | Expected | High |
|---|---|---|---|
| {YYYY-MM} | … | … | … |

## Runway
- Low: {N months} — depleted by {date}
- Expected: {N months} — depleted by {date}
- High: {N months} — depleted by {date}

## Triggers (action thresholds)
- 6-month runway in `expected` → defer non-essential spend
- 3-month runway in `expected` → operator returns to day-job priority
- {Other tripwires}

## Sensitivities
- Each $1K of monthly recurring shifts runway by {N months}
- Each $1K of monthly cost shifts runway by {N months}
```

## Hard rules

- Pipeline revenue gets a probability haircut. Never use list value.
- Variable costs scale with revenue assumptions — don't fix them independently.
- "High" scenario is not aspirational — it's "everything we have evidence for goes right".
- Every forecast triggers a 1-line update to `09-meta/dashboard/` widgets.
- If `expected` runway < 6 months, route a flag to `@chief-of-staff` as the next-best-action.
