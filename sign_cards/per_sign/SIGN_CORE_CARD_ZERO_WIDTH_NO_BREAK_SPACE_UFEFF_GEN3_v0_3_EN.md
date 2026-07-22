PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_ZERO_WIDTH_NO_BREAK_SPACE_UFEFF_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_ZERO_WIDTH_NO_BREAK_SPACE_UFEFF_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_ZERO_WIDTH_NO_BREAK_SPACE_UFEFF_GEN3_v0_3_EN
CODEPOINT: U+FEFF
VISIBLE_FORM: ⟨ZWNBSP/BOM⟩
UNICODE_NAME: ZERO WIDTH NO-BREAK SPACE
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: zero width no-break space / byte order mark (position-dependent dual role)
CATEGORY_ROADMAP: LLM (invisible zero-width injection, encoding confusion) · PHAGO: — (token / encoding masking)
GLYPH_NOTE: VISIBLE_FORM uses the marker ⟨ZWNBSP/BOM⟩; the sign itself (U+FEFF) is an invisible Format char (Cf) and is NEVER written literally here — a literal leading U+FEFF would be treated as this file's BOM. Examples use ⟨BOM⟩/%EF%BB%BF, never the byte.

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
VISIBLE_FORM: ⟨ZWNBSP/BOM⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: BOM_FORM ≠ EFFECT
SIGN_CATEGORY:
  - invisible Format char with a POSITION-DEPENDENT dual role
  - at the start of a stream: a Byte Order Mark (signals encoding/endianness), usually stripped
  - mid-stream: a zero width no-break space (deprecated for that use; WJ is the modern replacement)
  - (misused) invisible interior char / encoding-detection confusion / invisible glue that a BOM-strip misses mid-stream

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — being non-printing does not make it inert
  2. NOT_ALWAYS_A_BOM — only a LEADING U+FEFF is a BOM; mid-stream it is a zero-width no-break space, not metadata
  3. NOT_ALWAYS_STRIPPED — a strip that removes only a leading BOM leaves interior U+FEFF in place
  4. NOT_ENCODING_TRUTH — a BOM is a hint, not proof; it can lie about or mismatch the actual encoding
  5. NOT_ENCODED_SAFE — "%EF%BB%BF" may be decoded back to the U+FEFF later
  6. NOT_AUTHORITY — it does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; it deceives filters and encoding logic
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_WJ — for the no-break job it is superseded by U+2060; treating them as interchangeable misses one
  10. NOT_SANITIZED_PROOF — the presence of the char does not mean the input is sanitized
  11. NOT_SINGLE_TOKEN_PROOF — an interior U+FEFF can split a keyword while looking like nothing

BASE_FORMULAS:
  BOM_FORM ≠ EFFECT
  BOM_FORM ≠ ALWAYS_A_BOM_PROOF
  BOM_FORM ≠ ALWAYS_STRIPPED_PROOF
  BOM_FORM ≠ ENCODING_TRUTH_PROOF
  BOM_FORM ≠ ENCODED_SAFETY_PROOF
  BOM_FORM ≠ AUTHORITY
  BOM_FORM ≠ EXECUTION_TRIGGER
  BOM_FORM ≠ WJ_EQUIVALENCE_PROOF
  BOM_FORM ≠ INVISIBLE_HARMLESS_PROOF
  BOM_FORM ≠ SANITIZED_PROOF
  BOM_FORM ≠ SINGLE_TOKEN_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: U+FEFF (ZONE_1) has parallel functions (leading BOM metadata vs. interior no-break space vs. invisible injection) co-existing without cultural precession. Its meaning is position-dependent, not epoch-dependent.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: an encoding/no-break control with no gestural predecessor; the interior-injection and encoding-confusion misuse is layered on by the digital epoch in parallel with legitimate BOM use.

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
    INPUT: "U+FEFF is the byte order mark"
    CONTEXT: naming the char in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: BOM_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "a leading BOM signals encoding"
    CONTEXT: describing the legitimate leading role in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: BOM_FORM ≠ ENCODING_TRUTH_PROOF
  SAFE_CASE_003:
    INPUT: "the marker is written as <BOM> here"
    CONTEXT: a documentation marker, not the byte
    EXPECTED: INFO
    RISK: NONE
    GUARD: BOM_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "mid-stream it is a zero width no-break space"
    CONTEXT: describing the position-dependent role in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: BOM_FORM ≠ ALWAYS_A_BOM_PROOF
  SAFE_CASE_005:
    INPUT: "WJ is the modern replacement for the no-break use"
    CONTEXT: describing the deprecation in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: BOM_FORM ≠ WJ_EQUIVALENCE_PROOF
  SAFE_CASE_006:
    INPUT: "a leading BOM is usually stripped on read"
    CONTEXT: describing normal handling in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: BOM_FORM ≠ ALWAYS_STRIPPED_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: INTERIOR_BOM_SURVIVES_STRIP
    INPUT: "text with a mid-stream U+FEFF after a leading-BOM strip"
    CONTEXT: a strip that removes only the leading BOM, leaving interior copies
    RISK: HIGH
    ATTACK: the interior U+FEFF acts as invisible glue/splitter the sanitizer never touched
    GUARD: BOM_FORM ≠ ALWAYS_STRIPPED_PROOF
  RISK_CASE_002:
    NAME: KEYWORD_SPLIT
    INPUT: "jav<BOM>ascript: in a URL scheme check"
    CONTEXT: an interior U+FEFF splitting a keyword so a substring blocklist fails to match
    RISK: HIGH
    ATTACK: the blocklist misses "javascript" while a lenient parser ignores the U+FEFF
    GUARD: BOM_FORM ≠ SINGLE_TOKEN_PROOF
  RISK_CASE_003:
    NAME: ENCODING_MISDETECTION
    INPUT: "a BOM that does not match the actual byte encoding"
    CONTEXT: a lying/mismatched BOM steering encoding detection wrong
    RISK: MEDIUM
    ATTACK: the decoder trusts the BOM hint and mis-decodes the payload, changing its meaning
    GUARD: BOM_FORM ≠ ENCODING_TRUTH_PROOF
  RISK_CASE_004:
    NAME: ENCODED_BOM_BYPASS
    INPUT: "value%EF%BB%BFtail (with a later decode)"
    CONTEXT: a percent-encoded U+FEFF decoded back before use
    RISK: HIGH
    ATTACK: "%EF%BB%BF" decodes to the U+FEFF AFTER a check → hidden split reappears
    GUARD: BOM_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: WJ_CONFLATION_GAP
    INPUT: "a filter handling U+FEFF but not U+2060 (or vice versa)"
    CONTEXT: treating the no-break pair as one, missing the other
    RISK: MEDIUM
    ATTACK: a rule tuned for the BOM misses WJ, so the invisible glue survives
    GUARD: BOM_FORM ≠ WJ_EQUIVALENCE_PROOF
  RISK_CASE_006:
    NAME: HOMOGLYPH_STACK
    INPUT: "раy<BOM>раl (invisible char + confusable letters combined)"
    CONTEXT: an interior U+FEFF stacked with confusable letters to deepen a spoof
    RISK: MEDIUM
    ATTACK: the invisible char plus look-alike letters make a hostile string pass a shallow review
    GUARD: BOM_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨WJ⟩
    CODEPOINT: U+2060
    NAME: WORD JOINER
    RISK: HIGH
    RULE: WORD_JOINER ≠ ZERO_WIDTH_NO_BREAK_SPACE (same no-break job, but WJ is the non-BOM modern form; U+FEFF doubles as a BOM)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨ZWSP⟩
    CODEPOINT: U+200B
    NAME: ZERO WIDTH SPACE
    RISK: HIGH
    RULE: ZERO_WIDTH_SPACE ≠ ZERO_WIDTH_NO_BREAK_SPACE (ZWSP allows a break; U+FEFF forbids one and can be a BOM)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨NBSP⟩
    CODEPOINT: U+00A0
    NAME: NO-BREAK SPACE
    RISK: MEDIUM
    RULE: NO_BREAK_SPACE ≠ ZERO_WIDTH_NO_BREAK_SPACE (NBSP is a visible-advance space; U+FEFF is zero-width and BOM-capable)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨ZWJ⟩
    CODEPOINT: U+200D
    NAME: ZERO WIDTH JOINER
    RISK: LOW
    RULE: ZERO_WIDTH_JOINER ≠ ZERO_WIDTH_NO_BREAK_SPACE (ZWJ combines glyphs; U+FEFF is a no-break space / BOM)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨MVS⟩
    CODEPOINT: U+180E
    NAME: MONGOLIAN VOWEL SEPARATOR
    RISK: LOW
    RULE: MONGOLIAN_VOWEL_SEPARATOR ≠ ZERO_WIDTH_NO_BREAK_SPACE (historically treated as a zero-width space; another invisible format char a BOM-tuned filter overlooks)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "a U+FEFF is always a BOM, so it is metadata"
    RESPONSE: BOM_FORM ≠ ALWAYS_A_BOM_PROOF
    RULE: only a leading U+FEFF is a BOM; mid-stream it is a no-break space in the data
  CG2:
    TRIGGER: "an invisible char cannot be dangerous"
    RESPONSE: BOM_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: invisibility is orthogonal to effect; interior U+FEFF drives filter and encoding desync
  CG3:
    TRIGGER: "we strip the BOM, so U+FEFF is gone"
    RESPONSE: BOM_FORM ≠ ALWAYS_STRIPPED_PROOF
    RULE: a leading-BOM strip leaves interior U+FEFF untouched
  CG4:
    TRIGGER: "'%EF%BB%BF' is safe forever"
    RESPONSE: BOM_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to the U+FEFF before use
  CG5:
    TRIGGER: "the BOM tells us the encoding for sure"
    RESPONSE: BOM_FORM ≠ ENCODING_TRUTH_PROOF
    RULE: a BOM is a hint that can lie or mismatch the actual bytes
  CG6:
    TRIGGER: "U+FEFF and U+2060 are the same no-break char"
    RESPONSE: BOM_FORM ≠ WJ_EQUIVALENCE_PROOF
    RULE: WJ is the non-BOM modern form; handling one is not handling the other

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "leading U+FEFF then payload"
      NAME: BOM_PREFIX
      RISK_LEVEL: LOW
      POSSIBLE_CONTEXTS: a legitimate/expected BOM that should be stripped once on read
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "interior U+FEFF inside a token"
      NAME: INTERIOR_GLUE
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: an interior U+FEFF splitting a keyword after a leading-BOM strip
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "U+FEFF + confusable letters"
      NAME: INVISIBLE_HOMOGLYPH_STACK
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: an invisible char combined with look-alike letters for a spoof
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — position within the sequence is exactly what decides U+FEFF's meaning.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: U+FEFF masks tokens and confuses encoding (token/encoding masking), but does not imitate the existence of a verified entity. Its risks are filter/encoding desync, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of U+FEFF with WJ (U+2060) / ZWSP (U+200B) to vary the invisible byte / evade a BOM-only filter
  A2: percent-encoding "%EF%BB%BF" to slip past a raw-byte scan
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: interior U+FEFF surviving a leading-BOM strip and splitting a keyword
  B2: encoding misdetection via a lying/mismatched BOM
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "interior U+FEFF inside a token" (SC2) — interior glue
  C2: "U+FEFF + confusable letters" (SC3) — invisible homoglyph stack
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: interior U+FEFF presented as "just a harmless BOM" so it is ignored, then abused mid-stream
  D2: "%EF%BB%BF" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: invisible identifier/keyword confusion via interior U+FEFF
  E2: N/A — vector: no-break-pair conflation (U+FEFF vs U+2060) leaving one unhandled
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: a U+FEFF is always a BOM
  EXPECTED: FAIL_ALWAYS_A_BOM_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: an invisible char cannot be dangerous
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: stripping the leading BOM removes every U+FEFF
  EXPECTED: FAIL_ALWAYS_STRIPPED_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%EF%BB%BF" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: the BOM proves the encoding
  EXPECTED: FAIL_ENCODING_TRUTH_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: U+FEFF and U+2060 are interchangeable
  EXPECTED: FAIL_WJ_EQUIVALENCE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to strip a leading BOM once for encoding while still catching interior U+FEFF as an invisible injector, and to treat the BOM as an untrusted encoding hint rather than proof?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (a reader that consumes at most one leading BOM, flags/rejects interior U+FEFF, and validates the declared vs. detected encoding — an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "U+FEFF's meaning is position-dependent: leading = BOM hint (not truth), interior = invisible no-break space a BOM-strip misses".
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
