# How to write a founderstaff skill

A founderstaff "skill" is one markdown file with YAML frontmatter that Copilot reads natively from `.github/`.

## The three types

| Type | Location | Invoked as | When |
|---|---|---|---|
| `chatmode` | `skills/chatmodes/<id>.chatmode.md` | `@<id>` in chat | Persistent persona / agent |
| `prompt` | `skills/prompts/<id>.prompt.md` | `/<id>` in chat | One-shot task |
| `instructions` | `skills/instructions/<id>.instructions.md` | auto, via `applyTo` glob | Background guardrail |

## Anatomy

### Chatmode

```markdown
---
description: One sentence on what this persona does
tools: ['codebase', 'search', 'editFiles']
---
You are the {{BRAND}} [role]. Your job is...

## Rules
- ...
## Outputs
- ...
```

### Prompt

```markdown
---
description: One sentence on what this task produces
mode: agent
---
# {{role}} prompt

## Inputs you need
- ...

## Steps
1. ...

## Output format
...
```

### Instructions

```markdown
---
description: One sentence on what this guards
applyTo: 'folder/**'
---
# Rules for files matching folder/**

- Always ...
- Never ...
```

## Tokens

Anything in `{{UPPER_SNAKE}}` is substituted at sync time from the user's `.platform/platform.config.json#tokens`. Common tokens:

- `{{BRAND}}`, `{{BRAND_SHORT}}`, `{{BRAND_DOMAIN}}`, `{{BRAND_HANDLE}}`
- `{{OPERATOR}}`, `{{EMPLOYER_NAME}}`, `{{HOME_CURRENCY}}`, `{{HOURS_PER_WEEK}}`
- `{{EMPLOYER_FIREWALL_STRICTNESS}}`, `{{ANONYMOUS}}`

If a skill needs a new token, declare it in `requires_tokens` in `skills/index.json`.

## Quality bar

- One screen of frontmatter + body for prompts. Two screens max for chatmodes.
- Concrete output format (numbered list, table, code block) — never "structured response".
- One rule per line under `## Rules`. No prose paragraphs in guardrails.
- Versionable: a copy tweak is a patch. New behavior is a minor. Renaming inputs is a major.

## Where to find examples

- Simplest prompt: [skills/prompts/next-best-action.prompt.md](../skills/prompts/next-best-action.prompt.md)
- Persistent persona: [skills/chatmodes/chief-of-staff.chatmode.md](../skills/chatmodes/chief-of-staff.chatmode.md)
- Background guardrail: [skills/instructions/research-quality.instructions.md](../skills/instructions/research-quality.instructions.md)
