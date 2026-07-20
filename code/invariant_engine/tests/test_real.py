# -*- coding: utf-8 -*-
"""
Tests for the REAL MSL adapter (needs the msl_mip repo).
Run:  MSL_MIP_HOME=/path/to/msl_mip python tests/test_real.py
  or from inside the repo:  python tests/test_real.py
If the repo can't be found, these tests SKIP (they don't fail).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from invariant_engine import InvariantEngine, erg

ZWSP = chr(0x200B)

try:
    from invariant_engine.msl_real import real_text_reader
    real_text_reader("warmup")
    HAVE_MSL = True
except Exception as ex:                       # repo missing -> skip, don't fail
    HAVE_MSL = False
    _WHY = str(ex)

STREAM = ["hello"+ZWSP+"world", "please"+ZWSP+"review", "invoice"+ZWSP+"x",
          "see you monday", "lunch at 1pm", "confirm"+ZWSP+"now",
          "thanks", "urgent"+ZWSP+"do"]


def _engines():
    txt = InvariantEngine(real_text_reader,
                          erg.recurrence_survival(lambda s: STREAM, reader=real_text_reader))
    lone = InvariantEngine(real_text_reader, erg.no_stream)
    return txt, lone


def run():
    if not HAVE_MSL:
        print(f"SKIP  real MSL tests — msl_mip repo not found ({_WHY})")
        return True
    txt, lone = _engines()
    checks = [
        ("clean_text_ok",      lambda: lone.analyze("lunch at 1pm").risk == "OK"),
        ("clean_code_ok",      lambda: lone.analyze("def f(a): return a").risk == "OK"),
        ("phishing_alarm",     lambda: lone.analyze("paypal.com.security-check.ru/verify").risk == "ALARM"),
        ("path_traversal_alarm", lambda: lone.analyze("path/../../etc/passwd").risk == "ALARM"),
        ("manydots_no_fp",     lambda: lone.analyze("a.b.c.d.e.f.g").risk == "OK"),
        ("zwsp_lone_watch",    lambda: lone.analyze("hello"+ZWSP+"world").risk == "WATCH"),
        ("zwsp_recurring_alarm", lambda: txt.analyze("hello"+ZWSP+"world").risk == "ALARM"),
        ("real_engine_used",   lambda: "MSL" in lone.analyze("paypal.com.a.ru/x").finding.reason),
    ]
    ok = 0
    for name, fn in checks:
        try:
            assert fn(); print("PASS ", name); ok += 1
        except AssertionError:
            print("FAIL ", name)
    print(f"\n{ok}/{len(checks)} passed")
    return ok == len(checks)


if __name__ == "__main__":
    sys.exit(0 if run() else 1)
