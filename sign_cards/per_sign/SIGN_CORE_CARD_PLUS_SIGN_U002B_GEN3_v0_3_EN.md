PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_PLUS_SIGN_U002B_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_PLUS_SIGN_U002B_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_PLUS_SIGN_U002B_GEN3_v0_3_EN
CODEPOINT: U+002B
VISIBLE_FORM: +
UNICODE_NAME: PLUS SIGN
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: plus / URL space & concat
CATEGORY_ROADMAP: INJ (URL-space decode, SQL concat, regex quantifier) · PHAGO: — (encoding ambiguity)

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
VISIBLE_FORM: +
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: PLUS_SIGN_FORM ≠ EFFECT
SIGN_CATEGORY:
  - arithmetic addition / string concatenation (a + b)
  - space encoding in application/x-www-form-urlencoded (+)
  - SQL string concatenation (some dialects: 'a' + 'b')
  - regex quantifier "one or more" (a+)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_ADDITION_ONLY — "+" is not always arithmetic (in a form-encoded URL it means space)
  2. NOT_SPACE_DECODE_SAFE — a "+" decoding to a space can change how a value parses downstream
  3. NOT_CONCAT_SAFE — string concatenation can splice attacker data into a query/command
  4. NOT_ESCAPED_PROOF — the presence of "+" does not mean it is quoted/escaped
  5. NOT_ENCODED_SAFE — "%2B" may be decoded back to "+" later (or "+" to a space)
  6. NOT_AUTHORITY — "+" does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; context makes it decode/concat
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_REGEX_ONLY — "+" in a regex is a quantifier that can drive ReDoS
  10. NOT_SANITIZED_PROOF — the presence of "+" does not mean the input is sanitized
  11. NOT_OUTPUT_CONTEXT_PROOF — safety depends on the decode/parse context

BASE_FORMULAS:
  PLUS_SIGN_FORM ≠ EFFECT
  PLUS_SIGN_FORM ≠ ADDITION_ONLY_PROOF
  PLUS_SIGN_FORM ≠ SPACE_DECODE_SAFETY_PROOF
  PLUS_SIGN_FORM ≠ CONCAT_SAFETY_PROOF
  PLUS_SIGN_FORM ≠ ESCAPED_PROOF
  PLUS_SIGN_FORM ≠ ENCODED_SAFETY_PROOF
  PLUS_SIGN_FORM ≠ AUTHORITY
  PLUS_SIGN_FORM ≠ EXECUTION_TRIGGER
  PLUS_SIGN_FORM ≠ REGEX_ONLY_PROOF
  PLUS_SIGN_FORM ≠ SANITIZED_PROOF
  PLUS_SIGN_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "+" (ZONE_1) has parallel functions (addition, concatenation, URL space, regex quantifier) co-existing without cultural precession. Polysemy of a stable sign.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a mathematical sign with no gestural predecessor; the URL-space/concat/quantifier functions are layered on by the digital epoch in parallel.

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
    INPUT: "2 + 3 = 5"
    CONTEXT: arithmetic addition in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: PLUS_SIGN_FORM ≠ ADDITION_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "C++ programming"
    CONTEXT: "+" inside a language name
    EXPECTED: INFO
    RISK: NONE
    GUARD: PLUS_SIGN_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "+1 202 555 0100"
    CONTEXT: an international phone-number prefix
    EXPECTED: INFO
    RISK: NONE
    GUARD: PLUS_SIGN_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "a + b in code"
    CONTEXT: addition/concatenation shown as text
    EXPECTED: INFO
    RISK: NONE
    GUARD: PLUS_SIGN_FORM ≠ CONCAT_SAFETY_PROOF
  SAFE_CASE_005:
    INPUT: "temperature +5 degrees"
    CONTEXT: a positive sign in text
    EXPECTED: INFO
    RISK: NONE
    GUARD: PLUS_SIGN_FORM ≠ ADDITION_ONLY_PROOF
  SAFE_CASE_006:
    INPUT: "search?q=cats+dogs"
    CONTEXT: a normal form-encoded space between words
    EXPECTED: INFO
    RISK: NONE
    GUARD: PLUS_SIGN_FORM ≠ SPACE_DECODE_SAFETY_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: URL_SPACE_DECODE_DESYNC
    INPUT: "id=1+OR+1=1"
    CONTEXT: "+" decoding to spaces to form an SQL clause after decode
    RISK: HIGH
    ATTACK: "+" decodes to a space so "1 OR 1=1" reaches the query builder
    GUARD: PLUS_SIGN_FORM ≠ SPACE_DECODE_SAFETY_PROOF
  RISK_CASE_002:
    NAME: SQL_STRING_CONCAT
    INPUT: "'a'+(SELECT password FROM users)"
    CONTEXT: "+" concatenating a subquery into a string (MSSQL)
    RISK: HIGH
    ATTACK: "+" splices leaked data into the output via concatenation
    GUARD: PLUS_SIGN_FORM ≠ CONCAT_SAFETY_PROOF
  RISK_CASE_003:
    NAME: REGEX_QUANTIFIER_REDOS
    INPUT: "(a+)+$ on a long input"
    CONTEXT: a nested "+" quantifier causing catastrophic backtracking
    RISK: HIGH
    ATTACK: "+" over a group triggers ReDoS (denial of service)
    GUARD: PLUS_SIGN_FORM ≠ REGEX_ONLY_PROOF
  RISK_CASE_004:
    NAME: PLUS_VS_ENCODED_PLUS_AMBIGUITY
    INPUT: "token=a%2Bb (literal +) vs a+b (space)"
    CONTEXT: ambiguity between a literal "+" and a form-encoded space
    RISK: MEDIUM
    ATTACK: mismatched decoders read "+" as space or literal, corrupting a token/signature
    GUARD: PLUS_SIGN_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: EMAIL_SUBADDRESS_ABUSE
    INPUT: "victim+attacker@example.com"
    CONTEXT: "+" sub-addressing used to bypass a unique-email check
    RISK: MEDIUM
    ATTACK: "+tag" creates many aliases of one inbox to evade per-email limits
    GUARD: PLUS_SIGN_FORM ≠ EFFECT
  RISK_CASE_006:
    NAME: FULLWIDTH_PLUS_BYPASS
    INPUT: "1＋1 (fullwidth ＋ U+FF0B)"
    CONTEXT: a look-alike to bypass a "+" filter
    RISK: LOW
    ATTACK: a filter looks for ASCII "+", a normalizer may fold ＋ to "+"
    GUARD: PLUS_SIGN_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ＋
    CODEPOINT: U+FF0B
    NAME: FULLWIDTH PLUS SIGN
    RISK: HIGH
    RULE: FULLWIDTH_PLUS_SIGN ≠ PLUS_SIGN (bypasses a filter looking for ASCII "+")
  CONFUSABLE_002:
    VISIBLE_FORM: ﹢
    CODEPOINT: U+FE62
    NAME: SMALL PLUS SIGN
    RISK: MEDIUM
    RULE: SMALL_PLUS_SIGN ≠ PLUS_SIGN
  CONFUSABLE_003:
    VISIBLE_FORM: ⁺
    CODEPOINT: U+207A
    NAME: SUPERSCRIPT PLUS SIGN
    RISK: LOW
    RULE: SUPERSCRIPT_PLUS ≠ PLUS_SIGN
  CONFUSABLE_004:
    VISIBLE_FORM: ➕
    CODEPOINT: U+2795
    NAME: HEAVY PLUS SIGN
    RISK: LOW
    RULE: HEAVY_PLUS_SIGN ≠ PLUS_SIGN
  CONFUSABLE_005:
    VISIBLE_FORM: ﬩
    CODEPOINT: U+FB29
    NAME: HEBREW LETTER ALTERNATIVE PLUS SIGN
    RISK: LOW
    RULE: HEBREW_ALT_PLUS ≠ PLUS_SIGN

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "'+' is always arithmetic addition"
    RESPONSE: PLUS_SIGN_FORM ≠ ADDITION_ONLY_PROOF
    RULE: in a form-encoded URL "+" means a space; in SQL it concatenates
  CG2:
    TRIGGER: "a '+' decoding to a space is harmless"
    RESPONSE: PLUS_SIGN_FORM ≠ SPACE_DECODE_SAFETY_PROOF
    RULE: the decoded space can reshape a value into an injectable clause
  CG3:
    TRIGGER: "string concatenation cannot be dangerous"
    RESPONSE: PLUS_SIGN_FORM ≠ CONCAT_SAFETY_PROOF
    RULE: "+" can splice a subquery/attacker data into the output
  CG4:
    TRIGGER: "'%2B' / '+' encoding is safe forever"
    RESPONSE: PLUS_SIGN_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: decoders disagree on "+" vs space; the meaning can flip downstream
  CG5:
    TRIGGER: "an ASCII '+' filter catches all plus signs"
    RESPONSE: PLUS_SIGN_FORM ≠ EFFECT
    RULE: fullwidth ＋ (U+FF0B) and small ﹢ (U+FE62) are different codepoints
  CG6:
    TRIGGER: "the presence of '+' means the input is sanitized"
    RESPONSE: PLUS_SIGN_FORM ≠ SANITIZED_PROOF
    RULE: the presence of the sign says nothing about sanitization

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "+OR+"
      NAME: URL_SPACE_SQL
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: "+" decoding to spaces to form an SQL clause
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: ")+"
      NAME: REGEX_NESTED_QUANTIFIER
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: a quantifier over a group causing catastrophic backtracking
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "+@"
      NAME: EMAIL_SUBADDRESS
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: "+tag" sub-addressing to spawn many inbox aliases
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with "+" are central to decode-desync/concat/regex abuse.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "+" decodes to a space or concatenates values, but does not imitate the existence of a verified entity. Its risks are decode-desync/concat, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of ASCII "+" with fullwidth ＋ (U+FF0B) to bypass a filter
  A2: substitution with small ﹢ (U+FE62)
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: URL-space decode desync id=1+OR+1=1
  B2: SQL string concat 'a'+(SELECT password FROM users)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "+OR+" (SC1) — URL space to SQL clause
  C2: ")+" (SC2) — regex nested quantifier (ReDoS)
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "+" presented as harmless addition inside a query value
  D2: "%2B vs +" ambiguity treated as "safe" until a decoder flips it
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: decode-desync into a query builder
  E2: N/A — vector: concatenation leak into an MSSQL string
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: "+" is always arithmetic addition
  EXPECTED: FAIL_ADDITION_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: a "+" decoding to a space is harmless
  EXPECTED: FAIL_SPACE_DECODE_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: string concatenation cannot be dangerous
  EXPECTED: FAIL_CONCAT_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%2B" / "+" encoding is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: an ASCII "+" filter catches all plus look-alikes
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: the presence of "+" proves the input was sanitized
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to canonicalize "+" per context (form-decode/SQL/regex) without false positives on arithmetic/phone/C++/sub-address?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (consistent single-pass decoding + parameterized queries + regex-timeout is an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "the meaning of '+' (space vs literal vs concat) is decided by the decode/parse context".
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
