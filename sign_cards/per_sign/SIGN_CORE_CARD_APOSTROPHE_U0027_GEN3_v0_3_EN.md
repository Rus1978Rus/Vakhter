PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_APOSTROPHE_U0027_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_APOSTROPHE_U0027_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_APOSTROPHE_U0027_GEN3_v0_3_EN
CODEPOINT: U+0027
VISIBLE_FORM: '
UNICODE_NAME: APOSTROPHE
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: apostrophe / single quote
CATEGORY_ROADMAP: INJ (SQL injection string break) · PHAGO: — (structure masking)

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
VISIBLE_FORM: '
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: APOSTROPHE_FORM ≠ EFFECT
SIGN_CATEGORY:
  - string-literal delimiter (SQL/JS/shell: '...')
  - apostrophe/contraction in text (don't, O'Brien)
  - single quote / quotation

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_STRING_SAFE — "'" does not make a string literal safe (it breaks the context)
  2. NOT_ESCAPED_PROOF — the presence of "'" does not mean it is escaped
  3. NOT_APOSTROPHE_ONLY — "'" is not always an apostrophe (in SQL it is a string delimiter)
  4. NOT_PARAMETERIZED_PROOF — "'" does not mean the query is parameterized
  5. NOT_AUTHORITY — "'" does not confirm officialness
  6. NOT_EXECUTION_TRIGGER — by itself it executes nothing
  7. NOT_TRUST_SIGNAL — it does not increase trust
  8. NOT_SANITIZED_PROOF — the presence of "'" does not mean the input is sanitized
  9. NOT_QUOTE_BALANCE_PROOF — "'" does not guarantee quotes are balanced
  10. NOT_ENCODED_SAFE — "%27"/"&#39;" may be decoded back to "'"
  11. NOT_LITERAL_TEXT — "'" is not always literal text (it can close a string in a query)

BASE_FORMULAS:
  APOSTROPHE_FORM ≠ EFFECT
  APOSTROPHE_FORM ≠ STRING_SAFETY_PROOF
  APOSTROPHE_FORM ≠ ESCAPED_PROOF
  APOSTROPHE_FORM ≠ APOSTROPHE_ONLY_PROOF
  APOSTROPHE_FORM ≠ PARAMETERIZED_PROOF
  APOSTROPHE_FORM ≠ AUTHORITY
  APOSTROPHE_FORM ≠ EXECUTION_TRIGGER
  APOSTROPHE_FORM ≠ TRUST_SIGNAL
  APOSTROPHE_FORM ≠ SANITIZED_PROOF
  APOSTROPHE_FORM ≠ QUOTE_BALANCE_PROOF
  APOSTROPHE_FORM ≠ ENCODED_SAFETY_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "'" (ZONE_1) has parallel functions (apostrophe in text, string delimiter in code/SQL, quotation) co-existing without cultural precession. Polysemy of a stable sign.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a written punctuation sign with no gestural predecessor; the string-delimiter function is layered on by the digital epoch in parallel.

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
    INPUT: "don't worry"
    CONTEXT: apostrophe in a contraction
    EXPECTED: INFO
    RISK: NONE
    GUARD: APOSTROPHE_FORM ≠ APOSTROPHE_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "O'Brien"
    CONTEXT: apostrophe in a surname
    EXPECTED: INFO
    RISK: NONE
    GUARD: APOSTROPHE_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "it's fine"
    CONTEXT: apostrophe in text
    EXPECTED: INFO
    RISK: NONE
    GUARD: APOSTROPHE_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "name = 'value' (parameterized query)"
    CONTEXT: a string literal via a prepared statement (the value is a parameter)
    EXPECTED: INFO
    RISK: NONE
    GUARD: APOSTROPHE_FORM ≠ PARAMETERIZED_PROOF
  SAFE_CASE_005:
    INPUT: "l'école"
    CONTEXT: apostrophe in a French word
    EXPECTED: INFO
    RISK: NONE
    GUARD: APOSTROPHE_FORM ≠ APOSTROPHE_ONLY_PROOF
  SAFE_CASE_006:
    INPUT: "'a properly closed string literal'"
    CONTEXT: a correctly closed string literal
    EXPECTED: INFO
    RISK: NONE
    GUARD: APOSTROPHE_FORM ≠ QUOTE_BALANCE_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: SQLI_AUTH_BYPASS
    INPUT: "' OR '1'='1"
    CONTEXT: input into an unescaped SQL query
    RISK: CRITICAL
    ATTACK: "'" closes the string, "OR '1'='1" makes the condition always true — auth bypass
    GUARD: APOSTROPHE_FORM ≠ STRING_SAFETY_PROOF
  RISK_CASE_002:
    NAME: SQLI_STACKED_QUERY
    INPUT: "'; DROP TABLE users --"
    CONTEXT: breaking the string and appending a second query
    RISK: CRITICAL
    ATTACK: "'" closes the literal, ";" starts a new query, "--" comments the tail
    GUARD: APOSTROPHE_FORM ≠ SANITIZED_PROOF
  RISK_CASE_003:
    NAME: SQLI_UNION
    INPUT: "' UNION SELECT username,password FROM users --"
    CONTEXT: data extraction via UNION
    RISK: CRITICAL
    ATTACK: "'" breaks the string, UNION appends a foreign result set
    GUARD: APOSTROPHE_FORM ≠ PARAMETERIZED_PROOF
  RISK_CASE_004:
    NAME: COMMENT_TERMINATION
    INPUT: "admin'--"
    CONTEXT: closing the string and commenting the rest of the query
    RISK: HIGH
    ATTACK: "'--" cuts off the password check in a WHERE condition
    GUARD: APOSTROPHE_FORM ≠ QUOTE_BALANCE_PROOF
  RISK_CASE_005:
    NAME: ESCAPED_QUOTE_CONFUSION
    INPUT: "\\' (a backslash before the quote)"
    CONTEXT: escaping confusion between layers
    RISK: HIGH
    ATTACK: "\\'" is escaped in one layer, breaks the string in another (escape desync)
    GUARD: APOSTROPHE_FORM ≠ ESCAPED_PROOF
  RISK_CASE_006:
    NAME: SMART_QUOTE_BYPASS
    INPUT: "’ OR ’1’=’1 (right single quote ’ U+2019)"
    CONTEXT: a quote look-alike normalized by the backend to "'"
    RISK: MEDIUM
    ATTACK: a filter looks for ASCII "'", a normalizer/DB folds ’ to "'" → the injection comes alive
    GUARD: APOSTROPHE_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ’
    CODEPOINT: U+2019
    NAME: RIGHT SINGLE QUOTATION MARK
    RISK: HIGH
    RULE: RIGHT_SINGLE_QUOTE ≠ APOSTROPHE (smart quote, normalized to "'")
  CONFUSABLE_002:
    VISIBLE_FORM: ＇
    CODEPOINT: U+FF07
    NAME: FULLWIDTH APOSTROPHE
    RISK: HIGH
    RULE: FULLWIDTH_APOSTROPHE ≠ APOSTROPHE (bypasses an ASCII filter)
  CONFUSABLE_003:
    VISIBLE_FORM: ‘
    CODEPOINT: U+2018
    NAME: LEFT SINGLE QUOTATION MARK
    RISK: MEDIUM
    RULE: LEFT_SINGLE_QUOTE ≠ APOSTROPHE
  CONFUSABLE_004:
    VISIBLE_FORM: ´
    CODEPOINT: U+00B4
    NAME: ACUTE ACCENT
    RISK: LOW
    RULE: ACUTE_ACCENT ≠ APOSTROPHE
  CONFUSABLE_005:
    VISIBLE_FORM: ʼ
    CODEPOINT: U+02BC
    NAME: MODIFIER LETTER APOSTROPHE
    RISK: MEDIUM
    RULE: MODIFIER_APOSTROPHE ≠ APOSTROPHE

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "since the input is escaped once, '\''' is safe in SQL"
    RESPONSE: APOSTROPHE_FORM ≠ ESCAPED_PROOF
    RULE: escaping desync between layers; use parameterized queries
  CG2:
    TRIGGER: "'\''' is always an apostrophe"
    RESPONSE: APOSTROPHE_FORM ≠ APOSTROPHE_ONLY_PROOF
    RULE: in SQL/JS "'" delimits a string, not writes an apostrophe
  CG3:
    TRIGGER: "the presence of '\''' means the query is parameterized"
    RESPONSE: APOSTROPHE_FORM ≠ PARAMETERIZED_PROOF
    RULE: the only defense is prepared statements, not the presence/absence of a quote
  CG4:
    TRIGGER: "an ASCII '\''' filter catches all quotes"
    RESPONSE: APOSTROPHE_FORM ≠ EFFECT
    RULE: ’ (U+2019), ＇ (U+FF07) are different codepoints normalized to "'"
  CG5:
    TRIGGER: "'admin'--' is just text with an apostrophe"
    RESPONSE: APOSTROPHE_FORM ≠ SANITIZED_PROOF
    RULE: "'--" closes the string and comments the condition; sanitization is mandatory
  CG6:
    TRIGGER: "balanced quotes = safe"
    RESPONSE: APOSTROPHE_FORM ≠ QUOTE_BALANCE_PROOF
    RULE: quote balance does not prevent injection (' OR '1'='1 is balanced)

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "'--"
      NAME: QUOTE_COMMENT_TERMINATION
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: closing the string + commenting the rest of the SQL
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "' OR '"
      NAME: SQLI_TAUTOLOGY
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: a tautology for auth bypass (' OR '1'='1)
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "''"
      NAME: DOUBLED_QUOTE
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: an escaped quote in SQL OR an empty string — context-dependent
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with "'" are central to SQL injection.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "'" masks/breaks the STRUCTURE of a string literal (SQL/code) but does not imitate the existence of a verified entity. Its risks are injection, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of ASCII "'" with ’ (U+2019) / ＇ (U+FF07), normalized by the backend to "'"
  A2: %27 / &#39; (encoded quote) with a later decode
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: "' OR '1'='1" — auth bypass
  B2: "'; DROP TABLE users --" — stacked query
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "'--" (SC1) — string close + comment
  C2: "' UNION SELECT …" — data extraction
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "admin'--" disguised as an ordinary login
  D2: "\\'" — escaping confusion between layers
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: injection into a WHERE clause
  E2: N/A — vector: multibyte escaping bypass (e.g. GBK)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: a single escaping of "'" makes the SQL safe
  EXPECTED: FAIL_ESCAPE_DESYNC_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: "'" is always an apostrophe
  EXPECTED: FAIL_APOSTROPHE_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: the presence of "'" proves the query is parameterized
  EXPECTED: FAIL_PARAMETERIZED_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: an ASCII "'" filter catches all quote look-alikes
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: "admin'--" is harmless text with an apostrophe
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: balanced quotes mean safety
  EXPECTED: FAIL_QUOTE_BALANCE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to neutralize "'" without false positives on legit apostrophes (don't, O'Brien)?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (parameterized queries + normalization of quote look-alikes is an integrator/runtime concern; an apostrophe in data stays legit)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "safety comes from prepared statements, not the presence of '\''".
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
