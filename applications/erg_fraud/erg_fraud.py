# -*- coding: utf-8 -*-
"""
ERG-FRAUD — anomaly detection by "does the spike survive coarse-graining?" (MVP).

Spun out of the guard session's ERG idea (intensity != objectivity), applied to a
new field: fraud / anomaly detection on a stream of numbers (transactions per
window, amounts, event counts, sensor readings).

The core move: a real anomaly SURVIVES zoom-out. Coarse-grain the series at
several scales (average over bigger and bigger blocks) and see whether the peak
stays prominent:
  - a one-off spike (a single legit big purchase) is INTENSE at the finest scale
    but DISSOLVES when averaged -> NOISE, not fraud;
  - a distributed pattern (structuring / low-and-slow drain / a fraud ring: many
    small anomalous events clustered in time) SURVIVES coarse-graining -> REAL,
    even though no single event is large enough to trip a per-transaction threshold.

So it does the opposite of a naive threshold in exactly the two cases that matter:
it does NOT false-alarm on the legit one-off spike, and it DOES catch the
distributed fraud a threshold misses. No model, no training, no heavy database.
"""
import statistics as st
import random

SCALES = [1, 2, 4, 8, 16, 32]
PROMINENCE = 4.0      # peak must stand this many robust-sigma above typical
SURVIVE_SCALE = 8     # prominent up to at least this block size => structural (real)
MIN_BLOCKS = 12       # a scale is only reliable with at least this many blocks


def _blocks(series, scale):
    """Non-overlapping block means (the coarse-graining)."""
    return [st.mean(series[i:i + scale])
            for i in range(0, len(series) - scale + 1, scale)]


def _prominence(vals):
    """How far the peak stands above the typical value, in robust sigma (MAD)."""
    med = st.median(vals)
    mad = st.median([abs(v - med) for v in vals]) or 1e-9
    return (max(vals) - med) / (1.4826 * mad)


def analyze(series):
    proms = {}
    for s in SCALES:
        b = _blocks(series, s)
        if len(b) >= MIN_BLOCKS:               # skip coarse scales with too few blocks
            proms[s] = _prominence(b)
    prominent = [s for s, p in proms.items() if p >= PROMINENCE]
    top = max(prominent) if prominent else 0
    if not prominent:
        verdict = "CLEAN"
    elif top >= SURVIVE_SCALE:
        verdict = "REAL (survives coarse-graining)"
    else:
        verdict = "NOISE (intense but transient)"
    return verdict, top, proms


def naive_threshold(series, limit):
    """A per-event threshold detector, for contrast."""
    return "FLAG" if any(v > limit for v in series) else "clean"


# ---------- demo ----------
def _series(seed=42):
    # baseline: white-noise amounts ~ N(100, 23), length 512 (seeded -> reproducible)
    rng = random.Random(seed)
    base = [rng.gauss(100, 23) for _ in range(512)]

    normal = list(base)

    spike = list(base)
    spike[256] = 250                                  # one big-but-plausible purchase (~6 sigma)

    # distributed fraud: 32 consecutive mildly-elevated events (each ~137, only
    # ~1.5 sigma — individually unremarkable, under any per-transaction limit),
    # e.g. card-testing / structuring / a slow drain
    fraud = list(base)
    for i in range(200, 232):
        fraud[i] = rng.gauss(137, 5)
    return {"normal stream": normal, "one-off big purchase": spike,
            "distributed fraud (32 small)": fraud}


def run():
    LIMIT = 200
    print("ERG-FRAUD — 'does the spike survive coarse-graining?' (MVP)")
    print("=" * 72)
    print(f"{'stream':30} | {'naive >'+str(LIMIT):9} | ERG verdict")
    print("-" * 72)
    for name, series in _series().items():
        nv = naive_threshold(series, LIMIT)
        verdict, top, _ = analyze(series)
        note = ""
        if name.startswith("one-off") and nv == "FLAG":
            note = "  <- naive FALSE ALARM"
        if name.startswith("distributed") and nv == "clean":
            note = "  <- naive MISSES it"
        print(f"{name:30} | {nv:9} | {verdict:32}{note}")

    print("\n" + "=" * 72)
    print("Naive threshold: false-alarms on the legit spike AND misses the")
    print("distributed fraud. ERG does the opposite — because the fraud SURVIVES")
    print("zoom-out (a real structure) and the spike DISSOLVES (transient).")


if __name__ == "__main__":
    run()
