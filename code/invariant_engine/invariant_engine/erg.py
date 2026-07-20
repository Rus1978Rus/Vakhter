"""
ERG role — survival testers (the 'reality' axis).

Same question two ways: does the structure SURVIVE a transform?
  - across SCALE  : coarse-grain a signal grid (renormalization).
  - across TIME   : recurrence of a signature within a stream.

'reality' is 0..1. High = survived (objective). Low = collapsed (noise).
"""


# ---- across scale: coarse-graining (renormalization) -------------------
def _coarse_grain(grid):
    t = len(grid); n = len(grid[0]) if t else 0
    t2, n2 = (t + 1) // 2, (n + 1) // 2
    out = [[0.0] * n2 for _ in range(t2)]
    for i in range(t2):
        for j in range(n2):
            cells = [grid[2*i+di][2*j+dj]
                     for di in (0, 1) for dj in (0, 1)
                     if 2*i+di < t and 2*j+dj < n]
            out[i][j] = sum(cells) / len(cells)
    return out


def _peak(grid):
    return max((max(r) for r in grid), default=0.0)


def scale_survival(levels: int = 3):
    """ERG for signal grids: fraction of peak that survives coarse-graining."""
    def survive(grid, finding):
        g, p0 = grid, _peak(grid)
        if p0 <= 0:
            return 0.0
        for _ in range(levels):
            g = _coarse_grain(g)
        return _peak(g) / p0
    return survive


# ---- across time: recurrence within a stream ---------------------------
def recurrence_survival(get_stream, reader=None):
    """ERG for text/code: how much the finding recurs across a live stream.

    get_stream(subject) -> list of OTHER items (their raw form). Each is
    re-read with `reader` (the SAME structural reader the engine uses — stub
    or real MSL) and we count how many share this subject's signature.
    Self is excluded, so a lone item with no corroboration scores 0.
    """
    def survive(subject, finding):
        rd = reader
        if rd is None:
            from .msl import text_reader as rd
        stream = get_stream(subject) or []
        if len(stream) <= 1:
            return 0.0
        sig = finding.signature
        matches = sum(1 for item in stream if rd(item).signature == sig)
        matches = max(0, matches - 1)          # exclude the subject itself
        return matches / (len(stream) - 1)
    return survive


def no_stream(subject, finding):
    """ERG stub: no feed available -> nothing to corroborate against."""
    return 0.0
