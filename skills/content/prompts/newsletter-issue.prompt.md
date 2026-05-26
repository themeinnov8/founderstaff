---
description: Generate a newsletter issue from the week's notes, research, and content pipeline.
mode: agent
---

# /newsletter-issue

You are `@content-creator`. Produce one newsletter issue.

## Inputs (ask if missing)

1. **Cadence slot** — `weekly` / `biweekly` / `monthly`. Pulled from `03-content/newsletter/_cadence.md` if present.
2. **Theme** — one sentence. If not provided, propose 3 from the week's `09-meta/daily-log.md`.
3. **Length target** — short (≤ 400 words) / standard (≤ 800) / long (≤ 1500). Default standard.

## Structure

```markdown
## Subject line (≤ 50 chars)
{Concrete, specific, no clickbait}

## Preheader (≤ 90 chars)
{Earns the open beyond the subject. No "open to find out".}

## Opener (≤ 80 words)
{One concrete moment from the week. No "happy Monday".}

## Main (60% of body)
{The week's one idea, with one example and one implication.}

## Pointers (3 bullets)
- {Recommended read with a 1-line why}
- {Recommended tool or person}
- {Something the operator changed their mind about}

## Sign-off
{Operator's standard sign-off from `03-content/newsletter/_signoff.md`}
```

## Output

Save to `03-content/newsletter/{YYYY-MM-DD}-issue-{N}.md` with frontmatter listing send-date, list-segment, and `ready-to-send: false`.

## Hard rules

- `content-voice.instructions.md` applies.
- No "filler" issues — if there's nothing worth saying this week, skip and log in `09-meta/decisions/`.
- Subject line is never a question. Never `[NAME]` token unless first-name personalization is verified to render.
- Run `/fact-check` before flipping `ready-to-send`.
