PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_LESS_THAN_U003C_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_LESS_THAN_U003C_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_LESS_THAN_U003C_GEN3_v0_3_EN
CODEPOINT: U+003C
VISIBLE_FORM: <
UNICODE_NAME: LESS-THAN SIGN
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: less-than / tag open
CATEGORY_ROADMAP: INJ (XSS tag opening) · PHAGO: — (structure masking)

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
VISIBLE_FORM: <
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: LESS_THAN_FORM ≠ EFFECT
SIGN_CATEGORY:
  - "less-than" comparison operator (a < b)
  - HTML/XML tag opening (<script>, <div>)
  - shell input redirect/heredoc (< file, << EOF)
  - generic angle bracket

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_TAG_SAFE — "<" does not make an opened tag safe (the BROWSER executes it, not "<")
  2. NOT_COMPARISON_ONLY — "<" is not always a comparison (in an HTML context it is a tag)
  3. NOT_ESCAPED_PROOF — the presence of "<" does not mean it is escaped
  4. NOT_ENCODED_SAFE — "&lt;" may be decoded back to "<" later
  5. NOT_AUTHORITY — "<" does not confirm officialness
  6. NOT_EXECUTION_TRIGGER — by itself it executes nothing
  7. NOT_TRUST_SIGNAL — it does not increase trust
  8. NOT_HTML_CONTEXT_SAFE — the same input is safe in text but dangerous in HTML
  9. NOT_SANITIZED_PROOF — the presence of "<" does not mean the input is sanitized
  10. NOT_TEXT_LITERAL — "<" is not always literal text (it can open markup)
  11. NOT_OUTPUT_CONTEXT_PROOF — safety depends on the output context (HTML/attribute/JS)

BASE_FORMULAS:
  LESS_THAN_FORM ≠ EFFECT
  LESS_THAN_FORM ≠ TAG_SAFETY_PROOF
  LESS_THAN_FORM ≠ COMPARISON_ONLY_PROOF
  LESS_THAN_FORM ≠ ESCAPED_PROOF
  LESS_THAN_FORM ≠ ENCODED_SAFETY_PROOF
  LESS_THAN_FORM ≠ AUTHORITY
  LESS_THAN_FORM ≠ EXECUTION_TRIGGER
  LESS_THAN_FORM ≠ TRUST_SIGNAL
  LESS_THAN_FORM ≠ HTML_CONTEXT_SAFETY_PROOF
  LESS_THAN_FORM ≠ SANITIZED_PROOF
  LESS_THAN_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "<" (ZONE_1) has parallel functions (comparison, tag opening, input redirect) co-existing without cultural precession. Polysemy of a stable sign.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a mathematical/written sign with no gestural predecessor; the markup function is layered on by the digital epoch in parallel.

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
    INPUT: "5 < 10"
    CONTEXT: numeric comparison
    EXPECTED: INFO
    RISK: NONE
    GUARD: LESS_THAN_FORM ≠ COMPARISON_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "if (i < n)"
    CONTEXT: comparison in code
    EXPECTED: INFO
    RISK: NONE
    GUARD: LESS_THAN_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "price < 100"
    CONTEXT: comparison in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: LESS_THAN_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "&lt;div&gt; (shown as text)"
    CONTEXT: entity-encoded, displayed as text, not as a tag
    EXPECTED: INFO
    RISK: NONE
    GUARD: LESS_THAN_FORM ≠ ENCODED_SAFETY_PROOF
  SAFE_CASE_005:
    INPUT: "x <= y"
    CONTEXT: "less-than-or-equal" operator
    EXPECTED: INFO
    RISK: NONE
    GUARD: LESS_THAN_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "a < b and b < c"
    CONTEXT: a chain of comparisons
    EXPECTED: INFO
    RISK: NONE
    GUARD: LESS_THAN_FORM ≠ COMPARISON_ONLY_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: XSS_SCRIPT_TAG
    INPUT: "<script>alert(document.cookie)</script>"
    CONTEXT: user input placed into HTML without escaping
    RISK: CRITICAL
    ATTACK: "<" opens the <script> tag; the browser executes it as code (XSS)
    GUARD: LESS_THAN_FORM ≠ HTML_CONTEXT_SAFETY_PROOF
  RISK_CASE_002:
    NAME: XSS_EVENT_HANDLER
    INPUT: "<img src=x onerror=alert(1)>"
    CONTEXT: a tag with an event handler
    RISK: CRITICAL
    ATTACK: "<img …onerror>" runs JS without <script>
    GUARD: LESS_THAN_FORM ≠ SANITIZED_PROOF
  RISK_CASE_003:
    NAME: XSS_SVG_ONLOAD
    INPUT: "<svg onload=alert(1)>"
    CONTEXT: an SVG tag with onload
    RISK: HIGH
    ATTACK: <svg onload> bypasses filters that only look for <script>
    GUARD: LESS_THAN_FORM ≠ TAG_SAFETY_PROOF
  RISK_CASE_004:
    NAME: ENCODED_TAG_BYPASS
    INPUT: "&lt;script&gt; (with a later double decode)"
    CONTEXT: an encoded tag decoded back before output
    RISK: HIGH
    ATTACK: &lt; decodes to "<" AFTER the check → the tag comes alive
    GUARD: LESS_THAN_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: ATTRIBUTE_BREAKOUT
    INPUT: 'value"><script>…'
    CONTEXT: breaking out of an attribute via ">" and opening a new tag "<"
    RISK: CRITICAL
    ATTACK: closing the attribute/tag and "<script>" injects a new tag
    GUARD: LESS_THAN_FORM ≠ OUTPUT_CONTEXT_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_LT_BYPASS
    INPUT: "＜script＞ (fullwidth ＜ U+FF1C)"
    CONTEXT: an angle look-alike to bypass a tag filter
    RISK: MEDIUM
    ATTACK: a filter looks for ASCII "<", a normalizer may fold ＜ to "<"
    GUARD: LESS_THAN_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ＜
    CODEPOINT: U+FF1C
    NAME: FULLWIDTH LESS-THAN SIGN
    RISK: HIGH
    RULE: FULLWIDTH_LESS_THAN ≠ LESS_THAN (bypasses a tag filter looking for ASCII "<")
  CONFUSABLE_002:
    VISIBLE_FORM: ‹
    CODEPOINT: U+2039
    NAME: SINGLE LEFT-POINTING ANGLE QUOTATION MARK
    RISK: MEDIUM
    RULE: SINGLE_LEFT_ANGLE_QUOTE ≠ LESS_THAN
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨
    CODEPOINT: U+27E8
    NAME: MATHEMATICAL LEFT ANGLE BRACKET
    RISK: LOW
    RULE: MATH_LEFT_ANGLE ≠ LESS_THAN
  CONFUSABLE_004:
    VISIBLE_FORM: 〈
    CODEPOINT: U+3008
    NAME: LEFT ANGLE BRACKET
    RISK: LOW
    RULE: CJK_LEFT_ANGLE ≠ LESS_THAN
  CONFUSABLE_005:
    VISIBLE_FORM: ˂
    CODEPOINT: U+02C2
    NAME: MODIFIER LETTER LEFT ARROWHEAD
    RISK: LOW
    RULE: LEFT_ARROWHEAD ≠ LESS_THAN

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "since the input reached output, '<' is already safe"
    RESPONSE: LESS_THAN_FORM ≠ HTML_CONTEXT_SAFETY_PROOF
    RULE: safety depends on the output context; escape per context (HTML/attribute/JS)
  CG2:
    TRIGGER: "'<' is always a comparison"
    RESPONSE: LESS_THAN_FORM ≠ COMPARISON_ONLY_PROOF
    RULE: in an HTML context "<" opens a tag, not a comparison
  CG3:
    TRIGGER: "a filter on '<script>' catches all XSS"
    RESPONSE: LESS_THAN_FORM ≠ TAG_SAFETY_PROOF
    RULE: <img onerror>, <svg onload> run JS without <script>
  CG4:
    TRIGGER: "'&lt;' is safe forever"
    RESPONSE: LESS_THAN_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the entity may be decoded back to "<" before output
  CG5:
    TRIGGER: "an ASCII '<' filter catches all angles"
    RESPONSE: LESS_THAN_FORM ≠ EFFECT
    RULE: fullwidth ＜ (U+FF1C) is a different codepoint
  CG6:
    TRIGGER: "the presence of '<' means the input is sanitized"
    RESPONSE: LESS_THAN_FORM ≠ SANITIZED_PROOF
    RULE: the presence of the sign says nothing about sanitization

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "<script"
      NAME: SCRIPT_TAG_OPEN
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: opening an executable tag; classic XSS
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "</"
      NAME: TAG_CLOSE
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: closing a tag; breaking out of a text context (</textarea> etc.)
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "<!--"
      NAME: HTML_COMMENT_OPEN
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: opening a comment; conditional comments / parser manipulation
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with "<" are central to markup/XSS.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "<" masks/opens markup STRUCTURE (a tag) but does not imitate the existence of a verified entity (brand/account). Its risks are injection/execution, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of ASCII "<" with fullwidth ＜ (U+FF1C) to bypass a tag filter
  A2: mixing "<" with ‹ (U+2039) in a filter
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: <script>/<img onerror> in an HTML context (XSS)
  B2: attribute breakout value"><script>
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "<script" (SC1) as opening an executable tag
  C2: "</textarea>" to break out of a text context
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: <svg onload> bypasses a filter that only looks for <script>
  D2: "&lt;script&gt;" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: tag injection into a template
  E2: N/A — vector: sanitizer bypass via the ＜ look-alike
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: since the input reached output, "<" is already safe
  EXPECTED: FAIL_OUTPUT_CONTEXT_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: "<" is always a comparison
  EXPECTED: FAIL_COMPARISON_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: a filter on "<script>" catches all XSS
  EXPECTED: FAIL_TAG_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "&lt;" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: an ASCII "<" filter catches all angle look-alikes
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: the presence of "<" proves the input was sanitized
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to escape "<" per output context (HTML text/attribute/JS/URL) without false positives on comparison?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (context-aware output escaping is an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "the safety of '<' is decided by the output context".
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
