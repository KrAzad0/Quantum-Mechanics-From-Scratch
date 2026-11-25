# Authentication, request flow, and credential handling

Reviewed on 26 November 2026. This document describes the code in this repository;
it does not assert that uninspected GitHub account or repository settings are configured.

## Conclusion

The paper atlas is a public static application. It has **no application login,
user database, password handling, session cookies, OAuth callback, protected API,
access tokens, refresh tokens, or API keys**. Its reading-progress tracker is a
local convenience, not an authenticated user account. Reading the notes and
running the numerical examples requires no Claude subscription or API credential.

Authentication exists in a separate place: GitHub authenticates maintainers and
GitHub Actions authenticates deployment to GitHub Pages.

## Components and evidence

| Component | Source | Responsibility |
| --- | --- | --- |
| Static entry point | [`index.html`](../index.html) | Loads local CSS, the hero image, paper data, storage helpers, and UI code. There is no sign-in form. |
| Paper corpus | [`papers.js`](../papers.js), `rawPapers`, `window.QM_PAPERS`, `window.QM_ERAS` | Contains the curated paper metadata and outgoing source links. No network client or secret configuration. |
| UI | [`app.js`](../app.js), `visible()`, `render()`, `open()`, `toggle()` | Filters and displays the corpus, opens a local dialog, and changes reading state in the browser. |
| Local persistence | [`storage.js`](../storage.js), `QM_STORAGE.createStore()` | Validates non-sensitive progress/theme data and handles unavailable browser storage. |
| Styling | [`styles.css`](../styles.css) | Local styling; no third-party font or CSS import. |
| Build and deployment | [`.github/workflows/pages.yml`](../.github/workflows/pages.yml) | Validates/stages the static files, then deploys through the GitHub Pages environment. |
| Pull-request checks | [`.github/workflows/ci.yml`](../.github/workflows/ci.yml) | Runs checks with read-only repository access. It does not deploy contributor branches. |

## Reader request flow

1. A browser requests the public page from GitHub Pages (or a local HTTP server).
2. The HTML references local static assets. The script order loads `papers.js`,
   then `storage.js`, then `app.js`.
3. `papers.js` constructs the in-memory corpus. `app.js` creates a storage helper,
   restores validated progress and theme, renders the filter buttons, and renders
   the paper cards.
4. Search, era filtering, ordering, paper dialogs, and progress changes run in the
   browser. The atlas has no `fetch`, XMLHttpRequest, WebSocket, or backend endpoint
   to receive the search query or reading history. A paper fragment such as
   `#paper-1` selects a local dialog; it is not a credential.
5. Selecting **Open original source** navigates to the paper's external website.
   That provider may have its own account system or paywall. Its authentication is
   outside this repository; the atlas does not collect or forward its credentials.

The application code adds no analytics, advertising script, or application
cookie. This statement covers this code, not network metadata that a hosting
provider normally receives when serving a page.

## What the browser stores

| Key | Value | Validation and purpose |
| --- | --- | --- |
| `qm-from-scratch:v1:read` | JSON array of paper IDs, for example `[1, 3, 41]` | Only distinct integer IDs in the current corpus are retained. Records studied papers. |
| `qm-from-scratch:v1:theme` | `dark` or `light` | Other values fall back to the default theme. |

The storage helper catches access, parsing, and write failures. The page remains
usable with in-memory state when persistence is blocked; changes then last only
for the current page session. This is not token storage, encryption, synchronization,
or access control.

Browser local storage belongs to an **origin**, not a repository path. Other
applications served from the same `https://krazad0.github.io` origin share the
storage namespace. The project-specific key prefix avoids accidental collisions;
it does not isolate data from same-origin scripts. Do not add passwords, API keys,
or private notes to this storage. See [MDN's localStorage reference][storage-doc].

### Earlier progress data

The original parser removed the first character of each paper ID with
`line.slice(1)`, creating duplicate IDs. This update preserves each full ID.
Old `qm-read` values cannot be mapped reliably back to the papers a reader selected,
so they are not migrated into the new progress key. The old value is left untouched,
and the UI reports the need to mark papers again. A valid legacy `qm-theme` value
may be used as a display preference.

To remove only this application's stored data, use the browser's developer tools
to remove the two namespaced keys. Avoid clearing all origin storage if you want
to retain other projects' preferences. Removing storage does not revoke any token
because no reader token exists.

## GitHub Actions credentials and permissions

GitHub creates a job-scoped `GITHUB_TOKEN`, available to actions through
`github.token`. It is an installation token limited to this repository and expires
when the job finishes or reaches its effective lifetime. The project does not
provide a personal access token or store a long-lived deployment key. These are
platform properties documented in [GitHub's token guide][token-doc].

The workflow separates permissions by purpose:

| Job | Permission | Purpose |
| --- | --- | --- |
| Build / checks | `contents: read` | Read repository source for tests and static-file staging. |
| Deploy | `pages: write` | Create the Pages deployment. |
| Deploy | `id-token: write` | Request an OIDC token that verifies the deployment's workflow origin. |

The deployment sequence is:

1. A push to `main` or a manual workflow dispatch starts the Pages workflow.
   The deploy job additionally requires `github.ref == 'refs/heads/main'`, so a
   manual run on another branch can build and check code but skips deployment.
2. Checkout reads source with `persist-credentials: false`, so later repository
   scripts do not inherit persisted checkout credentials.
3. Checks run and an allowlisted `_site` artifact is prepared. Only the browser
   application and its assets are uploaded, not the repository working directory,
   `.git`, application drafts, tests, or local configuration.
4. The deploy job waits for the build, uses the `github-pages` environment, and
   invokes the official `actions/deploy-pages` action.
5. That action uses the job's GitHub token for the deployment API and an OIDC token
   as evidence of the workflow identity. Neither token is inserted into HTML,
   JavaScript, local storage, or the published artifact.

The workflow actions are pinned to complete commit SHAs. The deploy job does not
check out source or execute project tests. Build scripts and the pull-request
workflow have no Pages or OIDC write permission.

GitHub documents the required Pages permissions and environment in its
[custom workflow guide][pages-doc]. The [deploy-pages implementation and
documentation][deploy-doc] describe the token inputs and OIDC checks. The
[checkout documentation][checkout-doc] explains credential persistence.

This repository's files do not establish that branch protection, environment
approvals, required reviewers, or private vulnerability reporting are enabled.
Those settings must be checked in GitHub. Likewise, action pinning reduces
unintended action updates; it does not make third-party build code automatically
trustworthy.

## Trust boundaries and maintenance

- A reader may edit their own local progress. No authorization decision depends
  on it, so this changes only their display.
- Repository contributors can propose changes to executable browser code and
  source links. Maintainers must review those changes before merging or deploying.
- UI text is escaped before insertion into HTML; curated external links must use
  HTTPS. These measures complement source review.
- CI code runs in GitHub's runner. Keep publishing permissions in the deployment
  job, and do not give untrusted pull-request code deployment credentials.
- A Claude for Open Source application uses Anthropic's external GitHub sign-in.
  It is not implemented here, and its tokens must never be pasted into this
  repository. See the separate [application-readiness document](CLAUDE_APPLICATION.md).

For responsible reporting, see [`SECURITY.md`](../SECURITY.md).

[token-doc]: https://docs.github.com/en/actions/concepts/security/github_token
[pages-doc]: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
[deploy-doc]: https://github.com/actions/deploy-pages
[checkout-doc]: https://raw.githubusercontent.com/actions/checkout/v4/README.md
[storage-doc]: https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage
