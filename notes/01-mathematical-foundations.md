# 01 — Mathematical foundations

[Learning sequence](README.md) · [Next: quantum postulates](02-postulates-and-two-level-systems.md)

**Goal:** turn complex numbers and vectors into quantities that can represent
probabilities. Mathematics gives us a language; the physical interpretation
will be stated as postulates in the next chapter.

## 1. Complex numbers carry magnitude and phase

A complex number is $z=a+ib$, where $a,b$ are real and $i^2=-1$. Its conjugate
is $z^*=a-ib$. Multiplication gives

$$|z|^2=z^*z=(a-ib)(a+ib)=a^2+b^2.$$

For example, $z=3+4i$ has magnitude $5$. The quantity $z^2=-7+24i$ is not a
probability. The nonnegative real quantity $|z|^2=25$ can contribute to one after
normalization. In polar form,

$$z=r e^{i\theta}=r(\cos\theta+i\sin\theta),\qquad |z|^2=r^2.$$

An amplitude includes a phase $\theta$ that its squared magnitude alone does not
record. Two alternatives can therefore interfere when their amplitudes add.

## 2. States as vectors

Choose two orthonormal basis vectors

$$|0\rangle=\begin{pmatrix}1\\0\end{pmatrix},\qquad
|1\rangle=\begin{pmatrix}0\\1\end{pmatrix}.$$

A vector is $|\psi\rangle=a|0\rangle+b|1\rangle$. Its bra is the conjugate
transpose $\langle\psi|=(a^*,b^*)$. For
$|\phi\rangle=c|0\rangle+d|1\rangle$ the inner product is

$$\langle\phi|\psi\rangle=c^*a+d^*b.$$

The norm is $\|\psi\|=\sqrt{\langle\psi|\psi\rangle}$, so a normalized vector
satisfies $|a|^2+|b|^2=1$. Divide any nonzero vector by its norm to normalize it.
The zero vector cannot represent a state because it cannot be normalized.

For $|v\rangle=3|0\rangle+4i|1\rangle$,

$$\langle v|v\rangle=9+16=25,\qquad
|\psi\rangle=\frac35|0\rangle+\frac{4i}{5}|1\rangle.$$

Orthogonality means $\langle\phi|\psi\rangle=0$. For example, the normalized
vectors $|+\rangle=(|0\rangle+|1\rangle)/\sqrt2$ and
$|-\rangle=(|0\rangle-|1\rangle)/\sqrt2$ have inner product zero.

## 3. Global phase and relative phase

Multiplying the whole vector by $e^{i\alpha}$ changes no probability of the
form $|\langle\phi|\psi\rangle|^2$: the factor has magnitude one. That is
**global phase**. Multiplying just one coefficient changes a **relative phase**
and can change probabilities in another basis.

Consider the family

$$|\psi_\theta\rangle=\frac{|0\rangle+e^{i\theta}|1\rangle}{\sqrt2}.$$

The two basis amplitudes have equal squared magnitudes. However, its overlap
with $|+\rangle$ is $(1+e^{i\theta})/2$, giving

$$|\langle+|\psi_\theta\rangle|^2
=\frac{(1+e^{-i\theta})(1+e^{i\theta})}{4}
=\frac{1+\cos\theta}{2}.$$

The result is one for $\theta=0$, one-half for $\theta=\pi/2$, and zero for
$\theta=\pi$. Identical probabilities in one basis do not determine a state.

## 4. From vectors to wavefunctions

In a continuous position representation, a state is described by $\psi(x)$.
Sums become integrals:

$$\langle\phi|\psi\rangle=\int \phi^*(x)\psi(x)\,dx,\qquad
\int |\psi(x)|^2\,dx=1.$$

In one dimension, $\psi$ has units of inverse square root of length so that
$|\psi|^2dx$ is dimensionless. On a uniform grid, the approximation is
$\Delta x\sum_j|\psi_j|^2=1$. The factor $\Delta x$ is essential; it is why
an ordinary normalized numerical eigenvector requires rescaling in the
[square-well example](../examples/README.md).

## Exercises with worked answers

**1. Normalize $(1,i)$ and find its overlap with $|+\rangle$.**
The norm is $\sqrt2$, so the normalized state is $(1,i)/\sqrt2$. The overlap
is $(1+i)/2$, whose squared magnitude is $(1+1)/4=1/2$.

**2. Normalize a constant wavefunction on $0<x<L$.**
Write $\psi(x)=A$ inside the interval and zero elsewhere. Then
$1=\int_0^L |A|^2dx=|A|^2L$, so choose $A=1/\sqrt L$. This is a valid
normalization exercise; it does not satisfy the hard-wall energy-eigenstate
boundary conditions introduced in chapter 03.

**3. Are $(1,i)/\sqrt2$ and $(i,-1)/\sqrt2$ different physical pure states?**
The second equals $i$ times the first. Their global phase differs, but all
projective-measurement probabilities agree.

## Further study

For the underlying vector-space and bra-ket formalism, consult Barton
Zwiebach's [MIT 8.05 lecture notes, lectures 3–9](https://ocw.mit.edu/courses/8-05-quantum-physics-ii-fall-2013/pages/lecture-notes/).
For the wavefunction interpretation and normalization, see
[MIT 8.04, lecture 6](https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2016/d87c768c4e1181fde8d4366112169719_MIT8_04S16_LecNotes6.pdf).
