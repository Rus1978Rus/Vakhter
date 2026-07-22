PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_COMBINING_GRAPHEME_JOINER_U034F_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_COMBINING_GRAPHEME_JOINER_U034F_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_COMBINING_GRAPHEME_JOINER_U034F_GEN3_v0_3_EN
CODEPOINT: U+034F
VISIBLE_FORM: ⟨CGJ⟩
UNICODE_NAME: COMBINING GRAPHEME JOINER
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: combining grapheme joiner / an invisible COMBINING mark (Mn) that changes collation/matching
CATEGORY_ROADMAP: LLM (invisible combining-mark injection) · PHAGO: — (collation / equality masking)
GLYPH_NOTE: VISIBLE_FORM uses the marker ⟨CGJ⟩; the sign itself (U+034F) is an invisible COMBINING mark (category Mn, NOT Cf) and is NEVER written literally here — a literal CGJ would attach to the preceding character in this document. Examples use ⟨CGJ⟩/%CD%8F, never the byte.

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
VISIBLE_FORM: ⟨CGJ⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: CGJ_FORM ≠ EFFECT
SIGN_CATEGORY:
  - an invisible COMBINING mark (category Mn) with no glyph of its own
  - legitimate use: block a collation contraction, or keep a base + combining sequence treated as one grapheme
  - it affects collation/sort keys and can influence normalization grouping without any visible change
  - (misused) an invisible interior char that changes matching/collation/equality while looking identical, and that a Cf-only invisible scanner misses (it is Mn, not Cf)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — being non-printing does not make it inert
  2. NOT_A_FORMAT_CHAR — it is a COMBINING mark (Mn); a scanner that enumerates only Format chars (Cf) does not see it
  3. NOT_NO_EFFECT_ON_SORTING — it can block a collation contraction and change sort order / collation keys
  4. NOT_DISPLAY_ONLY — it has no glyph, but the byte carries through comparison, sorting and normalization
  5. NOT_ENCODED_SAFE — "%CD%8F" may be decoded back to the CGJ later
  6. NOT_AUTHORITY — it does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; it deceives comparison/collation logic
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_NORMALIZED_AWAY_PROOF — NFC/NFD do not remove it (it is not a compatibility char); presence does not mean it will be folded
  10. NOT_SANITIZED_PROOF — the presence of the char does not mean the input is sanitized
  11. NOT_EQUAL_STRING_PROOF — "admin" and "admin⟨CGJ⟩" look identical yet compare unequal

BASE_FORMULAS:
  CGJ_FORM ≠ EFFECT
  CGJ_FORM ≠ FORMAT_CHAR_PROOF
  CGJ_FORM ≠ NO_EFFECT_ON_SORTING_PROOF
  CGJ_FORM ≠ DISPLAY_ONLY_PROOF
  CGJ_FORM ≠ ENCODED_SAFETY_PROOF
  CGJ_FORM ≠ AUTHORITY
  CGJ_FORM ≠ EXECUTION_TRIGGER
  CGJ_FORM ≠ NORMALIZED_AWAY_PROOF
  CGJ_FORM ≠ INVISIBLE_HARMLESS_PROOF
  CGJ_FORM ≠ SANITIZED_PROOF
  CGJ_FORM ≠ EQUAL_STRING_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: CGJ (ZONE_1) has parallel functions (legitimate collation/grapheme control vs. invisible equality/collation injection) co-existing without cultural precession. Polysemy of a stable combining mark.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a glyphless combining-control with no gestural predecessor; the equality/collation-injection misuse is layered on by the digital epoch in parallel with legitimate collation use.

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
    INPUT: "CGJ is U+034F in Unicode"
    CONTEXT: naming the char in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: CGJ_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "a combining grapheme joiner can block a collation contraction"
    CONTEXT: describing the legitimate function in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: CGJ_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <CGJ> here"
    CONTEXT: a documentation marker, not the byte
    EXPECTED: INFO
    RISK: NONE
    GUARD: CGJ_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "it is a combining mark, not a format character"
    CONTEXT: describing its Unicode category in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: CGJ_FORM ≠ FORMAT_CHAR_PROOF
  SAFE_CASE_005:
    INPUT: "normalization does not remove it"
    CONTEXT: describing NFC/NFD behaviour in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: CGJ_FORM ≠ NORMALIZED_AWAY_PROOF
  SAFE_CASE_006:
    INPUT: "it has no glyph of its own"
    CONTEXT: describing its rendering in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: CGJ_FORM ≠ DISPLAY_ONLY_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: EQUALITY_BYPASS
    INPUT: "admin<CGJ> registered where admin is expected"
    CONTEXT: an invisible combining mark making two identifiers compare unequal while looking identical
    RISK: HIGH
    ATTACK: "admin<CGJ>" passes a uniqueness check as distinct from "admin" for impersonation or a duplicate
    GUARD: CGJ_FORM ≠ EQUAL_STRING_PROOF
  RISK_CASE_002:
    NAME: CF_ONLY_SCANNER_GAP
    INPUT: "input passing a scanner that enumerates only Format (Cf) invisibles"
    CONTEXT: a CGJ slipping past a filter that only looks at Cf format chars
    RISK: HIGH
    ATTACK: CGJ is category Mn, outside a Cf-only invisible sweep, so it survives
    GUARD: CGJ_FORM ≠ FORMAT_CHAR_PROOF
  RISK_CASE_003:
    NAME: COLLATION_ORDER_SHIFT
    INPUT: "a CGJ inserted to block a collation contraction"
    CONTEXT: a CGJ changing the sort key so an entry orders differently than expected
    RISK: MEDIUM
    ATTACK: the invisible mark shifts collation, hiding an entry from a range query or ordering it out of view
    GUARD: CGJ_FORM ≠ NO_EFFECT_ON_SORTING_PROOF
  RISK_CASE_004:
    NAME: ENCODED_CGJ_BYPASS
    INPUT: "value%CD%8Ftail (with a later decode)"
    CONTEXT: a percent-encoded CGJ decoded back before use
    RISK: HIGH
    ATTACK: "%CD%8F" decodes to the CGJ AFTER a check → the hidden mark reappears
    GUARD: CGJ_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: NORMALIZATION_ASSUMED_FOLD
    INPUT: "a pipeline assuming NFC removes the CGJ"
    CONTEXT: treating normalization as if it strips the combining joiner
    RISK: MEDIUM
    ATTACK: NFC/NFD keep the CGJ, so an assumed fold never happens and the mark persists
    GUARD: CGJ_FORM ≠ NORMALIZED_AWAY_PROOF
  RISK_CASE_006:
    NAME: INVISIBLE_HOMOGLYPH_STACK
    INPUT: "раy<CGJ>раl (combining mark + confusable letters combined)"
    CONTEXT: a CGJ stacked with confusable letters to deepen a spoof
    RISK: MEDIUM
    ATTACK: the invisible mark plus look-alike letters make a hostile string pass a shallow review
    GUARD: CGJ_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨ZWJ⟩
    CODEPOINT: U+200D
    NAME: ZERO WIDTH JOINER
    RISK: HIGH
    RULE: ZERO_WIDTH_JOINER ≠ COMBINING_GRAPHEME_JOINER ("joiner" in name only: ZWJ is a Cf format char joining glyphs; CGJ is an Mn combining mark affecting collation)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨ZWNJ⟩
    CODEPOINT: U+200C
    NAME: ZERO WIDTH NON-JOINER
    RISK: MEDIUM
    RULE: ZERO_WIDTH_NON_JOINER ≠ COMBINING_GRAPHEME_JOINER (a Cf joining control, not an Mn collation mark)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨ZWSP⟩
    CODEPOINT: U+200B
    NAME: ZERO WIDTH SPACE
    RISK: MEDIUM
    RULE: ZERO_WIDTH_SPACE ≠ COMBINING_GRAPHEME_JOINER (a Cf break opportunity, not a combining mark)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨COMBINING-ACUTE⟩
    CODEPOINT: U+0301
    NAME: COMBINING ACUTE ACCENT
    RISK: MEDIUM
    RULE: COMBINING_ACUTE_ACCENT ≠ COMBINING_GRAPHEME_JOINER (a VISIBLE combining accent in the same block; CGJ is glyphless)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨VS16⟩
    CODEPOINT: U+FE0F
    NAME: VARIATION SELECTOR-16
    RISK: LOW
    RULE: VARIATION_SELECTOR_16 ≠ COMBINING_GRAPHEME_JOINER (a variation selector requesting emoji presentation; a different invisible mechanism)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "our scanner covers the invisible format chars, so we are covered"
    RESPONSE: CGJ_FORM ≠ FORMAT_CHAR_PROOF
    RULE: CGJ is a combining mark (Mn), not a Format char (Cf); a Cf-only sweep misses it
  CG2:
    TRIGGER: "an invisible char cannot be dangerous"
    RESPONSE: CGJ_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: invisibility is orthogonal to effect; CGJ changes collation and equality
  CG3:
    TRIGGER: "it has no glyph, so it cannot change sorting"
    RESPONSE: CGJ_FORM ≠ NO_EFFECT_ON_SORTING_PROOF
    RULE: it blocks collation contractions and shifts sort keys
  CG4:
    TRIGGER: "'%CD%8F' is safe forever"
    RESPONSE: CGJ_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to the CGJ before use
  CG5:
    TRIGGER: "normalization strips it"
    RESPONSE: CGJ_FORM ≠ NORMALIZED_AWAY_PROOF
    RULE: NFC/NFD keep the CGJ; presence does not imply a fold
  CG6:
    TRIGGER: "the two strings look the same, so they are equal"
    RESPONSE: CGJ_FORM ≠ EQUAL_STRING_PROOF
    RULE: visual sameness is not byte equality; a hidden CGJ breaks equality

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "identifier with an interior CGJ"
      NAME: EQUALITY_SPLIT
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: a CGJ inside an ASCII identifier defeating a uniqueness/equality check
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "CGJ blocking a collation contraction"
      NAME: COLLATION_SHIFT
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: a CGJ shifting sort order to hide or misplace an entry
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "CGJ + confusable letters"
      NAME: INVISIBLE_HOMOGLYPH_STACK
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: a combining mark combined with look-alike letters for a spoof
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — CGJ's effect is on comparison/collation of the surrounding sequence.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: CGJ masks equality/collation (collation/equality masking), but does not imitate the existence of a verified entity. Its risks are comparison/sort desync, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of CGJ with ZWJ (U+200D) / ZWSP (U+200B) to vary the invisible char / evade a filter that models one category
  A2: percent-encoding "%CD%8F" to slip past a raw-byte scan
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: equality bypass (admin<CGJ> not equal to admin)
  B2: Cf-only scanner gap (an Mn combining mark survives a Format-char sweep)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "CGJ blocking a collation contraction" (SC2) — collation shift
  C2: "CGJ + confusable letters" (SC3) — invisible homoglyph stack
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: CGJ presented as a harmless "grapheme control" while it changes equality/collation
  D2: "%CD%8F" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: invisible identifier confusion (admin<CGJ> vs admin)
  E2: N/A — vector: normalization-assumed-fold leaving the mark in place
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: CGJ is a format character caught by a Cf sweep
  EXPECTED: FAIL_FORMAT_CHAR_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: an invisible char cannot be dangerous
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: a glyphless mark cannot change sorting
  EXPECTED: FAIL_NO_EFFECT_ON_SORTING_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%CD%8F" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: normalization removes the CGJ
  EXPECTED: FAIL_NORMALIZED_AWAY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: two strings that look the same are equal
  EXPECTED: FAIL_EQUAL_STRING_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to enumerate invisible characters by their actual effect (Default_Ignorable / combining / format), not by a single Unicode category, so an Mn mark like CGJ is caught alongside the Cf invisibles before equality/collation, without breaking legitimate combining sequences?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (a normalizer keyed on Default_Ignorable_Code_Point and combining properties, applied before compare/sort/uniqueness — an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "CGJ is an invisible combining mark (Mn), not a format char; it changes collation/equality and normalization does not remove it".
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
