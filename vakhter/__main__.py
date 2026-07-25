# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Vakhter CLI. Reads text from arguments or stdin, prints a one-line verdict, and
exits non-zero when the text is blocked (so it composes in shell pipelines).

    python -m vakhter "paypal.com login"          # text as arguments
    echo "suspicious text" | python -m vakhter    # text on stdin
    vakhter "..."                                 # after `pip install -e .`

Output:  <BLOCK|CLEAN>\t<label>\t<signature>   then the human reason on line 2.
Exit code: 1 when blocked, 0 when clean (2 on usage error).
"""
import sys

from vakhter import analyze


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if argv:
        text = " ".join(argv)
    else:
        if sys.stdin.isatty():
            sys.stderr.write("usage: vakhter \"text\"   OR   echo text | vakhter\n")
            return 2
        text = sys.stdin.read()

    f = analyze(text)
    blocked = f.label != "clean"
    print(f"{'BLOCK' if blocked else 'CLEAN'}\t{f.label}\t{f.signature or '-'}")
    print(f.reason)
    return 1 if blocked else 0


if __name__ == "__main__":
    sys.exit(main())
