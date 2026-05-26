---
description: Pre-publish gate for anything leaving the workspace on a public channel.
applyTo: "03-content/**/final/**,06-marketing/**/final/**"
---

# public-publishing

Applies to any artifact about to be posted on LinkedIn, a public blog, YouTube, newsletter, X, or any third-party platform under {{BRAND}}'s name.

## Pre-publish checklist (block on any fail)

1. **Voice pass** — `content-voice.instructions.md` rules satisfied.
2. **Fact-check** — `/fact-check` returns pass; cited sources resolve.
3. **Compliance** — `/compliance-check` returns pass against `09-meta/firewall.md`.
4. **Client mentions** — any named client has written consent in `05-clients/{slug}/_consent.md`.
5. **Employer mentions** — {{EMPLOYER}} and its competitors not named, not implied via job title or recent project.
6. **Self-attribution** — byline matches the channel (operator-personal vs {{BRAND}}-channel).
7. **Source disclosure** — if the piece uses AI-generated imagery or claims, disclosed per platform policy.

## Hard rules

- Never publish a draft that hasn't been read end-to-end at least once by {{OPERATOR}}.
- Never schedule publishing inside working hours of {{EMPLOYER}} timezone.
- Every publish event logs to `06-marketing/_publish-log.md` with channel, URL, hash of source markdown.

## Rollback protocol

- If a published piece is flagged post-hoc (correction, compliance, client complaint): take down within 4 working hours, file a decision record in `09-meta/decisions/`, do not re-publish without `/compliance-check` re-run.
