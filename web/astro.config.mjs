// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
  site: 'https://themeinnov8.github.io/founderstaff',
  base: '/founderstaff',
  integrations: [
    starlight({
      title: 'founderstaff',
      description:
        'An operating system for founders. 75 agentic skills across 10 packs. Works in GitHub Copilot and Claude Code.',
      logo: {
        src: './src/assets/logo.svg',
        alt: 'founderstaff',
        replacesTitle: false,
      },
      social: {
        github: 'https://github.com/themeinnov8/founderstaff',
      },
      editLink: {
        baseUrl:
          'https://github.com/themeinnov8/founderstaff/edit/main/web/src/content/docs/',
      },
      customCss: ['./src/styles/global.css'],
      sidebar: [
        {
          label: 'Getting Started',
          items: [
            { label: 'Concepts', link: '/getting-started/concepts/' },
            { label: 'Claude Code', link: '/getting-started/claude-code/' },
            { label: 'GitHub Copilot', link: '/getting-started/github-copilot/' },
          ],
        },
        {
          label: 'Agents',
          items: [
            { label: 'Overview', link: '/agents/' },
            { label: 'Core', link: '/agents/core/' },
            { label: 'Research', link: '/agents/research/' },
            { label: 'Content', link: '/agents/content/' },
            { label: 'Sales', link: '/agents/sales/' },
            { label: 'Marketing', link: '/agents/marketing/' },
            { label: 'Operations', link: '/agents/operations/' },
            { label: 'Delivery', link: '/agents/delivery/' },
            { label: 'Compliance', link: '/agents/compliance/' },
            { label: 'Finance', link: '/agents/finance/' },
            { label: 'Product', link: '/agents/product/' },
          ],
        },
        {
          label: 'Rhythms',
          items: [
            { label: 'Overview', link: '/rhythms/' },
            { label: 'Scheduling', link: '/rhythms/scheduling/' },
            { label: 'Councils (multi-agent)', link: '/rhythms/councils/' },
          ],
        },
        {
          label: 'Skills',
          items: [
            { label: 'Invoking skills', link: '/skills/invoking/' },
            { label: 'Packs', link: '/skills/packs/' },
            { label: 'Creating new skills', link: '/skills/creating-new/' },
          ],
        },
        {
          label: 'Examples',
          items: [
            { label: 'Overview', link: '/examples/' },
            { label: 'AI Consultancy', link: '/examples/ai-consultancy/' },
            { label: 'Indie SaaS', link: '/examples/indie-saas/' },
            { label: 'Content Creator OS', link: '/examples/content-creator/' },
            { label: 'Local Service Business', link: '/examples/local-service/' },
          ],
        },
      ],
    }),
  ],
});
