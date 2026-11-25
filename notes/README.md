# Quantum mechanics: first learning module

These original teaching notes connect mathematical definitions, physical
postulates, analytic calculations, and a reproducible numerical experiment.
Start here if the historical papers in the [research atlas](../index.html) feel
too advanced. Basic algebra, differentiation, and definite integration are
assumed; complex amplitudes and vector notation are introduced below.

## Available now

| Chapter | What you will calculate |
| --- | --- |
| [01 — Mathematical foundations](01-mathematical-foundations.md) | Complex magnitudes, inner products, normalization, and phase-dependent probabilities |
| [02 — Postulates and two-level systems](02-postulates-and-two-level-systems.md) | Measurement probabilities, expectation values, and exact two-level time evolution |
| [03 — The infinite square well](03-infinite-square-well.md) | Boundary conditions, energy quantization, normalized wavefunctions, and finite-difference convergence |
| [Computational exercise](../examples/README.md) | Run a Python eigensolver and test its predictions against the analytic result |

Each chapter includes worked exercises. Read the derivation, attempt an exercise
without looking at its solution, and then use the code to test one prediction.

## Current scope

This is a **starter module**, not a completed quantum-mechanics textbook. The
existing atlas is a route through historical research; the notes provide a
separate mathematical learning sequence. Harmonic oscillators, finite barriers,
angular momentum, hydrogen, perturbation theory, identical particles, and
time-dependent simulations are future work. See the [roadmap](../ROADMAP.md).

The calculations are educational and have not received independent specialist
peer review. Automated numerical checks support the included square-well
implementation; they do not prove every statement in the prose. Corrections
should identify the equation or code path, explain the issue, and include a
derivation or reproducible counterexample where possible.

## Attribution and conventions

These files contain original explanations and exercises. References point to
the instructors' published materials for independent study and cross-checking;
no external lecture text or figures are reproduced. The repository's
[MIT license](../LICENSE) applies to these original files. Linked publications
and third-party resources retain their own licenses.

Use $\hbar=h/(2\pi)$ for the reduced Planck constant, $i^2=-1$, and the physics
inner-product convention: conjugate-linear in the first argument and linear in
the second. A star denotes complex conjugation, and a dagger denotes the
conjugate transpose. The numerical example states its unit convention explicitly.
