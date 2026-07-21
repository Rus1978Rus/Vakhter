PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_PERCENT_U0025_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_PERCENT_U0025_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_PERCENT_U0025_GEN3_v0_3_EN
CODEPOINT: U+0025
VISIBLE_FORM: %
UNICODE_NAME: PERCENT SIGN
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: percent
CATEGORY_ROADMAP: PH/INJ (URL-encoding obfuscation) · PHAGO: — (structure masking, not entity mimicry)

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
VISIBLE_FORM: %
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_ENCODING_MARKER
BASE_MODE_FORMULA: PERCENT_FORM ≠ EFFECT
SIGN_CATEGORY:
  - punctuation / mathematical sign (percentages, "50%")
  - modulo operator in programming languages (a % b)
  - percent-encoding marker in URLs (%XX)
  - format specifier (printf "%s", "%d")

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_DECODED_SAFE — the presence of %XX does not mean the decoded value is safe
  2. NOT_SINGLE_DECODE_GUARANTEE — input may be double-encoded (%252F → %2F → /)
  3. NOT_ALWAYS_ENCODING — "%" is not always percent-encoding (percentages, modulo, format)
  4. NOT_PERCENTAGE_PROOF — "%" does not prove a percentage value is correct
  5. NOT_MODULO_SAFE — "%" as modulo does not guarantee the expression is safe
  6. NOT_FORMAT_STRING_SAFE — "%s"/"%n" is a format-string vector, not safety
  7. NOT_AUTHORITY — "%" does not confirm officialness
  8. NOT_EXECUTION_TRIGGER — by itself it launches nothing
  9. NOT_TRUST_SIGNAL — it does not increase trust
  10. NOT_STRING_TERMINATION_SAFE — %00 can truncate a string (null-byte)
  11. NOT_TRAVERSAL_SAFE — %2e%2e%2f may carry path traversal

BASE_FORMULAS:
  PERCENT_FORM ≠ EFFECT
  PERCENT_FORM ≠ DECODED_VALUE_SAFETY_PROOF
  PERCENT_FORM ≠ SINGLE_DECODE_GUARANTEE
  PERCENT_FORM ≠ ENCODING_ONLY_PROOF
  PERCENT_FORM ≠ PERCENTAGE_VALIDITY_PROOF
  PERCENT_FORM ≠ MODULO_SAFETY_PROOF
  PERCENT_FORM ≠ FORMAT_STRING_SAFETY_PROOF
  PERCENT_FORM ≠ AUTHORITY
  PERCENT_FORM ≠ TRUST_SIGNAL
  PERCENT_FORM ≠ STRING_TERMINATION_SAFETY
  PERCENT_FORM ≠ PATH_TRAVERSAL_SAFETY

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "%" (ZONE_1) has parallel functions (percentages, modulo, percent-encoding, format specifier) co-existing without cultural precession. Polysemy of a stable sign, not epoch change.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a written/typographic sign with no gestural predecessor; percent-encoding is a digital function layered on later (RFC 3986) but parallel to the mathematical meaning.

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
    INPUT: "50% off"
    CONTEXT: percentage value in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: PERCENT_FORM ≠ PERCENTAGE_VALIDITY_PROOF
  SAFE_CASE_002:
    INPUT: "loading 100%"
    CONTEXT: progress indicator
    EXPECTED: INFO
    RISK: NONE
    GUARD: PERCENT_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "remainder = a % b"
    CONTEXT: modulo in an expression
    EXPECTED: INFO
    RISK: NONE
    GUARD: PERCENT_FORM ≠ MODULO_SAFETY_PROOF
  SAFE_CASE_004:
    INPUT: "https://site.com/path%20name"
    CONTEXT: legit percent-encoding of a space (%20) in a URL
    EXPECTED: INFO
    RISK: NONE
    GUARD: PERCENT_FORM ≠ ENCODING_ONLY_PROOF
  SAFE_CASE_005:
    INPUT: 'printf("%s", name)'
    CONTEXT: a correct format specifier with an argument
    EXPECTED: INFO
    RISK: NONE
    GUARD: PERCENT_FORM ≠ FORMAT_STRING_SAFETY_PROOF
  SAFE_CASE_006:
    INPUT: "growth of 3% per year"
    CONTEXT: percentage in statistics
    EXPECTED: INFO
    RISK: NONE
    GUARD: PERCENT_FORM ≠ PERCENTAGE_VALIDITY_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: ENCODED_SLASH_BYPASS
    INPUT: "/api/%2F..%2Fadmin"
    CONTEXT: a percent-encoded slash bypasses a path filter
    RISK: HIGH
    ATTACK: %2F decodes to "/" AFTER the check, bypassing a literal-slash filter
    GUARD: PERCENT_FORM ≠ DECODED_VALUE_SAFETY_PROOF
  RISK_CASE_002:
    NAME: NULL_BYTE_TRUNCATION
    INPUT: "file.php%00.jpg"
    CONTEXT: %00 truncates the string in a vulnerable parser
    RISK: CRITICAL
    ATTACK: the null-byte (%00) cuts off ".jpg", leaving ".php" — bypasses the extension check
    GUARD: PERCENT_FORM ≠ STRING_TERMINATION_SAFETY
  RISK_CASE_003:
    NAME: DOUBLE_ENCODING
    INPUT: "%252F" (double-encoded "/")
    CONTEXT: bypassing single-pass decoding
    RISK: HIGH
    ATTACK: %25 → %, then %2F → / on the second pass; single decode does not see the slash
    GUARD: PERCENT_FORM ≠ SINGLE_DECODE_GUARANTEE
  RISK_CASE_004:
    NAME: ENCODED_TRAVERSAL
    INPUT: "%2e%2e%2fetc%2fpasswd"
    CONTEXT: percent-encoded path traversal (../../)
    RISK: HIGH
    ATTACK: encoding dots/slashes moves the traversal out from under a signature filter
    GUARD: PERCENT_FORM ≠ PATH_TRAVERSAL_SAFETY
  RISK_CASE_005:
    NAME: CRLF_INJECTION_ENCODED
    INPUT: "name=x%0d%0aSet-Cookie:evil"
    CONTEXT: percent-encoded CR/LF to split a header/log
    RISK: HIGH
    ATTACK: %0d%0a decode to CRLF, injecting a header/log line
    GUARD: PERCENT_FORM ≠ DECODED_VALUE_SAFETY_PROOF
  RISK_CASE_006:
    NAME: FORMAT_STRING_ATTACK
    INPUT: 'user input: "%n%n%s"'
    CONTEXT: user input used as a format string
    RISK: HIGH
    ATTACK: %n/%s without arguments — memory read/write (format-string vulnerability)
    GUARD: PERCENT_FORM ≠ FORMAT_STRING_SAFETY_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ％
    CODEPOINT: U+FF05
    NAME: FULLWIDTH PERCENT SIGN
    RISK: MEDIUM
    RULE: FULLWIDTH_PERCENT ≠ PERCENT (bypasses a filter looking for ASCII %)
  CONFUSABLE_002:
    VISIBLE_FORM: ٪
    CODEPOINT: U+066A
    NAME: ARABIC PERCENT SIGN
    RISK: MEDIUM
    RULE: ARABIC_PERCENT ≠ PERCENT
  CONFUSABLE_003:
    VISIBLE_FORM: ﹪
    CODEPOINT: U+FE6A
    NAME: SMALL PERCENT SIGN
    RISK: LOW
    RULE: SMALL_PERCENT ≠ PERCENT
  CONFUSABLE_004:
    VISIBLE_FORM: ‰
    CODEPOINT: U+2030
    NAME: PER MILLE SIGN
    RISK: LOW
    RULE: PER_MILLE ≠ PERCENT (per mille, a different magnitude)
  CONFUSABLE_005:
    VISIBLE_FORM: ⁒
    CODEPOINT: U+2052
    NAME: COMMERCIAL MINUS SIGN
    RISK: LOW
    RULE: COMMERCIAL_MINUS ≠ PERCENT (visually similar in some fonts)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "if a string is percent-decoded once, it is safe"
    RESPONSE: PERCENT_FORM ≠ SINGLE_DECODE_GUARANTEE
    RULE: double/multiple encoding is possible; decode to a stable point, then check
  CG2:
    TRIGGER: "%2F in a path is just text, not a slash"
    RESPONSE: PERCENT_FORM ≠ DECODED_VALUE_SAFETY_PROOF
    RULE: after decoding %2F becomes "/" — check the DECODED value
  CG3:
    TRIGGER: "%00 in a filename is harmless"
    RESPONSE: PERCENT_FORM ≠ STRING_TERMINATION_SAFETY
    RULE: a null-byte can truncate a string in a vulnerable parser (file.php%00.jpg)
  CG4:
    TRIGGER: "user input can be passed as a format string"
    RESPONSE: PERCENT_FORM ≠ FORMAT_STRING_SAFETY_PROOF
    RULE: %n/%s in input is a format-string vulnerability; input must not be the format string
  CG5:
    TRIGGER: "an ASCII % filter catches all percents"
    RESPONSE: PERCENT_FORM ≠ EFFECT
    RULE: fullwidth ％ / Arabic ٪ are different codepoints (see CONFUSABLES)
  CG6:
    TRIGGER: "the presence of % means percent-encoding"
    RESPONSE: PERCENT_FORM ≠ ENCODING_ONLY_PROOF
    RULE: % is also percentages, modulo and format; interpretation depends on context

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "%XX" (% + two hex digits)
      NAME: PERCENT_ENCODED_OCTET
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: a percent-encoded byte; danger depends on the decoded value (%2F, %00, %0a)
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "%25XX"
      NAME: DOUBLE_ENCODED_OCTET
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: double encoding to bypass single-pass decode
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "%00"
      NAME: NULL_BYTE
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: string truncation, extension/path check bypass
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — the sequences are real and central to this sign.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "%" masks STRUCTURE (encoding, filter bypass) but does not imitate the existence of a verified entity (brand/account). The sign's risks are obfuscation, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of ASCII % with fullwidth ％ (U+FF05) to bypass an encoding filter
  A2: mixing % with Arabic ٪ (U+066A) in a multibyte context
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: %2F/%2e%2e to bypass a path filter after decoding
  B2: %0d%0a for CRLF injection into a header/log
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: double encoding %252F (SC2) against single-pass decode
  C2: %00 (SC3) for string truncation and extension bypass
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: user input as a format string "%n%s" (format-string)
  D2: "100%" as a pseudo-guarantee ("100% safe") — trust inflation by number
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector replaced with obfuscation: %-encoding a blocklisted keyword
  E2: N/A — vector: %-encoding a control character to bypass a sanitizer
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: a single percent-decode is enough for safety
  EXPECTED: FAIL_SINGLE_DECODE_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: %2F in a path is just text, not a slash
  EXPECTED: FAIL_DECODED_VALUE_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: %00 in a filename is harmless
  EXPECTED: FAIL_NULL_BYTE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: user input can be passed as a format string
  EXPECTED: FAIL_FORMAT_STRING_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: an ASCII % filter catches all variants of the sign
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: "100% safe" is confirmed by the percent sign
  EXPECTED: FAIL_TRUST_INFLATION_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: to what depth should input be decoded before checking (decode-bomb risk)?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (an iterative decode-to-stable-point policy with a limit is a runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "check the decoded value, not the raw %XX".
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
