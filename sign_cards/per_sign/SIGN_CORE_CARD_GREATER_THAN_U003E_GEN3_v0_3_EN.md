PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_GREATER_THAN_U003E_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_GREATER_THAN_U003E_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_GREATER_THAN_U003E_GEN3_v0_3_EN
CODEPOINT: U+003E
VISIBLE_FORM: >
UNICODE_NAME: GREATER-THAN SIGN
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: greater-than / tag close
CATEGORY_ROADMAP: INJ (XSS tag closing) · PHAGO: — (structure masking)

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
VISIBLE_FORM: >
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: GREATER_THAN_FORM ≠ EFFECT
SIGN_CATEGORY:
  - "greater-than" comparison operator (a > b)
  - HTML/XML tag closing (<div>)
  - shell output redirect (> file, >> append)
  - generic angle bracket / arrow

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_TAG_CLOSE_SAFE — ">" closes a tag, activating executable content; the closing itself is not safe
  2. NOT_COMPARISON_ONLY — ">" is not always a comparison (in HTML it closes a tag)
  3. NOT_ESCAPED_PROOF — the presence of ">" does not mean it is escaped
  4. NOT_ENCODED_SAFE — "&gt;" may be decoded back to ">" later
  5. NOT_AUTHORITY — ">" does not confirm officialness
  6. NOT_EXECUTION_TRIGGER — by itself it executes nothing
  7. NOT_TRUST_SIGNAL — it does not increase trust
  8. NOT_ATTRIBUTE_SAFE — ">" can end an attribute/tag and break out of a context
  9. NOT_REDIRECT_SAFE — ">" in the shell overwrites a file (> /etc/passwd)
  10. NOT_SANITIZED_PROOF — the presence of ">" does not mean the input is sanitized
  11. NOT_OUTPUT_CONTEXT_PROOF — safety depends on the output context

BASE_FORMULAS:
  GREATER_THAN_FORM ≠ EFFECT
  GREATER_THAN_FORM ≠ TAG_CLOSE_SAFETY_PROOF
  GREATER_THAN_FORM ≠ COMPARISON_ONLY_PROOF
  GREATER_THAN_FORM ≠ ESCAPED_PROOF
  GREATER_THAN_FORM ≠ ENCODED_SAFETY_PROOF
  GREATER_THAN_FORM ≠ AUTHORITY
  GREATER_THAN_FORM ≠ EXECUTION_TRIGGER
  GREATER_THAN_FORM ≠ TRUST_SIGNAL
  GREATER_THAN_FORM ≠ REDIRECT_SAFETY_PROOF
  GREATER_THAN_FORM ≠ SANITIZED_PROOF
  GREATER_THAN_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: ">" (ZONE_1) has parallel functions (comparison, tag closing, output redirect) co-existing without cultural precession. Polysemy of a stable sign.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a mathematical/written sign with no gestural predecessor; the markup/redirect functions are layered on by the digital epoch in parallel.

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
    INPUT: "10 > 5"
    CONTEXT: numeric comparison
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREATER_THAN_FORM ≠ COMPARISON_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "if (x > 0)"
    CONTEXT: comparison in code
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREATER_THAN_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "price > 100"
    CONTEXT: comparison in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREATER_THAN_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "&gt;div&lt; (shown as text)"
    CONTEXT: entity-encoded, displayed as text
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREATER_THAN_FORM ≠ ENCODED_SAFETY_PROOF
  SAFE_CASE_005:
    INPUT: "x >= y"
    CONTEXT: "greater-than-or-equal" operator
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREATER_THAN_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "a > b > c"
    CONTEXT: a chain of comparisons
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREATER_THAN_FORM ≠ COMPARISON_ONLY_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: ATTRIBUTE_BREAKOUT
    INPUT: 'value"><script>alert(1)</script>'
    CONTEXT: breaking out of an attribute via ">" and opening a new tag
    RISK: CRITICAL
    ATTACK: '"' closes the attribute, ">" closes the tag, "<script>" injects a new tag (XSS)
    GUARD: GREATER_THAN_FORM ≠ OUTPUT_CONTEXT_PROOF
  RISK_CASE_002:
    NAME: TAG_CLOSE_INJECTION
    INPUT: "<img src=x onerror=alert(1)>"
    CONTEXT: ">" completes a tag with an event handler
    RISK: CRITICAL
    ATTACK: ">" closes <img …onerror>, making the tag active
    GUARD: GREATER_THAN_FORM ≠ TAG_CLOSE_SAFETY_PROOF
  RISK_CASE_003:
    NAME: SHELL_REDIRECT_OVERWRITE
    INPUT: "cmd > /etc/passwd"
    CONTEXT: an output redirect overwrites a file
    RISK: HIGH
    ATTACK: ">" overwrites the target file with the command's output
    GUARD: GREATER_THAN_FORM ≠ REDIRECT_SAFETY_PROOF
  RISK_CASE_004:
    NAME: SHELL_REDIRECT_APPEND
    INPUT: "echo evil >> ~/.bashrc"
    CONTEXT: appending to a config file
    RISK: HIGH
    ATTACK: ">>" adds a line to an executable profile (persistence)
    GUARD: GREATER_THAN_FORM ≠ REDIRECT_SAFETY_PROOF
  RISK_CASE_005:
    NAME: ENCODED_TAG_CLOSE_BYPASS
    INPUT: "&gt; (with a later double decode)"
    CONTEXT: an encoded ">" decoded back before output
    RISK: HIGH
    ATTACK: &gt; decodes to ">" AFTER the check → closes the tag
    GUARD: GREATER_THAN_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_GT_BYPASS
    INPUT: "＜script＞ (fullwidth ＞ U+FF1E)"
    CONTEXT: an angle look-alike to bypass a tag filter
    RISK: MEDIUM
    ATTACK: a filter looks for ASCII ">", a normalizer may fold ＞ to ">"
    GUARD: GREATER_THAN_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ＞
    CODEPOINT: U+FF1E
    NAME: FULLWIDTH GREATER-THAN SIGN
    RISK: HIGH
    RULE: FULLWIDTH_GREATER_THAN ≠ GREATER_THAN (bypasses a tag filter looking for ASCII ">")
  CONFUSABLE_002:
    VISIBLE_FORM: ›
    CODEPOINT: U+203A
    NAME: SINGLE RIGHT-POINTING ANGLE QUOTATION MARK
    RISK: MEDIUM
    RULE: SINGLE_RIGHT_ANGLE_QUOTE ≠ GREATER_THAN
  CONFUSABLE_003:
    VISIBLE_FORM: ⟩
    CODEPOINT: U+27E9
    NAME: MATHEMATICAL RIGHT ANGLE BRACKET
    RISK: LOW
    RULE: MATH_RIGHT_ANGLE ≠ GREATER_THAN
  CONFUSABLE_004:
    VISIBLE_FORM: 〉
    CODEPOINT: U+3009
    NAME: RIGHT ANGLE BRACKET
    RISK: LOW
    RULE: CJK_RIGHT_ANGLE ≠ GREATER_THAN
  CONFUSABLE_005:
    VISIBLE_FORM: ˃
    CODEPOINT: U+02C3
    NAME: MODIFIER LETTER RIGHT ARROWHEAD
    RISK: LOW
    RULE: RIGHT_ARROWHEAD ≠ GREATER_THAN

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "'>' is always a comparison"
    RESPONSE: GREATER_THAN_FORM ≠ COMPARISON_ONLY_PROOF
    RULE: in HTML ">" closes a tag, not a comparison
  CG2:
    TRIGGER: "since the input reached output, '>' is already safe"
    RESPONSE: GREATER_THAN_FORM ≠ OUTPUT_CONTEXT_PROOF
    RULE: safety depends on the output context; escape per context
  CG3:
    TRIGGER: "'>' in a command is just text"
    RESPONSE: GREATER_THAN_FORM ≠ REDIRECT_SAFETY_PROOF
    RULE: ">"/">>" overwrite/append to a file; escape in a shell context
  CG4:
    TRIGGER: "'&gt;' is safe forever"
    RESPONSE: GREATER_THAN_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the entity may be decoded back to ">" before output
  CG5:
    TRIGGER: "an ASCII '>' filter catches all angles"
    RESPONSE: GREATER_THAN_FORM ≠ EFFECT
    RULE: fullwidth ＞ (U+FF1E) is a different codepoint
  CG6:
    TRIGGER: "the presence of '>' means the input is sanitized"
    RESPONSE: GREATER_THAN_FORM ≠ SANITIZED_PROOF
    RULE: the presence of the sign says nothing about sanitization

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: '">'
      NAME: ATTRIBUTE_BREAKOUT
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: closing an attribute and tag to inject a new tag
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: ">>"
      NAME: SHELL_APPEND
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: appending to a file (persistence/config tampering)
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "/>"
      NAME: SELF_CLOSING_TAG
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: a self-closing tag; markup parser manipulation
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with ">" are central to XSS/redirect.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: ">" closes/masks markup STRUCTURE or redirects output, but does not imitate the existence of a verified entity. Its risks are injection/overwrite, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of ASCII ">" with fullwidth ＞ (U+FF1E) to bypass a tag filter
  A2: mixing ">" with › (U+203A) in a filter
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: attribute breakout value"><script>
  B2: shell redirect cmd > /etc/passwd (overwrite)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: '">' (SC1) — attribute breakout
  C2: ">>" (SC2) — appending to a file
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "<img …onerror=…>" — ">" activates the tag
  D2: "&gt;" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: tag-close injection into a template
  E2: N/A — vector: file overwrite via redirect
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: ">" is always a comparison
  EXPECTED: FAIL_COMPARISON_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: since the input reached output, ">" is already safe
  EXPECTED: FAIL_OUTPUT_CONTEXT_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: ">" in a command is harmless text
  EXPECTED: FAIL_REDIRECT_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "&gt;" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: an ASCII ">" filter catches all angle look-alikes
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: the presence of ">" proves the input was sanitized
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to escape ">" per context (HTML/attribute/shell) without false positives on comparison?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (context-aware output escaping + forbidding dangerous redirect is an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "the safety of '>' is decided by the output context".
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
