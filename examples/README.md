# Reproducible calculations

The first example solves the one-dimensional **infinite square well** using a
finite-difference Hamiltonian. It compares numerical eigenvalues with an exact
continuum solution. It makes no network requests and needs no API key or account.

## Run

From the repository root, with Python 3.11 or newer:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python examples/infinite_well.py --points 200 --states 3
python -m unittest discover -s tests -p 'test_quantum.py' -v
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1` instead. Package
installation requires internet access if NumPy is not cached; the calculation
itself runs locally. The reference environment is Python 3.12 and NumPy 2.3.5.

## What the numbers mean

The defaults use units in which the reduced Planck constant, particle mass, and
well width are each one. The exact first three energies are therefore
`4.9348022005`, `19.7392088022`, and `44.4132198049`. They are **not electronvolts**.
For a physical width `L` and mass `m`, multiply the default energy numbers by
`hbar_physical**2 / (m * L**2)` in a consistent unit system. Equivalently, supply
`--length`, `--mass`, and `--hbar` in one consistent set of units. SI input produces
energies in joules, but dimensionless calculation and subsequent rescaling are
preferable for extreme scales. The formatted table targets dimensionless examples.

`--points` counts interior points; two additional endpoints enforce zero
wavefunction at the walls. `--states` selects the lowest eigenstates and must not
exceed `--points`. Each wavefunction column obeys

$$\Delta x\sum_j |\psi_j|^2=1.$$

Do not treat a raw eigensolver vector with `sum(abs(v)**2)=1` as a sampled
continuum wavefunction: it must be divided by `sqrt(dx)` first. The overall sign
of a numerical eigenvector is arbitrary.

## Convergence and scope

Repeat with `--points 400`. For a fixed low-lying state, doubling the number of
intervals reduces the leading discretization error by approximately four. The
tests use 31, 63, and 127 interior points so the interval spacing halves exactly.
High-energy states near the grid resolution are inaccurate even when the
eigensolver residual is tiny. Compare the continuum energy and refine the grid.

This implementation intentionally uses a dense symmetric matrix: memory grows
as the square of the point count and dense diagonalization is expensive for
large grids. Start at 200 points. It is an inspectable learning example, not a
large-scale or general-purpose quantum simulator. No MATLAB implementation is
claimed in this release.

Read the [full derivation](../notes/03-infinite-square-well.md). The matrix solver
uses [`numpy.linalg.eigh`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigh.html),
which returns ascending eigenvalues and normalized eigenvectors for symmetric
or Hermitian matrices. The tests check the spectrum, second-order convergence,
weighted normalization and orthogonality, boundaries, eigenpair residuals,
sine-state overlaps, physical scaling, and invalid inputs.
