PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_WORD_JOINER_U2060_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_WORD_JOINER_U2060_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_WORD_JOINER_U2060_GEN3_v0_3_EN
CODEPOINT: U+2060
VISIBLE_FORM: ⟨WJ⟩
UNICODE_NAME: WORD JOINER
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: word joiner / invisible no-break glue (inverse of ZWSP; replacement for FEFF-as-ZWNBSP)
CATEGORY_ROADMAP: LLM (invisible zero-width injection) · PHAGO: — (token masking)
GLYPH_NOTE: VISIBLE_FORM uses the marker ⟨WJ⟩; the sign itself (U+2060) is an invisible Format char (Cf) with zero advance and is NEVER written literally here. Examples use ⟨WJ⟩/%E2%81%A0, never the byte. WJ forbids a line break at its position; it does NOT join glyphs like ZWJ.

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
VISIBLE_FORM: ⟨WJ⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: WJ_FORM ≠ EFFECT
SIGN_CATEGORY:
  - invisible zero-advance Format char that FORBIDS a line break at its position (a "glue")
  - the inverse of ZWSP: ZWSP allows a break, WJ prevents one
  - the recommended replacement for U+FEFF used as a zero-width no-break space
  - (misused) invisible glue inserted into an identifier/keyword to defeat matching, without a visible clue

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — being non-printing does not make it inert
  2. NOT_ZERO_WIDTH_MEANS_ABSENT — zero advance width does not mean the byte is not there
  3. NOT_ZWSP_INVERSE_MEANS_SAFE — being ZWSP's inverse (no-break vs break) does not make it harmless; it is still an invisible interior char
  4. NOT_A_GLYPH_JOINER — despite "joiner" in its name, it does NOT combine glyphs like ZWJ; it only forbids a break
  5. NOT_ENCODED_SAFE — "%E2%81%A0" may be decoded back to the WJ later
  6. NOT_AUTHORITY — it does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; it deceives filters and readers
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_BOM — U+2060 is not a byte-order mark; a filter keying only on U+FEFF misses it
  10. NOT_SANITIZED_PROOF — the presence of the char does not mean the input is sanitized
  11. NOT_SINGLE_TOKEN_PROOF — "ad⟨WJ⟩min" may render as "admin" yet compare unequal

BASE_FORMULAS:
  WJ_FORM ≠ EFFECT
  WJ_FORM ≠ ZERO_WIDTH_MEANS_ABSENT_PROOF
  WJ_FORM ≠ ZWSP_INVERSE_MEANS_SAFE_PROOF
  WJ_FORM ≠ GLYPH_JOINER_PROOF
  WJ_FORM ≠ ENCODED_SAFETY_PROOF
  WJ_FORM ≠ AUTHORITY
  WJ_FORM ≠ EXECUTION_TRIGGER
  WJ_FORM ≠ BOM_PROOF
  WJ_FORM ≠ INVISIBLE_HARMLESS_PROOF
  WJ_FORM ≠ SANITIZED_PROOF
  WJ_FORM ≠ SINGLE_TOKEN_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: WJ (ZONE_1) has parallel functions (legitimate no-break glue vs. invisible identifier-injection) co-existing without cultural precession. Polysemy of a stable Format char.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a line-break-suppression control with no gestural predecessor; the identifier-injection misuse is layered on by the digital epoch in parallel with legitimate no-break typography.

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
    INPUT: "WJ is U+2060 in Unicode"
    CONTEXT: naming the char in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: WJ_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "a word joiner forbids a line break at its position"
    CONTEXT: describing the no-break function in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: WJ_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <WJ> here"
    CONTEXT: a documentation marker, not the byte
    EXPECTED: INFO
    RISK: NONE
    GUARD: WJ_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "it replaces FEFF used as a no-break space"
    CONTEXT: describing the recommended modern use in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: WJ_FORM ≠ BOM_PROOF
  SAFE_CASE_005:
    INPUT: "it is the inverse of a zero width space"
    CONTEXT: distinguishing it from ZWSP in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: WJ_FORM ≠ ZWSP_INVERSE_MEANS_SAFE_PROOF
  SAFE_CASE_006:
    INPUT: "it does not combine glyphs the way a zero width joiner does"
    CONTEXT: distinguishing it from ZWJ in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: WJ_FORM ≠ GLYPH_JOINER_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: KEYWORD_SPLIT
    INPUT: "jav<WJ>ascript: in a URL scheme check"
    CONTEXT: a WJ splitting a keyword so a substring blocklist fails to match
    RISK: HIGH
    ATTACK: the blocklist misses "javascript" while a lenient parser ignores the WJ
    GUARD: WJ_FORM ≠ SINGLE_TOKEN_PROOF
  RISK_CASE_002:
    NAME: INVISIBLE_IN_IDENTIFIER
    INPUT: "ad<WJ>min vs admin (look-alike username)"
    CONTEXT: a WJ inside an ASCII identifier making it compare unequal while looking identical
    RISK: HIGH
    ATTACK: "ad<WJ>min" registers as a look-alike of "admin" for impersonation
    GUARD: WJ_FORM ≠ ZERO_WIDTH_MEANS_ABSENT_PROOF
  RISK_CASE_003:
    NAME: BOM_ONLY_FILTER_GAP
    INPUT: "input passing a filter that strips only U+FEFF"
    CONTEXT: a WJ slipping past a filter that only knows the BOM form
    RISK: MEDIUM
    ATTACK: a filter keyed on U+FEFF misses U+2060, so the invisible glue survives
    GUARD: WJ_FORM ≠ BOM_PROOF
  RISK_CASE_004:
    NAME: ENCODED_WJ_BYPASS
    INPUT: "value%E2%81%A0tail (with a later decode)"
    CONTEXT: a percent-encoded WJ decoded back before use
    RISK: HIGH
    ATTACK: "%E2%81%A0" decodes to the WJ AFTER a check → hidden split reappears
    GUARD: WJ_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: INVISIBLE_FAMILY_CONFLATION
    INPUT: "a filter treating WJ the same as ZWJ (both say 'joiner')"
    CONTEXT: a naive filter conflating names, mishandling WJ
    RISK: MEDIUM
    ATTACK: a rule assuming WJ joins glyphs mis-handles it; it actually only forbids a break
    GUARD: WJ_FORM ≠ GLYPH_JOINER_PROOF
  RISK_CASE_006:
    NAME: HOMOGLYPH_STACK
    INPUT: "раy<WJ>раl (invisible glue + confusable letters combined)"
    CONTEXT: a WJ stacked with confusable letters to deepen a spoof
    RISK: MEDIUM
    ATTACK: the invisible char plus look-alike letters make a hostile string pass a shallow review
    GUARD: WJ_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨ZWSP⟩
    CODEPOINT: U+200B
    NAME: ZERO WIDTH SPACE
    RISK: HIGH
    RULE: ZERO_WIDTH_SPACE ≠ WORD_JOINER (ZWSP allows a break; WJ forbids one — inverse semantics, both zero-width)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨ZWNBSP⟩
    CODEPOINT: U+FEFF
    NAME: ZERO WIDTH NO-BREAK SPACE
    RISK: HIGH
    RULE: ZERO_WIDTH_NO_BREAK_SPACE ≠ WORD_JOINER (same no-break job, but U+FEFF doubles as a BOM; WJ is the recommended non-BOM form)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨ZWJ⟩
    CODEPOINT: U+200D
    NAME: ZERO WIDTH JOINER
    RISK: MEDIUM
    RULE: ZERO_WIDTH_JOINER ≠ WORD_JOINER ("joiner" in name only: ZWJ combines glyphs, WJ forbids a break — different layers)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨NBSP⟩
    CODEPOINT: U+00A0
    NAME: NO-BREAK SPACE
    RISK: MEDIUM
    RULE: NO_BREAK_SPACE ≠ WORD_JOINER (NBSP is a visible-advance no-break space; WJ is zero-width)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨FA⟩
    CODEPOINT: U+2061
    NAME: FUNCTION APPLICATION
    RISK: LOW
    RULE: FUNCTION_APPLICATION ≠ WORD_JOINER (an invisible math operator next in the block; different purpose, both invisible)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "it has zero width, so it is effectively not there"
    RESPONSE: WJ_FORM ≠ ZERO_WIDTH_MEANS_ABSENT_PROOF
    RULE: zero advance width is a display metric; the byte is present in the data
  CG2:
    TRIGGER: "an invisible char cannot be dangerous"
    RESPONSE: WJ_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: invisibility is orthogonal to effect; WJ drives filter/identifier desync
  CG3:
    TRIGGER: "we already strip the BOM, so we are covered"
    RESPONSE: WJ_FORM ≠ BOM_PROOF
    RULE: WJ is U+2060, not U+FEFF; a BOM-only filter misses it
  CG4:
    TRIGGER: "'%E2%81%A0' is safe forever"
    RESPONSE: WJ_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to the WJ before use
  CG5:
    TRIGGER: "it is a joiner, so it combines glyphs like ZWJ"
    RESPONSE: WJ_FORM ≠ GLYPH_JOINER_PROOF
    RULE: WJ only forbids a line break; it does not combine glyphs
  CG6:
    TRIGGER: "the string looks like admin, so it is admin"
    RESPONSE: WJ_FORM ≠ SINGLE_TOKEN_PROOF
    RULE: display unity does not imply byte equality; an invisible char may hide inside

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "ASCII identifier with an interior WJ"
      NAME: SPLIT_IDENTIFIER
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: a WJ inside an ASCII name/keyword to defeat matching or impersonate
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "WJ where a BOM-only filter runs"
      NAME: BOM_ONLY_GAP
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: invisible glue surviving because only U+FEFF is stripped
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "WJ + confusable letters"
      NAME: INVISIBLE_HOMOGLYPH_STACK
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: an invisible char combined with look-alike letters for a spoof
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with WJ are central to invisible token gluing.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: WJ glues/masks tokens (token masking), but does not imitate the existence of a verified entity. Its risks are filter/parser desync and identifier confusion, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of WJ with ZWSP (U+200B) / ZWNBSP (U+FEFF) / NBSP (U+00A0) to vary the invisible byte / evade a WJ-only filter
  A2: percent-encoding "%E2%81%A0" to slip past a raw-byte scan
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: keyword split "jav<WJ>ascript:" defeating a substring blocklist
  B2: BOM-only filter gap (WJ survives a filter that strips only U+FEFF)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "ASCII identifier with an interior WJ" (SC1) — split identifier
  C2: "WJ + confusable letters" (SC3) — invisible homoglyph stack
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: WJ presented as a harmless "no-break glue" inside a hostile field
  D2: "%E2%81%A0" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: invisible identifier confusion (ad<WJ>min vs admin)
  E2: N/A — vector: name-based conflation with ZWJ mishandling WJ
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: zero width means the char is effectively absent
  EXPECTED: FAIL_ZERO_WIDTH_MEANS_ABSENT_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: an invisible char cannot be dangerous
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: stripping the BOM covers the word joiner too
  EXPECTED: FAIL_BOM_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E2%81%A0" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: a word joiner combines glyphs like a zero width joiner
  EXPECTED: FAIL_GLYPH_JOINER_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: a string that looks like admin is admin
  EXPECTED: FAIL_SINGLE_TOKEN_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to detect the whole invisible no-break/glue family (2060, FEFF, 00A0 and relatives) and enforce one normalization decision across filter and parser, without keying on U+FEFF alone?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (a normalizer covering the full invisible set — not just the BOM — deciding strip-or-reject once before both the check and the executor — an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "WJ is ZWSP's inverse and the non-BOM no-break form; a BOM-only filter misses it, and it is not a glyph joiner despite its name".
ALL_OPEN_QUESTIONS_CLOSED: NO (delegated, non-blocking)

============================================================
11. PATCH_HISTORY
============================================================
PATCH_HISTORY:
  v0_1_PATCH_01: initial creation (Ruslan Malyavsky, 2026-07-22) — draft from the GEN3_v0_3 template (Vakhter); not conveyor-run.
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
