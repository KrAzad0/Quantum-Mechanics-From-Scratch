# Claude for Open Source: application preparation

**Evidence checked:** 26 November 2026 (India).
**Repository:** [KrAzad0/Quantum-Mechanics-From-Scratch](https://github.com/KrAzad0/Quantum-Mechanics-From-Scratch).
**Status:** preparation for a maintainer's review; no application was submitted during this preparation.

The program currently offers six months of Claude Ultra. Six months describes the subscription benefit, not a required repository age. Building a useful repository and establishing eligibility are separate tasks. This document does not certify eligibility or predict approval.

**Known blocker on 26 November 2026:** the public GitHub profile reports that `KrAzad0` was created on 24 December 2024. It has not reached the program's two-year account minimum. That anniversary is 24 December 2026; reaching it would resolve only the age condition, assuming the terms remain unchanged. A qualifying contribution/impact route and the other general conditions would still need evidence. Keep this as preparation, rather than submitting a claim of present eligibility.

## What is actually available

At the inspected `main` commit [`3a0c5128ce6e450fa7236cf41f65368435984ecd`](https://github.com/KrAzad0/Quantum-Mechanics-From-Scratch/tree/3a0c5128ce6e450fa7236cf41f65368435984ecd), the project was a public, MIT-licensed static research atlas with 41 foundational quantum-mechanics papers and milestones. It provided source links, original summaries, equations, search, filters, and browser-local reading progress. It did not yet contain the new lecture-note chapters or the numerical solver described below.

This proposed update adds three introductory chapters on mathematical foundations, postulates and two-level systems, and the infinite square well, plus a NumPy finite-difference example and numerical checks. **These additions are pending integration into `main`.** Source published in a public pull request can be inspected before merging. Describe the additions as part of the default-branch release only after merging, and describe site changes as live only after successful deployment. The proposed material is introductory, not a complete quantum-mechanics course or a peer-reviewed resource.

| Verified repository fact | Evidence and limits |
| --- | --- |
| Public repository created 10 August 2026 | GitHub repository metadata inspected during preparation. This is not the account-creation date. |
| Last inspected `main` commit dated 11 August 2026 | Outside the 90 days before 26 November 2026. This does not establish the applicant's activity across other repositories. |
| MIT license | [LICENSE](../LICENSE). Verify any separately sourced material retains its own applicable rights. |
| 0 stars and 0 forks at inspection | A dated snapshot, not an impact measurement or an eligibility ruling. |
| 41 entries in the existing atlas | The curated corpus is a selected historical route, not an exhaustive bibliography. |
| GitHub account created 24 December 2024 | [Public profile API](https://api.github.com/users/KrAzad0), inspected 26 November 2026. This differs from the repository's creation date. |
| Recent public OSS activity verified elsewhere | [`openatom-tdse` commit `162cf04`](https://github.com/KrAzad0/openatom-tdse/commit/162cf0450d5261e600e71bc20a961832aa89c641), authored by `KrAzad0` / Kumar Azad on 24 November 2026 at 16:59:33 UTC, in a public MIT-licensed repository. This is within the preceding 90 days. |
| Downstream use, external contributions, and downloads | Not established by this repository inspection. Unknown values must not be represented as zero or as qualifying metrics. |

A separate [public merged-PR search](https://api.github.com/search/issues?q=is%3Apr%20is%3Amerged%20author%3AKrAzad0%20is%3Apublic%20-user%3AKrAzad0%20merged%3A%3E%3D2025-11-26&per_page=1) returned `total_count: 0` and `incomplete_results: false`. Its scope was merged public PRs authored by `KrAzad0`, dated on or after 26 November 2025, excluding repositories in the `KrAzad0` namespace. This is a dated, scoped search result, not an all-history contribution count or an audit of repository ownership through organizations.

## Program requirements versus evidence

Use the [official program page](https://claude.com/contact-sales/claude-for-oss) and [full terms](https://www.anthropic.com/claude-for-oss-terms) as the authority; recheck them immediately before submitting. The following is a compact preparation checklist, not a substitute for the terms.

### General conditions

These conditions come from terms section 2.3.

| Condition | Current evidence / next action |
| --- | --- |
| Individual; qualifying age and residence; applicable exclusions | Applicant must verify privately against the full terms. |
| GitHub account at least two years old and in good standing | Age condition is not met on the check date. The account reaches its second anniversary on 24 December 2026; standing has not been verified. |
| Public OSS contribution during the preceding 90 days | Evidenced by the 24 November 2026 [`openatom-tdse` commit](https://github.com/KrAzad0/openatom-tdse/commit/162cf0450d5261e600e71bc20a961832aa89c641). Anthropic still evaluates the substance and application as a whole. |
| Maintain or contribute to an OSI-licensed project | This repository has an MIT license. |

### At least one qualifying route

The alternatives below are summarized from the program page and terms sections 2.1–2.2. Metrics concern substantive, actual activity. A documentation checklist cannot create evidence of adoption.

| Route | Threshold / basis | Evidence available here |
| --- | --- | --- |
| Maintained packages | 500 dependent repositories, 100 dependent packages, or 200,000 monthly downloads in aggregate | Not established. |
| Recognized core role | Listed foundation/language-project committer or maintainer | Not established. |
| Contributions to others' repositories | 100 merged public PRs in 12 months | The scoped public search above returned 0. No qualifying evidence established. |
| External contributors | 20 unique contributors with merged PRs in a maintained repository in 12 months | Not established. |
| Critical infrastructure | OpenSSF criticality score at least 0.4 | Not established. |
| Discretionary ecosystem impact | Meaningful ecosystem dependence, supported by an explanation | Educational purpose is clear; actual ecosystem dependence has not been demonstrated. |

Meeting a threshold does not guarantee selection. The terms prohibit misleading applications and artificially inflated metrics. A new release can demonstrate work completed; it cannot establish historical adoption, an older account, or outside contributions that have not occurred.

## Form fields to prepare

The supplied application PDF shows the fields below. The live form may change. Terms section 3.1 specifies GitHub sign-in, email, planned use, and a qualification explanation of no more than 500 words. Enter account details directly in the official form; do not add email addresses, passwords, activation links, or tokens to this repository.

| Field | Suggested preparation |
| --- | --- |
| First name | Kumar, if this is the applicant's correct given name. |
| Last name | Azad, if this is the applicant's correct family name. |
| Account email | Enter the appropriate Claude/account email privately. No address is published here. |
| GitHub account / repository selector | Authenticate through the official form and choose `KrAzad0/Quantum-Mechanics-From-Scratch`. |
| GitHub handle, if displayed | `KrAzad0`. |
| Repository URL, if displayed | `https://github.com/KrAzad0/Quantum-Mechanics-From-Scratch`. |
| Project reach and impact | Use the factual draft below; add only independently verifiable evidence. |
| Intended subscription use | Use or adapt the development-use draft below. |
| Other information | Optional: link a public release, useful contributions, and validation instructions. Do not invent missing evidence. |

## Draft: project reach and impact

**Review draft; wording accurately separates the existing atlas from the proposed update.** Add the public PR URL once available; change the default-branch release status only after integration into `main`. This draft does not assert that a qualifying route has been met.

> I maintain Quantum Mechanics From Scratch, a public MIT-licensed educational project for students learning quantum mechanics through foundational research and reproducible calculations. The existing static atlas organizes 41 historical papers and milestones with source links, original summaries, central equations, search, and a local reading-progress tracker.
>
> A proposed update adds original introductory chapters on mathematical foundations, quantum postulates and two-level systems, and the infinite square well, together with a NumPy finite-difference example and tests against analytic results. Those additions are pending integration into main. The resource is introductory and is not yet a complete course or independently peer-reviewed.
>
> Its intended contribution is to connect historical reading, step-by-step derivations, and runnable calculations in one accessible learning resource. At the 26 November 2026 inspection, the repository had zero stars and zero forks. I do not yet have verified evidence of downstream dependence or broader adoption, and I am not claiming a numerical eligibility threshold. My recent public open-source activity includes an authored commit in the MIT-licensed openatom-tdse repository on 24 November 2026; that activity does not establish a qualifying impact route.
>
> My GitHub account was created on 24 December 2024, so it does not yet meet the current account-age requirement. This is preparation for a future review of eligibility, not a claim that I currently qualify.

This draft is below 500 words. Before applying, the maintainer should confirm the general conditions and identify a route with evidence. The discretionary route should be described only when there is a defensible case for meaningful ecosystem dependence; future educational ambition alone does not establish that case.

## Draft: intended subscription use

> I would use Claude to help maintain and expand the project's quantum-mechanics learning materials and computational examples. Planned work includes reviewing derivations for missing steps and inconsistent notation, checking numerical examples against analytic limits, improving explanations and accessibility, and helping review issues and proposed contributions. I would verify mathematical and numerical claims before publishing them, retain source attribution, and distinguish unreviewed drafts from validated examples. The development plan extends from foundational mathematics and one-dimensional systems to spin, the harmonic oscillator, angular momentum, and introductory approximation methods. Subscription support would help me carry out this maintenance and development work; it would not replace my responsibility for the accuracy of the material.

The [development roadmap](../ROADMAP.md) is a project plan, not an Anthropic requirement or a promise that a subscription will be awarded.

## Evidence to collect before submission

- Revisit the account-age condition on or after 24 December 2026, recheck the current terms, and confirm the remaining general conditions and recent public activity using the applicant's real history.
- Link the public PR once it exists and label it as pending integration. After review and merging, link the actual default-branch commit or release URL. Do not present an unpublished local branch as public evidence or an unmerged PR as a shipped default-branch release.
- Record the selected eligibility route and dated evidence: relevant public PRs, contributor records, registry statistics, recognized maintainer listing, or downstream adoption where applicable.
- Keep original verification output or a public CI result for the numerical examples. A passing test suite demonstrates a checked calculation; it does not demonstrate ecosystem impact.
- Re-read each application sentence against the public evidence. Keep planned work explicitly in the future tense and leave unknown facts unknown.

## Sources

- [Claude for Open Source: official offer and application](https://claude.com/contact-sales/claude-for-oss).
- [Official terms: eligibility, application, selection, and benefit](https://www.anthropic.com/claude-for-oss-terms), especially sections 2–4 and 7.
- [Open Source Initiative: MIT license](https://opensource.org/license/mit).
- Repository baseline: [inspected source commit](https://github.com/KrAzad0/Quantum-Mechanics-From-Scratch/tree/3a0c5128ce6e450fa7236cf41f65368435984ecd).
- Account creation date: [public GitHub profile API](https://api.github.com/users/KrAzad0).
- Recent public contribution: [`openatom-tdse` commit](https://github.com/KrAzad0/openatom-tdse/commit/162cf0450d5261e600e71bc20a961832aa89c641).
- Scoped contribution check: [public merged-PR search](https://api.github.com/search/issues?q=is%3Apr%20is%3Amerged%20author%3AKrAzad0%20is%3Apublic%20-user%3AKrAzad0%20merged%3A%3E%3D2025-11-26&per_page=1).

No application was submitted during this preparation, and no subscription or approval is claimed.
