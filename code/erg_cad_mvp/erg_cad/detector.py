"""
ERG-CAD · Objective Anomaly Detector — runnable MVP of the core node.

Demonstrates the founding principle of the whole ACDM-ST / ERG-CAD line:

    INTENSITY  !=  OBJECTIVITY
    (a strong signal is not necessarily an objective one)

A signal is treated as a field of activation over a grid of
(time steps  x  sensor nodes). The detector applies RG-style
coarse-graining (repeated block-averaging = a renormalization step)
and measures how much of the signal SURVIVES rescaling.

    - An isolated high spike collapses fast under coarse-graining
      -> high intensity, low objectivity  -> NOISE.
    - A weak but spatially/temporally persistent structure survives
      -> moderate intensity, high objectivity -> WATCH.
    - A strong AND persistent structure survives at high amplitude
      -> high intensity, high objectivity -> CRITICAL.

Pure standard library. No external dependencies (msl_mip house style).

Public/private boundary (per ERG-CAD security spec):
  - `analyze()` returns the FULL internal reading (PRIVATE — scores, survivals).
  - `mask_api_output()` returns only a safe client view (risk_level,
    explanation, confidence_band, recommended_action) — no raw internals.
"""

from dataclasses import dataclass, field
from typing import List, Dict


Grid = List[List[float]]


# --------------------------------------------------------------------------
# RG core: coarse-graining (renormalization step) and survival measurement
# --------------------------------------------------------------------------

def coarse_grain(grid: Grid) -> Grid:
    """One RG step: 2x2 average-pool. Halves each dimension (ceil).

    Average pooling is the key: an isolated hot cell gets diluted by its
    cold neighbours (peak ~ /4 per level), while a broad plateau keeps its
    amplitude. That asymmetry IS the intensity/objectivity separation.
    """
    t = len(grid)
    n = len(grid[0]) if t else 0
    t2, n2 = (t + 1) // 2, (n + 1) // 2
    out = [[0.0] * n2 for _ in range(t2)]
    for i in range(t2):
        for j in range(n2):
            cells = []
            for di in (0, 1):
                for dj in (0, 1):
                    ii, jj = 2 * i + di, 2 * j + dj
                    if ii < t and jj < n:
                        cells.append(grid[ii][jj])
            out[i][j] = sum(cells) / len(cells)
    return out


def peak(grid: Grid) -> float:
    return max((max(row) for row in grid), default=0.0)


def rg_filter_pipeline(grid: Grid, levels: int) -> List[float]:
    """Return the peak amplitude at each RG level (level 0 = raw)."""
    g = grid
    peaks = [peak(g)]
    for _ in range(levels):
        g = coarse_grain(g)
        peaks.append(peak(g))
    return peaks


# --------------------------------------------------------------------------
# Adaptive plasticity: thresholds tighten under "social stress" (system load)
# --------------------------------------------------------------------------

@dataclass
class Thresholds:
    objectivity_hi: float = 0.35   # min survival to be considered "real"
    intensity_hi: float = 0.60     # amplitude above which risk escalates


def adaptive_weight_update(base: Thresholds, social_stress: float) -> Thresholds:
    """Under load (0..1) demand MORE objectivity and MORE intensity to fire.

    Honours the 'Adaptive Aerodynamic Plasticity' requirement: an overloaded
    system trusts single events less and requires stronger persistence.
    """
    s = max(0.0, min(1.0, social_stress))
    return Thresholds(
        objectivity_hi=min(0.95, base.objectivity_hi + 0.40 * s),
        intensity_hi=min(0.95, base.intensity_hi + 0.25 * s),
    )


# --------------------------------------------------------------------------
# Detector
# --------------------------------------------------------------------------

@dataclass
class Reading:
    """PRIVATE internal reading — never returned raw through the public API."""
    intensity: float
    objectivity: float
    level_peaks: List[float] = field(default_factory=list)
    risk_level: str = "NOISE"
    thresholds: Thresholds = field(default_factory=Thresholds)


class ERGDetector:
    def __init__(self, rg_levels: int = 3, base_thresholds: Thresholds = None):
        self.rg_levels = rg_levels
        self.base = base_thresholds or Thresholds()

    # --- core detection --------------------------------------------------
    def analyze(self, grid: Grid, social_stress: float = 0.0) -> Reading:
        peaks = rg_filter_pipeline(grid, self.rg_levels)
        intensity = peaks[0]
        # objectivity = fraction of peak that survives full coarse-graining
        objectivity = (peaks[-1] / peaks[0]) if peaks[0] > 0 else 0.0
        th = adaptive_weight_update(self.base, social_stress)

        if objectivity < th.objectivity_hi:
            risk = "NOISE"                      # strong or not, it did not survive
        elif intensity < th.intensity_hi:
            risk = "WATCH"                       # weak but objective -> keep an eye
        else:
            risk = "CRITICAL"                    # strong AND objective

        return Reading(intensity=round(intensity, 4),
                       objectivity=round(objectivity, 4),
                       level_peaks=[round(p, 4) for p in peaks],
                       risk_level=risk,
                       thresholds=th)

    # --- public/private boundary ----------------------------------------
    @staticmethod
    def mask_api_output(reading: Reading) -> Dict[str, str]:
        """Client-safe view. No raw scores, weights, thresholds or traces."""
        explanations = {
            "NOISE":    "Signal did not survive coarse-graining; high local "
                        "intensity collapsed under aggregation.",
            "WATCH":    "Signal persisted across aggregation levels despite "
                        "moderate intensity.",
            "CRITICAL": "Signal persisted across several aggregation levels "
                        "and did not collapse under filtering.",
        }
        actions = {
            "NOISE": "No action; log as transient.",
            "WATCH": "Monitor; re-evaluate on recurrence.",
            "CRITICAL": "Escalate for human review.",
        }
        band = "high" if reading.objectivity >= 0.66 else \
               "medium" if reading.objectivity >= 0.33 else "low"
        return {
            "risk_level": reading.risk_level,
            "explanation": explanations[reading.risk_level],
            "confidence_band": band,
            "recommended_action": actions[reading.risk_level],
        }
