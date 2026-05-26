---
title: Content pack
description: Blog, LinkedIn, newsletter, YouTube generation in operator voice. Compliance-aware.
---

**Version**: `0.2.0` · **Skills**: 12 · **Requires**: `core`

## Chatmodes

| Agent | Role |
|---|---|
| `@content-creator` | Editorial director. Plans + briefs + routes; never writes long-form alone. |
| `@blog-publisher` | Long-form writer for blog posts. Citation-honest, voice-locked. |
| `@linkedin-ghostwriter` | LinkedIn posts + carousels in operator voice. Compliance-aware. |

## Prompts

| Command | What it does |
|---|---|
| `/blog-article` | Long-form blog draft (800-2000 words) with citation discipline |
| `/linkedin-post` | LinkedIn post in operator's voice with compliance gate |
| `/linkedin-carousel` | 5-10 slide LinkedIn carousel: caption + slide copy + visual brief |
| `/newsletter-issue` | Single newsletter issue from the week's notes + research |
| `/youtube-script` | Shootable YouTube script (short/standard/long) with B-roll cues |
| `/seo-optimize` | On-page SEO pass on a finished draft; never at the cost of voice |
| `/repurpose-content` | Convert one source piece into channel-native derivatives |

## Instructions

| Glob | Enforces |
|---|---|
| `03-content/**, 06-marketing/**` | Voice, tone, banned patterns |
| any final artifact to public channel | Pre-publish gate checklist |

## Typical activation

```
> /instantiate-agent content-creator
> /instantiate-agent linkedin-ghostwriter
> /schedule content-creator weekly day=sunday prompt="/newsletter-issue weekly digest"
> /schedule linkedin-ghostwriter weekdays prompt="/linkedin-post daily insight"
```

[← Back to agents overview](/agents/)
