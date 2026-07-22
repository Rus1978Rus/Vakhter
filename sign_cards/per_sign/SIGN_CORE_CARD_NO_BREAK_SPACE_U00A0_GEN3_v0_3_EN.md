PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_NO_BREAK_SPACE_U00A0_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_NO_BREAK_SPACE_U00A0_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_NO_BREAK_SPACE_U00A0_GEN3_v0_3_EN
CODEPOINT: U+00A0
VISIBLE_FORM: ⟨NBSP⟩
UNICODE_NAME: NO-BREAK SPACE
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: no-break space / a space that is not U+0020 (whitespace-check evasion)
CATEGORY_ROADMAP: LLM (space-homoglyph injection) · PHAGO: — (separator masking)
GLYPH_NOTE: VISIBLE_FORM uses the marker ⟨NBSP⟩; the sign itself (U+00A0) has a VISIBLE advance (it looks like a normal space) and is NOT written literally here — a literal U+00A0 would masquerade as an ordinary space in this document. Examples use ⟨NBSP⟩/%C2%A0, never the byte.

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
VISIBLE_FORM: ⟨NBSP⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: NBSP_FORM ≠ EFFECT
SIGN_CATEGORY:
  - a visible-advance space that FORBIDS a line break (keeps two words together)
  - legitimate typography (e.g. "10 kg", a name and title kept on one line)
  - looks like an ordinary space but is U+00A0, NOT U+0020 (a space homoglyph)
  - (misused) evades a whitespace check keyed on 0x20, defeats split-on-space tokenizers, survives a naive trim()

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_ORDINARY_SPACE — it renders like a space but is a different codepoint (U+00A0 ≠ U+0020)
  2. NOT_WHITESPACE_TO_EVERY_CHECK — a check testing only for 0x20 (or \t\n\r) does not see it as whitespace
  3. NOT_TRIMMED_BY_DEFAULT — many trim/strip routines keyed on ASCII whitespace leave U+00A0 in place
  4. NOT_SEPARATOR_GUARANTEE — a tokenizer splitting on U+0020 will not split on U+00A0, so two "words" stay one token
  5. NOT_ENCODED_SAFE — "%C2%A0" may be decoded back to the U+00A0 later
  6. NOT_AUTHORITY — it does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; it deceives whitespace logic
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_ZERO_WIDTH — unlike ZWSP/WJ it has a visible advance; it hides by looking normal, not by being invisible
  10. NOT_SANITIZED_PROOF — the presence of the char does not mean the input is sanitized
  11. NOT_EQUAL_STRING_PROOF — "admin " with a trailing U+00A0 is not equal to "admin" even after an ASCII trim

BASE_FORMULAS:
  NBSP_FORM ≠ EFFECT
  NBSP_FORM ≠ ORDINARY_SPACE_PROOF
  NBSP_FORM ≠ WHITESPACE_TO_EVERY_CHECK_PROOF
  NBSP_FORM ≠ TRIMMED_BY_DEFAULT_PROOF
  NBSP_FORM ≠ SEPARATOR_GUARANTEE_PROOF
  NBSP_FORM ≠ ENCODED_SAFETY_PROOF
  NBSP_FORM ≠ AUTHORITY
  NBSP_FORM ≠ EXECUTION_TRIGGER
  NBSP_FORM ≠ ZERO_WIDTH_PROOF
  NBSP_FORM ≠ SANITIZED_PROOF
  NBSP_FORM ≠ EQUAL_STRING_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: NBSP (ZONE_1) has parallel functions (legitimate no-break typography vs. space-homoglyph evasion) co-existing without cultural precession. Polysemy of a stable space char.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a no-break space with a real typographic role but no gestural predecessor; the whitespace-evasion misuse is layered on by the digital epoch in parallel with legitimate use.

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
    INPUT: "NBSP is U+00A0 in Unicode"
    CONTEXT: naming the char in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: NBSP_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "a no-break space keeps two words on one line"
    CONTEXT: describing legitimate typography in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: NBSP_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <NBSP> here"
    CONTEXT: a documentation marker, not the byte
    EXPECTED: INFO
    RISK: NONE
    GUARD: NBSP_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "it looks like a space but is a different codepoint"
    CONTEXT: describing the homoglyph property in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: NBSP_FORM ≠ ORDINARY_SPACE_PROOF
  SAFE_CASE_005:
    INPUT: "a Unicode-aware trim can normalize it"
    CONTEXT: describing careful sanitization in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: NBSP_FORM ≠ TRIMMED_BY_DEFAULT_PROOF
  SAFE_CASE_006:
    INPUT: "unlike a zero width space it has a visible advance"
    CONTEXT: distinguishing it from ZWSP in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: NBSP_FORM ≠ ZERO_WIDTH_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: WHITESPACE_CHECK_EVASION
    INPUT: "a required field filled with only U+00A0"
    CONTEXT: an 'is-blank' check keyed on 0x20 seeing the field as non-empty
    RISK: HIGH
    ATTACK: the field passes a non-empty check yet displays as blank, or vice versa
    GUARD: NBSP_FORM ≠ WHITESPACE_TO_EVERY_CHECK_PROOF
  RISK_CASE_002:
    NAME: TRIM_SURVIVAL
    INPUT: "admin<NBSP> submitted where admin is expected"
    CONTEXT: a trailing U+00A0 surviving an ASCII-only trim, so the value differs
    RISK: HIGH
    ATTACK: "admin<NBSP>" is stored/compared as distinct from "admin" for impersonation or a duplicate
    GUARD: NBSP_FORM ≠ EQUAL_STRING_PROOF
  RISK_CASE_003:
    NAME: TOKENIZER_SPLIT_EVASION
    INPUT: "drop<NBSP>table joined by a no-break space"
    CONTEXT: a split-on-U+0020 tokenizer keeping two words as one token
    RISK: MEDIUM
    ATTACK: two keywords look separated but tokenize as one, defeating a word-boundary rule
    GUARD: NBSP_FORM ≠ SEPARATOR_GUARANTEE_PROOF
  RISK_CASE_004:
    NAME: ENCODED_NBSP_BYPASS
    INPUT: "value%C2%A0tail (with a later decode)"
    CONTEXT: a percent-encoded U+00A0 decoded back before use
    RISK: HIGH
    ATTACK: "%C2%A0" decodes to the U+00A0 AFTER a check → the space-homoglyph reappears
    GUARD: NBSP_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: SPACE_HOMOGLYPH_STACK
    INPUT: "a display name using U+00A0 where a space is expected"
    CONTEXT: a no-break space passing as a normal separator in a visual review
    RISK: MEDIUM
    ATTACK: the look-alike space makes a crafted value read as a normal, harmless string
    GUARD: NBSP_FORM ≠ ORDINARY_SPACE_PROOF
  RISK_CASE_006:
    NAME: UNICODE_SPACE_FAMILY_GAP
    INPUT: "input using U+2007 / U+202F / U+3000 where only U+00A0 is filtered"
    CONTEXT: other Unicode spaces slipping past an NBSP-only filter
    RISK: MEDIUM
    ATTACK: filtering only U+00A0 misses the wider Unicode space family (figure/narrow/ideographic spaces)
    GUARD: NBSP_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨SP⟩
    CODEPOINT: U+0020
    NAME: SPACE
    RISK: HIGH
    RULE: SPACE ≠ NO_BREAK_SPACE (the ordinary breakable ASCII space; U+00A0 renders the same but is a different codepoint that forbids a break)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨NNBSP⟩
    CODEPOINT: U+202F
    NAME: NARROW NO-BREAK SPACE
    RISK: HIGH
    RULE: NARROW_NO_BREAK_SPACE ≠ NO_BREAK_SPACE (a narrower no-break space; same evasion, different codepoint an NBSP-only filter misses)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨FIGSP⟩
    CODEPOINT: U+2007
    NAME: FIGURE SPACE
    RISK: MEDIUM
    RULE: FIGURE_SPACE ≠ NO_BREAK_SPACE (a no-break digit-width space; another space-family member)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨IDSP⟩
    CODEPOINT: U+3000
    NAME: IDEOGRAPHIC SPACE
    RISK: MEDIUM
    RULE: IDEOGRAPHIC_SPACE ≠ NO_BREAK_SPACE (a wide CJK space; looks spacious but is yet another separator codepoint)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨ZWNBSP⟩
    CODEPOINT: U+FEFF
    NAME: ZERO WIDTH NO-BREAK SPACE
    RISK: LOW
    RULE: ZERO_WIDTH_NO_BREAK_SPACE ≠ NO_BREAK_SPACE (same no-break intent but zero-width and BOM-capable; U+00A0 has a visible advance)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "it looks like a space, so it is a space"
    RESPONSE: NBSP_FORM ≠ ORDINARY_SPACE_PROOF
    RULE: it renders like U+0020 but is U+00A0; equality and checks see a different byte
  CG2:
    TRIGGER: "our whitespace check covers it"
    RESPONSE: NBSP_FORM ≠ WHITESPACE_TO_EVERY_CHECK_PROOF
    RULE: a 0x20-only (or ASCII-only) check does not treat U+00A0 as whitespace
  CG3:
    TRIGGER: "trim removes trailing spaces, so it is gone"
    RESPONSE: NBSP_FORM ≠ TRIMMED_BY_DEFAULT_PROOF
    RULE: many trims are ASCII-only and leave U+00A0 in place
  CG4:
    TRIGGER: "'%C2%A0' is safe forever"
    RESPONSE: NBSP_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to the U+00A0 before use
  CG5:
    TRIGGER: "the tokenizer will split it like a space"
    RESPONSE: NBSP_FORM ≠ SEPARATOR_GUARANTEE_PROOF
    RULE: a split-on-U+0020 tokenizer does not split on U+00A0; two words stay one token
  CG6:
    TRIGGER: "we filter U+00A0, so all lookalike spaces are handled"
    RESPONSE: NBSP_FORM ≠ EFFECT
    RULE: the Unicode space family (U+2007/U+202F/U+3000 …) is wider than U+00A0 alone
  CG7:
    TRIGGER: "the two strings look the same, so they are equal"
    RESPONSE: NBSP_FORM ≠ EQUAL_STRING_PROOF
    RULE: visual sameness is not byte equality; a hidden U+00A0 breaks equality

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "trailing U+00A0 on a value"
      NAME: TRIM_SURVIVOR
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: a trailing no-break space surviving an ASCII trim and breaking equality
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "U+00A0 between two keywords"
      NAME: NO_SPLIT_GLUE
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: two words kept as one token past a split-on-space rule
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "mixed Unicode spaces (U+00A0 + U+202F + U+2007)"
      NAME: SPACE_FAMILY_MIX
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: several space-family codepoints combined to evade an NBSP-only filter
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — NBSP's risk is about how it sits within whitespace-sensitive sequences.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: NBSP masquerades as a separator (separator masking), but does not imitate the existence of a verified entity. Its risks are whitespace/equality desync, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of U+00A0 with U+202F / U+2007 / U+3000 to vary the space codepoint / evade an NBSP-only filter
  A2: percent-encoding "%C2%A0" to slip past a raw-byte scan
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: whitespace-check evasion (a required field filled with only U+00A0)
  B2: trim survival (admin<NBSP> not equal to admin after an ASCII trim)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "U+00A0 between two keywords" (SC2) — no-split glue
  C2: "mixed Unicode spaces" (SC3) — space-family mix past an NBSP-only filter
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: U+00A0 presented as an ordinary space so a reviewer treats it as harmless
  D2: "%C2%A0" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: separator confusion (a space that does not split)
  E2: N/A — vector: NBSP-only filter missing the wider Unicode space family
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: a no-break space is an ordinary space
  EXPECTED: FAIL_ORDINARY_SPACE_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: every whitespace check treats U+00A0 as whitespace
  EXPECTED: FAIL_WHITESPACE_TO_EVERY_CHECK_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: trim removes U+00A0 by default
  EXPECTED: FAIL_TRIMMED_BY_DEFAULT_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%C2%A0" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: a split-on-space tokenizer splits U+00A0
  EXPECTED: FAIL_SEPARATOR_GUARANTEE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: two strings that look the same are equal
  EXPECTED: FAIL_EQUAL_STRING_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to normalize the whole Unicode space family (U+00A0, U+2007, U+202F, U+3000 …) to a canonical form before whitespace checks, trims, tokenizers and equality — without breaking legitimate no-break typography where it matters?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (a Unicode-aware whitespace normalizer applied consistently before check, trim, tokenize and compare — an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "U+00A0 looks like a space but is not U+0020; ASCII-only whitespace/trim/split logic misses it, and it is only one of a wider space family".
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
