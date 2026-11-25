# Quantum-mechanics research ideas: provisional integration

**Status:** proposed research directions, not completed results, independently verified calculations, or a transcription of a YouTube video. Prepared 26 November 2026.

**Channel supplied by maintainer:** https://www.youtube.com/@thquantum-zero

## Source and attribution boundaries

This page is based on quantum-mechanics research topics the maintainer discussed in the project-planning conversation, **not** on independently inspected YouTube videos. At preparation time the channel's video list, descriptions and transcripts could not be retrieved reliably. Accordingly, no idea below is attributed to a particular video, no video-specific claim is made, and the channel's audience, reach and engagement are not asserted. The channel URL is recorded solely as a link awaiting verification.

To make a verified video-to-repository index, add each relevant **specific video URL**, its public title, publication date, and timestamps for the discussed idea after reviewing the source directly. Do not imply that the channel or these proposals establish eligibility for an external grant/subscription.

## Idea A — Hydrogen atom confined within a toroidal domain and driven by an attosecond pulse

**Research question:** How do boundary geometry and an external ultrafast electromagnetic field affect a simplified hydrogenic quantum model?

### First model to specify

- Decide what is confined: the electron relative coordinate, the atom's center of mass, or both. They are different physical models and must not be interchanged.
- Specify a solid torus with major radius `R` and minor radius `a`, satisfying `R > a > 0`: `(sqrt(x^2+y^2)-R)^2 + z^2 < a^2`.
- Write the Hamiltonian before attempting simulations. For an **electron fixed-nucleus approximation** with a chosen electromagnetic gauge, one possible starting point is
  `H(t) = [p + e A(r,t)]^2/(2 m_e) - e^2/(4 pi epsilon_0 |r-r_N|) + V_wall(r)`.
  This expression is schematic: the position of the nucleus, boundary implementation, field model, and approximations still need definition. For a model driven by a classical electric field in the dipole approximation, state the length-gauge form and its validity conditions instead. Do not combine gauge forms indiscriminately.
- Establish a solvable baseline **without** the field and check probability normalization, boundary behavior, energy convergence and geometry discretization.
- Introduce a pulse with explicitly stated envelope, center frequency, carrier-envelope phase, polarization, intensity, and atomic/SI units. Resolve the approximation regime (nonrelativistic; dipole or non-dipole; ionization included or excluded).

### Proposed validation

1. Recover an analytically checkable limit (e.g. the unconfined hydrogen atom with no drive, or a simpler hard-wall geometry).
2. Compare a grid method against an independent basis calculation for a tractable case.
3. Demonstrate spatial and temporal convergence, norm behavior, and gauge-consistent observables where applicable.
4. Compare field-on/off populations or spectra only after numerical errors are controlled.
5. Treat all early plots as exploratory rather than experimental predictions.

**Deliverable:** a model specification, derivation, reproducible code, tests and a limitations section. This is a possible future research extension, not implemented by the introductory square-well example.

## Idea B — Quantum calculations for the simplest biological system

**Research question:** What quantum-mechanical model is simple enough to compute reliably while providing a meaningful biological or biomolecular interpretation?

Begin by selecting a **specific** molecule or elementary biomolecular unit, rather than promising a quantum solution for an entire living organism. Clarify whether the observable is an electronic energy, vibrational frequency, proton transfer, or another defined quantity. State nuclear-motion treatment, environment/solvation assumptions and a reference calculation. A tiny molecule, a model hydrogen bond, or a one-dimensional double-well is a sensible pedagogical starting point, but no target has been selected.

**Deliverable:** documented molecular/model Hamiltonian, assumptions, computational method, convergence tests and a literature comparison. This is a separate proposal, not a verified biological prediction.

## Idea C — Reproducible analytical and numerical quantum mechanics from scratch

Extend the current educational path from the three starter chapters to scattering, the harmonic oscillator, angular momentum, hydrogen, approximation methods and time-dependent evolution. Each chapter should contain the full derivation, worked problems, source citations, and a testable numerical example where suitable. The existing first lab is an infinite-square-well solver. Do not describe planned modules as already completed.

**Deliverable:** an educational sequence that connects original derivations, numerical verification and historical paper reading.

## Proposed mapping to the YouTube channel

| Video title and URL | Specific timestamp / directly evidenced statement | Related idea | Repository artifact |
| --- | --- | --- | --- |
| Awaiting verification | Awaiting verification | A, B, or C, only after direct review | Link to a future note, notebook, code or issue |

Do **not** fill the table using guessed titles, search snippets for other channels, or topics mentioned only in private conversations.

## Relevance to Claude for Open Source

This page can document future open-source work and honest project scope. A channel link, a research proposal, or educational ambition is **not** proof of the program's required adoption, community activity, criticality or recognized maintainer status. Use only dated, independently verifiable activity and impact evidence in an application. See the application preparation notes in PR #2 and the official terms before submission.
