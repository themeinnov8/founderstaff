# founderstaff website

Marketing landing page + full documentation for [founderstaff.com](https://founderstaff.com).

## Stack

- **[Astro 5](https://astro.build/)** — static site generator
- **[Starlight](https://starlight.astro.build/)** — docs framework on top of Astro
- **[sharp](https://sharp.pixelplumbing.com/)** — image optimization

Zero runtime; all pages prerender to static HTML.

## Develop

```bash
cd web
npm install
npm run dev
```

Visit http://localhost:4321.

## Build

```bash
npm run build      # outputs to web/dist/
npm run preview    # serve the built site locally
```

## Structure

```
web/
├── astro.config.mjs                 # Starlight config, sidebar, edit links
├── src/
│   ├── assets/                      # static images (logo, etc.)
│   ├── content/
│   │   └── docs/                    # all docs pages (Starlight reads from here)
│   │       ├── index.mdx            # splash
│   │       ├── getting-started/
│   │       ├── agents/              # one page per pack
│   │       ├── rhythms/
│   │       ├── skills/
│   │       └── examples/            # 4 full walkthroughs
│   ├── content.config.ts            # docs collection schema
│   ├── pages/
│   │   └── index.astro              # marketing landing (replaces Starlight root)
│   ├── styles/
│   │   └── global.css               # brand CSS variable overrides
│   └── env.d.ts
└── public/
    ├── CNAME                        # founderstaff.com
    └── favicon.svg
```

## Deploy

Pushed to `main` with changes under `web/**` triggers [.github/workflows/deploy-web.yml](../.github/workflows/deploy-web.yml) which builds and deploys to GitHub Pages.

### One-time GitHub setup

1. Repo Settings → Pages → Source: **GitHub Actions**
2. Repo Settings → Pages → Custom domain: `founderstaff.com`, enable HTTPS once DNS resolves
3. DNS: point `founderstaff.com` A records to GitHub Pages IPs (or `CNAME` to `themeinnov8.github.io`)

## Content edits

- Marketing copy → [src/pages/index.astro](src/pages/index.astro)
- Docs pages → [src/content/docs/](src/content/docs/)
- Sidebar / nav → [astro.config.mjs](astro.config.mjs)
- Brand colors → [src/styles/global.css](src/styles/global.css)

## When the platform changes

Keep these in sync with the upstream platform:

| If you change... | Update... |
|---|---|
| `version.json` | `src/pages/index.astro` (header version pill, if shown) |
| `packs/*.pack.json` count | `src/content/docs/index.mdx` table, `src/content/docs/agents/index.md` table |
| Add/remove a pack | New page under `src/content/docs/agents/`, update sidebar in `astro.config.mjs` |
| Add a chatmode/prompt | Update relevant `src/content/docs/agents/<pack>.md` table |
| Skill IDs renamed | Search-and-replace across `src/content/docs/` |
