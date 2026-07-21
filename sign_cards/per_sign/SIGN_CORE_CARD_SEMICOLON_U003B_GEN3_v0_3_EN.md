PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_SEMICOLON_U003B_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_SEMICOLON_U003B_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_SEMICOLON_U003B_GEN3_v0_3_EN
CODEPOINT: U+003B
VISIBLE_FORM: ;
UNICODE_NAME: SEMICOLON
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: semicolon / statement separator
CATEGORY_ROADMAP: INJ (shell/SQL statement stacking) · PHAGO: — (command chaining)

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
VISIBLE_FORM: ;
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: SEMICOLON_FORM ≠ EFFECT
SIGN_CATEGORY:
  - shell command separator (cmd1; cmd2)
  - SQL statement terminator/stacker (SELECT …; DROP …)
  - programming statement separator (a=1; b=2)
  - punctuation in prose (clause separation)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_PUNCTUATION_ONLY — ";" is not always prose punctuation (in a shell it chains commands)
  2. NOT_SEPARATOR_SAFE — the "separation" it performs can start a second command
  3. NOT_TERMINATOR_SAFE — terminating one SQL statement lets a second one run
  4. NOT_ESCAPED_PROOF — the presence of ";" does not mean it is escaped/quoted
  5. NOT_ENCODED_SAFE — "%3B" may be decoded back to ";" later
  6. NOT_AUTHORITY — ";" does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; context makes it chain
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_COMMENT_SAFE — ";" is a comment marker in some dialects (INI/asm), not neutral
  10. NOT_SANITIZED_PROOF — the presence of ";" does not mean the input is sanitized
  11. NOT_OUTPUT_CONTEXT_PROOF — safety depends on the execution/parse context

BASE_FORMULAS:
  SEMICOLON_FORM ≠ EFFECT
  SEMICOLON_FORM ≠ PUNCTUATION_ONLY_PROOF
  SEMICOLON_FORM ≠ SEPARATOR_SAFETY_PROOF
  SEMICOLON_FORM ≠ TERMINATOR_SAFETY_PROOF
  SEMICOLON_FORM ≠ ESCAPED_PROOF
  SEMICOLON_FORM ≠ ENCODED_SAFETY_PROOF
  SEMICOLON_FORM ≠ AUTHORITY
  SEMICOLON_FORM ≠ EXECUTION_TRIGGER
  SEMICOLON_FORM ≠ TRUST_SIGNAL
  SEMICOLON_FORM ≠ SANITIZED_PROOF
  SEMICOLON_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: ";" (ZONE_1) has parallel functions (prose punctuation, shell/SQL/programming separator) co-existing without cultural precession. Polysemy of a stable sign.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a written punctuation sign with no gestural predecessor; the command/statement-separator functions are layered on by the digital epoch in parallel.

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
    INPUT: "I came; I saw; I left"
    CONTEXT: prose punctuation between clauses
    EXPECTED: INFO
    RISK: NONE
    GUARD: SEMICOLON_FORM ≠ PUNCTUATION_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "int a = 1; int b = 2;"
    CONTEXT: statement separators in code (as literal text)
    EXPECTED: INFO
    RISK: NONE
    GUARD: SEMICOLON_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "color: red; font-size: 12px;"
    CONTEXT: CSS declarations
    EXPECTED: INFO
    RISK: NONE
    GUARD: SEMICOLON_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "a;b;c"
    CONTEXT: a semicolon-delimited data list
    EXPECTED: INFO
    RISK: NONE
    GUARD: SEMICOLON_FORM ≠ SEPARATOR_SAFETY_PROOF
  SAFE_CASE_005:
    INPUT: "&amp; &lt; &gt;"
    CONTEXT: ";" terminating an HTML entity
    EXPECTED: INFO
    RISK: NONE
    GUARD: SEMICOLON_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "key=value; expires=..."
    CONTEXT: a cookie attribute separator
    EXPECTED: INFO
    RISK: NONE
    GUARD: SEMICOLON_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: SHELL_COMMAND_CHAIN
    INPUT: "ping 8.8.8.8; rm -rf /"
    CONTEXT: a second command runs after the first in a shell
    RISK: CRITICAL
    ATTACK: ";" ends the benign command and starts an attacker command
    GUARD: SEMICOLON_FORM ≠ SEPARATOR_SAFETY_PROOF
  RISK_CASE_002:
    NAME: SQL_STATEMENT_STACKING
    INPUT: "1; DROP TABLE users; --"
    CONTEXT: stacking a second SQL statement
    RISK: CRITICAL
    ATTACK: ";" terminates the query and injects a destructive statement
    GUARD: SEMICOLON_FORM ≠ TERMINATOR_SAFETY_PROOF
  RISK_CASE_003:
    NAME: GREEK_QUESTION_MARK_HOMOGLYPH
    INPUT: "cmd; (where ; is Greek ; U+037E)"
    CONTEXT: an identical-looking Greek question mark passes a ";" filter
    RISK: HIGH
    ATTACK: U+037E renders as ";" and may normalize to ";" after a filter check
    GUARD: SEMICOLON_FORM ≠ EFFECT
  RISK_CASE_004:
    NAME: ENCODED_SEMICOLON_BYPASS
    INPUT: "cmd%3B rm -rf ~ (with a later decode)"
    CONTEXT: an encoded ";" decoded back before execution
    RISK: HIGH
    ATTACK: %3B decodes to ";" AFTER the check → command chain
    GUARD: SEMICOLON_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: CRLF_HEADER_STACK
    INPUT: "value; injected=1 (in a header/cookie)"
    CONTEXT: adding an extra attribute/directive via ";"
    RISK: MEDIUM
    ATTACK: ";" appends an attacker-controlled directive to a header/cookie
    GUARD: SEMICOLON_FORM ≠ OUTPUT_CONTEXT_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_SEMICOLON_BYPASS
    INPUT: "cmd；rm （fullwidth ； U+FF1B）"
    CONTEXT: a look-alike to bypass a ";" filter
    RISK: MEDIUM
    ATTACK: a filter looks for ASCII ";", a normalizer may fold ； to ";"
    GUARD: SEMICOLON_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ;
    CODEPOINT: U+037E
    NAME: GREEK QUESTION MARK
    RISK: HIGH
    RULE: GREEK_QUESTION_MARK ≠ SEMICOLON (visually identical; bypasses an ASCII ";" filter)
  CONFUSABLE_002:
    VISIBLE_FORM: ；
    CODEPOINT: U+FF1B
    NAME: FULLWIDTH SEMICOLON
    RISK: HIGH
    RULE: FULLWIDTH_SEMICOLON ≠ SEMICOLON (bypasses a filter looking for ASCII ";")
  CONFUSABLE_003:
    VISIBLE_FORM: ؛
    CODEPOINT: U+061B
    NAME: ARABIC SEMICOLON
    RISK: MEDIUM
    RULE: ARABIC_SEMICOLON ≠ SEMICOLON
  CONFUSABLE_004:
    VISIBLE_FORM: ⁏
    CODEPOINT: U+204F
    NAME: REVERSED SEMICOLON
    RISK: LOW
    RULE: REVERSED_SEMICOLON ≠ SEMICOLON
  CONFUSABLE_005:
    VISIBLE_FORM: ﹔
    CODEPOINT: U+FE54
    NAME: SMALL SEMICOLON
    RISK: LOW
    RULE: SMALL_SEMICOLON ≠ SEMICOLON

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "';' is always prose punctuation"
    RESPONSE: SEMICOLON_FORM ≠ PUNCTUATION_ONLY_PROOF
    RULE: in a shell/SQL ";" starts a second command/statement
  CG2:
    TRIGGER: "a separator cannot execute anything"
    RESPONSE: SEMICOLON_FORM ≠ SEPARATOR_SAFETY_PROOF
    RULE: the separation begins a new executable unit
  CG3:
    TRIGGER: "since the input reached execution, ';' is already safe"
    RESPONSE: SEMICOLON_FORM ≠ OUTPUT_CONTEXT_PROOF
    RULE: safety depends on the parse/execution context; use parameterization/allow-lists
  CG4:
    TRIGGER: "'%3B' is safe forever"
    RESPONSE: SEMICOLON_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to ";" before execution
  CG5:
    TRIGGER: "an ASCII ';' filter catches all separators"
    RESPONSE: SEMICOLON_FORM ≠ EFFECT
    RULE: Greek ; (U+037E) and fullwidth ； (U+FF1B) are different codepoints
  CG6:
    TRIGGER: "the presence of ';' means the input is sanitized"
    RESPONSE: SEMICOLON_FORM ≠ SANITIZED_PROOF
    RULE: the presence of the sign says nothing about sanitization

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "; "
      NAME: SHELL_COMMAND_CHAIN
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: chaining a second shell command
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "; --"
      NAME: SQL_STACK_COMMENT
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: stacking a statement and commenting out the rest
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: ";&"
      NAME: CHAIN_BACKGROUND
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: chaining then backgrounding a command
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with ";" are central to command/statement injection.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: ";" chains commands/statements, but does not imitate the existence of a verified entity. Its risks are injection/stacking, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of ASCII ";" with Greek ; (U+037E) to bypass a filter
  A2: substitution with fullwidth ； (U+FF1B)
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: shell chain ping 8.8.8.8; rm -rf /
  B2: SQL stacking 1; DROP TABLE users; --
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "; " (SC1) — shell command chain
  C2: "; --" (SC2) — SQL stack + comment
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: ";" presented as harmless prose punctuation inside a command field
  D2: "%3B" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: chaining into an OS-command template
  E2: N/A — vector: second-statement injection into a query builder
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: ";" is always prose punctuation
  EXPECTED: FAIL_PUNCTUATION_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: a separator cannot execute anything
  EXPECTED: FAIL_SEPARATOR_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: since the input reached execution, ";" is already safe
  EXPECTED: FAIL_OUTPUT_CONTEXT_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%3B" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: an ASCII ";" filter catches all separator look-alikes
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: the presence of ";" proves the input was sanitized
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to neutralize ";" per context (shell/SQL/header) without false positives on prose/CSS/CSV?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (parameterized queries + argument-vector exec + context-aware quoting is an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "the safety of ';' is decided by the execution/parse context".
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
