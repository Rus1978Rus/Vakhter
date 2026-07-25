# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""One engine, four substrates. Run: python demo.py  (also self-verifies)."""

from invariant_engine import InvariantEngine, msl, erg

# ---- signals: same grid demo as before, now through the general core ----
def blank(t=8, n=8): return [[0.0]*n for _ in range(t)]
def spike(a=0.9):
    g = blank(); g[4][4] = a; return g
def persistent(a):
    g = blank()
    for i in range(1, 7):
        for j in range(1, 7): g[i][j] = a
    return g

signal_engine = InvariantEngine(msl.signal_reader, erg.scale_survival(levels=3))

# ---- text / prompt / code: one engine, a shared "inbox" stream ----------
STREAM = [
    "paypal.com.security-check.ru/verify",   # mimicry, repeated across the feed
    "paypal.com.login-alert.ru/confirm",
    "paypal.com.account-verify.ru/x",
    "hello team, lunch at 1pm?",
    "your invoice is attached, regards",
    "paypal.com.secure-id.ru/pay",
    "meeting moved to Thursday",
    "paypal.com.verify-now.ru/go",
]
text_engine = InvariantEngine(msl.text_reader, erg.recurrence_survival(lambda s: STREAM))
lone_engine = InvariantEngine(msl.text_reader, erg.no_stream)   # single item, no feed

# code with an invisible zero-width char (U+200B) hidden inside an identifier
CODE = "if user.is" + chr(0x200B) + "admin:  # looks fine, isn't\n    grant_access()"


def show(engine, subject, name):
    v = engine.analyze(subject)
    print(f"\n=== {name} ===")
    print(f"  risk={v.risk}  reality={v.reality}  [{v.finding.label}] {v.finding.reason}")
    print(f"  public: {engine.mask(v)}")
    return v


if __name__ == "__main__":
    print("INVARIANT ENGINE — one core across signal / text / prompt / code")
    print("=" * 66)

    a = show(signal_engine, spike(0.9),        "SIGNAL A: strong isolated spike")
    b = show(signal_engine, persistent(0.4),   "SIGNAL B: weak persistent")
    c = show(signal_engine, persistent(0.9),   "SIGNAL C: strong persistent")

    d = show(lone_engine, STREAM[0],           "TEXT D: one mimic URL, NO feed")
    e = show(text_engine, STREAM[0],           "TEXT E: same mimic URL, WITH feed")
    f = show(text_engine, "lunch at 1pm?",     "TEXT F: harmless message")
    g = show(lone_engine, CODE,                "CODE G: hidden invisible char in code")

    assert a.risk == "NOISE"                    # strong but transient
    assert b.risk == "WATCH" and c.risk == "ALARM"
    assert d.risk == "WATCH"                     # suspicious but unconfirmed (no many)
    assert e.risk == "ALARM"                     # same URL, but it recurs -> real
    assert f.risk == "OK"
    assert g.risk == "ALARM"                     # invisible char = conclusive, no feed needed

    print("\n" + "=" * 66)
    print("PROVEN on ONE core:")
    print("  • signal  : strong spike -> NOISE, weak-persistent -> WATCH   (scale axis)")
    print("  • text    : one mimic -> WATCH, but recurring mimic -> ALARM  (time axis)")
    print("  • code    : hidden invisible char -> ALARM (conclusive)")
    print("  intensity != objectivity  AND  substrate-independent  ✔")
