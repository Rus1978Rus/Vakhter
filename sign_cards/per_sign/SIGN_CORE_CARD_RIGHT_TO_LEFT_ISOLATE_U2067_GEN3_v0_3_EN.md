PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_RIGHT_TO_LEFT_ISOLATE_U2067_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_RIGHT_TO_LEFT_ISOLATE_U2067_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_RIGHT_TO_LEFT_ISOLATE_U2067_GEN3_v0_3_EN
CODEPOINT: U+2067
VISIBLE_FORM: ⟨RLI⟩
UNICODE_NAME: RIGHT-TO-LEFT ISOLATE
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: right-to-left isolate / scoped bidi reorder (mirror of LRI)
CATEGORY_ROADMAP: LLM (bidi isolate reorder, Trojan Source) · PHAGO: — (structure masking)
GLYPH_NOTE: VISIBLE_FORM uses the marker ⟨RLI⟩; the sign itself (U+2067) is an invisible Bidi_Control (Cf) and is NEVER written literally here — a literal RLI would reorder this document. Examples use ⟨RLI⟩/⟨PDI⟩/%E2%81%A7, never the byte.

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
VISIBLE_FORM: ⟨RLI⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: RLI_FORM ≠ EFFECT
SIGN_CATEGORY:
  - bidirectional isolate (opens an RTL run isolated from its surroundings)
  - Unicode Bidi_Control, the modern recommended alternative to embeddings/overrides
  - legitimate scoped RTL layout (does not affect neighbours)
  - (misused) mirror of LRI — a newer control a legacy embedding/override filter misses

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — being non-printing does not make it inert
  2. NOT_ISOLATE_MEANS_SAFE — "recommended" ≠ safe; it still reorders WITHIN its scope and still deceives
  3. NOT_DISPLAY_ONLY — it reorders the VISUAL run while logical bytes are unchanged (desync)
  4. NOT_SCOPE_CONTAINS_ALL — an unterminated isolate still bleeds to the end of the paragraph
  5. NOT_ENCODED_SAFE — "%E2%81%A7" may be decoded back to the isolate later
  6. NOT_AUTHORITY — it does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; it deceives the reader
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_EMBEDDING_ONLY_FILTER_SAFE — a filter handling only embeddings/overrides (202A-202E) misses isolates (2066-2069)
  10. NOT_SANITIZED_PROOF — the presence of the isolate does not mean the input is sanitized
  11. NOT_BALANCED_PROOF — an isolate needs a matching PDI; its presence is not balance

BASE_FORMULAS:
  RLI_FORM ≠ EFFECT
  RLI_FORM ≠ ISOLATE_MEANS_SAFE_PROOF
  RLI_FORM ≠ DISPLAY_ONLY_PROOF
  RLI_FORM ≠ SCOPE_CONTAINMENT_PROOF
  RLI_FORM ≠ ENCODED_SAFETY_PROOF
  RLI_FORM ≠ AUTHORITY
  RLI_FORM ≠ EXECUTION_TRIGGER
  RLI_FORM ≠ EMBEDDING_ONLY_FILTER_PROOF
  RLI_FORM ≠ INVISIBLE_HARMLESS_PROOF
  RLI_FORM ≠ SANITIZED_PROOF
  RLI_FORM ≠ BALANCED_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: RLI (ZONE_1) has parallel functions (legitimate scoped RTL layout vs. in-scope visual-order deception) co-existing without cultural precession. Polysemy of a stable Bidi_Control.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a formatting-isolate control with no gestural predecessor; the reorder-deception use is layered on by the digital epoch in parallel with legitimate scoped layout.

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
    INPUT: "RLI is U+2067 in Unicode"
    CONTEXT: naming the control in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLI_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "isolates are the modern recommended bidi control"
    CONTEXT: describing legitimate scoped layout in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLI_FORM ≠ ISOLATE_MEANS_SAFE_PROOF
  SAFE_CASE_003:
    INPUT: "the marker is written as <RLI> here"
    CONTEXT: a documentation marker, not the byte
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLI_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "an isolate does not affect surrounding text"
    CONTEXT: describing the scoping property in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLI_FORM ≠ SCOPE_CONTAINMENT_PROOF
  SAFE_CASE_005:
    INPUT: "a properly terminated isolate (RLI...PDI)"
    CONTEXT: describing balanced legitimate usage
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLI_FORM ≠ BALANCED_PROOF
  SAFE_CASE_006:
    INPUT: "the Bidirectional Algorithm scopes the isolate"
    CONTEXT: prose about the UBA
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLI_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: LEGACY_FILTER_GAP
    INPUT: "input passing a strip that only handles 202A-202E"
    CONTEXT: an isolate slipping past a filter that only knows embeddings/overrides
    RISK: HIGH
    ATTACK: the newer isolate (2066-2069) is not modelled, so the reorder survives the strip
    GUARD: RLI_FORM ≠ EMBEDDING_ONLY_FILTER_PROOF
  RISK_CASE_002:
    NAME: IN_SCOPE_CODE_REORDER
    INPUT: 'safe = true <RLI> // danger? <PDI>'
    CONTEXT: an isolate reordering a code run within its scope
    RISK: HIGH
    ATTACK: even scoped, the isolate reorders visible tokens so logic ≠ display
    GUARD: RLI_FORM ≠ ISOLATE_MEANS_SAFE_PROOF
  RISK_CASE_003:
    NAME: UNTERMINATED_ISOLATE_BLEED
    INPUT: "label<RLI>rest of the paragraph with no PDI"
    CONTEXT: an isolate with no PDI, bleeding to the end of the paragraph
    RISK: HIGH
    ATTACK: the unterminated isolate reorders everything to the paragraph end, beyond the intended scope
    GUARD: RLI_FORM ≠ SCOPE_CONTAINMENT_PROOF
  RISK_CASE_004:
    NAME: ISOLATE_TERMINATOR_MISMATCH
    INPUT: "RLI closed with <PDF> instead of PDI"
    CONTEXT: an isolate closed by the wrong terminator (PDF, not PDI)
    RISK: MEDIUM
    ATTACK: a parser pairing isolate with PDF mis-tracks nesting and leaves the isolate open
    GUARD: RLI_FORM ≠ BALANCED_PROOF
  RISK_CASE_005:
    NAME: ENCODED_ISOLATE_BYPASS
    INPUT: "value%E2%81%A7tail (with a later decode)"
    CONTEXT: a percent-encoded RLI decoded back before display
    RISK: HIGH
    ATTACK: "%E2%81%A7" decodes to the isolate AFTER a check → reorder deception
    GUARD: RLI_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: BIDI_HOMOGLYPH_STACK
    INPUT: "раyраl<RLI> ... (bidi + confusable letters combined)"
    CONTEXT: an isolate stacked with confusable letters to deepen the spoof
    RISK: MEDIUM
    ATTACK: the isolate plus look-alike letters make a hostile string pass a shallow visual review
    GUARD: RLI_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨LRI⟩
    CODEPOINT: U+2066
    NAME: LEFT-TO-RIGHT ISOLATE
    RISK: HIGH
    RULE: LEFT_TO_RIGHT_ISOLATE ≠ RIGHT_TO_LEFT_ISOLATE (mirror isolate, opposite direction; a naive filter conflates them)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨FSI⟩
    CODEPOINT: U+2068
    NAME: FIRST STRONG ISOLATE
    RISK: HIGH
    RULE: FIRST_STRONG_ISOLATE ≠ RIGHT_TO_LEFT_ISOLATE (FSI auto-picks direction from the first strong char — attacker-controllable)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨RLE⟩
    CODEPOINT: U+202B
    NAME: RIGHT-TO-LEFT EMBEDDING
    RISK: MEDIUM
    RULE: RIGHT_TO_LEFT_EMBEDDING ≠ RIGHT_TO_LEFT_ISOLATE (embedding affects neighbours; isolate scopes — different model)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨PDI⟩
    CODEPOINT: U+2069
    NAME: POP DIRECTIONAL ISOLATE
    RISK: LOW
    RULE: POP_DIRECTIONAL_ISOLATE ≠ RIGHT_TO_LEFT_ISOLATE (the terminator, not the opener)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨RLO⟩
    CODEPOINT: U+202E
    NAME: RIGHT-TO-LEFT OVERRIDE
    RISK: LOW
    RULE: RIGHT_TO_LEFT_OVERRIDE ≠ RIGHT_TO_LEFT_ISOLATE (override forces & affects neighbours; isolate scopes)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "isolates are recommended, so an isolate is safe"
    RESPONSE: RLI_FORM ≠ ISOLATE_MEANS_SAFE_PROOF
    RULE: recommended for correctness, not immunity; it still reorders within scope and deceives
  CG2:
    TRIGGER: "an invisible control char cannot be dangerous"
    RESPONSE: RLI_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: invisibility is orthogonal to effect; RLI drives visual/logical desync
  CG3:
    TRIGGER: "an isolate contains its effect, so nothing leaks"
    RESPONSE: RLI_FORM ≠ SCOPE_CONTAINMENT_PROOF
    RULE: an unterminated isolate bleeds to the end of the paragraph
  CG4:
    TRIGGER: "'%E2%81%A7' is safe forever"
    RESPONSE: RLI_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to the isolate before display
  CG5:
    TRIGGER: "our bidi filter handles embeddings and overrides, so we are covered"
    RESPONSE: RLI_FORM ≠ EMBEDDING_ONLY_FILTER_PROOF
    RULE: isolates (2066-2069) are a separate, newer range a legacy filter misses
  CG6:
    TRIGGER: "the presence of an isolate means the input is sanitized"
    RESPONSE: RLI_FORM ≠ SANITIZED_PROOF
    RULE: the presence of the sign says nothing about sanitization

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "RLI ... PDI"
      NAME: BALANCED_ISOLATE_SPAN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: a scoped isolate span used to reorder a specific token
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "RLI (no PDI)"
      NAME: UNTERMINATED_BLEED
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: an isolate with no terminator bleeding to the paragraph end
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "RLI ... PDF"
      NAME: WRONG_TERMINATOR
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: an isolate closed with PDF instead of PDI, mis-tracking nesting
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with RLI are central to scoped visual-order deception.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: RLI reorders a scoped run (structure masking), but does not imitate the existence of a verified entity. Its risks are visual/logical desync, not entity mimicry. (Filename spoof is more natural with override; see RLO/LRO.)
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of RLI with LRI (U+2066) / FSI (U+2068) to vary direction / evade an RLI-only filter
  A2: percent-encoding "%E2%81%A7" to slip past a raw-byte scan
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: legacy filter gap (isolate survives a 202A-202E-only strip)
  B2: in-scope code reorder safe=true <RLI> // danger? <PDI>
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "RLI (no PDI)" (SC2) — unterminated bleed to paragraph end
  C2: "RLI ... PDF" (SC3) — wrong terminator
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: RLI presented as a harmless "recommended safe" isolate inside a code field
  D2: "%E2%81%A7" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: scoped reorder deceiving a reviewer
  E2: N/A — vector: newer-range isolate bypassing a legacy embedding-only filter
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: an isolate is safe because it is the recommended control
  EXPECTED: FAIL_ISOLATE_MEANS_SAFE_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: an invisible control char cannot be dangerous
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: an isolate contains its effect, nothing leaks
  EXPECTED: FAIL_SCOPE_CONTAINMENT_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E2%81%A7" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: an embedding/override filter covers isolates too
  EXPECTED: FAIL_EMBEDDING_ONLY_FILTER_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: the presence of an isolate proves the input was sanitized
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to model the full Bidi_Control set incl. isolates (2066-2069) and FSI auto-direction, without false positives on legitimate scoped mixed-direction text?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (a stack-based checker covering embeddings, overrides AND isolates, pairing each opener with its correct terminator + rejecting unterminated/wrong-terminator — an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "isolates are recommended, not immune; a legacy embedding-only filter misses them".
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
