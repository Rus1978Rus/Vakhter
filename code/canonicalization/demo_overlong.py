# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Close the HIGH bands: overlong-UTF-8 evasion on the REAL MSL.
Run:  MSL_MIP_HOME=/path/to/msl_mip  python demo_overlong.py
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "invariant_engine")))

from canonicalize import canonicalize
from invariant_engine import InvariantEngine, erg
from invariant_engine.msl_real import real_text_reader

msl = InvariantEngine(real_text_reader, erg.no_stream)


def show(name, raw):
    canon, info = canonicalize(raw)
    r0 = msl.analyze(raw).risk
    r1 = msl.analyze(canon).risk
    print(f"\n=== {name} ===")
    print(f"  raw       : {raw!r}")
    print(f"              MSL -> {r0}")
    print(f"  canonical : {canon!r}   [overlong={info['overlong_utf8']}, passes={info['decode_passes']}]")
    print(f"              MSL -> {r1}")
    print(f"  result    : {'CAUGHT after pre-pass ✔' if r0=='OK' and r1!='OK' else ('escalated' if r0!=r1 else 'no change')}")


if __name__ == "__main__":
    print("HIGH-BAND CLOSURE — overlong UTF-8 on the REAL MSL")
    print("=" * 62)

    # "/" and "." smuggled as overlong 2-byte:  %c0%af = "/", %c0%ae = "."
    show("overlong-2byte traversal",
         "..%c0%af..%c0%afetc%c0%afpasswd")
    # 3-byte overlong "/" : %e0%80%af
    show("overlong-3byte slash",
         "app%e0%80%af..%e0%80%afconfig")
    # control: LEGIT multibyte UTF-8 (Cyrillic 'привет') must NOT be flagged overlong
    show("legit UTF-8 (not overlong)",
         "%d0%bf%d1%80%d0%b8%d0%b2%d0%b5%d1%82")

    print("\n" + "=" * 62)
    print("overlong %c0%af / %e0%80%af decode to '/' and are flagged overlong=True")
    print("-> existing SOLIDUS/DOT cards then catch the traversal.")
    print("legit Cyrillic decodes normally, overlong=False -> no false alarm.")
    print("This closes the high bands %8X..%FX by ENFORCEMENT, not by 6 more cards.")
