# -*- coding: utf-8 -*-
"""
Contract for the LDAP/NoSQL injection and short-form/zone SSRF checks closed after
the adversarial sweep (metachar_cards :: _LDAP/_NOSQL; harden_cards :: _ip_advanced),
reached through product.analyze.

FP-calibrated to the specific attack shapes: LDAP only on wildcard-paren / boolean
chaining / attr=* ; NoSQL only on a quoted key "$op" or bracketed [$op]; short-form
IP only inside a URL host. Ordinary code, JSON, prose and version numbers stay clean.
"""
from _support import ok, flags, clean
from product import analyze


def test_ldap_injection_flags():
    for s in ("*)(uid=*))(|(uid=*", "user=*)(objectClass=*", "x)(|(cn=*"):
        flags(analyze, s, "ldapi")


def test_nosql_injection_flags():
    for s in ('{"$gt": ""}', "username[$ne]=1", '{"$where": "1==1"}', "login[$regex]=^a"):
        flags(analyze, s, "nosqli")


def test_short_form_and_zone_ip_flags():
    for s in ("http://127.1/admin", "http://10.0.1/x",
              "http://[fe80::1%25eth0]/", "http://[::1]/"):
        flags(analyze, s)


def test_injection_no_false_positive():
    # ordinary code / JSON / prose must not trip LDAP or NoSQL
    for s in ("function()(x) chained call", "(a)(b) grouping", "math (x)(y) product",
              'JSON {"name": "value"}', '{"price": 10, "qty": 2}',
              "the $where clause in SQL docs", "array[$index] lookup",
              "price is $50 or more"):
        clean(analyze, s)


def test_version_numbers_not_ip():
    # short-form IP is URL-gated, so dotted version/aspect numbers stay clean
    for s in ("version 5.1 released", "see section 3.14", "ratio 16.9 aspect", "build 8.1"):
        clean(analyze, s)
