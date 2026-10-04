---
name: github-create-org-repo-and-list-branches
description: Create a new repository in an organization and then list its branches.
api: openapi/github-repos-api-openapi.yml
operations:
- repos/create-in-org
- repos/list-branches
generated: '2026-10-03'
method: generated
generator: extract-docs-artifacts.py skills (local)
source: openapi/github-repos-api-openapi.yml ; every operationId checked against the contract
---

# github-create-org-repo-and-list-branches

Create a new repository in an organization and then list its branches.

## Steps

1. 1. Call `repos/create-in-org` with the `org` path parameter and a JSON body containing at least `name` (the repository name) and optional settings; include the `Authorization: Bearer <token>` header.
2. 2. Call `repos/list-branches` with the `owner` (the organization name) and `repo` (the newly created repository name) path parameters; include the `Authorization: Bearer <token>` header.

## Rules

- Authentication: Use the `bearerHttpAuthentication` scheme – send `Authorization: Bearer <token>` header with each request.
- Rate limiting: Maximum 60 requests per hour; exceeding this returns no specific HTTP status code (as documented).
- Idempotency: The `repos/create-in-org` operation is not idempotent; repeated calls with the same name will result in a conflict.
- Pagination: Not applicable for these operations.
