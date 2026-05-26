---
description: Run a multi-agent council session. Each agent contributes in turn; a synthesis pass produces decisions.
mode: agent
---

# /council

Coordinate a structured discussion among 2+ agents on a roster rhythm. Outputs decisions, action items, and disagreements — not consensus theater.

## Inputs

- `rhythm_id` — optional. If provided, load `agents` and `prompt` topic from `rhythms.json`.
- `agents` — required if no `rhythm_id`. Comma-separated roster IDs (e.g., `chief-of-staff, brand-strategist, finance-analyst`).
- `topic` — required. The question or decision the council exists to address.
- `context_paths` — optional. Workspace paths the council should read before contributing (e.g., `00-strategy/positioning.md`, `04-pipeline/_pipeline.md`).

## Process

### Phase 1 — Setup
1. Resolve `agents` (from `rhythm_id` or input). Verify every agent is on `roster.json`.
2. Read each `context_paths` file. If any missing → list them, ask whether to proceed.
3. Announce: "Council convened: {agents}. Topic: {topic}. Context: {n} files."

### Phase 2 — Independent reads (round 1)
For each agent in turn:
1. Switch persona (`@{agent_id}`).
2. Give them ONLY the topic and context. Do not show other agents' takes yet.
3. Ask: "From your seat, what is the single most important point on this topic? What is your recommendation? What is the strongest counter to your own recommendation?"
4. Capture their reply as `## {agent_id} — round 1` in working notes.

### Phase 3 — Cross-reads (round 2)
1. Show all round-1 replies to all agents.
2. For each agent in turn:
   - Ask: "Reading the others' positions: where do you agree, where do you disagree, and what changes (if any) in your recommendation?"
3. Capture as `## {agent_id} — round 2`.

### Phase 4 — Synthesis
The current agent (you, in `/council` mode) — **not** any participating agent — writes:

```
## Synthesis ({today ISO})

### Decisions (≤ 3)
- DECISION 1: ...
- (decided by: {agents who agreed}; objection: {agent who didn't, if any})

### Action items
- [ ] {action} — owner: {agent_id or operator} — due: {date}

### Open disagreements
- {topic} — {agent_A says X} vs {agent_B says Y} — needs operator call

### Confidence
- Council confidence on each decision: HIGH / MEDIUM / LOW
```

### Phase 5 — Log
1. Write the full transcript (round 1 + round 2 + synthesis) to `09-meta/rhythms/councils/{today-ISO}-{rhythm_id or topic-slug}.md`.
2. Append a 3-line entry to `09-meta/rhythms/runs.md`.
3. If invoked via `rhythm_id`, update `last_run` in `rhythms.json`.

## Hard rules

- Minimum 2, maximum 6 agents per council. More than 6 = noise; split into two.
- Each agent must answer round 1 *without* seeing others' replies. Order matters less than isolation.
- Synthesis is written by the council coordinator, never by a participating agent (avoids capture).
- Disagreements are NOT papered over. If two agents disagree, log it as an open item, not a forced compromise.
- Never invent agreement. If only one agent supports a decision, mark it `weak signal`.
- Compliance gate: if council output is destined for a public channel, run `/compliance-check` before any external use.

## Output

- Path to the transcript markdown
- The Synthesis block printed inline
- Updated `last_run` (if rhythm-driven)
