# SPDX-License-Identifier: LicenseRef-Proprietary
"""Synthetic signal generators = the 'golden traces' test substrate.

Grid convention: grid[t][n]  (time steps x sensor nodes), values in 0..1.
"""

from typing import List

Grid = List[List[float]]


def blank(t: int = 8, n: int = 8) -> Grid:
    return [[0.0] * n for _ in range(t)]


def single_spike(amplitude: float = 0.9, t: int = 8, n: int = 8) -> Grid:
    """One node, one instant, very strong. High intensity, zero persistence."""
    g = blank(t, n)
    g[t // 2][n // 2] = amplitude
    return g


def persistent(amplitude: float, t: int = 8, n: int = 8,
               span_t: int = 6, span_n: int = 6) -> Grid:
    """A block sustained over time and across nodes. Survives coarse-graining."""
    g = blank(t, n)
    t0 = (t - span_t) // 2
    n0 = (n - span_n) // 2
    for i in range(t0, t0 + span_t):
        for j in range(n0, n0 + span_n):
            g[i][j] = amplitude
    return g


def weak_persistent(t: int = 8, n: int = 8) -> Grid:
    return persistent(0.40, t, n)


def strong_persistent(t: int = 8, n: int = 8) -> Grid:
    return persistent(0.90, t, n)
