# Quantum Mechanics from Scratch — Solved Problem Book, Volume I

**Version 0.1 · 26 November 2026 · Educational preprint · Open for contributions**

**Author/maintainer:** Kumar Azad. **Repository:** [Quantum Mechanics From Scratch](https://github.com/KrAzad0/Quantum-Mechanics-From-Scratch).

This is an **original, open educational workbook**, not a peer-reviewed paper, not a complete course, and **not a submission to or endorsement by arXiv**. The PDF companion was prepared in arXiv-inspired article format. We welcome factual corrections, improved derivations and evidence-based new problems. See [CONTRIBUTING_PROBLEMS.md](CONTRIBUTING_PROBLEMS.md).

## Conventions

The state vector has norm one, up to a global phase; `hbar = h/(2*pi)`; inner products conjugate the bra. For a wavefunction, `integral |psi(x)|^2 dx = 1`. Unless stated otherwise, the problems use isolated, nonrelativistic, finite-dimensional or one-dimensional models and ideal projective measurements. These concise solutions are a navigational companion to the fully worked PDF.

## Part I — Amplitudes and linear algebra

### 1. Why use complex amplitudes?
**Problem:** Normalize `v = (3,4i)` and find its basis probabilities.
**Solution:** `v†v = 9+16 = 25`; `psi=(3,4i)/5`; the probabilities are `9/25` and `16/25`.
**Intuition:** Probabilities come from squared magnitudes of amplitudes, not amplitudes themselves.

### 2. Global versus relative phase
**Problem:** Compare `(|0>+|1>)/sqrt(2)`, its multiple by `i`, and `(|0>-|1>)/sqrt(2)`.
**Solution:** Multiplying the first vector by `i` changes no measurable probability. The third vector is orthogonal to the first; in the `+/-` basis its probabilities are reversed.
**Intuition:** Global phase is unobservable; relative phase changes interference.

### 3. Inner products
**Problem:** Are `(1,i)/sqrt(2)` and `(i,-1)/sqrt(2)` orthogonal?
**Solution:** Their inner product is `i`, not zero; the second vector is `i` times the first.
**Intuition:** Check the complex inner product, not apparent component differences.

### 4. Normalizing a wavefunction
**Problem:** Normalize `psi=A exp(-k|x|)` for `k>0` on the real line.
**Solution:** `1=2|A|^2 int_0^infty exp(-2kx) dx=|A|^2/k`; choose `A=sqrt(k)`. Symmetry gives `P(x>0)=1/2`.
**Intuition:** Increased localization demands a taller probability-density peak.

## Part II — Measurement

### 5. Born rule and expectation value
**Problem:** For `psi=(3/5,4i/5)`, measure `Z=diag(1,-1)`.
**Solution:** Probabilities are `9/25`, `16/25`; `<Z>=-7/25`; `Delta Z=24/25`.
**Intuition:** The expectation is an ensemble average, not necessarily a single-run result.

### 6. Repeated measurement
**Problem:** Measure `Z` on `|+>`; condition on result `+1`; repeat immediately.
**Solution:** The first `+1` has probability `1/2`; the conditional state is `|0>`; the repeat yields `+1` with probability 1.
**Intuition:** Measurement updates the state when conditioned on an observed outcome.

### 7. Noncommuting observables
**Problem:** Evaluate `[X,Z]` for Pauli `X` and `Z`.
**Solution:** `[X,Z]=-2iY`, nonzero. They have no common orthonormal eigenbasis.
**Intuition:** Incompatible measurements cannot both be read in one shared eigenbasis.

### 8. Basis change
**Problem:** Measure `X` on `(|0>+i|1>)/sqrt(2)`.
**Solution:** The `+/-` amplitudes are `(1+i)/2` and `(1-i)/2`; probabilities are `1/2` each.
**Intuition:** Transform amplitudes before squaring them.

## Part III — Wave mechanics and uncertainty

### 9. Free-particle stationary state
**Problem:** Solve `-hbar^2 psi''/(2m)=E psi` for `E>0`.
**Solution:** `psi=A exp(ikx)+B exp(-ikx)` with `k=sqrt(2mE)/hbar`.
**Intuition:** Positive and negative momenta have the same free-particle kinetic energy. A plane wave on the whole line is not normalizable.

### 10. Unitary evolution
**Problem:** Prove Schrödinger evolution preserves norm for a self-adjoint Hamiltonian.
**Solution:** Differentiate `<psi|psi>` using `d|psi>/dt=-iH|psi>/hbar` and the adjoint equation; the contributions cancel.
**Intuition:** An isolated system redistributes probability without changing its total.

### 11. Two-level oscillation
**Problem:** Evolve `|0>` under `H=hbar*Omega*X/2`.
**Solution:** `psi(t)=cos(Omega*t/2)|0>-i sin(Omega*t/2)|1>`; `P(1)=sin^2(Omega*t/2)`.
**Intuition:** A stationary Hamiltonian can give changing measurement probabilities.

### 12. Gaussian uncertainty
**Problem:** For `psi proportional to exp[-x^2/(4sigma^2)]`, calculate uncertainties.
**Solution:** `Delta x=sigma`; `Delta p=hbar/(2sigma)`; their product is `hbar/2`.
**Intuition:** Tight spatial localization needs a broad momentum distribution.

### 13. Probability current
**Problem:** Derive local conservation for a real scalar potential.
**Solution:** Combining the Schrödinger equation and its conjugate yields `partial_t rho+partial_x j=0`, where `rho=|psi|^2` and `j=(hbar/m) Im(psi* partial_x psi)`.
**Intuition:** Probability enters or leaves a region through its boundaries.

## Part IV — Elementary bound states and barriers

### 14. Infinite square well spectrum
**Problem:** Solve a well on `0<x<L` with `psi(0)=psi(L)=0`.
**Solution:** `psi_n=sqrt(2/L) sin(n*pi*x/L)`, `E_n=hbar^2*pi^2*n^2/(2*m*L^2)`, `n>=1`.
**Intuition:** The wave must fit both walls, selecting discrete wavelengths.

### 15. Probability in the middle half
**Problem:** In the ground state, find `P(L/4<x<3L/4)`.
**Solution:** Integrating `(2/L)sin^2(pi*x/L)` gives `1/2+1/pi` (about 0.81831).
**Intuition:** The ground-state density is concentrated toward the center.

### 16. Energy scaling
**Problem:** What happens to well energies on doubling the width or the mass?
**Solution:** `E_n proportional to 1/(mL^2)`; doubling `L` quarters energy and doubling `m` halves it.
**Intuition:** Longer wavelengths mean smaller momenta.

### 17. Finite barrier and tunneling
**Problem:** For `0<E<V0`, solve inside a barrier of width `a`.
**Solution:** `psi=C exp(kappa*x)+D exp(-kappa*x)`, `kappa=sqrt(2m(V0-E))/hbar`. Matching wavefunction and derivative at both boundaries generally yields a nonzero transmitted amplitude.
**Intuition:** An evanescent wave is not identically zero; `exp(-2*kappa*a)` is a thick-barrier scaling, not the universal exact transmission coefficient.

### 18. Harmonic oscillator ground state
**Problem:** Test `psi0=A exp(-m*omega*x^2/(2*hbar))`.
**Solution:** Substitution into `H=p^2/(2m)+m*omega^2*x^2/2` gives `E0=hbar*omega/2`; normalization gives `A=(m*omega/(pi*hbar))^(1/4)`.
**Intuition:** The zero-point energy reflects the impossibility of perfectly definite position and momentum.

### 19. Ladder operators
**Problem:** With `[a,a†]=1` and `H=hbar*omega*(a†a+1/2)`, find energies.
**Solution:** `[a†a,a†]=a†`; repeated raising from the vacuum gives `En=hbar*omega*(n+1/2)`.
**Intuition:** Excitations are equally spaced.

## Part V — Spin and composites

### 20. Perpendicular spin measurement
**Problem:** Measure Pauli `X` on `|0>`.
**Solution:** Its overlap with each `X` eigenstate is `1/sqrt(2)`; each outcome has probability `1/2`.
**Intuition:** Certainty about one spin component need not imply certainty about another.

### 21. Entanglement and partial trace
**Problem:** Is `(|00>+|11>)/sqrt(2)` a product state?
**Solution:** A product would require `ad=bc=0` and `ac,bd != 0`, impossible. The one-qubit reduced density matrix is `I/2`.
**Intuition:** The joint pure state contains correlations absent from either subsystem alone.

### 22. Mixed versus coherent states
**Problem:** Compare the mixture of `|0>`, `|1>` (half each) with pure `|+>`.
**Solution:** The mixture has `rho=I/2`; the pure state has `rho=(1/2)[[1,1],[1,1]]`. They agree on `Z` probabilities but have different `<X>`: 0 versus 1.
**Intuition:** Off-diagonal coherence has experimentally observable consequences.

## Part VI — Reproducible calculations

### 23. Discrete Hamiltonian
**Problem:** Approximate the infinite-well kinetic operator using `N` interior points.
**Solution:** With `dx=L/(N+1)`, use diagonal `2c`, neighboring off-diagonal `-c`, `c=hbar^2/(2m dx^2)`, and endpoint values zero.
**Intuition:** Dirichlet walls constrain the numerical wavefunction through the omitted endpoints.

### 24. Grid normalization
**Problem:** Convert an eigensolver vector `v` with `sum |v_j|^2=1` to a sampled continuum wavefunction.
**Solution:** `psi_j=v_j/sqrt(dx)`, so `dx sum |psi_j|^2=1`.
**Intuition:** The probability of a grid cell is density multiplied by its width.

### 25. Convergence versus matrix residual
**Problem:** How do we test a finite-difference solution independently?
**Solution:** Compare numerical low-energy values with an analytic spectrum and refine grids `N=31,63,127`. Central differences have leading `O(dx^2)` error, so the energy error ratio should approach four when `dx` halves. Also test norm and boundaries.
**Intuition:** A tiny matrix residual does not prove an accurate continuum approximation.

## Reproducibility and references

For an independent square-well numerical example, see [the proposed source and tests in PR #2](https://github.com/KrAzad0/Quantum-Mechanics-From-Scratch/pull/2). For further reading, see [MIT 8.04](https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2016/), [MIT 8.05](https://ocw.mit.edu/courses/8-05-quantum-physics-ii-fall-2013/), and the [NumPy symmetric eigensolver reference](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigh.html).

The document does not claim original research discoveries, independent mathematical peer review, an arXiv ID, or qualifying ecosystem impact for Claude for Open Source. This educational resource is intended for continuous improvement and genuine external contributions.
