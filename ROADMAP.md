# Development roadmap

**Prepared:** 26 November 2026.
**Scope:** an accessible quantum-mechanics learning project combining original explanations, foundational papers, and reproducible calculations.

The existing atlas contains 41 papers and milestones. The proposed introductory release adds three chapters and a finite-difference infinite-square-well example. The project is at an early stage: a full course, community adoption, independent review, and the later calculations below remain future work.

This is a six-month development plan measured from the first reviewed introductory release. It is not an eligibility requirement for the Claude for Open Source program. Dates and scope can change with maintainer capacity; no external contributors or program support are assumed.

## Introductory release: current proposed work

| Deliverable | Location | Review expectation |
| --- | --- | --- |
| Mathematical foundations | [Chapter 1](notes/01-mathematical-foundations.md) | Check definitions, inner-product conventions, normalization, and worked exercises. |
| Postulates and two-level systems | [Chapter 2](notes/02-postulates-and-two-level-systems.md) | Check probabilities, measurement statements, and unitary evolution. |
| Infinite square well | [Chapter 3](notes/03-infinite-square-well.md) | Check boundary conditions, normalization, spectrum, and units. |
| Reproducible calculation | [Example instructions](examples/README.md) | Reproduce the analytic/numerical comparison in a clean environment. |
| Numerical verification | [Tests](tests/test_quantum.py) | Check meaningful agreement and convergence, not just successful execution. |

These links describe this proposed change. They should be treated as publicly released material only after the change has been integrated into the public repository. Passing numerical checks are not a substitute for mathematical or pedagogical review.

## Months 1–6

| Period | Learning content and software | Completion evidence |
| --- | --- | --- |
| Month 1: review the foundations | Review the three starter chapters, standardize notation and dimensions, improve exercises, and establish a reproducible setup. Publish a clearly scoped introductory release. | Recorded review fixes; reproducible example; passing numerical checks; release notes stating implemented scope and known limitations. |
| Month 2: wave packets and one-dimensional scattering | Add probability current, the continuity equation, Gaussian wave packets, finite steps, and tunnelling. Build one carefully bounded scattering or propagation example. | Derived conservation statement; specified boundary conditions and units; probability/flux checks; comparison with a known analytic case. |
| Month 3: harmonic oscillator | Develop ladder operators, stationary states, and the link between analytic and grid methods. Add a numerical oscillator example with domain and grid sensitivity explained. | Agreement with the analytic spectrum over a documented range; normalization and parity checks; convergence table distinguishing finite-domain and discretization error. |
| Month 4: spin and angular momentum | Extend the two-level material to spin measurements, commutators, angular-momentum algebra, and introductory addition of angular momenta. | Small matrix examples with verified eigenvalues and probabilities; consistent basis conventions; worked exercises with checked solutions. |
| Month 5: central potentials and hydrogen | Introduce separation in spherical coordinates, radial boundary conditions, hydrogen energy levels, and the role of quantum numbers. Add a limited, documented radial example if the earlier material is stable. | Analytic derivations with assumptions; convergence and boundary checks for any numerical solver; explicit exclusions and failure modes. |
| Month 6: approximation methods and consolidation | Introduce basic perturbation theory and the variational principle. Review prerequisites, fix reported errors, improve navigation, and assemble a coherent study sequence. | At least one approximation compared with an exactly solvable or converged reference; updated chapter index; reviewed release notes and citation metadata. |

Each month is a planning interval, not a commitment to a particular release date. Correcting a derivation or numerical limitation takes priority over adding another chapter.

## Quality standard for each chapter

1. State prerequisites, notation, assumptions, and the physical question.
2. Derive the central result with intermediate steps that a learner can follow.
3. Provide at least one worked example and exercises at clearly identified difficulty levels.
4. Check normalization, units, limits, and boundary conditions where applicable.
5. Cite original or authoritative references and write explanations in original language.
6. Label material that is still awaiting review. Never describe unpublished work as completed or independently validated.

## Quality standard for each calculation

Every example should identify its model, units, parameters, boundary conditions, numerical method, and known limitations. It should run from documented commands with a small dependency set. Verification should compare a physical result with an analytic solution, conservation law, or independently converged reference. State what the check does and does not establish.

For grid calculations, document the difference between spacing error and finite-domain error. For time evolution, check norm behavior and time-step sensitivity. For approximations, state the parameter range in which agreement has actually been examined. Avoid treating a visually plausible plot as numerical verification.

## Community and maintenance

Publish issues that correspond to real errors, missing explanations, or useful improvements. Review outside work on its merits and credit actual contributors. Keep a record of resolved corrections and releases so learners can identify which version they used.

Collect adoption evidence only when it exists: a course linking to the resource, a documented downstream reuse, substantive external contributions, or a reproducible bug report. Stars, download counters, and contribution counts should not become development targets. Do not manufacture activity to satisfy an application threshold.

## Deferred research extensions

Possible later projects include time-dependent driving, higher-dimensional discretization, and constrained geometries. These require their own model definitions, literature review, and validation plans. The introductory release makes no claim to implement a complete research calculation for a hydrogen atom in a toroidal domain or in an attosecond field.

## Review points

After each release, record what shipped, which checks were run, which limitations remain, and what should change next. At the three-month and six-month points, adjust the plan to observed learner needs and maintainer capacity. Keep the [application preparation document](docs/CLAUDE_APPLICATION.md) consistent with the evidence if it is used; a roadmap is never evidence that future work has already happened.
