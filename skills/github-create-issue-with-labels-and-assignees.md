---
name: github-create-issue-with-labels-and-assignees
description: Create a new issue in a repository and immediately assign users and labels to it.
api: openapi/github-issues-api-openapi.yml
operations:
- issues/create
- issues/add-assignees
- issues/add-labels
generated: '2026-10-03'
method: generated
generator: extract-docs-artifacts.py skills (local)
source: openapi/github-issues-api-openapi.yml ; every operationId checked against the contract
---

# github-create-issue-with-labels-and-assignees

Create a new issue in a repository and immediately assign users and labels to it.

## Steps

1. 1. Call `issues/create` with the required fields `owner`, `repo`, `title`, and optional `body`.
2. 2. Call `issues/add-assignees` with `owner`, `repo`, `issue_number` (from step 1) and the `assignees` array.
3. 3. Call `issues/add-labels` with `owner`, `repo`, `issue_number` (from step 1) and the `labels` array.

## Rules

- Auth: Include a `Authorization: Bearer <token>` header (bearerHttpAuthentication).
- Rate limit: 60 requests per hour; exceeding returns no specific HTTP status code.
- Idempotency: `issues/create` is not idempotent; repeat calls will create duplicate issues.
- Errors: API returns standard GitHub error responses (e.g., 4xx for validation errors).
