# Programmatic API Onboarding — GitHub

A single-file, zero-dependency Node.js (18+) CLI that reproduces SoundCloud's
`sc-api-auth.mjs` pattern for GitHub: register an application / obtain credentials
programmatically instead of clicking through a dashboard, so agents and developers
can onboard at the command line.

- Script: [`github-api-auth.mjs`](github-api-auth.mjs)
- Run `node github-api-auth.mjs --help` for usage and the required environment variables.
- Story / rationale: https://apievangelist.com/2026/08/17/github-app-manifest-browser-to-credentials/

Part of the API Evangelist "Programmatic API Onboarding for the Agentic Moment" series.
