PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_EXCLAMATION_MARK_U0021_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_EXCLAMATION_MARK_U0021_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_EXCLAMATION_MARK_U0021_GEN3_v0_3_EN
CODEPOINT: U+0021
VISIBLE_FORM: !
UNICODE_NAME: EXCLAMATION MARK
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: exclamation / negation & history
CATEGORY_ROADMAP: INJ (shell history expansion, logical negation) · PHAGO: — (condition inversion)

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
VISIBLE_FORM: !
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: EXCLAMATION_MARK_FORM ≠ EFFECT
SIGN_CATEGORY:
  - logical NOT / not-equal (!x, a != b)
  - shell history expansion (!!, !$, !cmd)
  - emphasis / interjection in prose
  - special marker in configs (e.g. YAML tags, ! negation in patterns)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_PUNCTUATION_ONLY — "!" is not always emphasis (in a shell it expands history)
  2. NOT_NEGATION_SAFE — a "!" negation can invert an authorization/condition
  3. NOT_HISTORY_SAFE — "!!" / "!cmd" re-executes or expands to prior/other commands
  4. NOT_ESCAPED_PROOF — the presence of "!" does not mean it is quoted/escaped
  5. NOT_ENCODED_SAFE — "%21" may be decoded back to "!" later
  6. NOT_AUTHORITY — "!" does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; context makes it expand/negate
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_PATTERN_SCOPE_SAFE — "!" in a glob/gitignore/ACL pattern inverts a rule's meaning
  10. NOT_SANITIZED_PROOF — the presence of "!" does not mean the input is sanitized
  11. NOT_OUTPUT_CONTEXT_PROOF — safety depends on the parse/expansion context

BASE_FORMULAS:
  EXCLAMATION_MARK_FORM ≠ EFFECT
  EXCLAMATION_MARK_FORM ≠ PUNCTUATION_ONLY_PROOF
  EXCLAMATION_MARK_FORM ≠ NEGATION_SAFETY_PROOF
  EXCLAMATION_MARK_FORM ≠ HISTORY_SAFETY_PROOF
  EXCLAMATION_MARK_FORM ≠ ESCAPED_PROOF
  EXCLAMATION_MARK_FORM ≠ ENCODED_SAFETY_PROOF
  EXCLAMATION_MARK_FORM ≠ AUTHORITY
  EXCLAMATION_MARK_FORM ≠ EXECUTION_TRIGGER
  EXCLAMATION_MARK_FORM ≠ PATTERN_SCOPE_PROOF
  EXCLAMATION_MARK_FORM ≠ SANITIZED_PROOF
  EXCLAMATION_MARK_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "!" (ZONE_1) has parallel functions (emphasis, logical NOT, shell history, pattern negation) co-existing without cultural precession. Polysemy of a stable sign.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a punctuation mark with no gestural predecessor; the negation/history/pattern functions are layered on by the digital epoch in parallel.

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
    INPUT: "Hello world!"
    CONTEXT: emphasis in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: EXCLAMATION_MARK_FORM ≠ PUNCTUATION_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "if (a != b)"
    CONTEXT: a not-equal comparison in code
    EXPECTED: INFO
    RISK: NONE
    GUARD: EXCLAMATION_MARK_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "return !flag"
    CONTEXT: logical NOT in code (as literal text)
    EXPECTED: INFO
    RISK: NONE
    GUARD: EXCLAMATION_MARK_FORM ≠ NEGATION_SAFETY_PROOF
  SAFE_CASE_004:
    INPUT: "5! = 120"
    CONTEXT: factorial notation in math prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: EXCLAMATION_MARK_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "Wait!"
    CONTEXT: an interjection in text
    EXPECTED: INFO
    RISK: NONE
    GUARD: EXCLAMATION_MARK_FORM ≠ PUNCTUATION_ONLY_PROOF
  SAFE_CASE_006:
    INPUT: "the shebang starts with #!"
    CONTEXT: describing a shebang line in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: EXCLAMATION_MARK_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: SHELL_HISTORY_EXPANSION
    INPUT: "echo hi; !!"
    CONTEXT: "!!" re-running the previous command via history expansion
    RISK: HIGH
    ATTACK: an interactive shell expands "!!" to re-execute the prior (possibly privileged) command
    GUARD: EXCLAMATION_MARK_FORM ≠ HISTORY_SAFETY_PROOF
  RISK_CASE_002:
    NAME: HISTORY_ARG_INJECTION
    INPUT: "rm !$"
    CONTEXT: "!$" expanding to the last argument of the previous command
    RISK: MEDIUM
    ATTACK: "!$" pulls a prior argument (e.g. a sensitive path) into a new command
    GUARD: EXCLAMATION_MARK_FORM ≠ HISTORY_SAFETY_PROOF
  RISK_CASE_003:
    NAME: NEGATION_LOGIC_INVERSION
    INPUT: "allow if !isBlocked (attacker sets isBlocked undefined)"
    CONTEXT: a "!" flipping an authorization decision on a loose value
    RISK: HIGH
    ATTACK: "!undefined" becomes true, inverting a block into an allow
    GUARD: EXCLAMATION_MARK_FORM ≠ NEGATION_SAFETY_PROOF
  RISK_CASE_004:
    NAME: GITIGNORE_ACL_UNNEGATE
    INPUT: "!secret.key (re-include an excluded file)"
    CONTEXT: "!" un-ignoring a path in a gitignore/ACL pattern
    RISK: MEDIUM
    ATTACK: "!" reverses an exclusion so a secret is re-included/shipped
    GUARD: EXCLAMATION_MARK_FORM ≠ PATTERN_SCOPE_PROOF
  RISK_CASE_005:
    NAME: ENCODED_BANG_BYPASS
    INPUT: "cmd%21%21 (with a later decode)"
    CONTEXT: an encoded "!!" decoded back before the shell
    RISK: MEDIUM
    ATTACK: %21%21 decodes to "!!" AFTER the check → history expansion
    GUARD: EXCLAMATION_MARK_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_BANG_BYPASS
    INPUT: "！！ (fullwidth ！ U+FF01)"
    CONTEXT: a look-alike to bypass a "!" filter
    RISK: LOW
    ATTACK: a filter looks for ASCII "!", a normalizer may fold ！ to "!"
    GUARD: EXCLAMATION_MARK_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ！
    CODEPOINT: U+FF01
    NAME: FULLWIDTH EXCLAMATION MARK
    RISK: HIGH
    RULE: FULLWIDTH_EXCLAMATION_MARK ≠ EXCLAMATION_MARK (bypasses a filter looking for ASCII "!")
  CONFUSABLE_002:
    VISIBLE_FORM: ǃ
    CODEPOINT: U+01C3
    NAME: LATIN LETTER RETROFLEX CLICK
    RISK: HIGH
    RULE: RETROFLEX_CLICK ≠ EXCLAMATION_MARK (a letter that looks identical to "!")
  CONFUSABLE_003:
    VISIBLE_FORM: ‼
    CODEPOINT: U+203C
    NAME: DOUBLE EXCLAMATION MARK
    RISK: LOW
    RULE: DOUBLE_EXCLAMATION_MARK ≠ EXCLAMATION_MARK (one glyph resembling "!!")
  CONFUSABLE_004:
    VISIBLE_FORM: ❗
    CODEPOINT: U+2757
    NAME: HEAVY EXCLAMATION MARK SYMBOL
    RISK: LOW
    RULE: HEAVY_EXCLAMATION_SYMBOL ≠ EXCLAMATION_MARK
  CONFUSABLE_005:
    VISIBLE_FORM: ﹗
    CODEPOINT: U+FE57
    NAME: SMALL EXCLAMATION MARK
    RISK: MEDIUM
    RULE: SMALL_EXCLAMATION_MARK ≠ EXCLAMATION_MARK

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "'!' is always emphasis"
    RESPONSE: EXCLAMATION_MARK_FORM ≠ PUNCTUATION_ONLY_PROOF
    RULE: in a shell "!" expands history; in code it negates
  CG2:
    TRIGGER: "a negation cannot be dangerous"
    RESPONSE: EXCLAMATION_MARK_FORM ≠ NEGATION_SAFETY_PROOF
    RULE: "!" can invert an authorization/condition on a loose value
  CG3:
    TRIGGER: "'!!' is just two exclamation marks"
    RESPONSE: EXCLAMATION_MARK_FORM ≠ HISTORY_SAFETY_PROOF
    RULE: an interactive shell expands "!!"/"!$" to prior commands/args
  CG4:
    TRIGGER: "'%21' is safe forever"
    RESPONSE: EXCLAMATION_MARK_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to "!" before the shell
  CG5:
    TRIGGER: "an ASCII '!' filter catches all exclamation marks"
    RESPONSE: EXCLAMATION_MARK_FORM ≠ EFFECT
    RULE: fullwidth ！ (U+FF01) and retroflex click ǃ (U+01C3) are different codepoints
  CG6:
    TRIGGER: "the presence of '!' means the input is sanitized"
    RESPONSE: EXCLAMATION_MARK_FORM ≠ SANITIZED_PROOF
    RULE: the presence of the sign says nothing about sanitization

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "!!"
      NAME: HISTORY_REEXEC
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: re-executing the previous shell command
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "!$"
      NAME: HISTORY_LAST_ARG
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: pulling the previous command's last argument
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "!pattern"
      NAME: PATTERN_UNNEGATE
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: inverting a gitignore/ACL/glob rule
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with "!" are central to history/negation abuse.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "!" expands history or inverts a condition/pattern, but does not imitate the existence of a verified entity. Its risks are expansion/inversion, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of ASCII "!" with fullwidth ！ (U+FF01) to bypass a filter
  A2: substitution with retroflex click ǃ (U+01C3), a letter that looks identical
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: shell history expansion echo hi; !!
  B2: negation logic inversion allow if !isBlocked
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "!!" (SC1) — history re-exec
  C2: "!pattern" (SC3) — gitignore/ACL un-negate
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "!" presented as harmless emphasis inside a command field
  D2: "%21" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: history expansion into an interactive shell
  E2: N/A — vector: condition inversion into an authorization check
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: "!" is always emphasis
  EXPECTED: FAIL_PUNCTUATION_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: a negation cannot be dangerous
  EXPECTED: FAIL_NEGATION_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: "!!" is just two exclamation marks
  EXPECTED: FAIL_HISTORY_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%21" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: an ASCII "!" filter catches all exclamation look-alikes
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: the presence of "!" proves the input was sanitized
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to neutralize "!" per context (interactive shell/negation/pattern) without false positives on emphasis/factorial/!=?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (disable history expansion in non-interactive contexts + strict boolean coercion + pattern-rule review is an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "the safety of '!' is decided by the parse/expansion context".
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
