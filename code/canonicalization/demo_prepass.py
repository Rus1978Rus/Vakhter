# -*- coding: utf-8 -*-
"""
Show the double bottom on the REAL MSL:
  raw (digit-encoded)  -> MSL misses (bypass)
  canonicalized        -> MSL's existing cards catch it

Run:  MSL_MIP_HOME=/path/to/msl_mip  python demo_prepass.py
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "invariant_engine")))

from canonicalize import canonicalize
from invariant_engine import InvariantEngine, erg
from invariant_engine.msl_real import real_text_reader

msl = InvariantEngine(real_text_reader, erg.no_stream)
ZWSP = chr(0x200B)


def verdict(t):
    v = msl.analyze(t)
    return v.risk, v.finding.reason


def show(name, raw):
    canon, info = canonicalize(raw)
    r_raw, why_raw = verdict(raw)
    r_can, why_can = verdict(canon)
    disp = lambda s: s.replace(ZWSP, "‹ZWSP›")
    print(f"\n=== {name} ===")
    print(f"  raw       : {disp(raw)!r}")
    print(f"              MSL -> {r_raw:6}  ({why_raw})")
    print(f"  canonical : {disp(canon)!r}   [decode passes={info['decode_passes']}]")
    print(f"              MSL -> {r_can:6}  ({why_can})")
    flip = "CAUGHT after pre-pass ✔" if (r_raw == "OK" and r_can != "OK") else \
           "no change" if r_raw == r_can else "changed"
    print(f"  result    : {flip}")


if __name__ == "__main__":
    print("CANONICALIZATION_PRE_PASS on the REAL MSL")
    print("=" * 60)

    show("percent-encoded traversal", "%2e%2e%2f%2e%2e%2fetc/hosts")
    show("DOUBLE-encoded traversal", "%252e%252e%252fboot.ini")
    show("HTML-entity rebuilds INVISIBLE (ZWSP)", "admin&#8203;istrator")
    show("decimal IP host (127.0.0.1)", "http://2130706433/login")
    show("OVER-DECODE caveat (benign text about encoding)",
         "note: %2f is how a slash is written in a URL")

    print("\n" + "=" * 60)
    print("percent/entity: pre-pass wakes the EXISTING dot/solidus/ZWSP cards.")
    print("decimal IP    : pre-pass normalizes, but MSL still needs the DIGIT/IP")
    print("                card to flag it -> pre-pass and card are complementary.")
    print("over-decode   : benign '%2f'-mention got decoded -> honest FP risk.")
