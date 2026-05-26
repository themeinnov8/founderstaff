---
title: Invoking skills
description: How to call chatmodes, slash commands, and how always-on instructions work.
---

import { Aside } from '@astrojs/starlight/components';

Three skill types, three invocation patterns.

## Chatmodes — switch personas

A chatmode is a persistent persona with declared tools and scope. Switch into it with `@<name>`:

```
> @chief-of-staff
> I need to decide between pursuing client A or product feature B today.
```

The agent stays active until you switch out (`@another-agent`) or close the chat. They follow their declared `tools` whitelist and stay within their declared write scope.

**Discovery**:
- **Claude Code** → `.claude/agents/*.md`
- **GitHub Copilot** → `.github/chatmodes/*.chatmode.md`

## Prompts — slash commands

A prompt is a one-shot contracted command. Invoke with `/<name>`:

```
> /next-best-action
> /market-research scan competitors for X
> /linkedin-post topic="why solo founders should use rhythms"
```

Prompts can take arguments (free-form after the command name, or named via `key=value`). Each prompt's documentation declares its inputs.

**Discovery**:
- **Claude Code** → `.claude/commands/*.md`
- **GitHub Copilot** → `.github/prompts/*.prompt.md`

## Instructions — always on, scoped

Instructions are guardrails that load automatically when you work in a matching path. They have no invocation — they just apply.

```yaml
---
applyTo: "03-content/**, 06-marketing/**"
---
```

Above means: any time the agent edits or reads a file under `03-content/` or `06-marketing/`, the `content-voice` guardrails are in effect (banned patterns, voice rules, etc.).

**Discovery**:
- **Claude Code** → concatenated into `CLAUDE.md` with `@-imports` from there
- **GitHub Copilot** → `.github/instructions/*.instructions.md` (auto-applied by glob)

## Composition patterns

### Single agent + single prompt

```
> @chief-of-staff
> /next-best-action
```

### Cross-agent handoff

```
> @research-analyst
> /market-research SaaS pricing for solo developer tools

[research analyst delivers cited research note]

> @brand-strategist
> Read 02-research/saas-pricing.md and give me 3 positioning options.
```

### Pipeline

```
> /customer-interview prep for tomorrow's call with prospect
[script created]
[call happens; record raw notes]
> /meeting-notes
[structured notes]
> /discovery-call-recap update the pipeline
```

### Council

```
> /council quarterly-strategy
[5-phase multi-agent session]
```

## Hard rules across all skills

- **Scope is declared**. Chatmodes write only to declared paths. If an agent says "I'd need to edit `05-clients/`", check its scope first.
- **Compliance auto-routes**. Public-facing prompts call `/compliance-check` internally. You'll see it pass or flag; you don't have to invoke it manually.
- **Never invent**. Research/fact-check skills refuse to fabricate. They surface gaps as "Not yet tracked" or "Confidence: LOW".
- **One next action**. `@chief-of-staff` always returns ONE action with reasoning, not a buffet.
- **Local edits respected**. If you've hand-edited a synced skill file, `relearn.py` will skip it on update and warn you.

<Aside type="note" title="If a skill isn't responding as documented">
Run `python .platform/relearn.py --status` to see versions. If a file is locally modified, the lockfile will show it. To accept upstream: delete the file and re-sync.
</Aside>
