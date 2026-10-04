---
name: github-create-repo-project-with-column-and-card
description: Create a repository project, add a column to it, and create a card in that column.
api: openapi/github-projects-api-openapi.yml
operations:
- projects/create-for-repo
- projects/create-column
- projects/create-card
generated: '2026-10-03'
method: generated
generator: extract-docs-artifacts.py skills (local)
source: openapi/github-projects-api-openapi.yml ; every operationId checked against the contract
---

# github-create-repo-project-with-column-and-card

Create a repository project, add a column to it, and create a card in that column.

## Steps

1. 1. `projects/create-for-repo` – requires the request body fields defined by the API (e.g., `name`, `body`, `state`).
2. 2. `projects/create-column` – requires the request body field `name` for the new column.
3. 3. `projects/create-card` – requires the request body fields `note` or `content_id` and `content_type` for the new card.

## Rules

- Auth: Include a Bearer token in the `Authorization` header as defined by the `bearerHttpAuthentication` scheme.
- Rate limit: 60 requests per hour; exceeding the limit returns no specific HTTP status code.
