# 03 — The infinite square well

[Previous: postulates](02-postulates-and-two-level-systems.md) · [Learning sequence](README.md) · [Run the calculation](../examples/README.md)

**Goal:** derive quantized energies from a differential equation and boundary
conditions, then test the result with an independently constructed matrix.

## 1. Define the model before solving it

A nonrelativistic particle of mass $m>0$ is confined to $0<x<L$. The potential
is zero inside and idealized as infinite outside. The mathematical problem is

$$-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}=E\psi,
\qquad \psi(0)=\psi(L)=0.$$

The endpoint conditions are **Dirichlet boundary conditions**. We do not impose
$\psi'=0$ at an infinite wall; imposing both value and derivative zero would
force the solution to vanish everywhere. This hard-wall model is an idealization
and does not describe tunneling through a finite barrier.

For a normalized energy eigenstate in the Hamiltonian's domain, integration by parts gives

$$E=\frac{\hbar^2}{2m}\int_0^L|\psi'(x)|^2dx>0.$$

The endpoint contribution vanishes. Equality would require a constant
wavefunction, and the endpoint conditions would then force the forbidden zero
state. We can therefore set $k=\sqrt{2mE}/\hbar>0$.

## 2. Boundary conditions select the energy

The equation becomes $\psi''+k^2\psi=0$, whose general solution is

$$\psi(x)=A\sin(kx)+B\cos(kx).$$

The left wall gives $B=0$. The right wall gives $A\sin(kL)=0$. A nonzero
state requires $A\ne0$, so $kL=n\pi$. The value $n=0$ gives a zero
wavefunction, and negative integers duplicate the positive states up to sign.
Hence

$$k_n=\frac{n\pi}{L},\qquad
E_n=\frac{\hbar^2\pi^2n^2}{2mL^2},\qquad n=1,2,3,\ldots.$$

Quantization came from requiring the differential equation and both boundary
conditions to hold simultaneously. It was not inserted by rounding energies.

## 3. Normalize and interpret

Use $\sin^2u=(1-\cos2u)/2$:

$$1=|A|^2\int_0^L\sin^2\left(\frac{n\pi x}{L}\right)dx
=|A|^2\frac L2.$$

Choosing a real positive normalization constant gives

$$\psi_n(x)=\sqrt{\frac2L}\sin\left(\frac{n\pi x}{L}\right),\qquad
\Psi_n(x,t)=\psi_n(x)e^{-iE_nt/\hbar}.$$

The phase changes with time but the probability density of this single energy
eigenstate does not. Product-to-sum identities also give
$\int_0^L\psi_m^*\psi_n dx=\delta_{mn}$. A normalized superposition is

$$\Psi(x,t)=\sum_n c_n\psi_n(x)e^{-iE_nt/\hbar},\qquad
\sum_n|c_n|^2=1.$$

Its energy-measurement probabilities are $|c_n|^2$. Its position density can
vary because different energies accumulate different phases.

## 4. Construct the finite-difference calculation

Place $N$ unknown samples at $x_j=j\Delta x$, where
$\Delta x=L/(N+1)$ and $j=1,\ldots,N$. The two walls are separate samples
$\psi_0=\psi_{N+1}=0$. Taylor expansion gives

$$\psi''(x_j)=\frac{\psi_{j+1}-2\psi_j+\psi_{j-1}}{\Delta x^2}
+O(\Delta x^2).$$

Therefore the Hamiltonian has diagonal entries $2\alpha$ and adjacent
off-diagonal entries $-\alpha$, where

$$\alpha=\frac{\hbar^2}{2m\Delta x^2}.$$

All other entries are zero. The matrix is real symmetric, so it can be
diagonalized with a symmetric eigensolver. The
[Python implementation](../examples/infinite_well.py) builds this matrix and
uses `numpy.linalg.eigh`. No analytic energy is used to construct its output.

The returned eigenvectors satisfy $\sum_j|v_j|^2=1$. To interpret them as
sampled continuum wavefunctions, use

$$\psi_j=\frac{v_j}{\sqrt{\Delta x}},\qquad
\Delta x\sum_j|\psi_j|^2=1.$$

An arbitrary eigenvector sign is harmless. Compare probabilities or the
absolute overlap with the analytic sine state. For fixed low $n$, reducing
$\Delta x$ by two should reduce the leading energy error by approximately
four. A small matrix eigenpair residual only means the **discrete** equation
was solved accurately; it does not measure the difference from the continuum.

## 5. Units and reproducible check

Run from the repository root after installing `requirements.txt`:

```bash
python examples/infinite_well.py --points 200 --states 3
python examples/infinite_well.py --points 400 --states 3
python -m unittest discover -s tests -p 'test_quantum.py' -v
```

The defaults set $\hbar=m=L=1$, so $E_1=\pi^2/2$, approximately
$4.9348022005$. To restore physical units, define $\xi=x/L$ and
$u(\xi)=\sqrt L\,\psi(x)$. The equation is

$$-\frac12\frac{d^2u}{d\xi^2}=\varepsilon u,\qquad
E=\frac{\hbar^2}{mL^2}\varepsilon.$$

Here $\varepsilon_n=n^2\pi^2/2$. The code's default numbers are these
$\varepsilon_n$, not energies in electronvolts. Consistent SI rescaling gives
joules. Increase resolution until the energy errors are acceptable for the
states being studied; the highest grid modes should not be assumed accurate.

## Exercises with worked answers

**1. What happens to $E_1$ when the well width doubles?**
The formula contains $L^{-2}$, so the energy becomes $E_1/4$. Doubling the
mass instead gives $E_1/2$. Both scaling laws are checked in the tests.

**2. What is the probability of finding a ground-state particle in the middle
half of the well?**
Integrate the density over $L/4<x<3L/4$:

$$P=\frac2L\int_{L/4}^{3L/4}\sin^2(\pi x/L)dx
=\left[\frac xL-\frac{\sin(2\pi x/L)}{2\pi}\right]_{L/4}^{3L/4}
=\frac12+\frac1\pi\approx0.81831.$$

**3. What energy is needed to raise the ground state to the first excited
state?**
The first excited state is $n=2$, so $E_2=4E_1$ and the energy difference is
$3E_1$. A photon supplying that energy would have angular frequency
$\omega=3E_1/\hbar$; whether an actual interaction drives the transition
also depends on its coupling matrix element.

**4. Why does $n=0$ fail even though zero satisfies $\sin(n\pi)=0$?**
It gives $\psi(x)=0$ for every position, whose norm is zero. It cannot be
normalized to one. Boundary conditions alone do not replace normalization.

## References and independent checks

For an instructor's treatment of the physical boundary conditions and exact
spectrum, see Barton Zwiebach,
[MIT 8.04, lecture 11](https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2016/a565b327f85c7721b18f1074dbd69ede_MIT8_04S16_LecNotes11.pdf),
section 1. For the matrix solver's API and normalization convention, see
[NumPy's `eigh` documentation](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigh.html).
The exercises, code, and validation checks in this module are original.
