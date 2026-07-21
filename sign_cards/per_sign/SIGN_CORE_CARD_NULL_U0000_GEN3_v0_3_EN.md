PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_NULL_U0000_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_NULL_U0000_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_NULL_U0000_GEN3_v0_3_EN
CODEPOINT: U+0000
VISIBLE_FORM: ␀
UNICODE_NAME: <control> NULL (NUL)
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: null byte / NUL (non-printing)
CATEGORY_ROADMAP: INJ (null-byte truncation, filter bypass) · PHAGO: — (string-boundary forgery)
GLYPH_NOTE: VISIBLE_FORM uses ␀ (U+2400 SYMBOL FOR NULL) as a printable picture; the sign itself (U+0000) is a non-printing control character.

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
VISIBLE_FORM: ␀
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: NULL_FORM ≠ EFFECT
SIGN_CATEGORY:
  - C-string terminator (end of a null-terminated string)
  - padding / filler byte in binary formats
  - field/record separator in some binary protocols
  - "no value" sentinel in low-level data

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_TERMINATOR_ONLY — NUL is not merely a benign string end (it can truncate a validated value)
  2. NOT_TRUNCATION_SAFE — a NUL can cut a string so a checked suffix is dropped at the sink
  3. NOT_INVISIBLE_MEANS_HARMLESS — being non-printing does not make it inert
  4. NOT_EMPTY_EQUIVALENT — a NUL is a real byte, not the absence of data
  5. NOT_ENCODED_SAFE — "%00" / "\\0" / "\\u0000" may be decoded back to NUL later
  6. NOT_AUTHORITY — NUL does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; context makes it truncate
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_LANGUAGE_UNIFORM — one layer keeps bytes after NUL, another stops at it (desync)
  10. NOT_SANITIZED_PROOF — the presence of a NUL does not mean the input is sanitized
  11. NOT_OUTPUT_CONTEXT_PROOF — safety depends on how each layer treats NUL

BASE_FORMULAS:
  NULL_FORM ≠ EFFECT
  NULL_FORM ≠ TERMINATOR_ONLY_PROOF
  NULL_FORM ≠ TRUNCATION_SAFETY_PROOF
  NULL_FORM ≠ INVISIBLE_HARMLESS_PROOF
  NULL_FORM ≠ EMPTY_EQUIVALENCE_PROOF
  NULL_FORM ≠ ENCODED_SAFETY_PROOF
  NULL_FORM ≠ AUTHORITY
  NULL_FORM ≠ EXECUTION_TRIGGER
  NULL_FORM ≠ LANGUAGE_UNIFORMITY_PROOF
  NULL_FORM ≠ SANITIZED_PROOF
  NULL_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: NUL (ZONE_1) has parallel functions (C-string terminator, padding, sentinel) co-existing without cultural precession. Polysemy of a stable control code.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a teletype/idle control code with no gestural predecessor; the string-terminator/sentinel functions are layered on by the digital epoch in parallel.

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
    INPUT: "strings end with \\0 in C"
    CONTEXT: a NUL shown as an escape in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: NULL_FORM ≠ TERMINATOR_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "NUL is 0x00 in ASCII"
    CONTEXT: naming the control code in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: NULL_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the null terminator ends a C string"
    CONTEXT: describing the terminator role in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: NULL_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "printf('%c', 0) writes a NUL"
    CONTEXT: a code example shown as literal text
    EXPECTED: INFO
    RISK: NONE
    GUARD: NULL_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "the file is NUL-padded to 512 bytes"
    CONTEXT: describing legitimate binary padding
    EXPECTED: INFO
    RISK: NONE
    GUARD: NULL_FORM ≠ TRUNCATION_SAFETY_PROOF
  SAFE_CASE_006:
    INPUT: "find -print0 uses NUL separators"
    CONTEXT: describing a NUL-delimited tool output
    EXPECTED: INFO
    RISK: NONE
    GUARD: NULL_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: PATH_EXTENSION_TRUNCATION
    INPUT: "shell.php%00.jpg"
    CONTEXT: a NUL truncating a path so an extension check is bypassed
    RISK: CRITICAL
    ATTACK: "%00" cuts the string at ".php" after the ".jpg" extension passed the check
    GUARD: NULL_FORM ≠ TRUNCATION_SAFETY_PROOF
  RISK_CASE_002:
    NAME: WAF_FILTER_TRUNCATION
    INPUT: "safe\\0<script>alert(1)</script>"
    CONTEXT: a NUL making a scanner stop reading before the payload
    RISK: HIGH
    ATTACK: a C-based filter stops at NUL; a later layer still processes the tail (XSS/SQLi)
    GUARD: NULL_FORM ≠ LANGUAGE_UNIFORMITY_PROOF
  RISK_CASE_003:
    NAME: LOG_TRUNCATION_HIDE
    INPUT: "user login\\0 ADMIN ESCALATION"
    CONTEXT: a NUL truncating a log line to hide the tail
    RISK: HIGH
    ATTACK: a viewer stops at NUL, hiding the attacker's appended action
    GUARD: NULL_FORM ≠ EFFECT
  RISK_CASE_004:
    NAME: AUTH_STRING_TRUNCATION
    INPUT: "admin\\0ignored"
    CONTEXT: a NUL trimming a username to a privileged prefix
    RISK: HIGH
    ATTACK: one layer compares "admin\\0ignored", another authenticates "admin"
    GUARD: NULL_FORM ≠ EMPTY_EQUIVALENCE_PROOF
  RISK_CASE_005:
    NAME: ENCODED_NUL_BYPASS
    INPUT: "value%00.. (with a later decode)"
    CONTEXT: an encoded NUL decoded back before the sink
    RISK: HIGH
    ATTACK: "%00" decodes to NUL AFTER validation → truncation/bypass
    GUARD: NULL_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: NUL_INSERTION_EVASION
    INPUT: "jav\\0ascript:alert(1)"
    CONTEXT: a NUL inserted mid-token to break a keyword match
    RISK: MEDIUM
    ATTACK: a NUL splits "javascript" for a naive matcher but is stripped downstream
    GUARD: NULL_FORM ≠ SANITIZED_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ␀
    CODEPOINT: U+2400
    NAME: SYMBOL FOR NULL
    RISK: LOW
    RULE: SYMBOL_FOR_NULL ≠ NULL (a printable picture pasted where a real NUL is meant)
  CONFUSABLE_002:
    VISIBLE_FORM: ␦
    CODEPOINT: U+001A
    NAME: SUBSTITUTE
    RISK: MEDIUM
    RULE: SUBSTITUTE ≠ NULL (Ctrl-Z / DOS EOF; a different truncation sentinel a blanket filter conflates)
  CONFUSABLE_003:
    VISIBLE_FORM: ␄
    CODEPOINT: U+0004
    NAME: END OF TRANSMISSION
    RISK: LOW
    RULE: END_OF_TRANSMISSION ≠ NULL (a stream terminator, not a C-string terminator)
  CONFUSABLE_004:
    VISIBLE_FORM: ␡
    CODEPOINT: U+007F
    NAME: DELETE
    RISK: LOW
    RULE: DELETE ≠ NULL (a control often stripped together with NUL, but behaves differently)
  CONFUSABLE_005:
    VISIBLE_FORM: ␁
    CODEPOINT: U+0001
    NAME: START OF HEADING
    RISK: LOW
    RULE: START_OF_HEADING ≠ NULL (adjacent C0 control a "strip NUL only" filter leaves behind)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "NUL is always just a string terminator"
    RESPONSE: NULL_FORM ≠ TERMINATOR_ONLY_PROOF
    RULE: a NUL can truncate a validated value so a checked suffix is dropped
  CG2:
    TRIGGER: "an invisible control char cannot be dangerous"
    RESPONSE: NULL_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: invisibility is orthogonal to effect; NUL drives string boundaries
  CG3:
    TRIGGER: "a NUL is the same as empty / no data"
    RESPONSE: NULL_FORM ≠ EMPTY_EQUIVALENCE_PROOF
    RULE: a NUL is a real byte that can trim, split, or desync a value
  CG4:
    TRIGGER: "'%00' / '\\0' is safe forever"
    RESPONSE: NULL_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to NUL before the sink
  CG5:
    TRIGGER: "every layer treats NUL the same way"
    RESPONSE: NULL_FORM ≠ LANGUAGE_UNIFORMITY_PROOF
    RULE: C stops at NUL; managed strings keep the tail → truncation desync
  CG6:
    TRIGGER: "the presence of a NUL means the input is sanitized"
    RESPONSE: NULL_FORM ≠ SANITIZED_PROOF
    RULE: the presence of the sign says nothing about sanitization

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "value + NUL + ext"
      NAME: EXTENSION_TRUNCATION
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: a NUL cutting a filename after an allowed extension check
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "prefix + NUL + tail"
      NAME: FILTER_TRUNCATION
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: a NUL making a scanner stop before the payload tail
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "token + NUL + token"
      NAME: KEYWORD_SPLIT
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: a NUL splitting a keyword for a naive matcher
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with NUL are central to truncation/desync bypass.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: NUL truncates or splits a STRING boundary, but does not imitate the existence of a verified entity. Its risks are truncation/desync, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of NUL with SUBSTITUTE (U+001A) as an alternate truncation sentinel
  A2: encoding NUL as "%00" / "\\u0000" to slip past a raw-byte filter
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: path extension truncation shell.php%00.jpg
  B2: filter truncation safe\\0<script>...
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "value + NUL + ext" (SC1) — extension truncation
  C2: "token + NUL + token" (SC3) — keyword split
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: NUL presented as harmless padding inside a checked value
  D2: "%00" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: extension-check truncation into a file upload
  E2: N/A — vector: auth-string truncation into a login comparator
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: NUL is always just a string terminator
  EXPECTED: FAIL_TERMINATOR_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: an invisible control char cannot be dangerous
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: a NUL is the same as empty / no data
  EXPECTED: FAIL_EMPTY_EQUIVALENCE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%00" / "\0" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: every layer treats NUL the same way
  EXPECTED: FAIL_LANGUAGE_UNIFORMITY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: the presence of a NUL proves the input was sanitized
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to reject/normalize NUL uniformly across layers (C / managed / DB) without false positives on legitimate binary padding or NUL-delimited tool output?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (reject NUL in text fields early + length-based (not NUL-based) string handling + consistent decoding is an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "NUL is a real byte; layers that stop at it desync from layers that do not".
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
