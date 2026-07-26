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

_PKG = os.path.dirname(os.path.abspath(__file__))

# Two layouts resolve identically:
#   installed (pip install .)  — the runtime dirs were copied INSIDE the package:
#                                vakhter/range, vakhter/canonicalization,
#                                vakhter/invariant_engine  (parent = the package).
#   source / editable          — they live at ../code/range, ../code/canonicalization,
#                                ../code/invariant_engine/invariant_engine.
# `invariant_engine` is imported as a package, so its PARENT dir goes on the path;
# `range` and `canonicalization` hold flat modules, so THOSE dirs go on the path.
if os.path.isdir(os.path.join(_PKG, "range")):
    _RANGE = os.path.join(_PKG, "range")
    _CANON = os.path.join(_PKG, "canonicalization")
    _IE_PARENT = _PKG                                      # holds vakhter/invariant_engine
else:
    _CODE = os.path.join(os.path.dirname(_PKG), "code")
    _RANGE = os.path.join(_CODE, "range")
    _CANON = os.path.join(_CODE, "canonicalization")
    _IE_PARENT = os.path.join(_CODE, "invariant_engine")  # holds .../invariant_engine

for _p in (_IE_PARENT, _CANON, _RANGE):
    if os.path.isdir(_p) and _p not in sys.path:
        sys.path.insert(0, _p)

from product import analyze  # noqa: E402  (path wiring must precede the import)

__all__ = ["analyze"]
__version__ = "0.1.0"
