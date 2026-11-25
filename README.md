# Quantum Mechanics From Scratch

Learn quantum mechanics through original lecture notes, reproducible calculations,
and a searchable atlas of foundational papers. Maintained by
[Kumar Azad](https://github.com/KrAzad0).

**Start with the [lecture notes](notes/README.md), run the [first numerical lab](examples/README.md),
or explore the [public paper atlas](https://krazad0.github.io/Quantum-Mechanics-From-Scratch/).**
The hosted atlas reflects the latest successful deployment from `main`; changes
viewed on a pull-request branch may not yet be live.

## Current scope

This is an early educational project, with three introductory chapters and one
validated numerical example. It is not yet a complete quantum-mechanics course,
and no independent peer review is claimed.

| Resource | Available material |
| --- | --- |
| [Mathematical foundations](notes/01-mathematical-foundations.md) | Complex amplitudes, inner products, normalization, orthogonality, worked examples and exercises. |
| [Postulates and two-level systems](notes/02-postulates-and-two-level-systems.md) | States, observables, measurement probabilities and unitary evolution. |
| [Infinite square well](notes/03-infinite-square-well.md) | Derivation from boundary conditions, exact energies and eigenstates, and finite differences. |
| [Numerical lab](examples/README.md) | A local NumPy solver with analytic comparison, normalization and convergence checks. |
| [Interactive atlas](index.html) | 41 selected papers and milestones, 1900–1964, with original summaries, source links, search, era filters, an Essential 20 path and reading progress. |

The paper corpus is a curated historical route, not an exhaustive bibliography.
Linked material includes publications, archival records and translations. Some
publisher pages require institutional access. Summaries are original educational
text, and linked publications remain subject to their own rights.

## Learning path

1. Work through Chapters 1–2 and check the worked exercise solutions.
2. Derive the square-well spectrum in Chapter 3 before running the calculation.
3. Change the number of grid points and explain the change in energy error.
4. Use the atlas to connect the formalism with the historical questions behind it.
5. Report a correction or propose a focused extension using [CONTRIBUTING.md](CONTRIBUTING.md).

Prerequisites are elementary algebra, trigonometry, derivatives and integrals.
The notes introduce the linear algebra used in the starter material.
The [roadmap](ROADMAP.md) identifies later topics and their validation goals.

## Run the atlas locally

No package installation, account or build service is needed for the browser app.
From this directory:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Open `http://127.0.0.1:8000`. Search and progress work locally. The browser stores
only studied-paper IDs and the theme; nothing is sent to an application backend.
Following a source link opens the external provider's website.

## Run the numerical example

Use Python 3.11 or newer; the reference environment is Python 3.12.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python examples/infinite_well.py --points 200 --states 3
```

For Windows activation and parameter/units details, see [examples/README.md](examples/README.md).
Dependency installation needs network access if NumPy is not cached; the solver
itself makes no network requests. Its default energies are dimensionless, not eV.
It uses a small dense matrix for teaching and is not a large-scale simulator.

## Verify changes

With the Python dependency installed and Node.js 22 available:

```bash
node --test tests/atlas.test.js
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts/check_site.py
python scripts/build_site.py
```

The checks cover complete and unique paper IDs, parsing equations that contain
vertical bars, safe local-storage behavior, the analytic spectrum, second-order
grid convergence, normalization, orthogonality, boundary conditions, and input
validation. Site checks verify local assets and learning links; they do not
certify that every external publisher URL is currently reachable.

## Components and authentication

The site consists of `index.html`, `styles.css`, `papers.js`, `storage.js`, `app.js`,
and the `assets/` directory. The numerical lab is separate Python code.

There is **no application authentication**: no login, passwords, access tokens,
refresh tokens, Claude API key, or reader database. GitHub handles contributor
authentication and deployment separately. The full [authentication review](docs/AUTHENTICATION.md)
explains the request flow, storage keys, GitHub Actions token permissions and OIDC.
See [SECURITY.md](SECURITY.md) for reporting and credential-handling practices.

Earlier atlas versions truncated paper IDs. The corrected version uses a new,
project-specific progress key because old selections cannot be mapped reliably.
Legacy data is left untouched; the page explains why progress starts fresh.

## GitHub Pages and contribution checks

Pull requests run read-only checks. On `main`, the Pages workflow checks the code,
stages an allowlisted `_site` directory, and deploys it with a separate job.
Checkout credentials are not persisted, and publishing permissions are restricted
to the deployment job. Actions are pinned to commit SHAs; Dependabot is configured
to propose dependency updates. The generated site includes only browser assets.

If hosting needs initial configuration, set **Settings → Pages → Source → GitHub
Actions**. The repository must have Pages enabled; a workflow file does not establish
environment protection or branch-review settings by itself.

## Contributing, citation and license

Useful contributions include clearer intermediate derivations, corrected sources,
reproducible numerical checks and accessibility improvements. Read
[CONTRIBUTING.md](CONTRIBUTING.md) and the [code of conduct](CODE_OF_CONDUCT.md).
Use [CITATION.cff](CITATION.cff) and identify the commit you used; the project
does not claim a DOI or a published academic article.

Original code and accompanying original documentation are covered by the existing
[MIT license](LICENSE). External publications and third-party material are not
relicensed by linking to them. Do not contribute copied textbook chapters or
publisher PDFs without the necessary rights.

## Claude for Open Source preparation

The [application preparation document](docs/CLAUDE_APPLICATION.md) records the
current official criteria, a truthful draft, dated evidence, and missing evidence.
As of 26 November 2026, the maintainer's GitHub account has not reached the required
two-year age; its second anniversary is 24 December 2026. The project also does
not yet establish a qualifying maintainer or ecosystem-impact route. These
repository improvements do not guarantee eligibility or approval.

Reading, running and contributing to this project never requires a Claude subscription.
