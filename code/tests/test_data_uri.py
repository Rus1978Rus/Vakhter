# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
data: URI carrier detection + autonomy lock (M3; AD-35).

Before this card the ONLY thing catching a data:text/html payload was the external
MSL engine; once MSL was made optional (autonomy), the "data: URI in an upload"
attack passed. These tests pin that the AUTONOMOUS guard (no MSL) catches it, and
that ordinary inline images are not false-flagged.
"""
import base64
import os

from _support import ok, flags, clean

from data_uri_cards import data_uri_cards_reader as D
import product


def _b64(mime, raw):
    return f"data:{mime};base64," + base64.b64encode(raw).decode()


def test_executable_mediatype_flags():
    flags(D, _b64("text/html", b"<script>alert(document.cookie)</script>"), "data_uri_exec")
    flags(D, "x data:text/html,<script>alert(1)</script>", "data_uri_exec")
    flags(D, _b64("image/svg+xml", b"<svg onload=alert(1)>"), "data_uri_exec")
    flags(D, _b64("application/javascript", b"fetch('/steal')"), "data_uri_exec")


def test_mislabeled_dropper_flags_via_magic_sniff():
    flags(D, _b64("image/png", b"MZ\x90\x00\x03 pretend PE"), "data_uri_dropper")
    flags(D, _b64("text/plain", b"\x7fELF pretend elf"), "data_uri_dropper")
    flags(D, _b64("image/gif", b"<script>x</script>"), "data_uri_dropper")


def test_benign_inline_resources_stay_clean():
    clean(D, "logo " + _b64("image/png", b"\x89PNG\r\n\x1a\n and pixels"))
    clean(D, _b64("image/jpeg", b"\xff\xd8\xff\xe0 jfif data"))
    clean(D, _b64("text/plain", b"just a harmless note"))
    clean(D, "completely normal text, no uri at all")


def test_guard_catches_data_uri_autonomously():
    # The point of AD-35: with NO external MSL the guard must still block this.
    old = os.environ.pop("MSL_MIP_HOME", None)
    try:
        payload = _b64("text/html", b"<script>alert(document.cookie)</script>")
        f = product.analyze(f"please read this uploaded file: {payload}")
        ok(f.label != "clean",
           f"autonomous guard must block a data:text/html script payload — got "
           f"{f.label}/{f.signature}")
    finally:
        if old is not None:
            os.environ["MSL_MIP_HOME"] = old
