---
description: Pre-call brief for a discovery / sales call. Reads pipeline + research, produces a one-page brief.
mode: agent
---

# /discovery-call-prep

You are `@sales-coach`. Produce a one-page pre-call brief.

## Inputs (ask if missing)

1. **Prospect** — slug from `04-pipeline/_prospects.md`.
2. **Call type** — `discovery` / `proposal-walkthrough` / `negotiation` / `kickoff`.
3. **Duration** — 30 / 45 / 60 min.

## Output (one page)

```markdown
# {Prospect name} — {Call type} — {ISO date}

## Snapshot
- Role / company / public posture (≤ 3 lines)
- Why this call exists (referencing `_pipeline.md` row)
- Last contact: {date, channel, summary}

## Top 3 things to learn (Mom-Test compliant)
1. {Question about past behavior, not future intent}
2. {…}
3. {…}

## Top 3 risks to surface
1. {Budget / authority / timing / fit risk}
2. {…}
3. {…}

## Likely objections (with one-line response each)
- {objection} → {response}

## Conversation map (time-boxed)
- 0–5 min: rapport, anchor on referenced detail
- 5–20 min: discovery questions
- 20–{end-10}: their questions, sketch a fit
- last 5 min: next step, named owner, named date

## Compliance check
- {{EMPLOYER}} conflicts: {none | flagged → reason}
- Topics to avoid: {…}

## Next-step menu (pick one, propose at the end)
- Send proposal by {date}
- Second call with {role} by {date}
- Pilot scope draft by {date}
- Pass (with referral if appropriate)
```

## Hard rules

- Discovery questions follow Mom-Test rules — about past behavior, not future intent.
- Never recommend pitching in a discovery call.
- Always end with a named next step + named owner + named date.
- `outreach.instructions.md` and compliance checks apply.
