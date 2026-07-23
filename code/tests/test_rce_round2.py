# -*- coding: utf-8 -*-
"""
Contract for the round-2 injection/RCE coverage (metachar._SQL stacked queries;
harden._rce_misc: deserialization / SSRF schemes / prototype pollution), via the
assembled guard.

Each is shape-specific and FP-calibrated: SQL only on ";<verb> <object>", Java/PHP
only on serialized magic (rO0AB / O:n:"..":n:{), SSRF only on exotic schemes
(gopher/dict/…), proto only on "__proto__" as a key/accessor. Ordinary prose, a
legit SELECT, ftp/mailto and "the __proto__ property" stay clean.
"""
from _support import ok, flags, clean
from product import analyze


def test_sql_stacked_flags():
    for s in ("1; DROP TABLE users--", "x; DELETE FROM accounts",
              "a'; INSERT INTO logs VALUES(1)--", "1; TRUNCATE TABLE t"):
        flags(analyze, s, "sqli")


def test_deserialization_flags():
    flags(analyze, "rO0ABXNyABit", "deserialize")                     # Java serialized
    flags(analyze, 'a=O:8:"stdClass":1:{s:3:"cmd";}', "deserialize")  # PHP object


def test_ssrf_scheme_flags():
    for s in ("gopher://127.0.0.1:6379/_INFO", "dict://127.0.0.1:11211/",
              "tftp://evil/x"):
        flags(analyze, s, "ssrf_scheme")


def test_prototype_pollution_flags():
    flags(analyze, '{"__proto__": {"isAdmin": true}}', "proto_pollution")
    flags(analyze, "obj.__proto__.polluted=1", "proto_pollution")


def test_round2_no_false_positive():
    for s in ("read the file; select the best option", "run this; delete later",
              "the __proto__ property in JS", "constructor of the class",
              "download from ftp://files.example.com/", "email me at mailto:a@b.com",
              "object O:1 in geometry", "SELECT name FROM users WHERE id=1",
              'JSON {"a": 1, "b": 2}'):
        clean(analyze, s)
