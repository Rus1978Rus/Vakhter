PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_TAB_U0009_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_TAB_U0009_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_TAB_U0009_GEN3_v0_3_EN
CODEPOINT: U+0009
VISIBLE_FORM: ␉
UNICODE_NAME: <control> CHARACTER TABULATION (TAB)
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: tab / horizontal tabulation (non-printing)
CATEGORY_ROADMAP: INJ (whitespace-filter bypass, delimiter injection) · PHAGO: — (field boundary confusion)
GLYPH_NOTE: VISIBLE_FORM uses ␉ (U+2409 SYMBOL FOR HORIZONTAL TABULATION) as a printable picture; the sign itself (U+0009) is a non-printing control character.

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
VISIBLE_FORM: ␉
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: TAB_FORM ≠ EFFECT
SIGN_CATEGORY:
  - horizontal indentation / alignment whitespace
  - field separator in TSV and some log formats
  - token/word separator alongside space in shells (IFS)
  - structural whitespace in Makefiles / some config formats

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_WHITESPACE_ONLY — TAB is not always "just spacing" (it separates shell tokens/fields)
  2. NOT_SPACE_EQUIVALENT — a TAB is a different codepoint than a space; filters diverge
  3. NOT_INVISIBLE_MEANS_HARMLESS — being non-printing does not make it inert
  4. NOT_TRIM_PROOF — a "trimmed" value may still carry an inner TAB
  5. NOT_ENCODED_SAFE — "%09" / "\t" may be decoded back to TAB later
  6. NOT_AUTHORITY — TAB does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; context makes it separate
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_DELIMITER_SAFE — a TAB can inject an extra TSV/log field or split a token
  10. NOT_SANITIZED_PROOF — the presence of a TAB does not mean the input is sanitized
  11. NOT_OUTPUT_CONTEXT_PROOF — safety depends on the parse/format context

BASE_FORMULAS:
  TAB_FORM ≠ EFFECT
  TAB_FORM ≠ WHITESPACE_ONLY_PROOF
  TAB_FORM ≠ SPACE_EQUIVALENCE_PROOF
  TAB_FORM ≠ INVISIBLE_HARMLESS_PROOF
  TAB_FORM ≠ TRIM_SAFETY_PROOF
  TAB_FORM ≠ ENCODED_SAFETY_PROOF
  TAB_FORM ≠ AUTHORITY
  TAB_FORM ≠ EXECUTION_TRIGGER
  TAB_FORM ≠ DELIMITER_SAFETY_PROOF
  TAB_FORM ≠ SANITIZED_PROOF
  TAB_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: TAB (ZONE_1) has parallel functions (indentation, TSV separator, shell token separator, structural whitespace) co-existing without cultural precession. Polysemy of a stable control code.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a typewriter tab-stop control with no gestural predecessor; the separator/structure functions are layered on by the digital epoch in parallel.

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
    INPUT: "name\\tvalue"
    CONTEXT: a TAB shown as an escape in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: TAB_FORM ≠ WHITESPACE_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "use \\t to indent"
    CONTEXT: describing the escape sequence in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: TAB_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "col1\\tcol2\\tcol3"
    CONTEXT: a legitimate TSV header (as literal text)
    EXPECTED: INFO
    RISK: NONE
    GUARD: TAB_FORM ≠ DELIMITER_SAFETY_PROOF
  SAFE_CASE_004:
    INPUT: "TAB is 0x09 in ASCII"
    CONTEXT: naming the control code in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: TAB_FORM ≠ WHITESPACE_ONLY_PROOF
  SAFE_CASE_005:
    INPUT: "Makefiles require a \\t for recipe lines"
    CONTEXT: describing structural TAB usage
    EXPECTED: INFO
    RISK: NONE
    GUARD: TAB_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "aligned\\tcolumns in a report"
    CONTEXT: indentation/alignment in stored text
    EXPECTED: INFO
    RISK: NONE
    GUARD: TAB_FORM ≠ SPACE_EQUIVALENCE_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: TSV_FIELD_INJECTION
    INPUT: "user\\tadmin\\ttrue"
    CONTEXT: an injected TAB adding extra TSV columns
    RISK: HIGH
    ATTACK: TAB injects extra fields (role=admin) into a tab-delimited record
    GUARD: TAB_FORM ≠ DELIMITER_SAFETY_PROOF
  RISK_CASE_002:
    NAME: WHITESPACE_FILTER_BYPASS
    INPUT: "SELECT\\t*\\tFROM\\tusers"
    CONTEXT: a TAB substituted for spaces to bypass a keyword/space filter
    RISK: HIGH
    ATTACK: a filter that splits on space misses TAB-separated SQL keywords
    GUARD: TAB_FORM ≠ SPACE_EQUIVALENCE_PROOF
  RISK_CASE_003:
    NAME: SHELL_TOKEN_SPLIT
    INPUT: "cmd\\t/etc/passwd"
    CONTEXT: a TAB acting as an IFS separator to split an argument
    RISK: HIGH
    ATTACK: TAB (part of default IFS) splits a "single" argument into two tokens
    GUARD: TAB_FORM ≠ WHITESPACE_ONLY_PROOF
  RISK_CASE_004:
    NAME: LOG_COLUMN_FORGERY
    INPUT: "ip\\t200 OK\\tadmin-action"
    CONTEXT: an injected TAB forging extra log columns
    RISK: MEDIUM
    ATTACK: TAB adds attacker-controlled columns a log parser trusts
    GUARD: TAB_FORM ≠ DELIMITER_SAFETY_PROOF
  RISK_CASE_005:
    NAME: ENCODED_TAB_BYPASS
    INPUT: "cmd%09arg (with a later decode)"
    CONTEXT: an encoded TAB decoded back before the sink
    RISK: MEDIUM
    ATTACK: %09 decodes to TAB AFTER the check → token/field split
    GUARD: TAB_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: TRIM_BYPASS_INNER_TAB
    INPUT: "ad\\tmin (inner TAB survives an edge-trim)"
    CONTEXT: an inner TAB inside a value that outer trimming misses
    RISK: MEDIUM
    ATTACK: trimming edges leaves an inner TAB that later splits/normalizes to "admin"
    GUARD: TAB_FORM ≠ TRIM_SAFETY_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: " "
    CODEPOINT: U+0020
    NAME: SPACE
    RISK: HIGH
    RULE: SPACE ≠ TAB (a space-only filter misses TAB and vice versa; both are IFS separators)
  CONFUSABLE_002:
    VISIBLE_FORM: " "
    CODEPOINT: U+00A0
    NAME: NO-BREAK SPACE
    RISK: MEDIUM
    RULE: NO_BREAK_SPACE ≠ TAB (NBSP is whitespace some parsers treat differently)
  CONFUSABLE_003:
    VISIBLE_FORM: " "
    CODEPOINT: U+2003
    NAME: EM SPACE
    RISK: LOW
    RULE: EM_SPACE ≠ TAB (a Unicode space that may fold to a separator in some normalizers)
  CONFUSABLE_004:
    VISIBLE_FORM: ␋
    CODEPOINT: U+000B
    NAME: LINE TABULATION
    RISK: MEDIUM
    RULE: LINE_TABULATION ≠ TAB (VT is a vertical tab some tools treat as whitespace)
  CONFUSABLE_005:
    VISIBLE_FORM: "　"
    CODEPOINT: U+3000
    NAME: IDEOGRAPHIC SPACE
    RISK: LOW
    RULE: IDEOGRAPHIC_SPACE ≠ TAB (a wide space that may normalize to a separator)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "TAB is always just spacing"
    RESPONSE: TAB_FORM ≠ WHITESPACE_ONLY_PROOF
    RULE: in a shell/TSV a TAB separates tokens/fields
  CG2:
    TRIGGER: "a TAB is the same as a space"
    RESPONSE: TAB_FORM ≠ SPACE_EQUIVALENCE_PROOF
    RULE: they are different codepoints; a space-only filter misses TAB
  CG3:
    TRIGGER: "an invisible control char cannot be dangerous"
    RESPONSE: TAB_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: invisibility is orthogonal to effect; TAB drives field/token boundaries
  CG4:
    TRIGGER: "'%09' / '\\t' is safe forever"
    RESPONSE: TAB_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to TAB before the sink
  CG5:
    TRIGGER: "trimming a value removes the TAB"
    RESPONSE: TAB_FORM ≠ TRIM_SAFETY_PROOF
    RULE: edge-trimming leaves an inner TAB that can still split/inject
  CG6:
    TRIGGER: "the presence of a TAB means the input is sanitized"
    RESPONSE: TAB_FORM ≠ SANITIZED_PROOF
    RULE: the presence of the sign says nothing about sanitization

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "TAB + field"
      NAME: TSV_FIELD_INJECTION
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: a TAB adding an extra tab-delimited field
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "keyword TAB keyword"
      NAME: SPACE_FILTER_BYPASS
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: TAB replacing spaces to bypass a keyword/space filter
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "arg TAB arg"
      NAME: IFS_TOKEN_SPLIT
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: TAB in default IFS splitting one argument into two
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with TAB are central to delimiter/whitespace bypass.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: TAB separates fields/tokens or bypasses a whitespace filter, but does not imitate the existence of a verified entity. Its risks are delimiter/split, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of a space with TAB to bypass a space-based filter
  A2: substitution of TAB with NBSP (U+00A0) to confuse a whitespace normalizer
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: TSV field injection user\\tadmin\\ttrue
  B2: whitespace-filter bypass SELECT\\t*\\tFROM\\tusers
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "TAB + field" (SC1) — TSV field injection
  C2: "arg TAB arg" (SC3) — IFS token split
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: TAB presented as harmless indentation inside a delimited field
  D2: "%09" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: extra-field injection into a TSV importer
  E2: N/A — vector: TAB-token split into a shell argument
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: TAB is always just spacing
  EXPECTED: FAIL_WHITESPACE_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: a TAB is the same as a space
  EXPECTED: FAIL_SPACE_EQUIVALENCE_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: an invisible control char cannot be dangerous
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%09" / "\t" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: trimming a value removes the TAB
  EXPECTED: FAIL_TRIM_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: the presence of a TAB proves the input was sanitized
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to normalize TAB per format (TSV/shell/config) without false positives on legitimate indentation and alignment?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (strict field parsing + argument-vector exec + explicit whitespace normalization is an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "the safety of TAB is decided by the parse/format context".
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
