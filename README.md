# GitHub (github)
GitHub is the world's leading software development platform providing Git hosting, CI/CD, project management, package registry, security scanning, and AI-powered development tools with comprehensive REST and GraphQL APIs.

**URL:** [Visit APIs.json URL](https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/apis.yml)

**Run:** [Capabilities Using Naftiko](https://github.com/naftiko/fleet?utm_source=api-evangelist&utm_medium=readme&utm_campaign=company-api-evangelist&utm_content=repo)

## Tags:

 - CI/CD, Code, Developer Tools, Git, Open Source, Security, Social Coding

## Timestamps

- **Created:** 2024-01-01
- **Modified:** 2026-04-17

## APIs

65 APIs covering Apps, Actions, Code Scanning, Codespaces, Copilot, Dependabot, Discussions, Gists, Issues, Migrations, Organizations, Packages, Pages, Projects, Pull Requests, Releases, Repos, Search, Secret Scanning, Security Advisories, Teams, Users, Webhooks, and more.

See [apis.yml](apis.yml) for the complete inventory.

## Features

| Name | Description |
|------|-------------|
| REST API | Comprehensive REST API v3 for managing all GitHub resources. |
| GraphQL API | Flexible GraphQL API v4 for querying exactly the data you need. |
| Webhooks | Real-time event notifications for repository and org events. |
| GitHub Apps | Fine-grained integrations with installation tokens and webhooks. |
| GitHub Actions | CI/CD automation with API access to runs, jobs, and artifacts. |
| Packages | Package registry for npm, Maven, NuGet, Docker, and RubyGems. |
| Code Search | Search across repos, code, issues, PRs, and users. |
| Security | Dependabot, code scanning, secret scanning, and advisories. |
| Copilot | AI-powered code completion and chat APIs. |
| Projects | Project boards with custom fields and automation. |
| Codespaces | Cloud dev environments with API management. |
| Discussions | Community forums with categories and reactions. |

## Artifacts

### OpenAPI

44 OpenAPI specs in [openapi/](openapi/).

### JSON Schema

259 standalone JSON Schema files in [json-schema/](json-schema/).

### JSON Structure

259 JSON Structure files in [json-structure/](json-structure/).

### JSON-LD

- [GitHub Context](json-ld/github-context.jsonld) — 259 types, 451 properties

### Examples

259 example JSON files in [examples/](examples/).

## Capabilities

Naftiko capabilities organized as shared per-API definitions composed into customer-facing workflows.

### Shared Per-API Definitions

- [Repos](capabilities/shared/repos.yaml) — repositories, branches, commits, tags, releases
- [Issues](capabilities/shared/issues.yaml) — issues, comments, labels, milestones
- [Pull Requests](capabilities/shared/pull-requests.yaml) — PRs, reviews, review comments
- [Actions](capabilities/shared/actions.yaml) — workflows, runs, jobs, artifacts, secrets
- [Security](capabilities/shared/security.yaml) — code scanning, dependabot, secret scanning
- [Users](capabilities/shared/users.yaml) — users, emails, SSH keys, GPG keys
- [Organizations](capabilities/shared/orgs.yaml) — orgs, teams, members
- [Packages](capabilities/shared/packages.yaml) — packages, versions
- [Projects](capabilities/shared/projects.yaml) — projects, columns, cards
- [Search](capabilities/shared/search.yaml) — code, issues, repos, users search
- [Gists](capabilities/shared/gists.yaml) — gists, comments, forks
- [Apps](capabilities/shared/apps.yaml) — GitHub Apps, installations

### Workflow Capabilities

| Workflow | APIs Combined | Persona |
|----------|--------------|---------|
| [Source Control](capabilities/source-control.yaml) | Repos + Pull Requests | Developer |
| [CI/CD](capabilities/ci-cd.yaml) | Actions + Repos | DevOps Engineer |
| [Project Management](capabilities/project-management.yaml) | Issues + Projects + Search | Project Manager |
| [Security Operations](capabilities/security-operations.yaml) | Security | Security Engineer |
| [Community](capabilities/community.yaml) | Gists + Users + Orgs | Community Manager |
| [Platform Administration](capabilities/platform-administration.yaml) | Apps + Orgs + Packages | Platform Admin |

## Vocabulary

- [GitHub Vocabulary](vocabulary/github-vocabulary.yaml) — 12 resources, 2 APIs, 5 domains, 5 personas

## Rules

- [GitHub Spectral Rules](rules/github-spectral-rules.yml) — 20 rules

## Maintainers

**FN:** Kin Lane

**Email:** kin@apievangelist.com
