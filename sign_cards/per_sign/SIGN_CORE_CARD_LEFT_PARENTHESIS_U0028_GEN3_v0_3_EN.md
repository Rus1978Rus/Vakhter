PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_LEFT_PARENTHESIS_U0028_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_LEFT_PARENTHESIS_U0028_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_LEFT_PARENTHESIS_U0028_GEN3_v0_3_EN
CODEPOINT: U+0028
VISIBLE_FORM: (
UNICODE_NAME: LEFT PARENTHESIS
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: left parenthesis / call & filter open
CATEGORY_ROADMAP: INJ (LDAP filter group, call/subshell open) · PHAGO: — (grouping forgery)

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
VISIBLE_FORM: (
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: LEFT_PARENTHESIS_FORM ≠ EFFECT
SIGN_CATEGORY:
  - grouping in math/prose (a (b))
  - function-call opener (fn(args))
  - LDAP filter grouping ((&(a)(b)))
  - shell subshell / regex group opener ((cmd), (a|b))

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_GROUPING_ONLY — "(" is not always benign grouping (it opens calls/filters/subshells)
  2. NOT_CALL_SAFE — a call opener can invoke a function with attacker-shaped arguments
  3. NOT_BALANCED_PROOF — a lone "(" can imbalance and inject into a filter/expression
  4. NOT_ESCAPED_PROOF — the presence of "(" does not mean it is quoted/escaped
  5. NOT_ENCODED_SAFE — "%28" may be decoded back to "(" later
  6. NOT_AUTHORITY — "(" does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; context makes it open a group/call
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_LDAP_GROUP_SAFE — "(" opens an LDAP filter clause that can inject logic
  10. NOT_SANITIZED_PROOF — the presence of "(" does not mean the input is sanitized
  11. NOT_OUTPUT_CONTEXT_PROOF — safety depends on the parse/expansion context

BASE_FORMULAS:
  LEFT_PARENTHESIS_FORM ≠ EFFECT
  LEFT_PARENTHESIS_FORM ≠ GROUPING_ONLY_PROOF
  LEFT_PARENTHESIS_FORM ≠ CALL_SAFETY_PROOF
  LEFT_PARENTHESIS_FORM ≠ BALANCED_PROOF
  LEFT_PARENTHESIS_FORM ≠ ESCAPED_PROOF
  LEFT_PARENTHESIS_FORM ≠ ENCODED_SAFETY_PROOF
  LEFT_PARENTHESIS_FORM ≠ AUTHORITY
  LEFT_PARENTHESIS_FORM ≠ EXECUTION_TRIGGER
  LEFT_PARENTHESIS_FORM ≠ LDAP_GROUP_SAFETY_PROOF
  LEFT_PARENTHESIS_FORM ≠ SANITIZED_PROOF
  LEFT_PARENTHESIS_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "(" (ZONE_1) has parallel functions (grouping, call opener, LDAP group, subshell/regex group) co-existing without cultural precession. Polysemy of a stable sign.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a punctuation/mathematical mark with no gestural predecessor; the call/filter/group functions are layered on by the digital epoch in parallel.

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
    INPUT: "the total (with tax) is 20"
    CONTEXT: parenthetical grouping in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: LEFT_PARENTHESIS_FORM ≠ GROUPING_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "call foo(x, y)"
    CONTEXT: a function call shown as text
    EXPECTED: INFO
    RISK: NONE
    GUARD: LEFT_PARENTHESIS_FORM ≠ CALL_SAFETY_PROOF
  SAFE_CASE_003:
    INPUT: "(a + b) * c"
    CONTEXT: math grouping in an expression
    EXPECTED: INFO
    RISK: NONE
    GUARD: LEFT_PARENTHESIS_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "see figure (3) below"
    CONTEXT: a reference number in parentheses
    EXPECTED: INFO
    RISK: NONE
    GUARD: LEFT_PARENTHESIS_FORM ≠ GROUPING_ONLY_PROOF
  SAFE_CASE_005:
    INPUT: "emoticon :-)"
    CONTEXT: a parenthesis inside an emoticon
    EXPECTED: INFO
    RISK: NONE
    GUARD: LEFT_PARENTHESIS_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "regex group (abc) matches abc"
    CONTEXT: describing a regex group in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: LEFT_PARENTHESIS_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: LDAP_FILTER_GROUP_INJECTION
    INPUT: "*)(uid=*))(|(uid=*"
    CONTEXT: "(" opening an injected LDAP filter clause
    RISK: CRITICAL
    ATTACK: "(" + ")" reshape the filter into an OR that matches any user (auth bypass)
    GUARD: LEFT_PARENTHESIS_FORM ≠ LDAP_GROUP_SAFETY_PROOF
  RISK_CASE_002:
    NAME: SSTI_CALL_OPEN
    INPUT: "{{ cycler.__init__.__globals__.os.popen('id') }}"
    CONTEXT: "(" opening a call in a server-side template
    RISK: CRITICAL
    ATTACK: "(" invokes a method (popen) inside an evaluated template → RCE
    GUARD: LEFT_PARENTHESIS_FORM ≠ CALL_SAFETY_PROOF
  RISK_CASE_003:
    NAME: SUBSHELL_OPEN
    INPUT: "$(id) or `(reboot)`"
    CONTEXT: "(" opening a subshell in command substitution
    RISK: HIGH
    ATTACK: "(" groups a command list executed as a subshell
    GUARD: LEFT_PARENTHESIS_FORM ≠ EFFECT
  RISK_CASE_004:
    NAME: REGEX_GROUP_REDOS
    INPUT: "(a+)+ on a long input"
    CONTEXT: "(" opening a nested quantified group (ReDoS)
    RISK: HIGH
    ATTACK: the group plus quantifiers cause catastrophic backtracking
    GUARD: LEFT_PARENTHESIS_FORM ≠ EFFECT
  RISK_CASE_005:
    NAME: ENCODED_PAREN_BYPASS
    INPUT: "%28uid=*%29 (with a later decode)"
    CONTEXT: an encoded "(" decoded back before the filter
    RISK: MEDIUM
    ATTACK: %28 decodes to "(" AFTER the check → filter grouping
    GUARD: LEFT_PARENTHESIS_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_PAREN_BYPASS
    INPUT: "（uid=* (fullwidth （ U+FF08)"
    CONTEXT: a look-alike to bypass a "(" filter
    RISK: MEDIUM
    ATTACK: a filter looks for ASCII "(", a normalizer may fold （ to "("
    GUARD: LEFT_PARENTHESIS_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: （
    CODEPOINT: U+FF08
    NAME: FULLWIDTH LEFT PARENTHESIS
    RISK: HIGH
    RULE: FULLWIDTH_LEFT_PARENTHESIS ≠ LEFT_PARENTHESIS (bypasses a filter looking for ASCII "(")
  CONFUSABLE_002:
    VISIBLE_FORM: ﹙
    CODEPOINT: U+FE59
    NAME: SMALL LEFT PARENTHESIS
    RISK: MEDIUM
    RULE: SMALL_LEFT_PARENTHESIS ≠ LEFT_PARENTHESIS
  CONFUSABLE_003:
    VISIBLE_FORM: ⁽
    CODEPOINT: U+207D
    NAME: SUPERSCRIPT LEFT PARENTHESIS
    RISK: LOW
    RULE: SUPERSCRIPT_LEFT_PARENTHESIS ≠ LEFT_PARENTHESIS
  CONFUSABLE_004:
    VISIBLE_FORM: ₍
    CODEPOINT: U+208D
    NAME: SUBSCRIPT LEFT PARENTHESIS
    RISK: LOW
    RULE: SUBSCRIPT_LEFT_PARENTHESIS ≠ LEFT_PARENTHESIS
  CONFUSABLE_005:
    VISIBLE_FORM: ❨
    CODEPOINT: U+2768
    NAME: MEDIUM LEFT PARENTHESIS ORNAMENT
    RISK: LOW
    RULE: MEDIUM_LEFT_PARENTHESIS_ORNAMENT ≠ LEFT_PARENTHESIS

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "'(' is always benign grouping"
    RESPONSE: LEFT_PARENTHESIS_FORM ≠ GROUPING_ONLY_PROOF
    RULE: "(" opens calls, LDAP filter clauses, subshells, and regex groups
  CG2:
    TRIGGER: "opening a call cannot be dangerous"
    RESPONSE: LEFT_PARENTHESIS_FORM ≠ CALL_SAFETY_PROOF
    RULE: "(" can invoke a method with attacker-shaped arguments (SSTI/RCE)
  CG3:
    TRIGGER: "an LDAP '(' just starts a group"
    RESPONSE: LEFT_PARENTHESIS_FORM ≠ LDAP_GROUP_SAFETY_PROOF
    RULE: "(" opens a filter clause that can inject an OR/any match
  CG4:
    TRIGGER: "'%28' is safe forever"
    RESPONSE: LEFT_PARENTHESIS_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to "(" before the parser
  CG5:
    TRIGGER: "an ASCII '(' filter catches all parentheses"
    RESPONSE: LEFT_PARENTHESIS_FORM ≠ EFFECT
    RULE: fullwidth （ (U+FF08) and small ﹙ (U+FE59) are different codepoints
  CG6:
    TRIGGER: "the presence of '(' means the input is sanitized"
    RESPONSE: LEFT_PARENTHESIS_FORM ≠ SANITIZED_PROOF
    RULE: the presence of the sign says nothing about sanitization

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: ")(|"
      NAME: LDAP_OR_INJECTION
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: closing then reopening a filter with an injected OR
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "$("
      NAME: SUBSHELL_SUBSTITUTION
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: opening a command substitution subshell
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "(a+)+"
      NAME: REGEX_NESTED_GROUP
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: a nested quantified group causing ReDoS
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with "(" are central to filter/call/subshell injection.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "(" opens a group/call/filter clause, but does not imitate the existence of a verified entity. Its risks are grouping/call injection, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of ASCII "(" with fullwidth （ (U+FF08) to bypass a filter
  A2: substitution with small ﹙ (U+FE59)
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: LDAP filter group injection *)(uid=*))(|(uid=*
  B2: SSTI call open cycler...popen('id')
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: ")(|" (SC1) — LDAP OR injection
  C2: "$(" (SC2) — subshell substitution
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "(" presented as harmless grouping inside a filter field
  D2: "%28" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: filter-group injection into an LDAP bind
  E2: N/A — vector: method call into a server-side template
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: "(" is always benign grouping
  EXPECTED: FAIL_GROUPING_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: opening a call cannot be dangerous
  EXPECTED: FAIL_CALL_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: an LDAP "(" just starts a group
  EXPECTED: FAIL_LDAP_GROUP_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%28" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: an ASCII "(" filter catches all parenthesis look-alikes
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: the presence of "(" proves the input was sanitized
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to escape "(" per context (LDAP/template/shell/regex) without false positives on prose/math/calls/emoticons?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (LDAP filter escaping + sandboxed templating + argument-vector exec + regex-timeout is an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "the safety of '(' is decided by the parse/expansion context".
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
