# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""One core, many substrates. Run: pytest  or  python tests/test_engine.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from invariant_engine import InvariantEngine, msl, erg


def blank(t=8, n=8): return [[0.0]*n for _ in range(t)]
def spike(a=0.9):
    g = blank(); g[4][4] = a; return g
def persistent(a):
    g = blank()
    for i in range(1, 7):
        for j in range(1, 7): g[i][j] = a
    return g

SIG = InvariantEngine(msl.signal_reader, erg.scale_survival(3))

STREAM = ["paypal.com.a.ru/x", "paypal.com.b.ru/y", "paypal.com.c.ru/z",
          "hi there", "invoice attached", "paypal.com.d.ru/w",
          "see you monday", "paypal.com.e.ru/q"]
TXT = InvariantEngine(msl.text_reader, erg.recurrence_survival(lambda s: STREAM))
LONE = InvariantEngine(msl.text_reader, erg.no_stream)
CODE_INVIS = "x = user.is" + chr(0x200B) + "admin"


# ---- signal axis (scale) : intensity != objectivity --------------------
def test_signal_strong_spike_is_noise():
    assert SIG.analyze(spike(0.9)).risk == "NOISE"

def test_signal_weak_persistent_is_watch():
    assert SIG.analyze(persistent(0.4)).risk == "WATCH"

def test_signal_strong_persistent_is_alarm():
    assert SIG.analyze(persistent(0.9)).risk == "ALARM"

def test_signal_intensity_is_not_objectivity():
    sp, wk = SIG.analyze(spike(0.9)), SIG.analyze(persistent(0.4))
    assert sp.finding.strength > wk.finding.strength      # spike stronger
    assert sp.reality < wk.reality                         # yet less objective
    assert sp.risk == "NOISE" and wk.risk == "WATCH"


# ---- text axis (time) : one-off vs recurring ---------------------------
def test_text_lone_mimic_is_watch():
    assert LONE.analyze("paypal.com.a.ru/x").risk == "WATCH"

def test_text_recurring_mimic_is_alarm():
    assert TXT.analyze("paypal.com.a.ru/x").risk == "ALARM"

def test_text_harmless_is_ok():
    assert LONE.analyze("lunch at 1pm?").risk == "OK"


# ---- code : structural, conclusive, no feed needed ---------------------
def test_code_invisible_char_is_alarm():
    v = LONE.analyze(CODE_INVIS)
    assert v.risk == "ALARM" and v.finding.conclusive

def test_code_clean_is_ok():
    assert LONE.analyze("def add(a, b): return a + b").risk == "OK"


# ---- one core drives all substrates ------------------------------------
def test_same_core_three_substrates():
    assert SIG.analyze(spike(0.9)).risk == "NOISE"       # signal
    assert TXT.analyze("paypal.com.a.ru/x").risk == "ALARM"  # text
    assert LONE.analyze(CODE_INVIS).risk == "ALARM"      # code


# ---- public API never leaks internals ----------------------------------
def test_api_masking_hides_internals():
    api = SIG.mask(SIG.analyze(persistent(0.9)))
    assert set(api) == {"risk_level", "explanation",
                        "confidence_band", "recommended_action"}


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    ok = 0
    for fn in fns:
        try:
            fn(); print("PASS ", fn.__name__); ok += 1
        except AssertionError as e:
            print("FAIL ", fn.__name__, e)
    print(f"\n{ok}/{len(fns)} passed")
    sys.exit(0 if ok == len(fns) else 1)
