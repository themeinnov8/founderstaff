# `.platform/` — founderstaff control plane for this workspace

This folder makes the current workspace a **founderstaff-managed business OS**.

| File | Role |
|------|------|
| `skills.manifest.yaml` | What you *want* installed (upstream, packs, extras, disabled). Hand-edited. |
| `platform.config.json` | Your tokens (`BRAND`, `OPERATOR`, ...). Copy from `.template`. Never commit secrets. |
| `skills.lock.json` | What's *actually* installed right now (versions + hashes). Auto-written. |
| `relearn.py` | Thin one-command wrapper. Pulls upstream, syncs skills into `.github/`. |

## Quickstart

```bash
cp .platform/platform.config.json.template .platform/platform.config.json
# edit your tokens
python .platform/relearn.py
```

## Adding a new pack

```bash
python .platform/relearn.py --pack n8n
```

## Status

```bash
python .platform/relearn.py --status
```

## What it does

1. `git pull origin main` on the cached upstream clone (`~/.founderstaff/cache/...`).
2. Resolves your packs + dependencies into a skill list.
3. Substitutes tokens from `platform.config.json`.
4. Writes resolved skills into this workspace's `.github/chatmodes/`, `.github/prompts/`, `.github/instructions/`.
5. Updates `skills.lock.json`.

Local edits to files in `.github/` are **detected by hash and never overwritten** — rename or delete first to accept an upstream update.
