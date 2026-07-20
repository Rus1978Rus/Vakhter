# -*- coding: utf-8 -*-
"""
TAG-block detector card (SIMULATOR of a draft) — the INVISIBLE-ASCII-SMUGGLE axis.

The Unicode TAG block (U+E0000..U+E007F) is a second, categorically distinct
invisible axis. Each tag char U+E0020..U+E007E is an invisible mirror of a
printable ASCII char (tag_'A' = U+E0041). A run of tag chars therefore carries a
COMPLETE, invisible ASCII message — the modern "invisible prompt injection"
vector against LLMs (smuggle "ignore your rules" as tag chars; a human sees
nothing, the model reads it).

The ONE legitimate use is the RGI emoji TAG SEQUENCE: a black-flag base
U+1F3F4 + region letters as tag chars + a U+E007F CANCEL TAG terminator
(🏴 + g b e n g + CANCEL = the England flag). That grammar is the whole
allowlist.

  ALARM (conclusive):
    tag characters that are NOT a well-formed emoji tag sequence:
      - tag chars with no U+1F3F4 flag base before them, OR
      - the deprecated LANGUAGE TAG U+E0001, OR
      - a flag base whose tag run is not terminated by U+E007F, OR
      - tag chars outside the region-letter set of a real sequence.
    The finding DECODES the hidden ASCII so the smuggled message is shown.
  OK (clean):
    a well-formed emoji tag sequence (flag base + region letters + CANCEL).
  (No WATCH: outside a valid flag sequence, tag chars have no legit text role,
   so an unexplained tag char is treated as smuggle, not merely watched.)
"""
from invariant_engine.core import Finding

TAG_BASE   = 0xE0000
LANG_TAG   = 0xE0001            # deprecated LANGUAGE TAG
TAG_SPACE  = 0xE0020           # tag ' '
TAG_TILDE  = 0xE007E           # tag '~'
CANCEL_TAG = 0xE007F
FLAG_BASE  = 0x1F3F4           # WAVING BLACK FLAG (emoji tag-seq base)
RGI_REGIONS = {"gbeng", "gbsct", "gbwls"}   # the RGI-recommended subdivision flags


def _is_tag(o):
    return TAG_BASE <= o <= CANCEL_TAG


def _decode_tag(o):
    """A printable-range tag char -> its ASCII twin; else None."""
    if TAG_SPACE <= o <= TAG_TILDE:
        return chr(o - TAG_BASE)
    return None


def _tag_runs(text):
    """Yield (start_index, [codepoints]) for each maximal run of tag chars."""
    runs, cur, start = [], [], None
    for i, ch in enumerate(text):
        o = ord(ch)
        if _is_tag(o):
            if not cur:
                start = i
            cur.append(o)
        elif cur:
            runs.append((start, cur)); cur = []
    if cur:
        runs.append((start, cur))
    return runs


def _valid_flag_sequence(text, start, run):
    """A run is a legit emoji tag sequence iff: preceded by U+1F3F4, its body is
    region letters (tag a-z / 0-9), and it ends with CANCEL TAG."""
    prev = ord(text[start - 1]) if start > 0 else None
    if prev != FLAG_BASE:
        return False
    if not run or run[-1] != CANCEL_TAG:
        return False
    body = run[:-1]
    letters = []
    for o in body:
        c = _decode_tag(o)
        if c is None or not (c.islower() or c.isdigit()):
            return False
        letters.append(c)
    return "".join(letters) in RGI_REGIONS


def tag_cards_reader(text):
    """TAG authority: ALARM invisible-ASCII smuggle (decoded) / OK emoji flag."""
    runs = _tag_runs(text)
    if not runs:
        return Finding("clean", 0.0, "tag-cards: no TAG-block characters")

    for start, run in runs:
        if _valid_flag_sequence(text, start, run):
            continue
        # decode whatever ASCII the run hides, for the human explanation
        hidden = "".join(_decode_tag(o) or "" for o in run)
        if LANG_TAG in run:
            why = "deprecated LANGUAGE TAG U+E0001"
        elif start == 0 or ord(text[start - 1]) != FLAG_BASE:
            why = "tag characters with no flag base"
        elif run[-1] != CANCEL_TAG:
            why = "flag base with tag run not terminated by CANCEL TAG"
        else:
            why = "tag characters outside a valid region sequence"
        shown = repr(hidden) if hidden else "(non-printable)"
        return Finding("suspect", 0.9,
            f"invisible-ASCII smuggle via TAG block — {why}; hidden text = {shown}",
            conclusive=True, signature="tag_smuggle")

    return Finding("clean", 0.0,
                   "tag-cards: all TAG runs are well-formed emoji flag sequences")
