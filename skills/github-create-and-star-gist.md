---
name: github-create-and-star-gist
description: Create a new gist and star it for the authenticated user.
api: openapi/github-gists-api-openapi.yml
operations:
- gists/create
- gists/star
- gists/get
generated: '2026-10-03'
method: generated
generator: extract-docs-artifacts.py skills (local)
source: openapi/github-gists-api-openapi.yml ; every operationId checked against the contract
---

# github-create-and-star-gist

Create a new gist and star it for the authenticated user.

## Steps

1. 1. Call `gists/create` with the request body fields `description`, `public`, and `files`.
2. 2. Call `gists/star` with the path parameter `gist_id` returned from the create step.
3. 3. Call `gists/get` with the same `gist_id` to verify the gist was created and starred.

## Rules

- Auth: Include a Bearer token in the `Authorization` header as defined by the `bearerHttpAuthentication` scheme.
- Rate limit: 60 requests per hour; exceeding this returns no specific HTTP status code.
- Idempotency: The `gists/star` operation is idempotent – starring an already‑starred gist has no additional effect.
