# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Ed25519 — pure Python, standard library only (hashlib.sha512 + big-int math).

WHY this exists: Vakhter keeps ZERO third-party dependencies (see AD-35). Real
integrity (AD-36) needs an ASYMMETRIC signature so the verifying side holds only a
PUBLIC key (safe to ship) while the private signing key never leaves the author's
offline machine. Python's stdlib has no asymmetric primitive, and pulling in a C
crypto library would break autonomy — so this is a faithful port of the public-
domain Ed25519 reference (Bernstein et al.; RFC 8032), verified here against the
RFC 8032 test vectors.

SCOPE / LIMITS — read before trusting:
  - This is used for OFFLINE manifest signing + startup VERIFICATION, not for
    high-rate or adversarial-timing use. It is NOT constant-time and is not a
    general-purpose crypto library. A manifest check at boot does not need
    constant-time; do not repurpose this for secret-dependent hot paths.
  - Correctness is pinned by RFC 8032 vectors in the test suite. The security of
    the integrity scheme rests on the PRIVATE KEY staying offline and the anchor
    being on a read-only mount (AD-36) — the crypto only proves authorship.
"""
import hashlib

_b = 256
_q = 2 ** 255 - 19
_L = 2 ** 252 + 27742317777372353535851937790883648493


def _H(m):
    return hashlib.sha512(m).digest()


def _inv(x):
    return pow(x, _q - 2, _q)


_d = -121665 * _inv(121666) % _q
_I = pow(2, (_q - 1) // 4, _q)


def _xrecover(y):
    xx = (y * y - 1) * _inv(_d * y * y + 1)
    x = pow(xx, (_q + 3) // 8, _q)
    if (x * x - xx) % _q != 0:
        x = (x * _I) % _q
    if x % 2 != 0:
        x = _q - x
    return x


_By = 4 * _inv(5) % _q
_Bx = _xrecover(_By)
_B = [_Bx % _q, _By % _q]


def _edwards(P, Q):
    x1, y1 = P
    x2, y2 = Q
    x3 = (x1 * y2 + x2 * y1) * _inv(1 + _d * x1 * x2 * y1 * y2)
    y3 = (y1 * y2 + x1 * x2) * _inv(1 - _d * x1 * x2 * y1 * y2)
    return [x3 % _q, y3 % _q]


def _scalarmult(P, e):
    """Iterative double-and-add (no recursion-limit / faster than the reference)."""
    Q = [0, 1]                       # neutral element
    while e > 0:
        if e & 1:
            Q = _edwards(Q, P)
        P = _edwards(P, P)
        e >>= 1
    return Q


def _bit(h, i):
    return (h[i // 8] >> (i % 8)) & 1


def _encodeint(y):
    return bytes((y >> (8 * i)) & 0xFF for i in range(_b // 8))


def _encodepoint(P):
    x, y = P
    bits = [(y >> i) & 1 for i in range(_b - 1)] + [x & 1]
    return bytes(sum(bits[i * 8 + j] << j for j in range(8)) for i in range(_b // 8))


def _Hint(m):
    h = _H(m)
    return sum(2 ** i * _bit(h, i) for i in range(2 * _b))


def publickey(sk):
    """32-byte secret seed -> 32-byte public key."""
    h = _H(sk)
    a = 2 ** (_b - 2) + sum(2 ** i * _bit(h, i) for i in range(3, _b - 2))
    return _encodepoint(_scalarmult(_B, a))


def sign(m, sk, pk=None):
    """Sign message bytes m with 32-byte secret seed sk. OFFLINE author use only."""
    if pk is None:
        pk = publickey(sk)
    h = _H(sk)
    a = 2 ** (_b - 2) + sum(2 ** i * _bit(h, i) for i in range(3, _b - 2))
    r = _Hint(h[_b // 8:_b // 4] + m)
    R = _scalarmult(_B, r)
    S = (r + _Hint(_encodepoint(R) + pk + m) * a) % _L
    return _encodepoint(R) + _encodeint(S)


def _isoncurve(P):
    x, y = P
    return (-x * x + y * y - 1 - _d * x * x * y * y) % _q == 0


def _decodeint(s):
    return sum(2 ** i * _bit(s, i) for i in range(_b))


def _decodepoint(s):
    y = sum(2 ** i * _bit(s, i) for i in range(_b - 1))
    x = _xrecover(y)
    if x & 1 != _bit(s, _b - 1):
        x = _q - x
    P = [x, y]
    if not _isoncurve(P):
        raise ValueError("point not on curve")
    return P


def verify(signature, m, pk):
    """Return True iff `signature` (64 bytes) is a valid Ed25519 sig of m under pk
    (32 bytes). Never raises for a bad signature — returns False."""
    try:
        if len(signature) != _b // 4 or len(pk) != _b // 8:
            return False
        R = _decodepoint(signature[:_b // 8])
        A = _decodepoint(pk)
        S = _decodeint(signature[_b // 8:_b // 4])
        h = _Hint(_encodepoint(R) + pk + m)
        return _scalarmult(_B, S) == _edwards(R, _scalarmult(A, h))
    except Exception:
        return False
