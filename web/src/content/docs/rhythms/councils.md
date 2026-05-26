---
title: Councils (multi-agent)
description: Five-phase flow for multi-agent collaborative sessions. Decisions, action items, preserved disagreements.
---

import { Aside } from '@astrojs/starlight/components';

A **council** is a rhythm with `kind: council` and 2–6 agents. Use councils when a decision genuinely needs multiple perspectives — quarterly strategy, launch readiness, pipeline review.

## When to use a council

| Good fit | Bad fit |
|---|---|
| Cross-functional decision (strategy needs brand + finance + research view) | Single-discipline question (use the relevant solo agent) |
| Stuck on tradeoffs (different agents will weigh differently) | Already know the answer (saves no time) |
| Recurring decision (quarterly, monthly) | One-off (just `@agent` the relevant person) |

## Convene a council

Two ways:

### Via a rhythm

```
/schedule chief-of-staff,brand-strategist,finance-analyst monthly day=1 prompt="/council quarterly-strategy"
```

Then each month: `/run-due` surfaces it; operator types `y` to convene.

### Ad-hoc

```
/council agents=chief-of-staff,brand-strategist,finance-analyst topic="Should we raise prices in Q3?"
```

## The 5-phase flow

### Phase 1 — Setup

- Resolve agents from rhythm or input
- Verify all are on the roster
- Read any `context_paths` files (positioning doc, pipeline, financials)
- Announce: "Council convened: {agents}. Topic: {topic}. Context: {n} files."

### Phase 2 — Independent round-1

Each agent answers **without seeing the others' takes**:

> From your seat, what is the single most important point on this topic? What is your recommendation? What is the strongest counter to your own recommendation?

Captured as `## {agent_id} — round 1`.

<Aside type="tip" title="Why isolation matters">
Round-1 isolation prevents anchoring. If the first speaker frames the discussion, everyone else accommodates. Independent round-1 surfaces the real diversity of view.
</Aside>

### Phase 3 — Cross-read round-2

Now show everyone all round-1 replies. Each agent answers:

> Reading the others' positions: where do you agree, where do you disagree, and what changes (if any) in your recommendation?

Captured as `## {agent_id} — round 2`.

### Phase 4 — Synthesis

The **`/council` coordinator** — not any participating agent — writes:

```markdown
## Synthesis (2026-05-24)

### Decisions (≤ 3)
- DECISION 1: Hold pricing flat in Q3; raise in Q4 with new tier
  (decided by: chief-of-staff, brand-strategist; objection: finance-analyst — wants Q3 raise)

### Action items
- [ ] Draft Q4 pricing tier — owner: brand-strategist — due: 2026-06-15
- [ ] Run pricing-elasticity research — owner: research-analyst — due: 2026-06-01

### Open disagreements
- Timing of price raise — finance-analyst says now; brand-strategist says wait — needs operator call

### Confidence
- DECISION 1: MEDIUM (2/3 agents, finance dissent)
```

<Aside type="caution" title="Synthesis isn't unanimous">
Councils don't manufacture consensus. If two agents disagree after round-2, that disagreement is logged as an open item for the operator, not papered over. "Slightly modified compromise" is fake; preserved tension is real.
</Aside>

### Phase 5 — Log

- Full transcript written to `09-meta/rhythms/councils/{date}-{rhythm_id-or-topic}.md`
- 3-line entry appended to `09-meta/rhythms/runs.md`
- If rhythm-driven: `last_run` updated

## Hard rules

1. **Minimum 2, maximum 6** agents per council. More than 6 = noise; split into two.
2. **Round-1 must be isolated.** Each agent answers without seeing others' replies.
3. **Synthesis is by the coordinator**, never by a participating agent (prevents capture).
4. **Disagreements are preserved**, not resolved.
5. **Compliance gate** applies to any council output destined for a public channel.

## Common council patterns

| Pattern | Agents | Cadence |
|---|---|---|
| Quarterly strategy review | `chief-of-staff` + `brand-strategist` + `finance-analyst` + `research-analyst` | `monthly` + manual quarterly trigger |
| Weekly pipeline review | `sales-coach` + `delivery-lead` | `weekly day=monday` |
| Pre-launch readiness | `brand-strategist` + `growth-marketer` + `delivery-lead` + `compliance-reviewer` | `manual` (fire 2 weeks before launch) |
| Hire decision | `chief-of-staff` + `finance-analyst` + `delivery-lead` | `manual` |
| Content strategy reset | `content-creator` + `brand-strategist` + `research-analyst` | `monthly day=15` |
