# Security policy

## Project scope

This repository contains a static educational application, lecture notes, and
local numerical examples. The atlas has no account system, server-side application,
credential store, or paid API dependency. Its browser storage contains only reading
progress and theme preferences. See the [authentication and data-flow review](docs/AUTHENTICATION.md)
for exact components, storage keys, and deployment permissions.

Please reproduce reports against the latest default-branch version and include
the commit SHA. There is no separately maintained long-term-support release line
or promised response deadline.

## Reporting a vulnerability

Use **Security → Report a vulnerability** on the repository if GitHub offers that
button. Private reporting must be enabled in repository settings; this file alone
does not enable it. If the button is absent, open an issue asking the maintainer
for a private security contact, without posting exploit instructions, credentials,
or personal data. This follows [GitHub's private-reporting guidance](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/report-privately).

A private report should include the affected commit, file or workflow, a minimal
reproduction, the expected and observed behavior, and an explanation of impact.
Use synthetic data and redact tokens. Do not test against other users' accounts
or unrelated websites.

Ordinary physics corrections, broken citations, layout problems, and numerical
accuracy issues belong in the normal issue tracker unless there is a separate
security impact.

## Contributor practices

- Keep credentials out of tracked files, screenshots, issue text, example inputs,
  browser storage, generated output, and logs. The project needs no Anthropic key.
- Keep tests and static builds read-only; reserve Pages and OIDC permissions for
  deployment. Do not execute untrusted pull-request code with deployment access.
- Review workflow permissions, action revisions, scripts, external links, and
  new browser dependencies before merging. Do not treat AI-generated changes as
  independently verified.
- Publish only the allowlisted static artifact. Local `.env` files, Git metadata,
  and maintainer-only material do not belong in the site artifact.
- Treat browser data as user-editable and validate it before use. Same-origin
  local storage is not suitable for private data or authentication tokens.

If a credential is accidentally exposed, revoke or rotate it at its issuing
service first. Deleting the current file does not invalidate the credential or
remove it from repository history. Coordinate any necessary history cleanup with
the maintainer rather than rewriting shared history without notice.
