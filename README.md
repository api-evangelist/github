# GitHub (github)
GitHub is a cloud-based platform for software development and version control, built on Git. It enables developers to store, manage, and collaborate on code. In addition to Gits distributed version control, GitHub offers access control, bug tracking, feature requests, task management, continuous integration, and wikis for projects. Headquartered in California, it has operated as a subsidiary of Microsoft since 2018.

**URL:** [Visit APIs.json URL](https://raw.githubusercontent.com/api-search/code/main/_apis/github/apis.md)

## Scope

- **Type:** Contract 
- **Position:** Consuming 
- **Access:** 3rd-Party 

## Tags:

 - Code, Source Control, Software Development, Platform, Pipelines, T1

## Timestamps

- **Created:** 2024/04/14 
- **Modified:** 2025-12-23 

## APIs

### GitHub App API
The GitHub App API is the set of REST/GraphQL endpoints and webhooks that lets a GitHub App securely integrate with and automate work across GitHub. Apps authenticate with a shortlived JSON Web Token and exchange it for installation access tokens to act on specific repositories or organizations with finegrained, leastprivilege permissions, or use user-to-server OAuth to act on behalf of a user when needed. Through the API, an app can manage its installations, control which repositories it has access to, and read/write resources like issues, pull requests, commits, checks, deployments, and releases, as well as report status and check results. Webhooks deliver event payloads (for example, pushes and PR activity) so the app can react in real time, and app manifests enable streamlined, oneclick setup. In short, it provides the permissionscoped surface for building secure bots, CI/CD integrations, and other automations on GitHub.

**Human URL:** [https://docs.github.com/en/rest/apps?apiVersion=2022-11-28](https://docs.github.com/en/rest/apps?apiVersion=2022-11-28)

**Base URL:** [https://api.github.com](https://api.github.com)


#### Tags:

 - Applications

#### Properties

- [OpenAPI](properties/github-app-api-openapi.yml)
- [Documentation](https://docs.github.com/en/rest/apps)
### GitHub Authorization API
The GitHub Authorization (OAuth Authorizations) API historically let you programmatically create, list, inspect, and revoke access tokens for a user or OAuth applicationsetting scopes, verifying token validity, rotating or deleting tokens, and generally managing what an app could do on a users behalf. It was commonly used with basic authentication (and 2FA) to mint personal access tokens and to manage OAuth app grants. For security reasons, these endpoints have been deprecated and disabled on GitHub.com; today, apps should use modern authorization flows (OAuth web or device flow) or GitHub Apps with finegrained permissions, and manage personal access tokens via the web UI or the current OAuth application endpoints for token verification and revocation.

**Human URL:** [https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28](https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28)

**Base URL:** [https://api.github.com](https://api.github.com)


#### Tags:

 - Authorization, Authentication

#### Properties

- [OpenAPI](properties/github-auth-api-openapi.yml)
- [Documentation](
https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api)
### GitHub Code of Conduct API
GitHubs Code of Conduct API lets apps discover and retrieve the community codes of conduct that GitHub supports and see which one a repository has adopted. Through REST endpoints, clients can list available templates (like the Contributor Covenant), fetch a specific code by key, and read a repositorys code-of-conduct metadata and text, including fields such as name, key, URL, and body. This enables tooling to display community standards, audit or report adoption, and bootstrap repo files. Some endpoints are (or have been) in preview and may require a special Accept header, authentication is needed for private repositories, and updates are not done via the API but by committing the file to the repo.

**Human URL:** [https://docs.github.com/en/rest/codes-of-conduct/codes-of-conduct?apiVersion=2022-11-28](https://docs.github.com/en/rest/codes-of-conduct/codes-of-conduct?apiVersion=2022-11-28)

**Base URL:** [https://api.github.com](https://api.github.com)


#### Tags:

 - Code of Conduct

#### Properties

- [OpenAPI](properties/github-code-of-conduct-api-openapi.yml)
- [Documentation](https://docs.github.com/en/rest/codes-of-conduct/codes-of-conduct)
### GitHub Emojis API
The GitHub Emojis API is a simple REST endpoint (GET /emojis or https://api.github.com/emojis) that returns a JSON dictionary mapping emoji shortcodes (like "smile" or "octocat") to the image URLs GitHub uses to render them. It covers both standard Unicode emoji and GitHub-specific custom ones, enabling clients to power emoji pickers, autocomplete for :shortcodes:, validation, or server-side rendering in apps that mirror GitHubs formatting. The endpoint is public and requires no auth, but using authentication increases rate limits; results change infrequently, so caching is recommended. Note that this list is broader than the specific set allowed for Reactions, which has its own constraints.

**Human URL:** [https://docs.github.com/en/rest/emojis?apiVersion=2022-11-28](https://docs.github.com/en/rest/emojis?apiVersion=2022-11-28)

**Base URL:** [https://api.github.com](https://api.github.com)


#### Tags:

 - Emojis

#### Properties

- [OpenAPI](openapi/github-emojis-openapi.yml)
- [Documentation](https://docs.github.com/en/rest/emojis)
### GitHub Events API
The GitHub Events API provides a read-only feed of recent activity on GitHub, exposing structured event objects you can poll to see what happened across the platform or within a specific repository, organization, or user account. It covers many event typessuch as pushes, pull requests, issues, comments, releases, stars, forks, and membership changeseach with consistent metadata (actor, repo, type, payload, timestamps, IDs). Endpoints like /events, /repos/{owner}/{repo}/events, /orgs/{org}/events, and user/received variants let you scope activity, and authenticated calls include private events youre authorized to view. Its useful for dashboards, analytics, and lightweight monitoring, but its not a streaming feed: events are transient, must be paginated and polled, are rate-limited, and arent guaranteed to be complete over long periods. For real-time reaction to changes, GitHub recommends Webhooks; for historical analyses, external archives or data exports are better suited.

**Human URL:** [https://docs.github.com/en/rest/activity/events?apiVersion=2022-11-28](https://docs.github.com/en/rest/activity/events?apiVersion=2022-11-28)

**Base URL:** [https://api.github.com](https://api.github.com)


#### Tags:

 - Events

#### Properties

- [OpenAPI](properties/github-events-api-openapi.yml)
### GitHub Feeds API
GitHubs Feeds API lets you programmatically discover the Atom feed URLs for GitHub activity thats relevant to you, such as the global timeline, a specific users activity, the authenticated users public and private activity, organization activity, and security advisories. It doesnt return events directly; instead, it provides the correct, authentication-aware links you can subscribe to with any RSS/Atom reader to receive updates like new issues, pull requests, comments, releases, and other public or authorized activity. Unauthenticated calls expose only public feeds, while authenticated calls include private feeds youre allowed to see. Clients typically fetch those feed URLs on an interval and use ETags for efficient polling, making it a simple way to integrate GitHub activity into dashboards, readers, or notification systems.

**Human URL:** [https://docs.github.com/en/rest/activity/feeds?apiVersion=2022-11-28](https://docs.github.com/en/rest/activity/feeds?apiVersion=2022-11-28)

**Base URL:** [https://api.github.com/](https://api.github.com/)


#### Tags:

 - Feeds

#### Properties

- [OpenAPI](properties/github-feeds-api-openapi.yml)
### GitHub Gists API
The GitHub Gists API lets you programmatically manage gistslightweight code snippets and notesover HTTP. You can create gists (public or secret/unlisted), read individual gists, list public gists, your own, a users, and those youve starred, fetch raw file contents, view version history and commits, update gists by adding/renaming/removing files or changing descriptions, and delete them. It also supports forking, starring/un-starring and checking star status, plus full CRUD for gist comments. Responses include metadata such as owner, files, visibility, timestamps, and revision SHAs, with pagination and conditional requests available. Public gists are readable without authentication; modifying gists or accessing private data requires an access token with the gist scope, and standard GitHub REST rate limits apply.

**Human URL:** [https://docs.github.com/en/rest/gists?apiVersion=2022-11-28](https://docs.github.com/en/rest/gists?apiVersion=2022-11-28)

**Base URL:** [https://api.github.com/](https://api.github.com/)


#### Tags:

 - Gists, Code, Artifacts

#### Properties

- [OpenAPI](properties/github-gists-api-openapi.yml)
### GitHub Gitignore Templates API
The GitHub Gitignore Templates API is a REST interface that lets you discover and fetch canonical .gitignore templates maintained by GitHub, so you can programmatically create ignore files tailored to specific languages, frameworks, IDEs, or operating systems. It provides endpoints to list all available template names and to retrieve the full content of a chosen template (for example, Node, Python, macOS, or VisualStudio) via GET /gitignore/templates and GET /gitignore/templates/{name}. The responses include the templates name and the text to write into .gitignore, making it easy to scaffold new repositories, standardize ignore rules across teams, and prevent accidental commits of build artifacts, dependencies, or OS/IDE files; its accessible publicly, with authentication available for higher rate limits.

**Human URL:** [https://docs.github.com/en/rest/gitignore?apiVersion=2022-11-28](https://docs.github.com/en/rest/gitignore?apiVersion=2022-11-28)

**Base URL:** [https://api.github.com](https://api.github.com)


#### Tags:

 - Templates, Gitignore

#### Properties

- [OpenAPI](properties/github-gitignore-templates-api-openapi.yml)
### GitHub Installation API
The GitHub Installation API is part of the GitHub Apps platform and lets an app understand and manage where its installed and what it can access, and act on behalf of that installation. Using these endpoints, an app can list its installations, fetch details for a specific installation, enumerate the repositories granted to it, and (when the app is configured for selected repositories) add or remove repository access. Critically, it allows the app to exchange its JWT for shortlived installation access tokens that carry the installations permissions and repository scope; those tokens are then used to call GitHubs REST or GraphQL APIs or to perform Git operations over HTTPS. All actions are constrained by the permissions defined in the apps manifest and the repositories selected at install time, ensuring leastprivilege access. In short, this API is how a GitHub App securely discovers its tenants (user/org accounts), scopes its access, and performs work on their repositories without acting as an end user.

**Base URL:** [https://api.github.com/](https://api.github.com/)


#### Tags:

 - Installations

#### Properties

- [OpenAPI](properties/github-installation-api-openapi.yml)
### GitHub Issues API
The GitHub Issues API lets you programmatically manage issue tracking on GitHub, enabling you to list and filter issues across repositories, create and edit issues, change their state (open/closed), and manage assignees, labels, and milestones. It supports adding, updating, and deleting comments; applying reactions; locking or unlocking conversations; and viewing issue events and timelines for auditing and automation. You can search issues, transfer them between repositories, and subscribe to notifications, and you can receive updates via webhooks. The API is available through both REST and GraphQL, with authentication and pagination/rate limiting, making it useful for building triage bots, dashboards, reports, and custom workflow automations.

**Human URL:** [https://docs.github.com/en/rest/issues?apiVersion=2022-11-28](https://docs.github.com/en/rest/issues?apiVersion=2022-11-28)

**Base URL:** [https://api.github.com/](https://api.github.com/)


#### Tags:

 - Issues

#### Properties

- [OpenAPI](properties/github-issues-api-openapi.yml)
### GitHub Licenses API
The GitHub Licenses API lets you programmatically discover and retrieve open source license information across GitHub. It provides endpoints to list the common licenses GitHub supports, get detailed metadata and the canonical text for a specific license (by its SPDX identifier), and fetch the detected license for a given repository. Responses include machine-readable fields such as name, key, spdx_id, description, and the permissions/conditions/limitations that summarize how a license can be used, plus the full license text/template you can render in your app. This makes it useful for compliance checks, inventory and reporting, helping users choose a license, and validating or displaying repository licensing in developer tools.

**Human URL:** [https://docs.github.com/en/rest/licenses?apiVersion=2022-11-28](https://docs.github.com/en/rest/licenses?apiVersion=2022-11-28)

**Base URL:** [https://api.github.com/](https://api.github.com/)


#### Tags:

 - Licenses

#### Properties

- [OpenAPI](properties/github-licenses-api-openapi.yml)
### GitHub Enterprise Management API
The GitHub Enterprise Management API lets administrators automate and integrate the operational and security management of their enterprise on GitHub. It covers tasks like provisioning and governing organizations, users, and teams; enforcing policies for repositories, security, and GitHub Actions; integrating identity and access management via SSO/SCIM; retrieving audit logs and usage data for compliance and billing; and managing self-hosted runners. For GitHub Enterprise Server, it also includes Management Console endpoints to configure instance settings (such as TLS, SMTP, and clustering), apply licenses, monitor health, and coordinate backups and restores. By exposing these controls via REST, GraphQL, and SCIM endpoints, the API enables large-scale automation and integration with ITSM, IdPs, and SIEM tools.

**Human URL:** [https://docs.github.com/en/rest?apiVersion=2022-11-28](https://docs.github.com/en/rest?apiVersion=2022-11-28)

**Base URL:** [https://api.github.com/](https://api.github.com/)


#### Tags:

 - Management

#### Properties

- [OpenAPI](properties/github-manage-api-openapi.yml)
### GitHub Markdown API
The GitHub Markdown API is a REST service that converts Markdownespecially GitHub Flavored Markdowninto the same HTML GitHub renders in READMEs, issues, and pull requests, so external apps can display content consistently with GitHub. You POST Markdown to its endpoints (/markdown or /markdown/raw) and get back HTML; you can choose standard markdown or gfm mode and optionally supply a repository context so shorthand references (like #123), commit SHAs, user mentions, emoji, task lists, tables, and other GFM features resolve as they do on GitHub. Its stateless and rate-limited, doesnt store your content, and returns HTML that your application should treat as untrusted and sanitize before inserting into a page.

**Human URL:** [https://docs.github.com/en/rest/markdown?apiVersion=2022-11-28](https://docs.github.com/en/rest/markdown?apiVersion=2022-11-28)

**Base URL:** [https://api.github.com/](https://api.github.com/)


#### Tags:

 - Markdown

#### Properties

- [OpenAPI](properties/github-markdown-api-openapi.yml)
- [Documentation](https://docs.github.com/en/rest/markdown)
### GitHub Meta API

Use the REST API to get meta information about GitHub, including the IP
addresses of GitHub services.

**Human URL:** [https://docs.github.com/en/rest/meta?apiVersion=2022-11-28](https://docs.github.com/en/rest/meta?apiVersion=2022-11-28)

**Base URL:** [https://api.github.com/](https://api.github.com/)


#### Tags:

 - Metadata

#### Properties

- [OpenAPI](properties/github-meta-api-openapi.yml)
- [Documentation](https://docs.github.com/en/rest/meta)
### GitHub Networks API
GitHubs Networks API lets you retrieve a stream of public activity that occurs across a repositorys network, meaning the original repo and all of its forks. Exposed via the Events API (for example, listing events for /networks/{owner}/{repo}/events), it returns the same event types you see in other GitHub event feedspushes, pull requests, issues, releases, and moreaggregated across every repo in that fork family. This makes it useful for monitoring whats happening across forks, building dashboards or notifications that track downstream and upstream changes, and analyzing collaboration patterns. Results are read-only, public-only, paginated, and subject to standard GitHub API rate limits.

**Human URL:** [https://docs.github.com/en/rest?apiVersion=2022-11-28](https://docs.github.com/en/rest?apiVersion=2022-11-28)

**Base URL:** [https://api.github.com/](https://api.github.com/)


#### Tags:

 - Networks

#### Properties

- [OpenAPI](properties/github-networks-api-openapi.yml)
### GitHub Notifications API
This GitHub REST API allows you to programmatically manage your GitHub notifications, which include updates on issues, pull requests, and commits. The API requires authentication via a personal access token (classic) and needs either the notifications or repo scope to function. 

**Human URL:** [
https://docs.github.com/en/rest/activity/notifications?apiVersion=2022-11-28](
https://docs.github.com/en/rest/activity/notifications?apiVersion=2022-11-28)

**Base URL:** [https://api.github.com/](https://api.github.com/)


#### Tags:

 - Notifications

#### Properties

- [OpenAPI](properties/github-notifications-api-openapi.yml)
### GitHub Octocat API
The GitHub Octocat API is a playful, non-functional endpoint in GitHubs REST API that returns an ASCII-art rendering of the Octocat mascot as plain text. Its primarily meant for fun and demospeople often use it to sanity-check connectivity, see how the API formats responses and headers, or showcase simple requests without touching real repository data. It doesnt manage or expose any GitHub resources, and in some clients you can even supply a short message that the Octocat says. Like other public endpoints, its accessible without authentication but still subject to GitHubs standard rate limits.

**Human URL:** [https://github.com/octokit/octokit.js](https://github.com/octokit/octokit.js)

**Base URL:** [https://api.github.com/](https://api.github.com/)


#### Tags:

 - Octocat

#### Properties

- [OpenAPI](properties/github-octocat-api-openapi.yml)
### GitHub Organization API
The GitHub Organization API lets you programmatically administer and integrate with organizations on GitHub, spanning both REST and GraphQL. It covers core governance tasks such as reading and updating org settings and policies, managing members and outside collaborators, sending invitations and assigning roles, organizing teams and their permissions, and controlling repository access at scale. It also supports operational and security workflows, including organization webhooks, audit log retrieval, required security and compliance settings (e.g., Dependabot and secret scanning policies), finegrained personal access token and GitHub App installation approvals, and management of Actions resources like selfhosted runners. Where applicable, it integrates with SSO/SCIM provisioning and exposes usage/billing and installation dataenabling endtoend automation of org operations, security, and permissions.

**Human URL:** [https://docs.github.com/en/rest/orgs?apiVersion=2022-11-28](https://docs.github.com/en/rest/orgs?apiVersion=2022-11-28)

**Base URL:** [https://api.github.com/](https://api.github.com/)


#### Tags:

 - Organizations

#### Properties

- [OpenAPI](properties/github-org-api-openapi.yml)
### GitHub Projects API
The GitHub Projects API enables developers to programmatically create and manage GitHub Projects, which are flexible tools for planning and tracking work using customizable boards, tables, and roadmaps. Through these REST API endpoints, you can create projects at the repository, organization, or user level, add and organize items like issues and pull requests, manage project fields and views, update item statuses and metadata, and automate project workflows. This API is particularly useful for integrating project management functionality into custom applications, automating project updates based on repository events, building dashboards and reporting tools, or synchronizing GitHub project data with external project management systems.

**Base URL:** [https://api.github.com/](https://api.github.com/)


#### Tags:

 - Projects

#### Properties

- [OpenAPI](properties/github-projects-api-openapi.yml)
### GitHub Rate Limit API
GitHubs Rate Limit API lets you programmatically see how much API quota you have left and when it will reset, so you can avoid hitting API rate limit exceeded errors. By calling the /rate_limit endpoint (or by reading the X-RateLimit headers on any response), you get current limit, remaining, used, and reset time for different resource categories (for example, core REST, search, and GraphQL). The values are scoped to how you authenticate (unauthenticated IP, personal access token, OAuth app, or GitHub App installation) and can vary by resource type and plan. Apps typically use this information to throttle requests, prioritize work, or back off and retry after the reported reset time. Note that separate secondary/abuse protections may still apply and arent reflected by this endpoint.

**Human URL:** [
https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28](
https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28)

**Base URL:** [https://api.github.com/](https://api.github.com/)


#### Tags:

 - Rate Limits

#### Properties

- [OpenAPI](openapi/github-rate-limit-openapi.yml)
### GitHub Repos API
The GitHub Repos API is a set of REST endpoints that let you programmatically create, read, update, and delete repositories and their resources, giving you control over a repos lifecycle and configuration. You can list and search repositories for users or organizations; retrieve metadata (visibility, default branch, license), topics, and languages; manage collaborators, teams, and permissions; create, archive, transfer, fork, star, and watch; manage branches and branch protection rules, tags, releases and assets; read and write repository contents (files, directories, blobs), commits, and compares; configure webhooks and deploy keys; and access traffic, vulnerabilities, and community health metrics. It uses token-based authentication with scopes (such as repo) and is rate-limited, making it suitable for automation, dashboards, and CI/CD integrations.

**Human URL:** [https://docs.github.com/en/rest/repos?apiVersion=2022-11-28](https://docs.github.com/en/rest/repos?apiVersion=2022-11-28)

**Base URL:** [https://api.github.com/](https://api.github.com/)


#### Tags:

 - Repos

#### Properties

- [OpenAPI](properties/github-repos-api-openapi.yml)
### GitHub SCIM API
GitHubs SCIM API implements the SCIM 2.0 standard to automate user lifecycle management from an identity provider (such as Entra ID/Azure AD, Okta, or OneLogin) to GitHub Enterprise Cloud. It lets you provision, update, suspend/reactivate, and deprovision users, keeping their GitHub access in sync with your IdP. For organizations that use SAML SSO, SCIM manages external identities and org membership; for enterprises using Enterprise Managed Users, it creates and maintains the managed user accounts themselves. Typical operations include creating users, updating profile attributes, and setting a users active state to revoke or restore access. SCIM complements SSO (authentication) by handling authorization and account lifecycle; it doesnt manage repositories or granular permissions beyond controlling whether a user exists and has access to the org or enterprise.

**Human URL:** [
https://docs.github.com/en/enterprise-cloud@latest/rest/scim?apiVersion=2022-11-28](
https://docs.github.com/en/enterprise-cloud@latest/rest/scim?apiVersion=2022-11-28)

**Base URL:** [https://api.github.com/](https://api.github.com/)


#### Tags:

 - SCIM

#### Properties

- [OpenAPI](openapi/github-scim-openapi.yml)
### GitHub Search API
The GitHub Search API lets you programmatically find and filter content across GitHubincluding repositories, code, issues and pull requests, commits, users, topics, and labelsusing a powerful query language with qualifiers (for example by language, stars, forks, org/user, path/filename, label, state, author, or committer). It returns ranked, paginated JSON results with total counts and optional sorting, so you can discover projects, locate code snippets, triage issues, or audit activity at scale. Authenticated requests enjoy higher rate limits and can search private resources the token can access, and the API returns only the first 1,000 matching results for any query.

**Human URL:** [https://docs.github.com/en/rest/search/search?apiVersion=2022-11-28](https://docs.github.com/en/rest/search/search?apiVersion=2022-11-28)

**Base URL:** [https://api.github.com/](https://api.github.com/)


#### Tags:

 - Search, Discovery

#### Properties

- [OpenAPI](properties/github-search-api-openapi.yml)
### GitHub Setup API
The GitHub Setup API is the administrative interface for GitHub Enterprise Server that lets you automate tasks normally done in the Management Console during first-time and ongoing configuration. It provides endpoints to upload and apply your license, set the hostname and TLS certificates, configure system services like SMTP, create or reset the initial admin credentials, start and monitor reconfiguration runs, and query setup status and health. This API is intended for bootstrapping and repeatable provisioning (for example, cloud deployment or disaster recovery) and is restricted to authorized administrators. It is separate from the public GitHub REST and GraphQL APIs used for repositories, issues, and other developer workflows.

**Human URL:** [https://docs.github.com/en/rest/using-the-rest-api/getting-started-with-the-rest-api?apiVersion=2022-11-28](https://docs.github.com/en/rest/using-the-rest-api/getting-started-with-the-rest-api?apiVersion=2022-11-28)

**Base URL:** [https://api.github.com/](https://api.github.com/)


#### Tags:

 - Setup

#### Properties

- [OpenAPI](openapi/github-setup-openapi.yml)
### GitHub Teams API
The GitHub Teams API lets you programmatically manage organization teams and the access they grant. With it, you can create, update, and delete teams; organize parent/child team hierarchies; add or remove members and maintainers; send and manage invitations; and list or audit team membership. It also lets you grant, adjust, or revoke a teams permissions to repositories (and, where applicable, projects), enabling consistent, leastprivilege access control at scale. For enterprise setups, it supports syncing teams with external identity provider groups. These capabilities are available via REST and GraphQL, and require appropriate organization admin or team maintainer permissions and token scopes.

**Base URL:** [https://api.github.com/](https://api.github.com/)


#### Tags:

 - Teams

#### Properties

- [OpenAPI](openapi/github-teams-openapi.yml)
### GitHub Zen API
The GitHub Zen API is a playful REST endpoint that returns a random aphorism from the Zen of GitHub, such as Keep it logically awesome. Each request to GET https://api.github.com/zen responds with a single plain-text line, making it useful for quick connectivity checks, demoing HTTP calls, or verifying authentication. It doesnt require auth, but you can include a token to benefit from higher rate limits. Because it returns just a simple string with minimal structure, it serves as a lightweight sanity check and a fun Easter egg within the GitHub API.


#### Tags:

 - Zen

#### Properties

- [OpenAPI](openapi/github-zen-openapi.yml)
### GitHub User API
The GitHub Users API (part of the REST API) lets applications read and, for the authenticated account, manage user-related data on GitHub. It can fetch public profiles for any user or the authenticated users private profile details, list a users public repositories and organizations, and view activity like followers and following. For the signed-in user it also supports actions such as updating profile metadata, following or unfollowing users, blocking users, and managing account artifacts like emails, SSH/GPG/signing keys, and linked social accounts. Endpoints honor pagination and conditional requests, and access to private data or write operations requires authentication with appropriate token scopes. This makes it useful for building integrations that personalize experiences, synchronize account data, or automate account settings.

**Human URL:** [https://docs.github.com/en/rest/users?apiVersion=2022-11-28](https://docs.github.com/en/rest/users?apiVersion=2022-11-28)

**Base URL:** [https://api.github.com/](https://api.github.com/)


#### Tags:

 - Users

#### Properties

- [OpenAPI](properties/github-users-api-openapi.yml)

## Common Properties

- [Plans](https://github.com/pricing)
- [RoadMap](https://github.com/github/roadmap)
- [About](https://github.com/about)
- [Documentation](https://docs.github.com/en/get-started/exploring-integrations/about-building-integrations)
- [Status](https://www.githubstatus.com/)
- [CLI](https://cli.github.com/)
- [GitHubOrganization](https://github.com/github)
- [Support](https://support.github.com/)
- [Partners](https://github.com/partners/)
- [Partners](https://github.com/partners/)
- [TermsOfService](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service)
- [PrivacyPolicy](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement)
- [PrivacyPolicy](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement)
- [RateLimits](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28)
- [Pagination](https://docs.github.com/en/rest/using-the-rest-api/using-pagination-in-the-rest-api?apiVersion=2022-11-28)
- [Authentication](https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28)
- [GettingStarted](https://docs.github.com/en/rest/using-the-rest-api/getting-started-with-the-rest-api?apiVersion=2022-11-28)

## Maintainers

**FN:** API Evangelist

**Email:** info@apievangelist.com

