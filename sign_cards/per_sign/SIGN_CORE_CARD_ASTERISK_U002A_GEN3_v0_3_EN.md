PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_ASTERISK_U002A_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_ASTERISK_U002A_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_ASTERISK_U002A_GEN3_v0_3_EN
CODEPOINT: U+002A
VISIBLE_FORM: *
UNICODE_NAME: ASTERISK
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: asterisk / wildcard
CATEGORY_ROADMAP: INJ (glob/regex/LDAP/SQL wildcard) · PHAGO: — (match-scope widening)

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
VISIBLE_FORM: *
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: ASTERISK_FORM ≠ EFFECT
SIGN_CATEGORY:
  - shell glob wildcard (*.txt)
  - regex quantifier "zero or more" (a*)
  - SQL/LDAP wildcard (SELECT *, cn=*)
  - multiplication / footnote / emphasis marker in text

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_MULTIPLY_ONLY — "*" is not always multiplication (in a shell it globs files)
  2. NOT_WILDCARD_SAFE — a wildcard widens a match to unintended targets
  3. NOT_GLOB_SCOPED — "*" can expand to files/args outside the intended set
  4. NOT_ESCAPED_PROOF — the presence of "*" does not mean it is quoted/escaped
  5. NOT_ENCODED_SAFE — "%2A" may be decoded back to "*" later
  6. NOT_AUTHORITY — "*" does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; context makes it expand
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_LDAP_FILTER_SAFE — "*" in an LDAP filter can turn an equality into "any" (auth bypass)
  10. NOT_SANITIZED_PROOF — the presence of "*" does not mean the input is sanitized
  11. NOT_OUTPUT_CONTEXT_PROOF — safety depends on the parse/expansion context

BASE_FORMULAS:
  ASTERISK_FORM ≠ EFFECT
  ASTERISK_FORM ≠ MULTIPLY_ONLY_PROOF
  ASTERISK_FORM ≠ WILDCARD_SAFETY_PROOF
  ASTERISK_FORM ≠ GLOB_SCOPE_PROOF
  ASTERISK_FORM ≠ ESCAPED_PROOF
  ASTERISK_FORM ≠ ENCODED_SAFETY_PROOF
  ASTERISK_FORM ≠ AUTHORITY
  ASTERISK_FORM ≠ EXECUTION_TRIGGER
  ASTERISK_FORM ≠ LDAP_FILTER_SAFETY_PROOF
  ASTERISK_FORM ≠ SANITIZED_PROOF
  ASTERISK_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "*" (ZONE_1) has parallel functions (multiplication, glob, regex quantifier, SQL/LDAP wildcard, footnote) co-existing without cultural precession. Polysemy of a stable sign.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a printer's/mathematical mark with no gestural predecessor; the glob/regex/wildcard functions are layered on by the digital epoch in parallel.

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
    INPUT: "3 * 4 = 12"
    CONTEXT: multiplication in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: ASTERISK_FORM ≠ MULTIPLY_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "see the footnote *"
    CONTEXT: a footnote marker in text
    EXPECTED: INFO
    RISK: NONE
    GUARD: ASTERISK_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "**bold** in Markdown"
    CONTEXT: emphasis markers (as literal text)
    EXPECTED: INFO
    RISK: NONE
    GUARD: ASTERISK_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "rating: 5 stars *****"
    CONTEXT: asterisks as star glyphs in text
    EXPECTED: INFO
    RISK: NONE
    GUARD: ASTERISK_FORM ≠ MULTIPLY_ONLY_PROOF
  SAFE_CASE_005:
    INPUT: "list all *.txt files"
    CONTEXT: describing a glob pattern in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: ASTERISK_FORM ≠ GLOB_SCOPE_PROOF
  SAFE_CASE_006:
    INPUT: "the * key on a phone"
    CONTEXT: naming the asterisk key in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: ASTERISK_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: LDAP_WILDCARD_AUTH_BYPASS
    INPUT: "cn=*)(uid=*"
    CONTEXT: an LDAP filter wildcard turning equality into "any"
    RISK: CRITICAL
    ATTACK: "*" matches any value and "(...)" injects filter logic → auth bypass
    GUARD: ASTERISK_FORM ≠ LDAP_FILTER_SAFETY_PROOF
  RISK_CASE_002:
    NAME: GLOB_ARG_INJECTION
    INPUT: "rm * (or rm -rf ./*)"
    CONTEXT: a glob expanding to unintended files/arguments
    RISK: HIGH
    ATTACK: "*" expands to every entry, possibly to filenames that look like flags (-rf)
    GUARD: ASTERISK_FORM ≠ GLOB_SCOPE_PROOF
  RISK_CASE_003:
    NAME: REGEX_QUANTIFIER_REDOS
    INPUT: "(a+)*$ on a long input"
    CONTEXT: a nested quantifier causing catastrophic backtracking
    RISK: HIGH
    ATTACK: "*" over a group triggers ReDoS (denial of service)
    GUARD: ASTERISK_FORM ≠ EFFECT
  RISK_CASE_004:
    NAME: SQL_WILDCARD_OVERMATCH
    INPUT: "name LIKE '%*%' widening a search"
    CONTEXT: a wildcard broadening a query beyond intent
    RISK: MEDIUM
    ATTACK: "*"/"%" broadens the match to expose more rows than intended
    GUARD: ASTERISK_FORM ≠ WILDCARD_SAFETY_PROOF
  RISK_CASE_005:
    NAME: ENCODED_ASTERISK_BYPASS
    INPUT: "cn=%2A (with a later decode)"
    CONTEXT: an encoded "*" decoded back before the filter
    RISK: MEDIUM
    ATTACK: %2A decodes to "*" AFTER the check → wildcard match
    GUARD: ASTERISK_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_ASTERISK_BYPASS
    INPUT: "cn=＊ (fullwidth ＊ U+FF0A)"
    CONTEXT: a look-alike to bypass an "*" filter
    RISK: MEDIUM
    ATTACK: a filter looks for ASCII "*", a normalizer may fold ＊ to "*"
    GUARD: ASTERISK_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ＊
    CODEPOINT: U+FF0A
    NAME: FULLWIDTH ASTERISK
    RISK: HIGH
    RULE: FULLWIDTH_ASTERISK ≠ ASTERISK (bypasses a filter looking for ASCII "*")
  CONFUSABLE_002:
    VISIBLE_FORM: ∗
    CODEPOINT: U+2217
    NAME: ASTERISK OPERATOR
    RISK: MEDIUM
    RULE: ASTERISK_OPERATOR ≠ ASTERISK
  CONFUSABLE_003:
    VISIBLE_FORM: ⁎
    CODEPOINT: U+204E
    NAME: LOW ASTERISK
    RISK: LOW
    RULE: LOW_ASTERISK ≠ ASTERISK
  CONFUSABLE_004:
    VISIBLE_FORM: ✱
    CODEPOINT: U+2731
    NAME: HEAVY ASTERISK
    RISK: LOW
    RULE: HEAVY_ASTERISK ≠ ASTERISK
  CONFUSABLE_005:
    VISIBLE_FORM: ٭
    CODEPOINT: U+066D
    NAME: ARABIC FIVE POINTED STAR
    RISK: LOW
    RULE: ARABIC_FIVE_POINTED_STAR ≠ ASTERISK

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "'*' is always multiplication"
    RESPONSE: ASTERISK_FORM ≠ MULTIPLY_ONLY_PROOF
    RULE: in a shell/regex/LDAP "*" is a wildcard/quantifier
  CG2:
    TRIGGER: "a wildcard cannot be dangerous"
    RESPONSE: ASTERISK_FORM ≠ WILDCARD_SAFETY_PROOF
    RULE: "*" widens a match to unintended targets or expands to unexpected args
  CG3:
    TRIGGER: "an LDAP '*' just means the field is present"
    RESPONSE: ASTERISK_FORM ≠ LDAP_FILTER_SAFETY_PROOF
    RULE: "*" turns an equality filter into "any", enabling auth bypass
  CG4:
    TRIGGER: "'%2A' is safe forever"
    RESPONSE: ASTERISK_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to "*" before the filter
  CG5:
    TRIGGER: "an ASCII '*' filter catches all stars"
    RESPONSE: ASTERISK_FORM ≠ EFFECT
    RULE: fullwidth ＊ (U+FF0A) and asterisk operator ∗ (U+2217) are different codepoints
  CG6:
    TRIGGER: "the presence of '*' means the input is sanitized"
    RESPONSE: ASTERISK_FORM ≠ SANITIZED_PROOF
    RULE: the presence of the sign says nothing about sanitization

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "*)("
      NAME: LDAP_FILTER_INJECTION
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: a wildcard plus filter parentheses injecting LDAP logic
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "./*"
      NAME: GLOB_ARG_EXPANSION
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: a glob expanding to files that look like command flags
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: ")*"
      NAME: REGEX_NESTED_QUANTIFIER
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: a quantifier over a group causing catastrophic backtracking
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with "*" are central to wildcard/glob/regex abuse.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "*" widens a match or expands a glob, but does not imitate the existence of a verified entity. Its risks are over-match/expansion, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of ASCII "*" with fullwidth ＊ (U+FF0A) to bypass a filter
  A2: substitution with asterisk operator ∗ (U+2217)
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: LDAP wildcard auth bypass cn=*)(uid=*
  B2: SQL/LDAP over-match name LIKE '%*%'
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "*)(" (SC1) — LDAP filter injection
  C2: ")*" (SC3) — regex nested quantifier (ReDoS)
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "*" presented as harmless multiplication inside a filter field
  D2: "%2A" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: wildcard auth bypass into an LDAP bind
  E2: N/A — vector: glob expansion into a shell argument vector
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: "*" is always multiplication
  EXPECTED: FAIL_MULTIPLY_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: a wildcard cannot be dangerous
  EXPECTED: FAIL_WILDCARD_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: an LDAP "*" just means the field is present
  EXPECTED: FAIL_LDAP_FILTER_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%2A" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: an ASCII "*" filter catches all star look-alikes
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: the presence of "*" proves the input was sanitized
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to escape "*" per context (LDAP/glob/regex/SQL) without false positives on multiplication/footnotes/Markdown?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (LDAP filter escaping + glob-disabling/quoting + regex-timeout/escaping + parameterized LIKE is an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "the safety of '*' is decided by the parse/expansion context".
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
