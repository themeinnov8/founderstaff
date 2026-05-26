---
description: Generate a discovery / customer interview script for a target audience segment. Outputs Mom-Test compliant questions.
mode: agent
---

# /customer-interview

Generate an interview script for a target audience segment. Follows *The Mom Test* discipline: ask about past behavior, not future intent. Outputs a script the operator can run on a 30-minute call.

## Inputs

- `segment`: audience name (e.g., "Mid-career PMs in India considering AI upskilling")
- `purpose`: pricing-validation | offering-validation | positioning | onboarding-friction | churn
- `n_interviews_target`: typically 5–8
- `decision_at_stake`: what OS change this evidence will trigger

## Output

A markdown file at `02-research/interview/{YYYY-MM-DD}-{segment-slug}-script.md` containing:

```
# Interview script — {segment} — {purpose}

## Goal
{single sentence}

## Decision this informs
{decision_at_stake}

## Sample (target n={n})
- Source: {LI, Topmate, community}
- Screening criteria: {3 bullets}
- Compensation: {none / ₹500 voucher / etc.}

## Script (30 min)

### Warm-up (3 min)
- Tell me about your current work and the last 6 months.

### Past behavior (15 min) — primary
- What's the last thing you tried to learn AI/ship better PM work?
- Walk me through what you actually did. (probe: timeline, tools, what stuck)
- What did you spend money on in the last 12 months for career growth? (probe: amounts, why, regret?)
- When was the last time you {specific pain we hypothesize}? What did you do?

### Specific evidence (8 min)
- Show me the last AI prompt you used at work. (concrete artifact)
- How long did the last {workflow we'd improve} take last time you did it?

### Constraints (3 min)
- What stops you from doing X today? (probe: time, money, permission)

### Wrap (1 min)
- Who else should I talk to?
- Can I follow up in 4 weeks?

## Banned questions (do NOT ask)
- Would you pay for {our product}?  [hypothetical]
- Do you think {our idea} is good?  [seeks validation]
- How often would you use {our feature}?  [imagined future]

## Synthesis template (fill after each call)
| Quote | Behavior signal | Pain confirmed? | Pricing signal | Follow-up |

## Decision rule
We will {decision} if ≥{n} of {n_target} interviews show {observable signal}.
```

## Hard rules

- Past behavior, not future intent. Every question must ask about something that already happened.
- Concrete artifacts > stated preferences. Ask to see the actual file/screenshot.
- Money: ask what they spent, not what they would spend.
- Never reveal the offering before the call ends — bias kills the signal.
- Anonymize interview notes — use handles like P1, P2 in `02-research/interview/notes/`.
