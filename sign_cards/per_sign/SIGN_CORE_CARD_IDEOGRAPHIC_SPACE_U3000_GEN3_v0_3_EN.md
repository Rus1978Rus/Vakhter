PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_IDEOGRAPHIC_SPACE_U3000_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_IDEOGRAPHIC_SPACE_U3000_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_IDEOGRAPHIC_SPACE_U3000_GEN3_v0_3_EN
CODEPOINT: U+3000
VISIBLE_FORM: ⟨IDSP⟩
UNICODE_NAME: IDEOGRAPHIC SPACE
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: ideographic space / a full-width CJK space that is not U+0020 (space-family evasion)
CATEGORY_ROADMAP: LLM (space-homoglyph injection) · PHAGO: — (separator masking)
GLYPH_NOTE: VISIBLE_FORM uses the marker ⟨IDSP⟩; the sign itself (U+3000) has a wide VISIBLE advance (a full-width space) and is NOT written literally here — a literal U+3000 would masquerade as spacing in this document. Examples use ⟨IDSP⟩/%E3%80%80, never the byte.

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
VISIBLE_FORM: ⟨IDSP⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: IDSP_FORM ≠ EFFECT
SIGN_CATEGORY:
  - a full-width (em-wide) space used in CJK typography
  - legitimate use: spacing/alignment in CJK text and forms
  - looks like generous spacing but is U+3000, NOT U+0020 (a space homoglyph, breakable)
  - (misused) evades a whitespace check keyed on 0x20, and slips past a filter tuned only for U+00A0 / U+202F

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_ORDINARY_SPACE — it renders as wide spacing but is a different codepoint (U+3000 ≠ U+0020)
  2. NOT_ASCII_TRIMMED — an ASCII-only trim/strip keyed on 0x20 leaves U+3000 in place
  3. NOT_WHITESPACE_TO_EVERY_CHECK — a check testing only for 0x20 does not see it as whitespace
  4. NOT_SEPARATOR_GUARANTEE — a tokenizer splitting on U+0020 will not split on U+3000, so two "words" stay one token
  5. NOT_ENCODED_SAFE — "%E3%80%80" may be decoded back to the U+3000 later
  6. NOT_AUTHORITY — it does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; it deceives whitespace logic
  8. NOT_SINGLE_SPACE_FAMILY_MEMBER — it is one of a wider Unicode space family (U+00A0/U+202F/U+2000-200A/U+205F); filtering it alone misses the rest
  9. NOT_ZERO_WIDTH — it has a wide visible advance; it hides by looking like ordinary spacing, not by being invisible
  10. NOT_SANITIZED_PROOF — the presence of the char does not mean the input is sanitized
  11. NOT_EQUAL_STRING_PROOF — two strings that look the same may differ by a hidden U+3000

BASE_FORMULAS:
  IDSP_FORM ≠ EFFECT
  IDSP_FORM ≠ ORDINARY_SPACE_PROOF
  IDSP_FORM ≠ ASCII_TRIMMED_PROOF
  IDSP_FORM ≠ WHITESPACE_TO_EVERY_CHECK_PROOF
  IDSP_FORM ≠ SEPARATOR_GUARANTEE_PROOF
  IDSP_FORM ≠ ENCODED_SAFETY_PROOF
  IDSP_FORM ≠ AUTHORITY
  IDSP_FORM ≠ EXECUTION_TRIGGER
  IDSP_FORM ≠ SINGLE_SPACE_FAMILY_MEMBER_PROOF
  IDSP_FORM ≠ ZERO_WIDTH_PROOF
  IDSP_FORM ≠ SANITIZED_PROOF
  IDSP_FORM ≠ EQUAL_STRING_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: IDSP (ZONE_1) has parallel functions (legitimate CJK spacing vs. space-homoglyph evasion) co-existing without cultural precession. Polysemy of a stable space char.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a full-width space with a real typographic role but no gestural predecessor; the whitespace-evasion misuse is layered on by the digital epoch in parallel with legitimate CJK use.

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
    INPUT: "IDSP is U+3000 in Unicode"
    CONTEXT: naming the char in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: IDSP_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "an ideographic space is used for CJK spacing"
    CONTEXT: describing legitimate typography in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: IDSP_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <IDSP> here"
    CONTEXT: a documentation marker, not the byte
    EXPECTED: INFO
    RISK: NONE
    GUARD: IDSP_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "it looks like wide spacing but is a different codepoint"
    CONTEXT: describing the homoglyph property in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: IDSP_FORM ≠ ORDINARY_SPACE_PROOF
  SAFE_CASE_005:
    INPUT: "it is one of a wider Unicode space family"
    CONTEXT: describing the space family in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: IDSP_FORM ≠ SINGLE_SPACE_FAMILY_MEMBER_PROOF
  SAFE_CASE_006:
    INPUT: "a Unicode-aware normalizer can fold it"
    CONTEXT: describing careful sanitization in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: IDSP_FORM ≠ ASCII_TRIMMED_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: ASCII_ONLY_FILTER_GAP
    INPUT: "input using U+3000 where a filter only handles U+0020 / U+00A0"
    CONTEXT: a full-width space slipping past an ASCII/NBSP-only normalizer
    RISK: HIGH
    ATTACK: the filter handles common spaces but not U+3000, so the space-homoglyph survives
    GUARD: IDSP_FORM ≠ SINGLE_SPACE_FAMILY_MEMBER_PROOF
  RISK_CASE_002:
    NAME: TRIM_SURVIVAL
    INPUT: "admin<IDSP> submitted where admin is expected"
    CONTEXT: a trailing U+3000 surviving an ASCII-only trim, so the value differs
    RISK: HIGH
    ATTACK: "admin<IDSP>" is stored/compared as distinct from "admin" for impersonation or a duplicate
    GUARD: IDSP_FORM ≠ EQUAL_STRING_PROOF
  RISK_CASE_003:
    NAME: TOKENIZER_SPLIT_EVASION
    INPUT: "drop<IDSP>table joined by a full-width space"
    CONTEXT: a split-on-U+0020 tokenizer keeping two words as one token
    RISK: MEDIUM
    ATTACK: two keywords look separated but tokenize as one, defeating a word-boundary rule
    GUARD: IDSP_FORM ≠ SEPARATOR_GUARANTEE_PROOF
  RISK_CASE_004:
    NAME: ENCODED_IDSP_BYPASS
    INPUT: "value%E3%80%80tail (with a later decode)"
    CONTEXT: a percent-encoded U+3000 decoded back before use
    RISK: HIGH
    ATTACK: "%E3%80%80" decodes to the U+3000 AFTER a check → the space-homoglyph reappears
    GUARD: IDSP_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: WHITESPACE_CHECK_EVASION
    INPUT: "a required field filled with only U+3000"
    CONTEXT: an 'is-blank' check keyed on 0x20 seeing the field as non-empty
    RISK: MEDIUM
    ATTACK: the field passes a non-empty check yet displays as blank, or vice versa
    GUARD: IDSP_FORM ≠ WHITESPACE_TO_EVERY_CHECK_PROOF
  RISK_CASE_006:
    NAME: SPACE_FAMILY_MIX
    INPUT: "input mixing U+3000 with U+00A0 / U+202F / U+2009"
    CONTEXT: several space-family codepoints combined to defeat a single-codepoint filter
    RISK: MEDIUM
    ATTACK: handling one space codepoint at a time misses the wider Unicode space family
    GUARD: IDSP_FORM ≠ ORDINARY_SPACE_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨SP⟩
    CODEPOINT: U+0020
    NAME: SPACE
    RISK: HIGH
    RULE: SPACE ≠ IDEOGRAPHIC_SPACE (the ordinary ASCII space; U+3000 renders wider and is a different codepoint an ASCII check misses)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨NBSP⟩
    CODEPOINT: U+00A0
    NAME: NO-BREAK SPACE
    RISK: HIGH
    RULE: NO_BREAK_SPACE ≠ IDEOGRAPHIC_SPACE (a no-break space; U+3000 is breakable and full-width — a different space-family member)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨NNBSP⟩
    CODEPOINT: U+202F
    NAME: NARROW NO-BREAK SPACE
    RISK: MEDIUM
    RULE: NARROW_NO_BREAK_SPACE ≠ IDEOGRAPHIC_SPACE (a narrow no-break space; the opposite width, another family member)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨ENSP⟩
    CODEPOINT: U+2002
    NAME: EN SPACE
    RISK: MEDIUM
    RULE: EN_SPACE ≠ IDEOGRAPHIC_SPACE (a fixed-width en space; another visible space codepoint in the family)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨MMSP⟩
    CODEPOINT: U+205F
    NAME: MEDIUM MATHEMATICAL SPACE
    RISK: LOW
    RULE: MEDIUM_MATHEMATICAL_SPACE ≠ IDEOGRAPHIC_SPACE (a math-context space; yet another family member a single-codepoint filter misses)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "it looks like spacing, so it is a space"
    RESPONSE: IDSP_FORM ≠ ORDINARY_SPACE_PROOF
    RULE: it renders like wide spacing but is U+3000; equality and checks see a different byte
  CG2:
    TRIGGER: "trim removes trailing spaces, so it is gone"
    RESPONSE: IDSP_FORM ≠ ASCII_TRIMMED_PROOF
    RULE: an ASCII-only trim leaves U+3000 in place
  CG3:
    TRIGGER: "our whitespace check covers it"
    RESPONSE: IDSP_FORM ≠ WHITESPACE_TO_EVERY_CHECK_PROOF
    RULE: a 0x20-only check does not treat U+3000 as whitespace
  CG4:
    TRIGGER: "'%E3%80%80' is safe forever"
    RESPONSE: IDSP_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to the U+3000 before use
  CG5:
    TRIGGER: "the tokenizer will split it like a space"
    RESPONSE: IDSP_FORM ≠ SEPARATOR_GUARANTEE_PROOF
    RULE: a split-on-U+0020 tokenizer does not split on U+3000; two words stay one token
  CG6:
    TRIGGER: "we filter U+3000, so all lookalike spaces are handled"
    RESPONSE: IDSP_FORM ≠ SINGLE_SPACE_FAMILY_MEMBER_PROOF
    RULE: the Unicode space family (U+00A0/U+202F/U+2000-200A/U+205F …) is wider than U+3000 alone
  CG7:
    TRIGGER: "the two strings look the same, so they are equal"
    RESPONSE: IDSP_FORM ≠ EQUAL_STRING_PROOF
    RULE: visual sameness is not byte equality; a hidden U+3000 breaks equality

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "trailing U+3000 on a value"
      NAME: TRIM_SURVIVOR
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: a trailing full-width space surviving an ASCII trim and breaking equality
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "U+3000 between two keywords"
      NAME: NO_SPLIT_GLUE
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: two words kept as one token past a split-on-space rule
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "mixed Unicode spaces (U+3000 + U+00A0 + U+202F)"
      NAME: SPACE_FAMILY_MIX
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: several space-family codepoints combined to evade a single-codepoint filter
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — IDSP's risk is about how it sits within whitespace-sensitive sequences.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: IDSP masquerades as a separator (separator masking), but does not imitate the existence of a verified entity. Its risks are whitespace/equality desync, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of U+3000 with U+00A0 / U+202F / U+2002 to vary the space codepoint / evade a single-codepoint filter
  A2: percent-encoding "%E3%80%80" to slip past a raw-byte scan
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: ASCII/NBSP-only filter gap (U+3000 survives a fold that handles only common spaces)
  B2: trim survival (admin<IDSP> not equal to admin after an ASCII trim)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "U+3000 between two keywords" (SC2) — no-split glue
  C2: "mixed Unicode spaces" (SC3) — space-family mix past a single-codepoint filter
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: U+3000 presented as ordinary wide spacing so a reviewer treats it as harmless
  D2: "%E3%80%80" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: separator confusion (a space that does not split)
  E2: N/A — vector: single-codepoint filter missing the wider Unicode space family
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: an ideographic space is an ordinary space
  EXPECTED: FAIL_ORDINARY_SPACE_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: an ASCII trim removes U+3000
  EXPECTED: FAIL_ASCII_TRIMMED_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: every whitespace check treats U+3000 as whitespace
  EXPECTED: FAIL_WHITESPACE_TO_EVERY_CHECK_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E3%80%80" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: a split-on-space tokenizer splits U+3000
  EXPECTED: FAIL_SEPARATOR_GUARANTEE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: filtering U+3000 handles all lookalike spaces
  EXPECTED: FAIL_SINGLE_SPACE_FAMILY_MEMBER_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to normalize the whole Unicode space family (U+00A0, U+202F, U+2000-200A, U+205F, U+3000 …) to a canonical form before whitespace checks, trims, tokenizers and equality — without breaking legitimate CJK/typographic spacing where it matters?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (a Unicode-aware whitespace normalizer applied consistently before check, trim, tokenize and compare — an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "U+3000 looks like wide spacing but is not U+0020; an ASCII-only or single-codepoint filter misses it, and it is one of a wider space family".
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
