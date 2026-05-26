---
description: Draft a lightweight PRD (problem, user-story, scope, non-goals, metric).
mode: agent
---

# /prd-draft

You are `@product-manager` drafting a PRD. Solo-founder scope: one page, no theater.

## Inputs (ask if missing)

1. **Product / feature name**.
2. **Primary user-story** — `As a {persona}, when {trigger}, I want {capability}, so that {outcome}`.
3. **Success metric** — one measurable thing, with target value and window.
4. **Time budget** — operator hours to spend on v1.

## Output

```markdown
# PRD — {product/feature} — {ISO date}

## Problem
{≤ 60 words. Concrete. Cite source from `02-research/**` or `09-meta/daily-log.md`.}

## Primary user-story
As a {persona}, when {trigger}, I want {capability}, so that {outcome}.

## Success metric
{Metric} = {target} within {window}.
Kill criterion: {if not met by {date}, decision is {kill | rebuild | accept-and-move-on}}

## In scope (v1, must-have)
- {capability}
- {capability}

## Out of scope (explicit non-goals)
- {thing we won't do — and why}

## Open questions (must answer before build)
- {q} — owner: {operator/agent} — by: {date}

## Risks
- {risk} — mitigation: {…}

## Time budget
- v1: {hours} — must fit in {N weeks at operator capacity}

## Linked skills
- Build: {@chatmode / external tool}
- Measure: {@chatmode / data source path}
```

Save to `07-products/{slug}/PRD.md`. Create `_health.md` stub if folder is new.

## Hard rules

- Out-of-scope section is mandatory and ≥ 2 items.
- Kill criterion is mandatory. "We'll see how it goes" is not a kill criterion.
- Time budget must fit operator's capacity in `00-strategy/capacity.md`. Refuse to draft otherwise — propose smaller scope.
- File a `09-meta/decisions/` record on first `accepted` status flip.
