# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""Packaging shim so setuptools ships this runtime dir inside the `vakhter`
wheel. The modules here are imported FLAT (the dir is placed on sys.path by
vakhter/__init__.py), not as a subpackage — this file only makes `pip install .`
copy the directory; it is intentionally empty of logic."""
