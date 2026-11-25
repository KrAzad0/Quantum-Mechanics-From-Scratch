# 02 — Postulates and two-level systems

[Previous: mathematics](01-mathematical-foundations.md) · [Learning sequence](README.md) · [Next: infinite well](03-infinite-square-well.md)

**Goal:** predict measurement probabilities and solve one time-dependent
quantum system exactly. This chapter treats pure states and ideal projective
measurements in finite dimensions. Mixed states and general measurements are
outside this first module.

## 1. The working postulates

A normalized state vector $|\psi\rangle$ represents a pure state, with vectors
that differ only by a global phase representing the same state. An observable
is represented by a Hermitian matrix $A=A^\dagger$. Its spectral decomposition
is

$$A=\sum_a aP_a,$$

where the real eigenvalues $a$ are possible measurement results and $P_a$ is
the orthogonal projector onto the corresponding eigenspace. This formulation
also handles degeneracy. For an ideal projective measurement,

$$p(a)=\langle\psi|P_a|\psi\rangle,\qquad
|\psi\rangle\longrightarrow\frac{P_a|\psi\rangle}{\sqrt{p(a)}}$$

conditional on observing an outcome with $p(a)>0$. For a nondegenerate
eigenvector $|a\rangle$, the probability reduces to
$|\langle a|\psi\rangle|^2$. The expectation value is

$$\langle A\rangle=\sum_a a\,p(a)=\langle\psi|A|\psi\rangle.$$

It is an average over repeated preparations, not necessarily a value available
in a single measurement. In continuous-variable systems, operator domains and
self-adjointness need additional care; a formal conjugate transpose alone is
not sufficient.

Between measurements an isolated system evolves according to

$$i\hbar\frac{d}{dt}|\psi(t)\rangle=H(t)|\psi(t)\rangle.$$

The Hermitian Hamiltonian $H$ is the energy operator. For time-independent $H$,
$|\psi(t)\rangle=e^{-iHt/\hbar}|\psi(0)\rangle$. Hermiticity makes this
evolution unitary and preserves the norm. These are physical postulates whose
predictions are tested experimentally, not consequences of normalization alone.

## 2. A measurement calculation

Use the dimensionless observable

$$Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
|\psi\rangle=\frac35|0\rangle+\frac{4i}{5}|1\rangle.$$

The results are $+1$ and $-1$, with probabilities $9/25$ and $16/25$.
Consequently,

$$\langle Z\rangle=\frac9{25}-\frac{16}{25}=-\frac7{25}.$$

Because $Z^2=I$, the variance is

$$ (\Delta Z)^2=\langle Z^2\rangle-\langle Z\rangle^2
=1-\frac{49}{625}=\frac{576}{625}.$$

The standard deviation is $24/25$. For a physical spin component
$S_z=(\hbar/2)Z$, multiply the expectation and standard deviation by
$\hbar/2$. The available spin results are then $\pm\hbar/2$.

## 3. A solvable two-level Hamiltonian

Let $\Omega>0$ have units of inverse time and choose

$$H=\frac{\hbar\Omega}{2}X,\qquad
X=\begin{pmatrix}0&1\\1&0\end{pmatrix}.$$

Since $X^2=I$, even and odd terms of the exponential series separate:

$$U(t)=e^{-i\Omega tX/2}
=I\cos\left(\frac{\Omega t}{2}\right)
-iX\sin\left(\frac{\Omega t}{2}\right).$$

Starting from $|0\rangle$ and using $X|0\rangle=|1\rangle$ gives

$$|\psi(t)\rangle=\cos\left(\frac{\Omega t}{2}\right)|0\rangle
-i\sin\left(\frac{\Omega t}{2}\right)|1\rangle.$$

Thus a measurement in the original basis has probabilities

$$p_0(t)=\cos^2\left(\frac{\Omega t}{2}\right),\qquad
p_1(t)=\sin^2\left(\frac{\Omega t}{2}\right).$$

They sum to one. At $t=\pi/\Omega$ the state is $-i|1\rangle$, so outcome
1 is certain. At $t=2\pi/\Omega$ it is $-|0\rangle$, which represents the
same physical state as the initial one.

The energy eigenvectors are $|+\rangle$ and $|-\rangle$, with energies
$+\hbar\Omega/2$ and $-\hbar\Omega/2$. In that basis the evolution simply
changes two phases. Their changing relative phase produces oscillations when
we measure in the original basis. The negative eigenvalue is allowed: this
Hamiltonian's energy zero was chosen halfway between its two levels.

## Exercises with worked answers

**1. What is $\langle Z\rangle(t)$ for the evolving state above?**
Subtract the two outcome probabilities:
$\langle Z\rangle=p_0-p_1=\cos(\Omega t)$.

**2. Does changing occupation probability mean the average energy changes?**
No. The Hamiltonian is time independent and the system is isolated. Directly,
$\langle X\rangle=2\operatorname{Re}(a^*b)=0$ because
$a=\cos(\Omega t/2)$ and $b=-i\sin(\Omega t/2)$. Hence
$\langle H\rangle=0$ at all times. The initial energy probabilities are equal.

**3. If result $+1$ is observed in a $Z$ measurement, what happens on an immediate
repeat with no intervening evolution?**
The conditional state is $|0\rangle$, up to global phase. Its probability of
another $+1$ result is one. The state before the first measurement need not
have been $|0\rangle$.

## Further study

The formalism and dynamics can be checked against Barton Zwiebach's
[MIT 8.05 instructor notes](https://ocw.mit.edu/courses/8-05-quantum-physics-ii-fall-2013/pages/lecture-notes/),
especially lectures 3–4 (spin and operators), 12–16 (quantum dynamics), and
16–18 (two-state systems). The worked numerical choices and derivation here
are original to this module.
