"""pytest suite = ERG-CAD acceptance criteria A/B/C + security (API masking).

Run:  pytest            (if pytest installed)
  or:  python tests/test_detector.py   (falls back to a plain runner)
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from erg_cad import ERGDetector, signals


det = ERGDetector()


def test_A_single_spike_is_noise():
    r = det.analyze(signals.single_spike(0.9))
    assert r.risk_level == "NOISE"
    assert r.intensity >= 0.9          # it really is a strong spike
    assert r.objectivity < 0.35        # ...but it did not survive


def test_B_weak_persistent_passes():
    r = det.analyze(signals.weak_persistent())
    assert r.risk_level == "WATCH"
    assert r.objectivity >= 0.50        # clearly survives (vs ~0.016 for a spike)
    assert r.intensity < 0.6            # yet only moderate intensity


def test_C_strong_persistent_is_critical():
    r = det.analyze(signals.strong_persistent())
    assert r.risk_level == "CRITICAL"


def test_intensity_is_not_objectivity():
    spike = det.analyze(signals.single_spike(0.9))
    weak = det.analyze(signals.weak_persistent())
    assert spike.intensity > weak.intensity        # spike is STRONGER
    assert spike.objectivity < weak.objectivity    # but LESS objective
    assert spike.risk_level == "NOISE" and weak.risk_level == "WATCH"


def test_adaptive_plasticity_tightens_under_stress():
    calm = det.analyze(signals.weak_persistent(), social_stress=0.0)
    stressed = det.analyze(signals.weak_persistent(), social_stress=0.9)
    assert stressed.thresholds.objectivity_hi > calm.thresholds.objectivity_hi


def test_api_masking_hides_internals():
    r = det.analyze(signals.strong_persistent())
    api = det.mask_api_output(r)
    assert set(api) == {"risk_level", "explanation",
                        "confidence_band", "recommended_action"}
    blob = repr(api).lower()
    for leak in ("intensity", "objectivity", "threshold", "peak", "0."):
        assert leak not in blob, f"leaked: {leak}"


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    passed = 0
    for fn in fns:
        try:
            fn(); print(f"PASS  {fn.__name__}"); passed += 1
        except AssertionError as e:
            print(f"FAIL  {fn.__name__}: {e}")
    print(f"\n{passed}/{len(fns)} passed")
    sys.exit(0 if passed == len(fns) else 1)
