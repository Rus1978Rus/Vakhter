PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_POP_DIRECTIONAL_ISOLATE_U2069_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_POP_DIRECTIONAL_ISOLATE_U2069_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_POP_DIRECTIONAL_ISOLATE_U2069_GEN3_v0_3_EN
CODEPOINT: U+2069
VISIBLE_FORM: ⟨PDI⟩
UNICODE_NAME: POP DIRECTIONAL ISOLATE
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: pop directional isolate / bidi isolate terminator
CATEGORY_ROADMAP: LLM (bidi isolate terminator, balance deception) · PHAGO: — (structure masking)
GLYPH_NOTE: VISIBLE_FORM uses the marker ⟨PDI⟩; the sign itself (U+2069) is an invisible Bidi_Control (Cf) and is NEVER written literally here. Examples use ⟨PDI⟩/⟨LRI⟩/%E2%81%A9, never the byte.

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
VISIBLE_FORM: ⟨PDI⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: PDI_FORM ≠ EFFECT
SIGN_CATEGORY:
  - terminator for the most recent isolate (LRI/RLI/FSI)
  - Unicode Bidi_Control, the modern isolate closer
  - legitimate closer that ends a scoped isolate run
  - (misused) mis-placed/extra/missing isolate terminator that breaks nesting balance

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — being non-printing does not make it inert
  2. NOT_TERMINATOR_MEANS_BALANCED — the presence of a PDI does not prove the isolates are balanced
  3. NOT_CLOSES_EMBEDDINGS — PDI closes ISOLATES only; embeddings/overrides use PDF (U+202C) — do not conflate
  4. NOT_NEUTRAL_CLOSER — a mis-placed or extra PDI can prematurely close a legitimate isolate
  5. NOT_ESCAPED_PROOF — the presence of a bidi mark does not mean it is quoted/escaped
  6. NOT_ENCODED_SAFE — "%E2%81%A9" may be decoded back to the terminator later
  7. NOT_AUTHORITY — it does not confirm officialness
  8. NOT_EXECUTION_TRIGGER — by itself it executes nothing; it governs isolate nesting
  9. NOT_STANDALONE_SAFE — a PDI with no matching isolate opener is a nesting error, not a no-op
  10. NOT_LEGACY_FILTER_COVERED — a filter modelling only PDF (202C) does not track PDI (2069)
  11. NOT_ORDER_INDEPENDENT — where the PDI sits determines which isolate it closes

BASE_FORMULAS:
  PDI_FORM ≠ EFFECT
  PDI_FORM ≠ TERMINATOR_MEANS_BALANCED_PROOF
  PDI_FORM ≠ CLOSES_EMBEDDINGS_PROOF
  PDI_FORM ≠ NEUTRAL_CLOSER_PROOF
  PDI_FORM ≠ ESCAPED_PROOF
  PDI_FORM ≠ ENCODED_SAFETY_PROOF
  PDI_FORM ≠ AUTHORITY
  PDI_FORM ≠ EXECUTION_TRIGGER
  PDI_FORM ≠ INVISIBLE_HARMLESS_PROOF
  PDI_FORM ≠ STANDALONE_SAFETY_PROOF
  PDI_FORM ≠ LEGACY_FILTER_COVERAGE_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: PDI (ZONE_1) has parallel functions (legitimate isolate closer vs. balance-deception via mis-count/mis-placement/wrong-terminator) co-existing without cultural precession. Polysemy of a stable Bidi_Control.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: an isolate-terminator control with no gestural predecessor; the balance-deception use is layered on by the digital epoch in parallel with legitimate isolate closing.

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
    INPUT: "PDI is U+2069 in Unicode"
    CONTEXT: naming the control in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: PDI_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "a balanced isolate: LRI ... PDI"
    CONTEXT: describing a legitimate isolate open/close pair in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: PDI_FORM ≠ TERMINATOR_MEANS_BALANCED_PROOF
  SAFE_CASE_003:
    INPUT: "the marker is written as <PDI> here"
    CONTEXT: a documentation marker, not the byte
    EXPECTED: INFO
    RISK: NONE
    GUARD: PDI_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "PDI closes isolates; PDF closes embeddings/overrides"
    CONTEXT: prose distinguishing the two terminators
    EXPECTED: INFO
    RISK: NONE
    GUARD: PDI_FORM ≠ CLOSES_EMBEDDINGS_PROOF
  SAFE_CASE_005:
    INPUT: "the closer ends a scoped isolate run"
    CONTEXT: describing legitimate closing behavior
    EXPECTED: INFO
    RISK: NONE
    GUARD: PDI_FORM ≠ NEUTRAL_CLOSER_PROOF
  SAFE_CASE_006:
    INPUT: "the Bidirectional Algorithm pops the isolate"
    CONTEXT: prose about the UBA
    EXPECTED: INFO
    RISK: NONE
    GUARD: PDI_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: FALSE_BALANCE_CLAIM
    INPUT: "opener<LRI>...<PDI>...<RLI> (one PDI, two isolate openers)"
    CONTEXT: a single PDI making a "has a terminator" check believe the isolates are balanced
    RISK: HIGH
    ATTACK: an unmatched second isolate opener stays live; a naive "PDI present → balanced" check clears a reorder
    GUARD: PDI_FORM ≠ TERMINATOR_MEANS_BALANCED_PROOF
  RISK_CASE_002:
    NAME: WRONG_TERMINATOR_FOR_EMBEDDING
    INPUT: "embedding opened with RLE but closed with <PDI> not PDF"
    CONTEXT: a parser treating PDI as if it closed an embedding
    RISK: MEDIUM
    ATTACK: PDI does not close an embedding; a wrong-terminator model mis-tracks nesting and leaves a span open
    GUARD: PDI_FORM ≠ CLOSES_EMBEDDINGS_PROOF
  RISK_CASE_003:
    NAME: PREMATURE_ISOLATE_CLOSE
    INPUT: "legit<LRI>text<PDI-injected>more (an extra PDI closing early)"
    CONTEXT: an injected extra PDI closing a legitimate isolate before its intended end
    RISK: MEDIUM
    ATTACK: the extra terminator re-exposes the outer direction, corrupting the remaining display
    GUARD: PDI_FORM ≠ NEUTRAL_CLOSER_PROOF
  RISK_CASE_004:
    NAME: LEGACY_FILTER_GAP
    INPUT: "PDI passing a filter that only knows PDF (202C)"
    CONTEXT: a legacy bidi filter that models embeddings/overrides but not isolates
    RISK: HIGH
    ATTACK: the isolate terminator (and thus the isolate span) is invisible to the filter
    GUARD: PDI_FORM ≠ LEGACY_FILTER_COVERAGE_PROOF
  RISK_CASE_005:
    NAME: ENCODED_PDI_BYPASS
    INPUT: "value%E2%81%A9 (with a later decode)"
    CONTEXT: a percent-encoded PDI decoded back before display
    RISK: MEDIUM
    ATTACK: "%E2%81%A9" decodes to the terminator AFTER a check → isolate nesting manipulation
    GUARD: PDI_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: STANDALONE_PDI_NESTING_ERROR
    INPUT: "text<PDI>more (a PDI with no matching isolate opener)"
    CONTEXT: a lone PDI treated as a harmless no-op
    RISK: MEDIUM
    ATTACK: the unmatched PDI is a nesting error a lenient renderer may resolve unpredictably
    GUARD: PDI_FORM ≠ STANDALONE_SAFETY_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨PDF⟩
    CODEPOINT: U+202C
    NAME: POP DIRECTIONAL FORMATTING
    RISK: HIGH
    RULE: POP_DIRECTIONAL_FORMATTING ≠ POP_DIRECTIONAL_ISOLATE (PDF closes embeddings/overrides; PDI closes isolates — not interchangeable)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨LRI⟩
    CODEPOINT: U+2066
    NAME: LEFT-TO-RIGHT ISOLATE
    RISK: MEDIUM
    RULE: LEFT_TO_RIGHT_ISOLATE ≠ POP_DIRECTIONAL_ISOLATE (opener vs terminator; a filter must pair them, not lump them)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨RLI⟩
    CODEPOINT: U+2067
    NAME: RIGHT-TO-LEFT ISOLATE
    RISK: MEDIUM
    RULE: RIGHT_TO_LEFT_ISOLATE ≠ POP_DIRECTIONAL_ISOLATE
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨FSI⟩
    CODEPOINT: U+2068
    NAME: FIRST STRONG ISOLATE
    RISK: LOW
    RULE: FIRST_STRONG_ISOLATE ≠ POP_DIRECTIONAL_ISOLATE (an opener whose direction auto-detects; PDI is its closer)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨ALM⟩
    CODEPOINT: U+061C
    NAME: ARABIC LETTER MARK
    RISK: LOW
    RULE: ARABIC_LETTER_MARK ≠ POP_DIRECTIONAL_ISOLATE (a bidi mark, not a terminator; invisible to a PDI-only filter)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "the run has a PDI, so the isolates are balanced and safe"
    RESPONSE: PDI_FORM ≠ TERMINATOR_MEANS_BALANCED_PROOF
    RULE: one PDI does not match every isolate opener; count and nesting must be verified
  CG2:
    TRIGGER: "PDI closes any bidi span"
    RESPONSE: PDI_FORM ≠ CLOSES_EMBEDDINGS_PROOF
    RULE: PDI closes isolates only; embeddings/overrides need PDF — a wrong-terminator model mis-tracks
  CG3:
    TRIGGER: "a closer cannot be dangerous"
    RESPONSE: PDI_FORM ≠ NEUTRAL_CLOSER_PROOF
    RULE: an extra/mis-placed PDI closes a legit isolate early, corrupting later display
  CG4:
    TRIGGER: "'%E2%81%A9' is safe forever"
    RESPONSE: PDI_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to the terminator before display
  CG5:
    TRIGGER: "our filter handles PDF, so bidi terminators are covered"
    RESPONSE: PDI_FORM ≠ LEGACY_FILTER_COVERAGE_PROOF
    RULE: PDI (2069) is a separate, newer terminator a PDF-only filter misses
  CG6:
    TRIGGER: "a lone PDI is a harmless no-op"
    RESPONSE: PDI_FORM ≠ STANDALONE_SAFETY_PROOF
    RULE: an unmatched PDI is a nesting error a lenient renderer resolves unpredictably

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "isolate opener ... PDI (mismatched count)"
      NAME: FALSE_BALANCE
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: one terminator making a shallow check believe multiple isolates are balanced
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "PDI for an embedding"
      NAME: WRONG_TERMINATOR
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: PDI used where PDF is required, mis-tracking embedding nesting
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "extra PDI"
      NAME: PREMATURE_CLOSE
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: an injected PDI closing a legitimate isolate early
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — PDI's risk lives entirely in the isolate pairing/nesting sequence.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: PDI closes a directional isolate (structure/nesting control), but does not imitate the existence of a verified entity. Its risks are balance/nesting deception, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of PDI with PDF (U+202C) so an isolate/embedding pairing is mis-modelled
  A2: percent-encoding "%E2%81%A9" to slip past a raw-byte scan
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: false balance — one PDI, two isolate openers, clearing a "has terminator" check
  B2: legacy filter gap — PDI invisible to a PDF-only bidi filter
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "isolate ... PDI (mismatched)" (SC1) — false balance
  C2: "PDI for an embedding" (SC2) — wrong terminator
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: PDI presented as a harmless closer that "proves" the isolate is balanced
  D2: "%E2%81%A9" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: false-balance clearing an isolate reorder for review
  E2: N/A — vector: premature isolate close corrupting later display
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: a run with a PDI has balanced isolates and is safe
  EXPECTED: FAIL_TERMINATOR_MEANS_BALANCED_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: PDI closes any bidi span including embeddings
  EXPECTED: FAIL_CLOSES_EMBEDDINGS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: a closer cannot be dangerous
  EXPECTED: FAIL_NEUTRAL_CLOSER_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E2%81%A9" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: a PDF-only filter covers all bidi terminators
  EXPECTED: FAIL_LEGACY_FILTER_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: a lone PDI is a harmless no-op
  EXPECTED: FAIL_STANDALONE_SAFETY_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to verify isolate balance (match LRI/RLI/FSI to PDI by type AND count AND nesting, separately from PDF) without false positives on legitimate scoped mixed-direction text?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (a stack-based checker that pairs isolates with PDI and embeddings/overrides with PDF, rejecting cross-type/over/under-pop — an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "PDI closes isolates only; a PDF-only model and a presence-check both fail".
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
