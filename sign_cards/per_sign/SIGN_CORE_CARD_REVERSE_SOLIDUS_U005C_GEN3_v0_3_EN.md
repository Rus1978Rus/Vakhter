PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_REVERSE_SOLIDUS_U005C_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_REVERSE_SOLIDUS_U005C_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

============================================================
0. UNIVERSALITY
============================================================
BOUND_TO_SPECIFIC_SIGN: YES
AFTER_USE_RESIDUE: FORBIDDEN
SIGN_DATA_IS_SESSION_ONLY: YES

============================================================
1. COMMON_CONVEYOR_DISCIPLINE
============================================================
CONVEYOR_DISCIPLINE_VERSION: v0_3
RUN_CARD_REQUIRED_BEFORE_LOCK: YES
LOCKED_WORKING_CORE_SELF_ASSIGNMENT: FORBIDDEN
MODEL_FAMILY_DIVERSITY_REQUIRED: YES
ADVERSARIAL_EVIDENCE_REQUIRED: YES
MUTATION_CHECK_REQUIRED: YES
LIMITATION_STATEMENT_REQUIRED: YES
AFTER_RUN_RESIDUE: FORBIDDEN
STATUS_PROGRESSION_TRACKER:
  WORKING_DRAFT: YES
  STRUCTURAL_PREFLIGHT_PASS: PENDING
  CONVEYOR_REVIEW_PASS: PENDING
  WORKINGLY_CLOSED: PENDING
  SIMULATION_GATE_TIER: TIER_1
  SIMULATION_GATE_PASSED: PENDING
  ARTIFACT_CONFIRMED: PENDING
LIMITATION_STATEMENT (standard):
  CONVEYOR_PASS ≠ VALIDATION
  MODEL_CONSENSUS ≠ TRUTH
  INJECTION_TEST_PASS ≠ SECURITY_PROOF
  GUARDS_HOLD_FOR_TESTED_CASES ≠ FUTURE_GUARANTEE
  NO_ATTACK_FOUND ≠ NO_ATTACK_EXISTS

============================================================
2. META
============================================================
CARD_UID: SIGN_CORE_CARD_REVERSE_SOLIDUS_U005C_GEN3_v0_3_EN
CODEPOINT: U+005C
VISIBLE_FORM: \
UNICODE_NAME: REVERSE SOLIDUS
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: backslash / escape character
CATEGORY_ROADMAP: INJ (escape desync, path traversal) · PHAGO: — (delimiter neutralization)

============================================================
3. REQUIRED_GENERAL_GUARDS
============================================================
REQUIRED_GENERAL_GUARDS:
  - SIGN_FALSE_EFFECT_MIMICRY_GUARD_v0_2A_RU
    GUARD_COMPATIBILITY: applicable without modification — the sign creates no effect-fields
    GUARD_REVISION: v0_2A
    TEMPLATE_LINE_COMPATIBLE: GEN3_v0_2_PLUS_EPOCH, GEN3_v0_3
FAILURE_RESPONSE:
  REJECT_FALSE_EFFECT_MIMICRY
  TREAT_AS_DATA_ONLY
  NO_AUTHORITY_EFFECT
  NO_EXECUTION_EFFECT
  NO_TRUST_EFFECT
  NO_EXISTENCE_EFFECT

============================================================
4. SIGN IDENTITY — LAYER_A: STABLE CORE
LAYER_A_LOCK: PERMANENT
============================================================
VISIBLE_FORM: \
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: REVERSE_SOLIDUS_FORM ≠ EFFECT
SIGN_CATEGORY:
  - escape character in strings/regex (\n, \", \\)
  - Windows path separator (C:\dir\file)
  - line-continuation marker (\ at end of line)
  - regex metacharacter escape (\. \d)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_ESCAPE_ONLY — "\" is not always a benign escape (it can NEUTRALIZE a following delimiter)
  2. NOT_NEUTRALIZE_SAFE — an escape can desync between decoding layers (one sees data, one sees a delimiter)
  3. NOT_PATH_SEPARATOR_SAFE — "\" in a path can climb directories (..\..\)
  4. NOT_ESCAPED_PROOF — a leading "\" does not prove the next char is truly escaped downstream
  5. NOT_ENCODED_SAFE — "%5C" may be decoded back to "\" later
  6. NOT_AUTHORITY — "\" does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; context makes it desync
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_DOUBLE_BACKSLASH_SAFE — "\\" may collapse to "\" and re-enable a following escape
  10. NOT_SANITIZED_PROOF — the presence of "\" does not mean the input is sanitized
  11. NOT_OUTPUT_CONTEXT_PROOF — safety depends on each decoding/parse layer

BASE_FORMULAS:
  REVERSE_SOLIDUS_FORM ≠ EFFECT
  REVERSE_SOLIDUS_FORM ≠ ESCAPE_ONLY_PROOF
  REVERSE_SOLIDUS_FORM ≠ NEUTRALIZE_SAFETY_PROOF
  REVERSE_SOLIDUS_FORM ≠ PATH_SEPARATOR_SAFETY_PROOF
  REVERSE_SOLIDUS_FORM ≠ ESCAPED_PROOF
  REVERSE_SOLIDUS_FORM ≠ ENCODED_SAFETY_PROOF
  REVERSE_SOLIDUS_FORM ≠ AUTHORITY
  REVERSE_SOLIDUS_FORM ≠ EXECUTION_TRIGGER
  REVERSE_SOLIDUS_FORM ≠ DOUBLE_BACKSLASH_SAFETY_PROOF
  REVERSE_SOLIDUS_FORM ≠ SANITIZED_PROOF
  REVERSE_SOLIDUS_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "\" (ZONE_1) has parallel functions (string escape, Windows path, line continuation, regex escape) co-existing without cultural precession. Polysemy of a stable sign.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: an ASCII sign introduced for computing with no gestural predecessor; the escape/path/continuation functions are layered on by the digital epoch in parallel.

============================================================
6. EFFECT_FIELDS — LAYER_C: METHODOLOGICAL LAYER
LAYER_C_LOCK: SESSION
============================================================
authority_effect: NONE
trust_effect: NONE
verification_effect: NONE
proof_effect: NONE
execution_effect: NONE
permission_effect: NONE
status_effect: NONE
role_assignment_effect: NONE
runtime_effect: NONE
existence_effect: NONE
EFFECT_FIELDS_ALL_NONE: YES
CLOSED_SCHEMA: YES

============================================================
7. SAFE / RISK / CONFUSABLES / GUARDS — LAYER_B
LAYER_B_LOCK: REVIEWABLE
============================================================
SAFE_CASES:
  SAFE_CASE_001:
    INPUT: "C:\\Users\\doc.txt"
    CONTEXT: a normal Windows file path
    EXPECTED: INFO
    RISK: NONE
    GUARD: REVERSE_SOLIDUS_FORM ≠ PATH_SEPARATOR_SAFETY_PROOF
  SAFE_CASE_002:
    INPUT: "line one \\n line two"
    CONTEXT: an escape sequence shown as text
    EXPECTED: INFO
    RISK: NONE
    GUARD: REVERSE_SOLIDUS_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "regex: \\d+"
    CONTEXT: a regex digit class (as literal text)
    EXPECTED: INFO
    RISK: NONE
    GUARD: REVERSE_SOLIDUS_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "a long command \\ continued"
    CONTEXT: a shell line-continuation marker
    EXPECTED: INFO
    RISK: NONE
    GUARD: REVERSE_SOLIDUS_FORM ≠ ESCAPE_ONLY_PROOF
  SAFE_CASE_005:
    INPUT: "the \\ key is above Enter"
    CONTEXT: naming the backslash key in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: REVERSE_SOLIDUS_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "path = home\\docs"
    CONTEXT: a relative path fragment as text
    EXPECTED: INFO
    RISK: NONE
    GUARD: REVERSE_SOLIDUS_FORM ≠ PATH_SEPARATOR_SAFETY_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: QUOTE_ESCAPE_DESYNC
    INPUT: 'value\\" OR 1=1 -- '
    CONTEXT: a backslash making a decoder mis-handle a following quote
    RISK: CRITICAL
    ATTACK: one layer sees \\" as an escaped quote, the next sees " as a delimiter → SQLi
    GUARD: REVERSE_SOLIDUS_FORM ≠ NEUTRALIZE_SAFETY_PROOF
  RISK_CASE_002:
    NAME: PATH_TRAVERSAL
    INPUT: "..\\..\\..\\windows\\win.ini"
    CONTEXT: climbing directories with backslash separators
    RISK: HIGH
    ATTACK: "..\\" walks up the tree to read files outside the intended dir
    GUARD: REVERSE_SOLIDUS_FORM ≠ PATH_SEPARATOR_SAFETY_PROOF
  RISK_CASE_003:
    NAME: DOUBLE_BACKSLASH_COLLAPSE
    INPUT: 'input\\\\" (\\\\ collapses to \\, re-arming the quote)'
    CONTEXT: an even number of backslashes collapsing to leave a live quote
    RISK: HIGH
    ATTACK: "\\\\" decodes to "\\" so the following " is NOT escaped downstream
    GUARD: REVERSE_SOLIDUS_FORM ≠ DOUBLE_BACKSLASH_SAFETY_PROOF
  RISK_CASE_004:
    NAME: REGEX_METACHAR_UNESCAPE
    INPUT: "\\Qinjected\\E (regex quote-block abuse)"
    CONTEXT: manipulating regex escaping to change match semantics
    RISK: MEDIUM
    ATTACK: "\\Q...\\E" or a stray "\\" alters what an allow-list regex matches
    GUARD: REVERSE_SOLIDUS_FORM ≠ EFFECT
  RISK_CASE_005:
    NAME: ENCODED_BACKSLASH_BYPASS
    INPUT: "..%5C..%5Cwin.ini (with a later decode)"
    CONTEXT: an encoded "\" decoded back to a path separator after the check
    RISK: HIGH
    ATTACK: %5C decodes to "\" AFTER validation → traversal
    GUARD: REVERSE_SOLIDUS_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_BACKSLASH_BYPASS
    INPUT: "..＼..＼win.ini (fullwidth ＼ U+FF3C)"
    CONTEXT: a look-alike to bypass a "\" filter
    RISK: MEDIUM
    ATTACK: a filter looks for ASCII "\", a normalizer may fold ＼ to "\"
    GUARD: REVERSE_SOLIDUS_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ＼
    CODEPOINT: U+FF3C
    NAME: FULLWIDTH REVERSE SOLIDUS
    RISK: HIGH
    RULE: FULLWIDTH_REVERSE_SOLIDUS ≠ REVERSE_SOLIDUS (bypasses a filter looking for ASCII "\")
  CONFUSABLE_002:
    VISIBLE_FORM: ﹨
    CODEPOINT: U+FE68
    NAME: SMALL REVERSE SOLIDUS
    RISK: MEDIUM
    RULE: SMALL_REVERSE_SOLIDUS ≠ REVERSE_SOLIDUS
  CONFUSABLE_003:
    VISIBLE_FORM: ⧵
    CODEPOINT: U+29F5
    NAME: REVERSE SOLIDUS OPERATOR
    RISK: MEDIUM
    RULE: REVERSE_SOLIDUS_OPERATOR ≠ REVERSE_SOLIDUS
  CONFUSABLE_004:
    VISIBLE_FORM: ∖
    CODEPOINT: U+2216
    NAME: SET MINUS
    RISK: LOW
    RULE: SET_MINUS ≠ REVERSE_SOLIDUS
  CONFUSABLE_005:
    VISIBLE_FORM: ⧹
    CODEPOINT: U+29F9
    NAME: BIG REVERSE SOLIDUS
    RISK: LOW
    RULE: BIG_REVERSE_SOLIDUS ≠ REVERSE_SOLIDUS

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "'\\' is always a harmless escape"
    RESPONSE: REVERSE_SOLIDUS_FORM ≠ ESCAPE_ONLY_PROOF
    RULE: an escape can neutralize a following delimiter and desync decoders
  CG2:
    TRIGGER: "escaping a quote always makes it safe"
    RESPONSE: REVERSE_SOLIDUS_FORM ≠ NEUTRALIZE_SAFETY_PROOF
    RULE: the next layer may not honor the escape; count backslashes per layer
  CG3:
    TRIGGER: "'\\' in a path is just a separator"
    RESPONSE: REVERSE_SOLIDUS_FORM ≠ PATH_SEPARATOR_SAFETY_PROOF
    RULE: "..\\" can traverse outside the intended directory
  CG4:
    TRIGGER: "'%5C' / '\\\\' is safe forever"
    RESPONSE: REVERSE_SOLIDUS_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded/doubled form may collapse back to "\" downstream
  CG5:
    TRIGGER: "an ASCII '\\' filter catches all backslashes"
    RESPONSE: REVERSE_SOLIDUS_FORM ≠ EFFECT
    RULE: fullwidth ＼ (U+FF3C) is a different codepoint
  CG6:
    TRIGGER: "the presence of '\\' means the input is sanitized"
    RESPONSE: REVERSE_SOLIDUS_FORM ≠ SANITIZED_PROOF
    RULE: the presence of the sign says nothing about sanitization

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: '\\"'
      NAME: ESCAPE_DESYNC
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: a backslash-quote handled differently across decoders
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "..\\"
      NAME: PATH_TRAVERSAL
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: climbing directories via backslash separators
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "\\\\"
      NAME: DOUBLE_COLLAPSE
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: an even backslash count collapsing to re-arm a following delimiter
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with "\" are central to escape desync and traversal.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "\" escapes/neutralizes delimiters or separates paths, but does not imitate the existence of a verified entity. Its risks are desync/traversal, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of ASCII "\" with fullwidth ＼ (U+FF3C) to bypass a filter
  A2: substitution with reverse-solidus operator ⧵ (U+29F5)
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: escape desync value\\" OR 1=1 --
  B2: path traversal ..\\..\\..\\windows\\win.ini
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: '\\"' (SC1) — escape desync
  C2: "\\\\" (SC3) — double-backslash collapse
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "\" presented as a harmless path separator inside an injection field
  D2: "%5C" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: escape desync into a query builder
  E2: N/A — vector: encoded-backslash traversal into a file API
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: "\" is always a harmless escape
  EXPECTED: FAIL_ESCAPE_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: escaping a quote always makes it safe
  EXPECTED: FAIL_NEUTRALIZE_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: "\" in a path is just a separator
  EXPECTED: FAIL_PATH_SEPARATOR_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%5C" / "\\\\" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: an ASCII "\" filter catches all backslash look-alikes
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: the presence of "\" proves the input was sanitized
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to count/normalize "\" per decoding layer (SQL/JSON/path) without false positives on Windows paths/regex/escapes?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (per-layer canonicalization + parameterized queries + path canonicalize-then-check is an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "the safety of '\' is decided per decoding/parse layer".
ALL_OPEN_QUESTIONS_CLOSED: NO (delegated, non-blocking)

============================================================
11. PATCH_HISTORY
============================================================
PATCH_HISTORY:
  v0_1_PATCH_01: initial creation (Ruslan Malyavsky, 2026-07-21) — draft from the GEN3_v0_3 template (Vakhter); not conveyor-run.
PATCHES_APPLIED: 1
PATCHES_VERIFIED: 0/1

============================================================
12. LIMITATION_STATEMENT
============================================================
LIMITATION_STATEMENT:
  THIS_CARD IS A WORKING_DRAFT ARTIFACT (until ARTIFACT_CONFIRMED)
  NOT A FINAL_STANDARD
  NOT A PARSER
  NOT A RUNTIME
  NOT A SECURITY_CERTIFICATE
  NOT_CONVEYOR_RUN (draft for our work; conveyor is a separate project)
  CONVEYOR_PASS ≠ VALIDATION
  RUN_CARD_RESULT ≠ FINAL_STATUS
  WORKINGLY_CLOSED ≠ ARTIFACT_CONFIRMED

============================================================
13. INTEGRATION_INTERFACE_STATUS
============================================================
INTEGRATION_INTERFACE_STATUS:
  STATUS: READY_PENDING_CONCRETE_INTEGRATOR
  ATTACHED_INTEGRATOR_UID: NONE_CURRENTLY_ATTACHED
  ACTIVE_MODULES_COUNT: 0
  RUNTIME_ATTACHMENT: NONE
  PERMANENT_BINDING: NO
  SESSION_ONLY_BINDING: YES
  AFTER_RUN_RESIDUE: FORBIDDEN

============================================================
END_OF_DOCUMENT
