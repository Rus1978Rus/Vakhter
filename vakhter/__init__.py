# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Vakhter — an autonomous structural security guard that sits in front of an LLM.

It is a turnstile for STRUCTURE, not meaning: it catches homoglyphs, invisible
characters, encoding carriers, look-alike domains, and injection / RCE / data:-URI
structure — and is BLIND by design to plain natural-language prompt injection
(that is the semantic layer's job, which sits beside it). Fail-closed, DoS-guarded,
per-component isolated, zero third-party dependencies.

Public API — one call:

    from vakhter import analyze
    finding = analyze("some untrusted text")
    blocked = finding.label != "clean"     # act on this
    #   finding.label      "clean" | "suspect"
    #   finding.signature  stable machine key of the catch (e.g. "data_uri_exec")
    #   finding.reason     human explanation

MSL/MIP is an OPTIONAL relative, not a dependency: set the env var MSL_MIP_HOME to
an msl_mip repo to add it as an extra reinforcing reader. Without it the guard runs
fully autonomously on its own card detectors.
"""
import os
import sys

_ROOT = os.path.dirname(os.path.abspath(__file__))
_CODE = os.path.join(os.path.dirname(_ROOT), "code")
# product.py self-wires canonicalization + invariant_engine relative to itself;
# we only need its own directory (code/range) on the path to import it.
_RANGE = os.path.join(_CODE, "range")
if os.path.isdir(_RANGE) and _RANGE not in sys.path:
    sys.path.insert(0, _RANGE)

from product import analyze  # noqa: E402  (path wiring must precede the import)

__all__ = ["analyze"]
__version__ = "0.1.0"
