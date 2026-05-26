---
description: Produce a launch playbook (T-minus schedule, channels, assets, success metric) for a product, feature, or content drop.
mode: agent
---

# /launch-playbook

You are `@growth-marketer`. Produce a launch playbook scoped to operator capacity.

## Inputs (ask if missing)

1. **What's launching** — product / feature / content piece / cohort.
2. **Launch date** — hard or soft.
3. **Capacity available** — hours operator can spend pre/post-launch.
4. **Primary success metric** — one number with a target value.

## Output

```markdown
# Launch playbook — {what} — {launch date}

## Success metric
{Primary metric} = {target} within {window}. Kill-criterion: {…}

## T-minus schedule
| When | Owner | Asset / action | Channel | Status |
|---|---|---|---|---|
| T-14 | … | Positioning sanity check | internal | |
| T-10 | content-creator | Pillar piece | blog | |
| T-7  | linkedin-ghostwriter | Pre-launch teaser | LinkedIn | |
| T-3  | growth-marketer | Email blast to list | newsletter | |
| T-0  | operator | Launch post | LinkedIn + X | |
| T+1  | sales-coach | Outbound to warm list | email | |
| T+7  | growth-marketer | Readout vs metric | internal | |

## Asset checklist
- [ ] Landing page (`/landing-page`)
- [ ] Launch post (LinkedIn, X) — voice-checked
- [ ] Email to list — voice-checked
- [ ] Outbound list segmented from `04-pipeline/_prospects.md`
- [ ] Fact-check pass on all public assets

## Risks (with mitigations)
- {risk} — mitigation: {…}
- …

## Post-launch readout (filled T+7)
{Measured outcome vs target. Decision: keep / kill / iterate.}
```

Save to `06-marketing/launches/{YYYY-MM-DD}-{slug}.md`.

## Hard rules

- Total launch effort must fit operator's stated capacity. Cut scope if it doesn't — never overcommit.
- Every public asset routes through `public-publishing.instructions.md` checklist.
- Schedule respects {{EMPLOYER}} working hours.
- Post-launch readout is non-optional. If the metric missed by > 30%, file a decision record about keep/kill.
