# SPDX-License-Identifier: LicenseRef-Proprietary
"""
MSL role — structural readers (the 'nature' axis).

Each reader takes a subject and returns a Finding: WHAT it is and how
blatant, by STRUCTURE alone — no database, no training data.

NOTE: these are honest MINIMAL stand-ins. The real MSL/MIP runtime is far
richer; the point here is that the *general core* accepts any reader, and
the same core drives signal / text / code. Swap in msl_mip_runtime later.
"""

import unicodedata
from .core import Finding

# Zero-width & bidi control characters (Trojan-Source / hidden payloads)
INVISIBLE = {
    0x200B, 0x200C, 0x200D, 0x2060, 0xFEFF,          # zero-width family
    0x202A, 0x202B, 0x202C, 0x202D, 0x202E,          # bidi embeddings/overrides
    0x2066, 0x2067, 0x2068, 0x2069,                  # bidi isolates
}

# a tiny illustrative brand list (real MSL derives this structurally)
BRANDS = {"paypal", "google", "apple", "microsoft", "amazon",
          "sberbank", "binance", "telegram"}


# ---- signal grid: nature is just magnitude ('activation') --------------
def signal_reader(grid, floor: float = 0.05) -> Finding:
    pk = max((max(r) for r in grid), default=0.0)
    if pk <= floor:
        return Finding("clean", 0.0, "no activation")
    return Finding("activation", round(pk, 4),
                   f"activation present (peak {round(pk,3)})",
                   signature="signal")


# ---- text / prompt / code: structural reading --------------------------
def text_reader(s: str) -> Finding:
    # 1) invisible / bidi controls — conclusive (works for code too)
    hidden = sorted({c for c in s if ord(c) in INVISIBLE})
    if hidden:
        names = ", ".join(f"U+{ord(c):04X}" for c in hidden)
        return Finding("suspect", 0.95,
                       f"hidden/invisible control chars present ({names}) "
                       f"— possible Trojan-Source / concealed payload",
                       conclusive=True, signature="invisible")

    low = s.lower()

    # 2) URL brand mimicry — a brand label not in the registrable position
    host = low.split("//")[-1].split("/")[0]           # strip scheme + path
    labels = host.split(".")
    for i, lab in enumerate(labels):
        if lab in BRANDS and i < len(labels) - 2:       # brand not in reg. domain
            reg = ".".join(labels[-2:]) if len(labels) >= 2 else host
            return Finding("suspect", 0.7,
                           f"brand '{lab}' in non-final domain position; "
                           f"real registrable domain is '{reg}' (mimicry)",
                           signature=f"mimicry:{lab}")

    # 3) delimiter / bracket balance — structural integrity
    pairs = {")": "(", "]": "[", "}": "{"}
    stack, opens = [], set(pairs.values())
    for ch in s:
        if ch in opens:
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return Finding("suspect", 0.5,
                               "unbalanced/mismatched delimiters "
                               "(structural integrity)", signature="delim")
    if stack:
        return Finding("suspect", 0.5,
                       "unclosed delimiter (structural integrity)",
                       signature="delim")

    return Finding("clean", 0.0, "no structural anomaly")
