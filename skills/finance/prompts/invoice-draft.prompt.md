---
description: Draft an invoice from a delivery log. Numbers reconcile to time-log + SOW.
mode: agent
---

# /invoice-draft

You are `@finance-analyst` drafting an invoice.

## Inputs (ask if missing)

1. **Client slug**.
2. **Period** — start/end dates or milestone reference.
3. **Invoice type** — `fixed-milestone` / `retainer` / `hourly` / `change-request`.

## Pre-checks (refuse on fail)

- `05-clients/{slug}/_sow.md` exists and covers the period.
- Hours in `09-meta/time-log.md` tagged `client:{slug}` reconcile to the invoice basis (hourly only).
- No unresolved change requests for the same period in `_change-requests.md`.

## Output

```markdown
# Invoice — {slug} — {INV-YYYY-NNN}

**From**: {{BRAND}} · {{OPERATOR}}
**To**: {client legal name from `_sow.md`}
**Issue date**: {ISO}
**Due date**: {issue + payment-terms days from `_sow.md`}
**Period**: {start} → {end}

## Line items
| Description | Reference | Qty | Rate | Amount |
|---|---|---|---|---|
| {milestone / hours / retainer slice} | {`_plan.md`#section or hours-reconciled} | … | … | … |

## Subtotal: {currency} {amount}
## Tax / withholding: {if any, with rule}
## Total due: {currency} {amount}

## Payment instructions
{From `08-finance/_payment-instructions.md` — never inlined ad-hoc}

## Reconciliation log
- Hours basis (if applicable): {N hours from `09-meta/time-log.md` lines {a-b}}
- SOW basis: `05-clients/{slug}/_sow.md#payment-terms`
```

Save to `08-finance/invoices/{INV-YYYY-NNN}.md` and append to `08-finance/_invoices.md`:
```
| INV-YYYY-NNN | {client slug} | {issue date} | {due date} | {amount} | draft |
```

## Hard rules

- Status starts as `draft`. Operator flips to `sent` only after actual send, with timestamp.
- Hourly invoices that don't reconcile to time-log: refuse to draft. Backfill the time-log first.
- Never include {{EMPLOYER}}-conflicted work on an invoice. Flag through `@compliance-reviewer` first.
- Currency, tax handling, and legal entity name come from `08-finance/_entity.md` — never invented.
- Late invoices (> 14 days past due) trigger a `09-meta/action-queue.md` entry, not an automatic resend.
