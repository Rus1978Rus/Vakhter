# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Control-character detection (digit-card carrier class R7-3/R8-2/R9-1; measured gap).

Verifying the digit drafts against the runtime surfaced one real gap: C1 controls
(NEL U+0085, CSI U+009B) and DEL U+007F / ESC U+001B decoded cleanly but no
detector flagged them, though the drafts list them as injection carriers. These
tests pin that they are now caught AND that ordinary whitespace (tab/LF/CR) and
normal multilingual text stay clean (no false positives).
"""
from _support import flags, clean

from metachar_cards import metachar_cards_reader as M


def test_c1_del_esc_controls_flag():
    for ch in ("\x85", "\x9b", "\x7f", "\x1b", "\x01", "\x07", "\x1f"):
        flags(M, f"header{ch}value", "control_char")


def test_whitespace_and_nul_keep_their_own_meaning():
    # tab / LF / CR / VT / FF are whitespace, not this class -> not control_char
    clean(M, "line one\nline two\twith tab\r\nand more\x0b\x0c")
    # NUL keeps its own dedicated signature, not control_char
    f = M("x\x00y")
    assert f.signature == "null_byte", f"NUL must stay null_byte, got {f.signature}"


def test_normal_text_stays_clean():
    for s in ("a perfectly normal sentence.",
              "версия 1.0, привет мир 😀",
              "これは文です。次の文もある。",
              "multi\nline\ndocument\twith tabs"):
        clean(M, s)
