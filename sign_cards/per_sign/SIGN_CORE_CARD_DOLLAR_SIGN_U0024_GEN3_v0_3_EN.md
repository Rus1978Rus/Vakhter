PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_DOLLAR_SIGN_U0024_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_DOLLAR_SIGN_U0024_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_DOLLAR_SIGN_U0024_GEN3_v0_3_EN
CODEPOINT: U+0024
VISIBLE_FORM: $
UNICODE_NAME: DOLLAR SIGN
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: dollar sign / variable expansion
CATEGORY_ROADMAP: INJ (shell variable/command expansion, template) · PHAGO: — (interpolation)

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
VISIBLE_FORM: $
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: DOLLAR_SIGN_FORM ≠ EFFECT
SIGN_CATEGORY:
  - shell variable expansion ($VAR, ${VAR})
  - shell command substitution ($(cmd))
  - template / interpolation marker (${expr}, $name)
  - currency symbol / regex end-anchor in prose or patterns

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_CURRENCY_ONLY — "$" is not always a currency symbol (in a shell it expands)
  2. NOT_VARIABLE_SAFE — variable expansion can splice attacker-controlled values into a command
  3. NOT_SUBSTITUTION_SAFE — "$(...)" runs the enclosed command like backticks
  4. NOT_ESCAPED_PROOF — the presence of "$" does not mean it is escaped/single-quoted
  5. NOT_ENCODED_SAFE — "%24" may be decoded back to "$" later
  6. NOT_AUTHORITY — "$" does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; context makes it expand
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_TEMPLATE_SAFE — "${...}" in a template can evaluate an expression (SSTI/JS)
  10. NOT_SANITIZED_PROOF — the presence of "$" does not mean the input is sanitized
  11. NOT_OUTPUT_CONTEXT_PROOF — safety depends on the execution/parse context

BASE_FORMULAS:
  DOLLAR_SIGN_FORM ≠ EFFECT
  DOLLAR_SIGN_FORM ≠ CURRENCY_ONLY_PROOF
  DOLLAR_SIGN_FORM ≠ VARIABLE_SAFETY_PROOF
  DOLLAR_SIGN_FORM ≠ SUBSTITUTION_SAFETY_PROOF
  DOLLAR_SIGN_FORM ≠ ESCAPED_PROOF
  DOLLAR_SIGN_FORM ≠ ENCODED_SAFETY_PROOF
  DOLLAR_SIGN_FORM ≠ AUTHORITY
  DOLLAR_SIGN_FORM ≠ EXECUTION_TRIGGER
  DOLLAR_SIGN_FORM ≠ TEMPLATE_SAFETY_PROOF
  DOLLAR_SIGN_FORM ≠ SANITIZED_PROOF
  DOLLAR_SIGN_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "$" (ZONE_1) has parallel functions (currency, shell expansion, command substitution, template marker, regex anchor) co-existing without cultural precession. Polysemy of a stable sign.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a currency/written sign with no gestural predecessor; the expansion/substitution/template functions are layered on by the digital epoch in parallel.

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
    INPUT: "Total: $19.99"
    CONTEXT: a currency amount in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: DOLLAR_SIGN_FORM ≠ CURRENCY_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "It costs $5 and $10"
    CONTEXT: currency figures in text
    EXPECTED: INFO
    RISK: NONE
    GUARD: DOLLAR_SIGN_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "regex: word$"
    CONTEXT: a regex end-of-line anchor (as literal text)
    EXPECTED: INFO
    RISK: NONE
    GUARD: DOLLAR_SIGN_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "the $ symbol on the keyboard"
    CONTEXT: naming the dollar glyph in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: DOLLAR_SIGN_FORM ≠ CURRENCY_ONLY_PROOF
  SAFE_CASE_005:
    INPUT: "jQuery uses $ as an alias"
    CONTEXT: "$" as an identifier in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: DOLLAR_SIGN_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "price rose from $2 to $3"
    CONTEXT: two currency amounts in a sentence
    EXPECTED: INFO
    RISK: NONE
    GUARD: DOLLAR_SIGN_FORM ≠ CURRENCY_ONLY_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: COMMAND_SUBSTITUTION
    INPUT: "echo $(rm -rf ~)"
    CONTEXT: "$(...)" executing the enclosed command
    RISK: CRITICAL
    ATTACK: the shell runs the command inside "$(...)" and inlines its output
    GUARD: DOLLAR_SIGN_FORM ≠ SUBSTITUTION_SAFETY_PROOF
  RISK_CASE_002:
    NAME: VARIABLE_SPLICE
    INPUT: "cp $USERFILE /etc/ (USERFILE=/etc/passwd; evil)"
    CONTEXT: an attacker-controlled variable spliced into a command
    RISK: HIGH
    ATTACK: "$USERFILE" expands to an attacker value, changing the command's meaning
    GUARD: DOLLAR_SIGN_FORM ≠ VARIABLE_SAFETY_PROOF
  RISK_CASE_003:
    NAME: SSTI_TEMPLATE_EVAL
    INPUT: "${T(java.lang.Runtime).getRuntime().exec('id')}"
    CONTEXT: server-side template injection via "${...}"
    RISK: CRITICAL
    ATTACK: "${...}" is evaluated by the template engine, executing code
    GUARD: DOLLAR_SIGN_FORM ≠ TEMPLATE_SAFETY_PROOF
  RISK_CASE_004:
    NAME: NOSQL_OPERATOR_INJECTION
    INPUT: '{"user": {"$ne": null}}'
    CONTEXT: a "$"-prefixed MongoDB operator injected via JSON
    RISK: HIGH
    ATTACK: "$ne" turns a value match into an always-true query (auth bypass)
    GUARD: DOLLAR_SIGN_FORM ≠ EFFECT
  RISK_CASE_005:
    NAME: ENCODED_DOLLAR_BYPASS
    INPUT: "cmd%24%28id%29 (with a later decode)"
    CONTEXT: an encoded "$(" decoded back before execution
    RISK: HIGH
    ATTACK: %24%28 decodes to "$(" AFTER the check → command substitution
    GUARD: DOLLAR_SIGN_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_DOLLAR_BYPASS
    INPUT: "＄(id) (fullwidth ＄ U+FF04)"
    CONTEXT: a look-alike to bypass a "$" filter
    RISK: MEDIUM
    ATTACK: a filter looks for ASCII "$", a normalizer may fold ＄ to "$"
    GUARD: DOLLAR_SIGN_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ＄
    CODEPOINT: U+FF04
    NAME: FULLWIDTH DOLLAR SIGN
    RISK: HIGH
    RULE: FULLWIDTH_DOLLAR_SIGN ≠ DOLLAR_SIGN (bypasses a filter looking for ASCII "$")
  CONFUSABLE_002:
    VISIBLE_FORM: ﹩
    CODEPOINT: U+FE69
    NAME: SMALL DOLLAR SIGN
    RISK: MEDIUM
    RULE: SMALL_DOLLAR_SIGN ≠ DOLLAR_SIGN
  CONFUSABLE_003:
    VISIBLE_FORM: ৳
    CODEPOINT: U+09F3
    NAME: BENGALI RUPEE SIGN
    RISK: LOW
    RULE: BENGALI_RUPEE ≠ DOLLAR_SIGN (currency look-alike only)
  CONFUSABLE_004:
    VISIBLE_FORM: ₴
    CODEPOINT: U+20B4
    NAME: HRYVNIA SIGN
    RISK: LOW
    RULE: HRYVNIA ≠ DOLLAR_SIGN (currency look-alike only)
  CONFUSABLE_005:
    VISIBLE_FORM: Ѕ
    CODEPOINT: U+0405
    NAME: CYRILLIC CAPITAL LETTER DZE
    RISK: LOW
    RULE: CYRILLIC_DZE ≠ DOLLAR_SIGN (S-shape with a stroke rendering overlap only)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "'$' is always a currency symbol"
    RESPONSE: DOLLAR_SIGN_FORM ≠ CURRENCY_ONLY_PROOF
    RULE: in a shell "$" expands variables and runs "$(...)"
  CG2:
    TRIGGER: "variable expansion just substitutes text, it cannot harm"
    RESPONSE: DOLLAR_SIGN_FORM ≠ VARIABLE_SAFETY_PROOF
    RULE: the expanded value can change the command's meaning or splice new args
  CG3:
    TRIGGER: "'${...}' in a template is inert"
    RESPONSE: DOLLAR_SIGN_FORM ≠ TEMPLATE_SAFETY_PROOF
    RULE: the template engine may evaluate "${...}" as an expression (SSTI)
  CG4:
    TRIGGER: "'%24' is safe forever"
    RESPONSE: DOLLAR_SIGN_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to "$" before execution
  CG5:
    TRIGGER: "an ASCII '$' filter catches all dollar signs"
    RESPONSE: DOLLAR_SIGN_FORM ≠ EFFECT
    RULE: fullwidth ＄ (U+FF04) is a different codepoint
  CG6:
    TRIGGER: "the presence of '$' means the input is sanitized"
    RESPONSE: DOLLAR_SIGN_FORM ≠ SANITIZED_PROOF
    RULE: the presence of the sign says nothing about sanitization

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "$("
      NAME: COMMAND_SUBSTITUTION
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: opening a command substitution that runs the enclosed command
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "${"
      NAME: EXPANSION_OR_TEMPLATE
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: variable expansion or template-expression evaluation (SSTI)
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "$IFS"
      NAME: FIELD_SEPARATOR_ABUSE
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: using "$IFS" to inject spaces into a filtered command
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with "$" are central to expansion/substitution injection.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "$" expands/substitutes/interpolates values, but does not imitate the existence of a verified entity. Its risks are expansion/evaluation, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of ASCII "$" with fullwidth ＄ (U+FF04) to bypass a filter
  A2: substitution with small ﹩ (U+FE69)
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: command substitution echo $(rm -rf ~)
  B2: NoSQL operator injection {"$ne": null}
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "$(" (SC1) — command substitution
  C2: "${" (SC2) — expansion / template eval
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "$" presented as a harmless currency symbol inside a command field
  D2: "%24" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: substitution into an OS-command template
  E2: N/A — vector: SSTI expression eval in a rendered template
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: "$" is always a currency symbol
  EXPECTED: FAIL_CURRENCY_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: variable expansion cannot cause harm
  EXPECTED: FAIL_VARIABLE_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: "${...}" in a template is inert
  EXPECTED: FAIL_TEMPLATE_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%24" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: an ASCII "$" filter catches all dollar look-alikes
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: the presence of "$" proves the input was sanitized
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to neutralize "$" per context (shell/template/NoSQL) without false positives on currency/regex/prose?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (single-quoting/argument-vector exec + sandboxed templating + operator-key filtering is an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "the safety of '$' is decided by the execution/parse context".
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
