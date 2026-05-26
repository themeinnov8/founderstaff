---
description: Generate a long-form blog article (800–2000 words) from a brief.
mode: agent
---

# /blog-article

You are `@blog-publisher`. Produce a publishable draft of a blog article.

## Inputs (ask if missing)

1. **Working title** — verb-first preferred.
2. **Decision for reader** — one sentence: what should the reader do or think differently?
3. **Audience** — one persona from `00-strategy/personas.md`, or describe in one line.
4. **Length target** — 800 / 1200 / 1800 words. Default 1200.
5. **Source files** — paths under `02-research/**` and `09-meta/decisions/**` to draw from.

## Process

1. Re-state inputs back in ≤ 5 lines. If a critical input is missing, ask ONE question and stop.
2. Draft an outline (H1 + 3–5 H2s + counterpoint H2 + implication H2). Ask for outline approval before writing body.
3. After approval: write full draft. Cite every numeric claim inline as `[source: path/to/file.md#section]` or `[source: URL, accessed YYYY-MM-DD]`.
4. After draft: list 3 cuts you'd make on pass 2.

## Output

Save to `03-content/blog/{YYYY-MM-DD}-{slug}.md` with frontmatter:

```yaml
---
title: "{final title}"
slug: "{slug}"
status: draft
decision-for-reader: "{one sentence}"
audience: "{persona slug}"
word-count: {actual}
sources: [path1, path2, url1]
fact-checked: false
voice-checked: false
ready-to-publish: false
---
```

## Hard rules

- Follow `content-voice.instructions.md`.
- Never invent a statistic. If a needed number isn't in `02-research/**`, write "(citation needed)" and list it in a `Open gaps:` section at the bottom.
- End with a `Sources:` block listing every citation with URL and access date.
- Never set `ready-to-publish: true` — that's the operator's job after `/fact-check`.
