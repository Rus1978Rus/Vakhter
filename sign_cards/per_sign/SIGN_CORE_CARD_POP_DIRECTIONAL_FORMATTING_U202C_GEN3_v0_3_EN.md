PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_POP_DIRECTIONAL_FORMATTING_U202C_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_POP_DIRECTIONAL_FORMATTING_U202C_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_POP_DIRECTIONAL_FORMATTING_U202C_GEN3_v0_3_EN
CODEPOINT: U+202C
VISIBLE_FORM: ⟨PDF⟩
UNICODE_NAME: POP DIRECTIONAL FORMATTING
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: pop directional formatting / bidi terminator
CATEGORY_ROADMAP: LLM (bidi terminator, balance deception) · PHAGO: — (structure masking)
GLYPH_NOTE: VISIBLE_FORM uses the marker ⟨PDF⟩; the sign itself (U+202C) is an invisible Bidi_Control (Cf) and is NEVER written literally here. Examples use ⟨PDF⟩/⟨RLO⟩/%E2%80%AC, never the byte. (PDF here = Pop Directional Formatting, NOT the file format.)

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
VISIBLE_FORM: ⟨PDF⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: PDF_FORM ≠ EFFECT
SIGN_CATEGORY:
  - terminator for the most recent embedding/override (LRE/RLE/LRO/RLO)
  - Unicode Bidi_Control (part of the Bidirectional Algorithm)
  - legitimate closer that restores the prior direction level
  - (misused) mis-placed/extra/missing terminator that breaks nesting balance

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — being non-printing does not make it inert
  2. NOT_TERMINATOR_MEANS_BALANCED — the presence of a PDF does not prove the spans are balanced (counts/nesting can be off)
  3. NOT_NEUTRAL_CLOSER — a mis-placed or extra PDF can prematurely close a legitimate span, re-exposing outer direction
  4. NOT_CLOSES_ISOLATES — PDF terminates embeddings/overrides ONLY; isolates need PDI (U+2069) — do not conflate
  5. NOT_ESCAPED_PROOF — the presence of a bidi mark does not mean it is quoted/escaped
  6. NOT_ENCODED_SAFE — "%E2%80%AC" may be decoded back to the terminator later
  7. NOT_AUTHORITY — it does not confirm officialness
  8. NOT_EXECUTION_TRIGGER — by itself it executes nothing; it governs nesting
  9. NOT_STANDALONE_SAFE — a PDF with no matching opener is a nesting error, not a no-op
  10. NOT_SANITIZED_PROOF — the presence of a PDF does not mean the input is sanitized
  11. NOT_ORDER_INDEPENDENT — where the PDF sits determines which span it closes

BASE_FORMULAS:
  PDF_FORM ≠ EFFECT
  PDF_FORM ≠ TERMINATOR_MEANS_BALANCED_PROOF
  PDF_FORM ≠ NEUTRAL_CLOSER_PROOF
  PDF_FORM ≠ CLOSES_ISOLATES_PROOF
  PDF_FORM ≠ ESCAPED_PROOF
  PDF_FORM ≠ ENCODED_SAFETY_PROOF
  PDF_FORM ≠ AUTHORITY
  PDF_FORM ≠ EXECUTION_TRIGGER
  PDF_FORM ≠ INVISIBLE_HARMLESS_PROOF
  PDF_FORM ≠ STANDALONE_SAFETY_PROOF
  PDF_FORM ≠ ORDER_INDEPENDENCE_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: PDF (ZONE_1) has parallel functions (legitimate span closer vs. balance-deception via mis-count/mis-placement) co-existing without cultural precession. Polysemy of a stable Bidi_Control.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a formatting-terminator control with no gestural predecessor; the balance-deception use is layered on by the digital epoch in parallel with legitimate span closing.

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
    INPUT: "PDF is U+202C in Unicode"
    CONTEXT: naming the control in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: PDF_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "a balanced run: RLE ... PDF"
    CONTEXT: describing a legitimate opener/closer pair in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: PDF_FORM ≠ TERMINATOR_MEANS_BALANCED_PROOF
  SAFE_CASE_003:
    INPUT: "the marker is written as <PDF> here"
    CONTEXT: a documentation marker, not the byte
    EXPECTED: INFO
    RISK: NONE
    GUARD: PDF_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "PDF closes embeddings/overrides; PDI closes isolates"
    CONTEXT: prose distinguishing the two terminators
    EXPECTED: INFO
    RISK: NONE
    GUARD: PDF_FORM ≠ CLOSES_ISOLATES_PROOF
  SAFE_CASE_005:
    INPUT: "the closer restores the prior direction level"
    CONTEXT: describing legitimate restore behavior
    EXPECTED: INFO
    RISK: NONE
    GUARD: PDF_FORM ≠ NEUTRAL_CLOSER_PROOF
  SAFE_CASE_006:
    INPUT: "the Bidirectional Algorithm pops the level"
    CONTEXT: prose about the UBA
    EXPECTED: INFO
    RISK: NONE
    GUARD: PDF_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: FALSE_BALANCE_CLAIM
    INPUT: "opener<RLO>...<PDF>...<RLO> (one PDF, two openers)"
    CONTEXT: a single PDF making a "has a terminator" check believe the run is balanced
    RISK: HIGH
    ATTACK: an unmatched second opener stays live; a naive "PDF present → balanced" check clears a reorder
    GUARD: PDF_FORM ≠ TERMINATOR_MEANS_BALANCED_PROOF
  RISK_CASE_002:
    NAME: PREMATURE_CLOSE
    INPUT: "legit<RLE>text<PDF-injected>more (an extra PDF closing early)"
    CONTEXT: an injected extra PDF closing a legitimate span before its intended end
    RISK: MEDIUM
    ATTACK: the extra terminator re-exposes the outer direction, corrupting the remaining display
    GUARD: PDF_FORM ≠ NEUTRAL_CLOSER_PROOF
  RISK_CASE_003:
    NAME: ISOLATE_CONFUSION
    INPUT: "isolate opened with LRI but closed with <PDF> not PDI"
    CONTEXT: a filter/parser treating PDF as if it closed an isolate
    RISK: MEDIUM
    ATTACK: PDF does not close an isolate; a wrong-terminator model mis-tracks nesting and leaves a span open
    GUARD: PDF_FORM ≠ CLOSES_ISOLATES_PROOF
  RISK_CASE_004:
    NAME: STANDALONE_PDF_NESTING_ERROR
    INPUT: "text<PDF>more (a PDF with no matching opener)"
    CONTEXT: a lone PDF treated as a harmless no-op
    RISK: MEDIUM
    ATTACK: the unmatched PDF is a nesting error a lenient renderer may resolve unpredictably
    GUARD: PDF_FORM ≠ STANDALONE_SAFETY_PROOF
  RISK_CASE_005:
    NAME: ENCODED_PDF_BYPASS
    INPUT: "value%E2%80%AC (with a later decode)"
    CONTEXT: a percent-encoded PDF decoded back before display
    RISK: MEDIUM
    ATTACK: "%E2%80%AC" decodes to the terminator AFTER a check → nesting manipulation
    GUARD: PDF_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: BALANCE_COUNT_MISMATCH
    INPUT: "two openers, three PDFs (over-popping the stack)"
    CONTEXT: more PDFs than openers, popping past the base level
    RISK: MEDIUM
    ATTACK: over-popping affects text outside the intended span, a case a per-line-only check misses
    GUARD: PDF_FORM ≠ TERMINATOR_MEANS_BALANCED_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨PDI⟩
    CODEPOINT: U+2069
    NAME: POP DIRECTIONAL ISOLATE
    RISK: HIGH
    RULE: POP_DIRECTIONAL_ISOLATE ≠ POP_DIRECTIONAL_FORMATTING (PDI closes isolates; PDF closes embeddings/overrides — not interchangeable)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨RLE⟩
    CODEPOINT: U+202B
    NAME: RIGHT-TO-LEFT EMBEDDING
    RISK: MEDIUM
    RULE: RIGHT_TO_LEFT_EMBEDDING ≠ POP_DIRECTIONAL_FORMATTING (opener vs terminator; a filter must pair them, not lump them)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨LRE⟩
    CODEPOINT: U+202A
    NAME: LEFT-TO-RIGHT EMBEDDING
    RISK: MEDIUM
    RULE: LEFT_TO_RIGHT_EMBEDDING ≠ POP_DIRECTIONAL_FORMATTING
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨RLO⟩
    CODEPOINT: U+202E
    NAME: RIGHT-TO-LEFT OVERRIDE
    RISK: LOW
    RULE: RIGHT_TO_LEFT_OVERRIDE ≠ POP_DIRECTIONAL_FORMATTING (the override PDF terminates, not the terminator itself)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨ALM⟩
    CODEPOINT: U+061C
    NAME: ARABIC LETTER MARK
    RISK: LOW
    RULE: ARABIC_LETTER_MARK ≠ POP_DIRECTIONAL_FORMATTING (a bidi mark, not a terminator; invisible to a PDF-only filter)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "the run has a PDF, so it is balanced and safe"
    RESPONSE: PDF_FORM ≠ TERMINATOR_MEANS_BALANCED_PROOF
    RULE: one PDF does not match every opener; count and nesting must be verified
  CG2:
    TRIGGER: "a closer cannot be dangerous"
    RESPONSE: PDF_FORM ≠ NEUTRAL_CLOSER_PROOF
    RULE: an extra/mis-placed PDF closes a legit span early, corrupting later display
  CG3:
    TRIGGER: "PDF closes any bidi span"
    RESPONSE: PDF_FORM ≠ CLOSES_ISOLATES_PROOF
    RULE: PDF closes embeddings/overrides only; isolates need PDI — a wrong-terminator model mis-tracks
  CG4:
    TRIGGER: "'%E2%80%AC' is safe forever"
    RESPONSE: PDF_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to the terminator before display
  CG5:
    TRIGGER: "a lone PDF is a harmless no-op"
    RESPONSE: PDF_FORM ≠ STANDALONE_SAFETY_PROOF
    RULE: an unmatched PDF is a nesting error a lenient renderer resolves unpredictably
  CG6:
    TRIGGER: "the presence of a PDF means the input is sanitized"
    RESPONSE: PDF_FORM ≠ SANITIZED_PROOF (via INVISIBLE_HARMLESS_PROOF)
    RULE: the presence of the sign says nothing about sanitization

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "opener ... PDF (mismatched count)"
      NAME: FALSE_BALANCE
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: one terminator making a shallow check believe multiple openers are balanced
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "extra PDF"
      NAME: PREMATURE_CLOSE
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: an injected PDF closing a legitimate span early
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "PDF for an isolate"
      NAME: WRONG_TERMINATOR
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: PDF used where PDI is required, mis-tracking isolate nesting
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — PDF's risk lives entirely in the pairing/nesting sequence.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: PDF closes a directional span (structure/nesting control), but does not imitate the existence of a verified entity. Its risks are balance/nesting deception, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of PDF with PDI (U+2069) so an isolate/embedding pairing is mis-modelled
  A2: percent-encoding "%E2%80%AC" to slip past a raw-byte scan
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: false balance — one PDF, two openers, clearing a "has terminator" check
  B2: premature close — an injected extra PDF corrupting later display
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "opener ... PDF (mismatched)" (SC1) — false balance
  C2: "PDF for an isolate" (SC3) — wrong terminator
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: PDF presented as a harmless closer that "proves" the run is balanced
  D2: "%E2%80%AC" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: false-balance clearing a reorder for review
  E2: N/A — vector: over-popping the stack past the base level
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: a run with a PDF is balanced and safe
  EXPECTED: FAIL_TERMINATOR_MEANS_BALANCED_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: a closer cannot be dangerous
  EXPECTED: FAIL_NEUTRAL_CLOSER_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: PDF closes any bidi span including isolates
  EXPECTED: FAIL_CLOSES_ISOLATES_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E2%80%AC" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: a lone PDF is a harmless no-op
  EXPECTED: FAIL_STANDALONE_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: an invisible control char cannot be dangerous
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to verify bidi balance (match openers to PDF/PDI by type AND count AND nesting) without false positives on legitimate balanced mixed-direction text?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (a stack-based bidi balance checker that pairs each opener with the correct terminator type + rejects over/under-pop — an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "a terminator's presence is not a balance proof; type and count and nesting must match".
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
