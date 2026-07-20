"""ERG-CAD demo — proves 'intensity != objectivity' on synthetic signals.

Run:  python demo.py
Also self-verifies (asserts) so it doubles as a no-dependency test.
"""

from erg_cad import ERGDetector, signals


def show(name, grid, stress=0.0):
    det = ERGDetector()
    r = det.analyze(grid, social_stress=stress)
    api = det.mask_api_output(r)
    print(f"\n=== {name}  (social_stress={stress}) ===")
    print(f"  [private] intensity={r.intensity}  objectivity={r.objectivity}  "
          f"peaks={r.level_peaks}")
    print(f"  [public ] {api}")
    return r, api


if __name__ == "__main__":
    print("ERG-CAD Objective Anomaly Detector — intensity != objectivity\n"
          "----------------------------------------------------------------")

    r1, a1 = show("A. Single STRONG spike (0.9, isolated)", signals.single_spike(0.9))
    r2, a2 = show("B. WEAK persistent signal (0.4, sustained)", signals.weak_persistent())
    r3, a3 = show("C. STRONG persistent signal (0.9, sustained)", signals.strong_persistent())
    r4, a4 = show("D. Same weak-persistent under HIGH stress", signals.weak_persistent(), stress=0.9)

    # ---- the money assertions: strong-but-transient loses to weak-but-persistent
    assert r1.risk_level == "NOISE", r1.risk_level
    assert r2.risk_level == "WATCH", r2.risk_level
    assert r3.risk_level == "CRITICAL", r3.risk_level
    assert r1.intensity > r2.intensity          # A is STRONGER than B ...
    assert r1.objectivity < r2.objectivity      # ... yet LESS objective
    # public API must never leak internal numbers
    for a in (a1, a2, a3, a4):
        assert set(a) == {"risk_level", "explanation",
                          "confidence_band", "recommended_action"}

    print("\n----------------------------------------------------------------")
    print("PROVEN: A (intensity 0.9) -> NOISE  while  B (intensity 0.4) -> WATCH.")
    print("Strong signal was rejected; weak-but-objective signal passed.")
    print("intensity != objectivity  ✔   API masking  ✔")
