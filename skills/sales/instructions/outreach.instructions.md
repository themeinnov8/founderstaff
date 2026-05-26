---
description: Hard rules for any outbound contact (cold email, LinkedIn DM, follow-up) on behalf of {{BRAND}}.
applyTo: "04-pipeline/**,06-marketing/outreach/**"
---

# outreach

Applies to every outbound message draft, sequence, and prospect list.

## Required before sending

1. Prospect exists as a row in `04-pipeline/_prospects.md` with `source`, `relevance_reason`, `last_contact`.
2. The prospect is NOT on `09-meta/do-not-contact.md`.
3. The prospect's employer is NOT on `09-meta/conflict-list.md` (cross-check {{EMPLOYER}} conflicts).
4. The message references a specific, verifiable detail about the recipient (post, role, product, mutual context). No "I came across your profile".

## Banned patterns

- "Quick question" / "Hope this finds you well" / "Picking your brain" openers.
- Multi-paragraph cold opens. Cold first-touch must be ≤ 90 words.
- Calendar links in first message.
- Fake personalization (Mail-merged "I loved your post about {topic}" without naming the post).
- Sending without a clear next-step ask (one question, one CTA).

## Cadence rules

- Max 4 touches per prospect per quarter unless they replied.
- Min 4 working days between touches.
- After a "no" or no reply by touch 4: move to `nurture` state, do not message for 90 days.

## Compliance

- Public-sector / regulated prospects: route through `/compliance-check` before send.
- If the operator's day job ({{EMPLOYER}}) has any relationship with the prospect's org, hard block.
- Log every send in `04-pipeline/_outreach-log.md` with timestamp, channel, message hash.
