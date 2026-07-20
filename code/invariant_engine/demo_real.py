# -*- coding: utf-8 -*-
"""
REAL demo — the invariant engine driven by the ACTUAL msl_mip runtime
(no stub). Needs the msl_mip repo:  MSL_MIP_HOME=/path/to/msl_mip python demo_real.py
(or run from inside the repo).
"""
from invariant_engine import InvariantEngine, erg
from invariant_engine.msl_real import real_text_reader

ZWSP = chr(0x200B)

# A live "inbox": some items carry a zero-width space (MSL -> queue_for_review),
# so the SAME ambiguous signature recurs across the stream.
STREAM = [
    "hello" + ZWSP + "world",
    "please" + ZWSP + "review",
    "invoice" + ZWSP + "2026",
    "see you monday",
    "lunch at 1pm",
    "confirm" + ZWSP + "now",
    "thanks, regards",
    "urgent" + ZWSP + "action",
]

text_engine = InvariantEngine(
    real_text_reader,
    erg.recurrence_survival(lambda s: STREAM, reader=real_text_reader))
lone_engine = InvariantEngine(real_text_reader, erg.no_stream)


def show(engine, subject, name):
    v = engine.analyze(subject)
    print(f"\n=== {name} ===")
    print(f"  input : {subject.replace(ZWSP, '<ZWSP>')!r}")
    print(f"  risk={v.risk}  reality={v.reality}  [{v.finding.label}] {v.finding.reason}")
    print(f"  public: {engine.mask(v)}")
    return v


if __name__ == "__main__":
    print("INVARIANT ENGINE + REAL msl_mip runtime")
    print("=" * 64)

    a = show(lone_engine, "lunch at 1pm, see you there", "clean message")
    b = show(lone_engine, "def add(a, b): return a + b", "clean code")
    c = show(lone_engine, "paypal.com.security-check.ru/verify", "phishing URL")
    d = show(lone_engine, "path/../../etc/passwd", "path traversal")
    e = show(lone_engine, "hello" + ZWSP + "world", "ONE zero-width item, NO feed")
    f = show(text_engine, "hello" + ZWSP + "world", "SAME zero-width item, WITH feed")
    g = show(lone_engine, "a.b.c.d.e.f.g", "many dots (no-mimicry control)")

    assert a.risk == "OK" and b.risk == "OK"
    assert c.risk == "ALARM"        # real MSL: hold_pending_review, conclusive
    assert d.risk == "ALARM"        # real MSL caught path traversal structurally
    assert e.risk == "WATCH"        # queue-level, ambiguous, unconfirmed alone
    assert f.risk == "ALARM"        # same item, but it recurs -> real
    assert g.risk == "OK"           # no false positive on many dots

    print("\n" + "=" * 64)
    print("REAL MSL wired in:")
    print("  • phishing URL / path traversal -> ALARM  (structural, no blocklist)")
    print("  • clean text & code             -> OK     (no false positives)")
    print("  • zero-width: one -> WATCH, recurring -> ALARM  (ERG earns its keep)")
