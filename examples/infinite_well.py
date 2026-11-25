"""Finite-difference eigenstates of an infinite square well on [0, length].

Default units set hbar = mass = length = 1; the exact energies are n^2*pi^2/2.
All inputs must use one consistent unit system. No credentials or network access
are needed. See notes/03-infinite-square-well.md for the derivation.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from numbers import Integral, Real

import numpy as np


@dataclass(frozen=True)
class WellSolution:
    """Coordinates include both walls; wavefunctions are stored in columns."""

    x: np.ndarray
    energies: np.ndarray
    wavefunctions: np.ndarray
    dx: float


def _positive_real(name: str, value: float) -> float:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise ValueError(f"{name} must be a finite positive real number")
    value = float(value)
    if not np.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be a finite positive real number")
    return value


def _positive_integer(name: str, value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, Integral) or value < 1:
        raise ValueError(f"{name} must be a positive integer")
    return int(value)


def analytical_energies(
    states: int = 3, *, length: float = 1.0, mass: float = 1.0, hbar: float = 1.0
) -> np.ndarray:
    """Return continuum energies for n = 1, ..., states, in ascending order."""
    states = _positive_integer("states", states)
    length = _positive_real("length", length)
    mass = _positive_real("mass", mass)
    hbar = _positive_real("hbar", hbar)
    n = np.arange(1, states + 1, dtype=float)
    return (hbar * np.pi * n / length) ** 2 / (2.0 * mass)


def build_hamiltonian(
    points: int = 200, *, length: float = 1.0, mass: float = 1.0, hbar: float = 1.0
) -> tuple[np.ndarray, np.ndarray]:
    """Return interior coordinates and a real symmetric Hamiltonian matrix.

    ``points`` counts interior unknowns, not walls. Dirichlet values at x=0 and
    x=length are zero, so they are excluded from the matrix. The three-point
    second derivative has O(dx**2) truncation error for smooth eigenfunctions.
    A dense matrix keeps this teaching implementation easy to inspect.
    """
    points = _positive_integer("points", points)
    length = _positive_real("length", length)
    mass = _positive_real("mass", mass)
    hbar = _positive_real("hbar", hbar)
    dx = length / (points + 1)
    x = dx * np.arange(1, points + 1, dtype=float)
    coefficient = hbar**2 / (2.0 * mass * dx**2)
    diagonal = np.full(points, 2.0 * coefficient)
    off_diagonal = np.full(points - 1, -coefficient)
    hamiltonian = (
        np.diag(diagonal)
        + np.diag(off_diagonal, k=1)
        + np.diag(off_diagonal, k=-1)
    )
    return x, hamiltonian


def solve_well(
    points: int = 200,
    states: int = 3,
    *,
    length: float = 1.0,
    mass: float = 1.0,
    hbar: float = 1.0,
) -> WellSolution:
    """Solve for low-lying states and normalize with dx*sum(abs(psi)**2)=1.

    ``numpy.linalg.eigh`` normalizes vectors by sum(abs(v)**2)=1. Dividing by
    sqrt(dx) converts to sampled continuum wavefunctions. Endpoints are padded
    with exact zeros; these do not change the weighted norm. Eigenvector signs
    are arbitrary and should not be used as a correctness criterion.
    """
    points = _positive_integer("points", points)
    states = _positive_integer("states", states)
    if states > points:
        raise ValueError("states cannot exceed the number of interior points")
    interior, hamiltonian = build_hamiltonian(
        points, length=length, mass=mass, hbar=hbar
    )
    dx = float(interior[0])
    energies, vectors = np.linalg.eigh(hamiltonian)
    wavefunctions = np.zeros((points + 2, states), dtype=float)
    wavefunctions[1:-1, :] = vectors[:, :states] / np.sqrt(dx)
    x = np.concatenate(([0.0], interior, [float(length)]))
    return WellSolution(x, energies[:states], wavefunctions, dx)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--points", type=int, default=200, help="interior grid points")
    parser.add_argument("--states", type=int, default=3, help="lowest states to report")
    parser.add_argument("--length", type=float, default=1.0, help="well width")
    parser.add_argument("--mass", type=float, default=1.0, help="particle mass")
    parser.add_argument("--hbar", type=float, default=1.0, help="reduced Planck constant")
    args = parser.parse_args()
    parameters = {"length": args.length, "mass": args.mass, "hbar": args.hbar}
    try:
        solution = solve_well(args.points, args.states, **parameters)
        exact = analytical_energies(args.states, **parameters)
    except ValueError as error:
        parser.error(str(error))

    print(f"Infinite well: L={args.length:g}, m={args.mass:g}, hbar={args.hbar:g}")
    print(f"Interior points: {args.points}; dx={solution.dx:.8g}")
    print("n   numerical energy   exact energy       relative error   weighted norm")
    norms = solution.dx * np.sum(np.abs(solution.wavefunctions) ** 2, axis=0)
    for n, (numeric, analytic, norm) in enumerate(
        zip(solution.energies, exact, norms), start=1
    ):
        error = abs(numeric - analytic) / analytic
        print(f"{n:<3d} {numeric:16.10f} {analytic:16.10f} {error:16.6e} {norm:15.10f}")
    print("Energies use the units implied by L, m, and hbar; defaults are dimensionless.")
    print("Repeat with --points 400 to check convergence of the low-energy states.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
