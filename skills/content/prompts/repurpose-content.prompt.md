---
description: Convert one source piece into N derivative formats (LinkedIn, X thread, newsletter teaser, YouTube short).
mode: agent
---

# /repurpose-content

You are `@content-creator`. Convert one source artifact into multiple channel-native pieces.

## Inputs (ask if missing)

1. **Source** — path under `03-content/**` or `02-research/**`.
2. **Target channels** — subset of: `linkedin-post`, `linkedin-carousel`, `twitter-thread`, `newsletter-teaser`, `youtube-short`.
3. **Spacing** — earliest day to publish each derivative (no two on the same day by default).

## Process

1. Read source end-to-end. Extract: (a) the one core claim, (b) 3–5 supporting beats, (c) the strongest concrete example.
2. For each target channel, route to the right specialist:
   - `linkedin-post` → `/linkedin-post` with the source as seed
   - `linkedin-carousel` → `/linkedin-carousel`
   - `youtube-short` → `/youtube-script` with format=short
   - `newsletter-teaser` → custom inline (no full issue)
3. Each derivative must reframe the angle — never paste-and-trim. If a channel adds no new value, drop it.

## Output

For each derivative: save under its channel folder. Then write a summary table:

```markdown
| Channel | File | Angle | Publish-not-before |
|---|---|---|---|
| linkedin-post | … | story | 2026-05-26 |
| youtube-short | … | contrarian | 2026-05-29 |
```

## Hard rules

- Never publish all derivatives same-day — cannibalizes reach.
- Never reuse the same hook line across channels.
- Source piece must be `ready-to-publish: true` before derivatives are queued.
- `content-voice.instructions.md` applies to every derivative.
