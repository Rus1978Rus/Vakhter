PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_QUOTATION_MARK_U0022_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_QUOTATION_MARK_U0022_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_QUOTATION_MARK_U0022_GEN3_v0_3_EN
CODEPOINT: U+0022
VISIBLE_FORM: "
UNICODE_NAME: QUOTATION MARK
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: double quote / string delimiter
CATEGORY_ROADMAP: INJ (attribute/string break in HTML/SQL/JSON) · PHAGO: — (delimiter breakout)

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
VISIBLE_FORM: "
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: QUOTATION_MARK_FORM ≠ EFFECT
SIGN_CATEGORY:
  - string literal delimiter ("text")
  - HTML attribute value delimiter (attr="value")
  - JSON key/value delimiter ({"k":"v"})
  - typographic quotation of speech ("hi")

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_STRING_CLOSE_SAFE — '"' closes a string/attribute; the closing itself opens a breakout context
  2. NOT_QUOTE_ONLY — '"' is not always literary quotation (in code it delimits/breaks a value)
  3. NOT_ESCAPED_PROOF — the presence of '"' does not mean it is escaped (\")
  4. NOT_ENCODED_SAFE — "&quot;" or %22 may be decoded back to '"' later
  5. NOT_AUTHORITY — '"' does not confirm officialness
  6. NOT_EXECUTION_TRIGGER — by itself it executes nothing
  7. NOT_TRUST_SIGNAL — it does not increase trust
  8. NOT_ATTRIBUTE_SAFE — '"' can end an attribute value and break out into tag context
  9. NOT_SQL_SAFE — '"' can break an identifier/string boundary in some SQL dialects
  10. NOT_SANITIZED_PROOF — the presence of '"' does not mean the input is sanitized
  11. NOT_OUTPUT_CONTEXT_PROOF — safety depends on the output context (HTML/JS/SQL/JSON)
  12. NOT_SMART_QUOTE_EQUIVALENT — a curly “ ” is a different codepoint, not this delimiter

BASE_FORMULAS:
  QUOTATION_MARK_FORM ≠ EFFECT
  QUOTATION_MARK_FORM ≠ STRING_CLOSE_SAFETY_PROOF
  QUOTATION_MARK_FORM ≠ QUOTE_ONLY_PROOF
  QUOTATION_MARK_FORM ≠ ESCAPED_PROOF
  QUOTATION_MARK_FORM ≠ ENCODED_SAFETY_PROOF
  QUOTATION_MARK_FORM ≠ AUTHORITY
  QUOTATION_MARK_FORM ≠ EXECUTION_TRIGGER
  QUOTATION_MARK_FORM ≠ TRUST_SIGNAL
  QUOTATION_MARK_FORM ≠ ATTRIBUTE_SAFETY_PROOF
  QUOTATION_MARK_FORM ≠ SANITIZED_PROOF
  QUOTATION_MARK_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: '"' (ZONE_1) has parallel functions (literary quotation, string/attribute/JSON delimiter) co-existing without cultural precession. Polysemy of a stable sign.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a written/typographic sign with no gestural predecessor; the code-delimiter functions are layered on by the digital epoch in parallel.

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
    INPUT: 'say "hello"'
    CONTEXT: literary quotation in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: QUOTATION_MARK_FORM ≠ QUOTE_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: 'attr="value"'
    CONTEXT: properly closed HTML attribute
    EXPECTED: INFO
    RISK: NONE
    GUARD: QUOTATION_MARK_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: '{"k":"v"}'
    CONTEXT: well-formed JSON
    EXPECTED: INFO
    RISK: NONE
    GUARD: QUOTATION_MARK_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: 'width="100"'
    CONTEXT: numeric attribute value
    EXPECTED: INFO
    RISK: NONE
    GUARD: QUOTATION_MARK_FORM ≠ ATTRIBUTE_SAFETY_PROOF
  SAFE_CASE_005:
    INPUT: 'She said "hi" and left'
    CONTEXT: quoted speech in text
    EXPECTED: INFO
    RISK: NONE
    GUARD: QUOTATION_MARK_FORM ≠ QUOTE_ONLY_PROOF
  SAFE_CASE_006:
    INPUT: 'print("done")'
    CONTEXT: properly closed string literal in code
    EXPECTED: INFO
    RISK: NONE
    GUARD: QUOTATION_MARK_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: ATTRIBUTE_BREAKOUT
    INPUT: '" onmouseover="alert(1)'
    CONTEXT: closing an attribute value and injecting a new event-handler attribute
    RISK: CRITICAL
    ATTACK: '"' closes the value, then a new attribute (onmouseover) is injected → XSS
    GUARD: QUOTATION_MARK_FORM ≠ OUTPUT_CONTEXT_PROOF
  RISK_CASE_002:
    NAME: ATTRIBUTE_TAG_BREAKOUT
    INPUT: '"><script>alert(1)</script>'
    CONTEXT: closing the attribute and the tag, then opening a new tag
    RISK: CRITICAL
    ATTACK: '"' closes the value, ">" closes the tag, "<script>" injects (XSS)
    GUARD: QUOTATION_MARK_FORM ≠ ATTRIBUTE_SAFETY_PROOF
  RISK_CASE_003:
    NAME: SQL_STRING_BREAK
    INPUT: '" OR "1"="1'
    CONTEXT: breaking a double-quoted SQL string/identifier boundary
    RISK: CRITICAL
    ATTACK: '"' closes the literal and injects always-true logic (SQLi in dialects using ")
    GUARD: QUOTATION_MARK_FORM ≠ EFFECT
  RISK_CASE_004:
    NAME: JSON_INJECTION
    INPUT: '","admin":true,"x":"'
    CONTEXT: closing a JSON value and injecting a new key
    RISK: HIGH
    ATTACK: '"' closes the value; a forged "admin":true key is injected into the object
    GUARD: QUOTATION_MARK_FORM ≠ OUTPUT_CONTEXT_PROOF
  RISK_CASE_005:
    NAME: ESCAPE_DESYNC
    INPUT: '\\" (backslash-quote decoded inconsistently)'
    CONTEXT: an escaped quote that one layer treats as literal and another as a delimiter
    RISK: HIGH
    ATTACK: \" survives one decoder but closes the string in the next → boundary desync
    GUARD: QUOTATION_MARK_FORM ≠ ESCAPED_PROOF
  RISK_CASE_006:
    NAME: SMART_QUOTE_BYPASS
    INPUT: '“ onmouseover=alert(1) (curly “ U+201C)'
    CONTEXT: a look-alike quote to bypass a filter, later folded to '"'
    RISK: MEDIUM
    ATTACK: a filter looks for ASCII '"', a normalizer may fold “ to '"' after the check
    GUARD: QUOTATION_MARK_FORM ≠ ENCODED_SAFETY_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ＂
    CODEPOINT: U+FF02
    NAME: FULLWIDTH QUOTATION MARK
    RISK: HIGH
    RULE: FULLWIDTH_QUOTATION_MARK ≠ QUOTATION_MARK (bypasses a filter looking for ASCII '"')
  CONFUSABLE_002:
    VISIBLE_FORM: “
    CODEPOINT: U+201C
    NAME: LEFT DOUBLE QUOTATION MARK
    RISK: MEDIUM
    RULE: LEFT_DOUBLE_QUOTE ≠ QUOTATION_MARK
  CONFUSABLE_003:
    VISIBLE_FORM: ”
    CODEPOINT: U+201D
    NAME: RIGHT DOUBLE QUOTATION MARK
    RISK: MEDIUM
    RULE: RIGHT_DOUBLE_QUOTE ≠ QUOTATION_MARK
  CONFUSABLE_004:
    VISIBLE_FORM: „
    CODEPOINT: U+201E
    NAME: DOUBLE LOW-9 QUOTATION MARK
    RISK: LOW
    RULE: DOUBLE_LOW9_QUOTE ≠ QUOTATION_MARK
  CONFUSABLE_005:
    VISIBLE_FORM: ″
    CODEPOINT: U+2033
    NAME: DOUBLE PRIME
    RISK: LOW
    RULE: DOUBLE_PRIME ≠ QUOTATION_MARK

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "'\"' is always literary quotation"
    RESPONSE: QUOTATION_MARK_FORM ≠ QUOTE_ONLY_PROOF
    RULE: in code '"' delimits/breaks a string or attribute, not just quotes speech
  CG2:
    TRIGGER: "since the input reached output, '\"' is already safe"
    RESPONSE: QUOTATION_MARK_FORM ≠ OUTPUT_CONTEXT_PROOF
    RULE: safety depends on the output context; escape per context (HTML/JS/SQL/JSON)
  CG3:
    TRIGGER: "'\\\"' means the quote is escaped"
    RESPONSE: QUOTATION_MARK_FORM ≠ ESCAPED_PROOF
    RULE: escaping may desync across decoders; a later layer can still see a delimiter
  CG4:
    TRIGGER: "'&quot;' is safe forever"
    RESPONSE: QUOTATION_MARK_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the entity/percent form may be decoded back to '"' before output
  CG5:
    TRIGGER: "an ASCII '\"' filter catches all quotes"
    RESPONSE: QUOTATION_MARK_FORM ≠ EFFECT
    RULE: fullwidth ＂ (U+FF02) and curly “ ” are different codepoints
  CG6:
    TRIGGER: "the presence of '\"' means the input is sanitized"
    RESPONSE: QUOTATION_MARK_FORM ≠ SANITIZED_PROOF
    RULE: the presence of the sign says nothing about sanitization

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: '">'
      NAME: ATTRIBUTE_TAG_BREAKOUT
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: closing an attribute and tag to inject a new tag
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: '" '
      NAME: ATTRIBUTE_INJECTION
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: closing a value and injecting a new attribute (onmouseover=)
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: '\\"'
      NAME: ESCAPE_DESYNC
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: backslash-quote handled differently across decoding layers
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with '"' are central to attribute/string breakout.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: '"' breaks/closes a delimiter BOUNDARY (string/attribute/JSON), but does not imitate the existence of a verified entity. Its risks are injection/desync, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of ASCII '"' with fullwidth ＂ (U+FF02) to bypass a filter
  A2: mixing '"' with curly “ ” (U+201C/U+201D) in a filter
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: attribute breakout " onmouseover="alert(1)
  B2: SQL string break " OR "1"="1
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: '">' (SC1) — attribute + tag breakout
  C2: '\\"' (SC3) — escape desync across decoders
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: '","admin":true,"x":"' — JSON key injection
  D2: "&quot;" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: attribute injection into a template
  E2: N/A — vector: JSON object forgery via delimiter break
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: '"' is always literary quotation
  EXPECTED: FAIL_QUOTE_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: since the input reached output, '"' is already safe
  EXPECTED: FAIL_OUTPUT_CONTEXT_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: '\"' proves the quote is neutralized
  EXPECTED: FAIL_ESCAPED_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "&quot;" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: an ASCII '"' filter catches all quote look-alikes
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: the presence of '"' proves the input was sanitized
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to escape '"' per context (HTML attribute/JS string/SQL/JSON) without false positives on literary quotation?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (context-aware output escaping + parameterized queries is an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "the safety of '\"' is decided by the output context".
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
