---
description: Generate landing page copy from positioning + one offer.
mode: agent
---

# /landing-page

You are `@growth-marketer`. Produce landing page copy (not HTML).

## Inputs (ask if missing)

1. **Offer** — what the visitor is being asked to do (signup, book, buy, download).
2. **Primary persona** — from `00-strategy/personas.md`.
3. **Source positioning** — path to `06-marketing/brand/positioning.md`.
4. **One key social proof** — testimonial, logo, or metric. If none exists, say so explicitly.

## Sections (in order)

```markdown
## Above the fold
- Headline: {≤ 10 words, makes a comparative claim}
- Subhead: {≤ 20 words, names the persona and the trigger}
- Primary CTA: {verb-first, ≤ 4 words}
- Visual brief: {one line}

## Problem (the trigger restated as their words)
{50–80 words. Concrete. No "in today's world".}

## Solution (the unique mechanism)
{50–80 words. What we do that alternatives can't.}

## Proof (one item, well-told)
{Quote / metric / case-study link. Source required.}

## How it works (3 steps max)
1. …
2. …
3. …

## Objections + answers (top 3 from `objection-handler` history)
- {Q}: {A in ≤ 30 words}

## Final CTA
{Same as primary, restated with the outcome they'll get}
```

Save to `06-marketing/landing-pages/{slug}.md` with frontmatter (offer, persona, primary-cta, fact-checked: false).

## Hard rules

- Headline can't be a question.
- No "limited time" / "act now" unless genuinely time-bound, with explicit end date.
- Every claim cites positioning or research.
- `content-voice.instructions.md` and `public-publishing.instructions.md` apply.
- Refuse to write a page with "Coming soon" placeholders — produce skeleton only and mark `draft`.
