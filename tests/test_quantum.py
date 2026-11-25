"""Physical and numerical checks independent of a particular eigenvector sign."""

import unittest

import numpy as np

from examples.infinite_well import analytical_energies, build_hamiltonian, solve_well


class InfiniteWellTests(unittest.TestCase):
    def test_low_energies_match_continuum_solution(self):
        result = solve_well(points=200, states=3)
        expected = np.pi**2 * np.array([1.0, 4.0, 9.0]) / 2.0
        np.testing.assert_allclose(result.energies, expected, rtol=2e-4)
        self.assertTrue(np.all(result.energies > 0))

    def test_error_converges_at_second_order(self):
        exact_ground = np.pi**2 / 2.0
        errors = [
            abs(solve_well(points=n, states=1).energies[0] - exact_ground)
            for n in (31, 63, 127)
        ]
        # These point counts halve dx exactly. A second-order method reduces
        # the asymptotic error by four, not merely by an arbitrary tolerance.
        for coarse, fine in zip(errors, errors[1:]):
            self.assertGreater(coarse / fine, 3.9)
            self.assertLess(coarse / fine, 4.1)

    def test_weighted_normalization_and_orthogonality(self):
        result = solve_well(points=63, states=5, length=2.5)
        gram = result.dx * result.wavefunctions.conj().T @ result.wavefunctions
        np.testing.assert_allclose(gram, np.eye(5), rtol=0, atol=2e-13)

    def test_boundaries_and_grid(self):
        result = solve_well(points=20, states=3, length=2.0)
        self.assertEqual(result.wavefunctions.shape, (22, 3))
        self.assertEqual(result.x[0], 0.0)
        self.assertEqual(result.x[-1], 2.0)
        np.testing.assert_array_equal(result.wavefunctions[[0, -1], :], 0.0)
        np.testing.assert_allclose(np.diff(result.x), result.dx, atol=1e-14)

    def test_hamiltonian_is_hermitian_and_eigenpairs_have_small_residual(self):
        _, hamiltonian = build_hamiltonian(points=63)
        np.testing.assert_array_equal(hamiltonian, hamiltonian.conj().T)
        result = solve_well(points=63, states=4)
        interior = result.wavefunctions[1:-1]
        residual = hamiltonian @ interior - interior * result.energies
        relative_residual = np.linalg.norm(residual, axis=0) / (
            np.linalg.norm(hamiltonian, ord=np.inf)
            * np.linalg.norm(interior, axis=0)
        )
        self.assertLess(float(relative_residual.max()), 2e-14)

    def test_wavefunctions_match_sine_states_up_to_sign(self):
        result = solve_well(points=63, states=4, length=1.7)
        n = np.arange(1, 5)
        exact = np.sqrt(2.0 / 1.7) * np.sin(np.pi * result.x[:, None] * n / 1.7)
        overlaps = result.dx * np.sum(exact * result.wavefunctions, axis=0)
        np.testing.assert_allclose(np.abs(overlaps), 1.0, atol=2e-13, rtol=0)

    def test_physical_parameter_scaling(self):
        base = solve_well(points=40, states=3).energies
        for parameters, factor in (
            ({"length": 2.0}, 0.25),
            ({"mass": 2.0}, 0.5),
            ({"hbar": 2.0}, 4.0),
        ):
            with self.subTest(parameters=parameters):
                result = solve_well(points=40, states=3, **parameters)
                np.testing.assert_allclose(result.energies, base * factor, rtol=2e-12)
                np.testing.assert_allclose(
                    analytical_energies(3, **parameters),
                    np.pi**2 * np.array([1.0, 4.0, 9.0]) / 2.0 * factor,
                    rtol=2e-15,
                )

    def test_invalid_grid_and_state_counts_are_rejected(self):
        for value in (0, -1, 3.5, True, "10"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    solve_well(points=value, states=1)
                with self.assertRaises(ValueError):
                    solve_well(points=10, states=value)
                with self.assertRaises(ValueError):
                    analytical_energies(value)
        with self.assertRaises(ValueError):
            solve_well(points=2, states=3)

    def test_invalid_physical_parameters_are_rejected(self):
        for name in ("length", "mass", "hbar"):
            for value in (0.0, -1.0, np.nan, np.inf, True, "1.0", 1j):
                with self.subTest(name=name, value=value):
                    with self.assertRaises(ValueError):
                        solve_well(points=5, states=1, **{name: value})
                    with self.assertRaises(ValueError):
                        analytical_energies(1, **{name: value})


if __name__ == "__main__":
    unittest.main()
