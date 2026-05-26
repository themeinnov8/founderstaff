---
description: Voice, tone, and never-do rules for any content destined for public publishing.
applyTo: "03-content/**,06-marketing/**"
---

# content-voice

These rules apply to any draft created under `03-content/**` or `06-marketing/**`.

## Voice (default — override per brand)

- First-person singular when {{OPERATOR}} is the byline; first-person plural ("we") when {{BRAND}} is the byline.
- Concrete > abstract. Numbers, names, specifics. No "in today's fast-paced world".
- One claim per paragraph. Lead with the punchline.
- Sentence length: median ≤ 18 words. No run-ons.

## Tone

- Confident, not boastful. Curious, not credulous. Direct, not blunt.
- Allowed: dry wit, mild self-deprecation, technical precision.
- Banned: hype words (game-changing, revolutionary, unlock, supercharge, leverage), emoji-as-punctuation, "let's dive in", AI-tells ("in this article we will explore…").

## Never do

1. Invent statistics. If a number isn't cited from `02-research/**`, replace with a qualitative claim.
2. Quote a person without a verifiable source link.
3. Use a competitor's name negatively in published content.
4. Publish anything touching {{EMPLOYER}} without `/compliance-check` returning pass.
5. End with "Thoughts?" or "What do you think?" as the only CTA — give the reader something to actually do.

## Required artifacts before publish

- Source row in `03-content/_content-pipeline.md` exists and is in `ready` state.
- Fact-check pass logged via `/fact-check`.
- If the piece touches a client, written client approval logged in `09-meta/decisions/`.
