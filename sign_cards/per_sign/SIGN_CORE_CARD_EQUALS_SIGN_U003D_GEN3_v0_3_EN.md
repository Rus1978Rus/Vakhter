PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_EQUALS_SIGN_U003D_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_EQUALS_SIGN_U003D_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_EQUALS_SIGN_U003D_GEN3_v0_3_EN
CODEPOINT: U+003D
VISIBLE_FORM: =
UNICODE_NAME: EQUALS SIGN
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: equals / assignment & filter
CATEGORY_ROADMAP: INJ (LDAP filter, param/env assignment) · PHAGO: — (key-value forgery)

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
VISIBLE_FORM: =
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: EQUALS_SIGN_FORM ≠ EFFECT
SIGN_CATEGORY:
  - assignment operator (x = 1) / comparison (a == b)
  - key-value separator (URL query, cookie, env, config)
  - LDAP filter equality (cn=value)
  - Base64 padding / math equality in prose

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_EQUALITY_ONLY — "=" is not always math equality (it assigns/filters/binds)
  2. NOT_ASSIGN_SAFE — an assignment can overwrite a trusted key (param/env/config)
  3. NOT_KV_SCOPED — an extra "=" can split a value into an unexpected key-value pair
  4. NOT_ESCAPED_PROOF — the presence of "=" does not mean it is quoted/escaped
  5. NOT_ENCODED_SAFE — "%3D" may be decoded back to "=" later
  6. NOT_AUTHORITY — "=" does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; context makes it bind
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_LDAP_FILTER_SAFE — "=" builds an LDAP equality that can be widened/injected
  10. NOT_SANITIZED_PROOF — the presence of "=" does not mean the input is sanitized
  11. NOT_OUTPUT_CONTEXT_PROOF — safety depends on the parse/bind context

BASE_FORMULAS:
  EQUALS_SIGN_FORM ≠ EFFECT
  EQUALS_SIGN_FORM ≠ EQUALITY_ONLY_PROOF
  EQUALS_SIGN_FORM ≠ ASSIGN_SAFETY_PROOF
  EQUALS_SIGN_FORM ≠ KV_SCOPE_PROOF
  EQUALS_SIGN_FORM ≠ ESCAPED_PROOF
  EQUALS_SIGN_FORM ≠ ENCODED_SAFETY_PROOF
  EQUALS_SIGN_FORM ≠ AUTHORITY
  EQUALS_SIGN_FORM ≠ EXECUTION_TRIGGER
  EQUALS_SIGN_FORM ≠ LDAP_FILTER_SAFETY_PROOF
  EQUALS_SIGN_FORM ≠ SANITIZED_PROOF
  EQUALS_SIGN_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "=" (ZONE_1) has parallel functions (math equality, assignment, key-value separator, LDAP equality, Base64 padding) co-existing without cultural precession. Polysemy of a stable sign.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a mathematical sign with no gestural predecessor; the assignment/binding/filter functions are layered on by the digital epoch in parallel.

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
    INPUT: "2 + 2 = 4"
    CONTEXT: math equality in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: EQUALS_SIGN_FORM ≠ EQUALITY_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "let x = 10"
    CONTEXT: an assignment in a code example (as literal text)
    EXPECTED: INFO
    RISK: NONE
    GUARD: EQUALS_SIGN_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "?page=1"
    CONTEXT: a normal URL key-value pair
    EXPECTED: INFO
    RISK: NONE
    GUARD: EQUALS_SIGN_FORM ≠ KV_SCOPE_PROOF
  SAFE_CASE_004:
    INPUT: "if (a == b)"
    CONTEXT: a comparison in code
    EXPECTED: INFO
    RISK: NONE
    GUARD: EQUALS_SIGN_FORM ≠ EQUALITY_ONLY_PROOF
  SAFE_CASE_005:
    INPUT: "dGVzdA== (Base64 padding)"
    CONTEXT: "=" as Base64 padding
    EXPECTED: INFO
    RISK: NONE
    GUARD: EQUALS_SIGN_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "color=red in a config line"
    CONTEXT: a benign key-value config entry
    EXPECTED: INFO
    RISK: NONE
    GUARD: EQUALS_SIGN_FORM ≠ ASSIGN_SAFETY_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: LDAP_EQUALITY_INJECTION
    INPUT: "cn=admin)(|(password=*"
    CONTEXT: an "=" building an injected LDAP equality/filter
    RISK: CRITICAL
    ATTACK: "=" plus filter syntax injects LDAP logic (auth bypass / data disclosure)
    GUARD: EQUALS_SIGN_FORM ≠ LDAP_FILTER_SAFETY_PROOF
  RISK_CASE_002:
    NAME: PARAMETER_KEY_INJECTION
    INPUT: "name=x&isAdmin=true"
    CONTEXT: an injected "=" forging an extra key-value parameter
    RISK: HIGH
    ATTACK: "=" defines a new key (isAdmin) the backend may honor (privilege change)
    GUARD: EQUALS_SIGN_FORM ≠ KV_SCOPE_PROOF
  RISK_CASE_003:
    NAME: ENV_VAR_INJECTION
    INPUT: "value\\nLD_PRELOAD=/tmp/evil.so"
    CONTEXT: an injected "=" defining a dangerous environment variable
    RISK: HIGH
    ATTACK: "=" binds an attacker-controlled env var that alters runtime behavior
    GUARD: EQUALS_SIGN_FORM ≠ ASSIGN_SAFETY_PROOF
  RISK_CASE_004:
    NAME: SQL_ALWAYS_TRUE
    INPUT: "' OR 1=1 -- "
    CONTEXT: an "=" building an always-true SQL condition
    RISK: HIGH
    ATTACK: "1=1" makes a WHERE clause always match (auth bypass)
    GUARD: EQUALS_SIGN_FORM ≠ EFFECT
  RISK_CASE_005:
    NAME: ENCODED_EQUALS_BYPASS
    INPUT: "cn%3Dadmin (with a later decode)"
    CONTEXT: an encoded "=" decoded back before the filter/parser
    RISK: MEDIUM
    ATTACK: %3D decodes to "=" AFTER the check → key-value/filter binding
    GUARD: EQUALS_SIGN_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_EQUALS_BYPASS
    INPUT: "cn＝admin (fullwidth ＝ U+FF1D)"
    CONTEXT: a look-alike to bypass an "=" filter
    RISK: MEDIUM
    ATTACK: a filter looks for ASCII "=", a normalizer may fold ＝ to "="
    GUARD: EQUALS_SIGN_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ＝
    CODEPOINT: U+FF1D
    NAME: FULLWIDTH EQUALS SIGN
    RISK: HIGH
    RULE: FULLWIDTH_EQUALS_SIGN ≠ EQUALS_SIGN (bypasses a filter looking for ASCII "=")
  CONFUSABLE_002:
    VISIBLE_FORM: ﹦
    CODEPOINT: U+FE66
    NAME: SMALL EQUALS SIGN
    RISK: MEDIUM
    RULE: SMALL_EQUALS_SIGN ≠ EQUALS_SIGN
  CONFUSABLE_003:
    VISIBLE_FORM: ꞊
    CODEPOINT: U+A78A
    NAME: MODIFIER LETTER SHORT EQUALS SIGN
    RISK: MEDIUM
    RULE: MODIFIER_SHORT_EQUALS ≠ EQUALS_SIGN
  CONFUSABLE_004:
    VISIBLE_FORM: ⩵
    CODEPOINT: U+2A75
    NAME: TWO CONSECUTIVE EQUALS SIGNS
    RISK: LOW
    RULE: TWO_CONSECUTIVE_EQUALS ≠ EQUALS_SIGN (a single glyph resembling "==")
  CONFUSABLE_005:
    VISIBLE_FORM: ═
    CODEPOINT: U+2550
    NAME: BOX DRAWINGS DOUBLE HORIZONTAL
    RISK: LOW
    RULE: BOX_DOUBLE_HORIZONTAL ≠ EQUALS_SIGN (visual overlap only)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "'=' is always math equality"
    RESPONSE: EQUALS_SIGN_FORM ≠ EQUALITY_ONLY_PROOF
    RULE: "=" assigns, binds key-values, and builds LDAP/SQL filters
  CG2:
    TRIGGER: "an assignment cannot be dangerous"
    RESPONSE: EQUALS_SIGN_FORM ≠ ASSIGN_SAFETY_PROOF
    RULE: "=" can overwrite a trusted key or bind a dangerous env var
  CG3:
    TRIGGER: "an LDAP '=' just tests equality"
    RESPONSE: EQUALS_SIGN_FORM ≠ LDAP_FILTER_SAFETY_PROOF
    RULE: "=" plus filter syntax injects logic (auth bypass)
  CG4:
    TRIGGER: "'%3D' is safe forever"
    RESPONSE: EQUALS_SIGN_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to "=" before the parser
  CG5:
    TRIGGER: "an ASCII '=' filter catches all equals signs"
    RESPONSE: EQUALS_SIGN_FORM ≠ EFFECT
    RULE: fullwidth ＝ (U+FF1D) and small ﹦ (U+FE66) are different codepoints
  CG6:
    TRIGGER: "the presence of '=' means the input is sanitized"
    RESPONSE: EQUALS_SIGN_FORM ≠ SANITIZED_PROOF
    RULE: the presence of the sign says nothing about sanitization

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "=*"
      NAME: LDAP_PRESENCE_WILDCARD
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: an equality turned into a presence/any match
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "&key="
      NAME: PARAM_KEY_INJECTION
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: injecting an extra key-value parameter
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "1=1"
      NAME: ALWAYS_TRUE
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: an always-true condition in SQL/filters
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with "=" are central to filter/key-value injection.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "=" binds key-values or builds filters, but does not imitate the existence of a verified entity. Its risks are assignment/filter injection, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of ASCII "=" with fullwidth ＝ (U+FF1D) to bypass a filter
  A2: substitution with small ﹦ (U+FE66)
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: LDAP equality injection cn=admin)(|(password=*
  B2: HTTP parameter key injection name=x&isAdmin=true
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "=*" (SC1) — LDAP presence/wildcard
  C2: "1=1" (SC3) — always-true condition
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "=" presented as harmless math equality inside a filter field
  D2: "%3D" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: env-var binding into a process launch
  E2: N/A — vector: forged key-value injection into a parameter parser
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: "=" is always math equality
  EXPECTED: FAIL_EQUALITY_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: an assignment cannot be dangerous
  EXPECTED: FAIL_ASSIGN_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: an LDAP "=" just tests equality
  EXPECTED: FAIL_LDAP_FILTER_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%3D" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: an ASCII "=" filter catches all equals look-alikes
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: the presence of "=" proves the input was sanitized
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to escape "=" per context (LDAP/query/env/SQL) without false positives on math/assignment/Base64?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (LDAP filter escaping + strict parameter parsing + env allow-listing + parameterized queries is an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "the safety of '=' is decided by the parse/bind context".
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
