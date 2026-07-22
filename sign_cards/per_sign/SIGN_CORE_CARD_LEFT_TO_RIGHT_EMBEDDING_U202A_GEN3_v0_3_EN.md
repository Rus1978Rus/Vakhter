PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_LEFT_TO_RIGHT_EMBEDDING_U202A_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_LEFT_TO_RIGHT_EMBEDDING_U202A_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_LEFT_TO_RIGHT_EMBEDDING_U202A_GEN3_v0_3_EN
CODEPOINT: U+202A
VISIBLE_FORM: ⟨LRE⟩
UNICODE_NAME: LEFT-TO-RIGHT EMBEDDING
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: left-to-right embedding / bidi reorder (mirror of RLE)
CATEGORY_ROADMAP: LLM (bidi visual reorder, Trojan Source) · PHAGO: — (structure masking)
GLYPH_NOTE: VISIBLE_FORM uses the marker ⟨LRE⟩; the sign itself (U+202A) is an invisible Bidi_Control (Cf) and is NEVER written literally here — a literal LRE would reorder this document. Examples use ⟨LRE⟩/⟨PDF⟩/%E2%80%AA, never the byte.

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
VISIBLE_FORM: ⟨LRE⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: LRE_FORM ≠ EFFECT
SIGN_CATEGORY:
  - bidirectional embedding (opens an LTR level, RESPECTING strong-character direction)
  - Unicode Bidi_Control (part of the Bidirectional Algorithm)
  - legitimate nested LTR text inside an RTL paragraph
  - (misused) mirror of RLE — subtler-than-override reorder in Trojan Source variants

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — being non-printing does not make it inert
  2. NOT_DISPLAY_ONLY — it reorders the VISUAL run while logical bytes are unchanged (desync)
  3. NOT_WEAKER_MEANS_SAFE — embedding is subtler than override but still reorders and still deceives
  4. NOT_RENDERING_COSMETIC — the reorder changes what a human approves vs what executes/stores
  5. NOT_ENCODED_SAFE — "%E2%80%AA" may be decoded back to the embedding later
  6. NOT_AUTHORITY — it does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; it deceives the reader
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_BALANCED_PROOF — an unterminated embedding (no PDF/PDI) bleeds the level onto the rest
  10. NOT_SANITIZED_PROOF — the presence of the embedding does not mean the input is sanitized
  11. NOT_OVERRIDE_ONLY_FILTER_SAFE — a strip targeting only RLO/LRO leaves RLE/LRE live

BASE_FORMULAS:
  LRE_FORM ≠ EFFECT
  LRE_FORM ≠ DISPLAY_ONLY_PROOF
  LRE_FORM ≠ WEAKER_MEANS_SAFE_PROOF
  LRE_FORM ≠ RENDERING_COSMETIC_PROOF
  LRE_FORM ≠ LOGICAL_ORDER_PROOF
  LRE_FORM ≠ ENCODED_SAFETY_PROOF
  LRE_FORM ≠ AUTHORITY
  LRE_FORM ≠ EXECUTION_TRIGGER
  LRE_FORM ≠ INVISIBLE_HARMLESS_PROOF
  LRE_FORM ≠ SANITIZED_PROOF
  LRE_FORM ≠ BALANCED_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: LRE (ZONE_1) has parallel functions (legitimate nested LTR layout vs. visual-order deception) co-existing without cultural precession. Polysemy of a stable Bidi_Control.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a formatting control with no gestural predecessor; the reorder-deception use is layered on by the digital epoch in parallel with legitimate nested LTR layout.

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
    INPUT: "LRE is U+202A in Unicode"
    CONTEXT: naming the control in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: LRE_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "LRE opens a nested LTR run in an RTL paragraph"
    CONTEXT: describing legitimate nested LTR layout in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: LRE_FORM ≠ RENDERING_COSMETIC_PROOF
  SAFE_CASE_003:
    INPUT: "the marker is written as <LRE> here"
    CONTEXT: a documentation marker, not the byte
    EXPECTED: INFO
    RISK: NONE
    GUARD: LRE_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "embedding respects strong chars; override forces"
    CONTEXT: prose distinguishing embedding from override
    EXPECTED: INFO
    RISK: NONE
    GUARD: LRE_FORM ≠ WEAKER_MEANS_SAFE_PROOF
  SAFE_CASE_005:
    INPUT: "a properly terminated embedding (LRE...PDF)"
    CONTEXT: describing balanced legitimate usage
    EXPECTED: INFO
    RISK: NONE
    GUARD: LRE_FORM ≠ BALANCED_PROOF
  SAFE_CASE_006:
    INPUT: "the Bidirectional Algorithm handles direction"
    CONTEXT: prose about the UBA
    EXPECTED: INFO
    RISK: NONE
    GUARD: LRE_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: EMBEDDING_CODE_REORDER
    INPUT: 'value = safe <LRE> // danger? <PDF>'
    CONTEXT: an embedding reordering a code run to mislead a reviewer
    RISK: HIGH
    ATTACK: the embedding reorders the visual run (subtler than override) so logic ≠ display
    GUARD: LRE_FORM ≠ RENDERING_COSMETIC_PROOF
  RISK_CASE_002:
    NAME: OVERRIDE_FILTER_GAP
    INPUT: "input passing a strip that removes only RLO/LRO overrides"
    CONTEXT: a filter that neutralizes overrides but leaves LRE/RLE embeddings
    RISK: HIGH
    ATTACK: an override-only strip leaves the embedding reorder live (weaker ≠ safe)
    GUARD: LRE_FORM ≠ OVERRIDE_ONLY_FILTER_SAFE
  RISK_CASE_003:
    NAME: UNTERMINATED_EMBEDDING_BLEED
    INPUT: "label<LRE>rest of the line with no PDF"
    CONTEXT: an embedding with no PDF/PDI, bleeding the LTR level onto later content
    RISK: HIGH
    ATTACK: the unterminated embedding corrupts the direction of everything after its intended span
    GUARD: LRE_FORM ≠ BALANCED_PROOF
  RISK_CASE_004:
    NAME: NESTED_EMBEDDING_CRAFT
    INPUT: "outer<LRE>inner<LRE>...<PDF><PDF> (deep nesting)"
    CONTEXT: nested embeddings crafting a multi-level reorder that survives shallow checks
    RISK: MEDIUM
    ATTACK: deep nesting reorders segments a single-level check does not model
    GUARD: LRE_FORM ≠ EFFECT
  RISK_CASE_005:
    NAME: ENCODED_BIDI_BYPASS
    INPUT: "value%E2%80%AAtail (with a later decode)"
    CONTEXT: a percent-encoded LRE decoded back before display
    RISK: HIGH
    ATTACK: "%E2%80%AA" decodes to the embedding AFTER a check → reorder deception
    GUARD: LRE_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: BIDI_HOMOGLYPH_STACK
    INPUT: "раyраl<LRE> ... (bidi + confusable letters combined)"
    CONTEXT: an embedding stacked with confusable letters to deepen the spoof
    RISK: MEDIUM
    ATTACK: the embedding plus look-alike letters make a hostile string pass a shallow visual review
    GUARD: LRE_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨RLE⟩
    CODEPOINT: U+202B
    NAME: RIGHT-TO-LEFT EMBEDDING
    RISK: HIGH
    RULE: RIGHT_TO_LEFT_EMBEDDING ≠ LEFT_TO_RIGHT_EMBEDDING (mirror embedding, opposite level; a naive filter conflates them)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨LRO⟩
    CODEPOINT: U+202D
    NAME: LEFT-TO-RIGHT OVERRIDE
    RISK: HIGH
    RULE: LEFT_TO_RIGHT_OVERRIDE ≠ LEFT_TO_RIGHT_EMBEDDING (override forces direction; embedding respects strong chars)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨RLO⟩
    CODEPOINT: U+202E
    NAME: RIGHT-TO-LEFT OVERRIDE
    RISK: MEDIUM
    RULE: RIGHT_TO_LEFT_OVERRIDE ≠ LEFT_TO_RIGHT_EMBEDDING
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨LRI⟩
    CODEPOINT: U+2066
    NAME: LEFT-TO-RIGHT ISOLATE
    RISK: MEDIUM
    RULE: LEFT_TO_RIGHT_ISOLATE ≠ LEFT_TO_RIGHT_EMBEDDING (isolate scopes and does not affect surroundings; embedding does)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨PDF⟩
    CODEPOINT: U+202C
    NAME: POP DIRECTIONAL FORMATTING
    RISK: LOW
    RULE: POP_DIRECTIONAL_FORMATTING ≠ LEFT_TO_RIGHT_EMBEDDING (the terminator, not the opener; presence of PDF ≠ balanced)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "a bidi embedding only changes display, so it is cosmetic"
    RESPONSE: LRE_FORM ≠ RENDERING_COSMETIC_PROOF
    RULE: the reorder changes what a human approves vs what executes/stores (logic ≠ display)
  CG2:
    TRIGGER: "an invisible control char cannot be dangerous"
    RESPONSE: LRE_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: invisibility is orthogonal to effect; LRE drives visual/logical desync
  CG3:
    TRIGGER: "embedding is weaker than override, so it is safe"
    RESPONSE: LRE_FORM ≠ WEAKER_MEANS_SAFE_PROOF
    RULE: weaker still reorders and still deceives; an override-only filter misses it
  CG4:
    TRIGGER: "'%E2%80%AA' is safe forever"
    RESPONSE: LRE_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to the embedding before display
  CG5:
    TRIGGER: "stripping LRE stops bidi attacks"
    RESPONSE: LRE_FORM ≠ EFFECT
    RULE: RLE/RLO/LRO/LRI/PDF also participate; a single-char strip misses the family
  CG6:
    TRIGGER: "the presence of a bidi mark means the input is sanitized"
    RESPONSE: LRE_FORM ≠ SANITIZED_PROOF
    RULE: the presence of the sign says nothing about sanitization

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "LRE ... PDF"
      NAME: BALANCED_EMBEDDING_SPAN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: a scoped nested LTR span used to reorder a specific token
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "LRE (no PDF)"
      NAME: UNTERMINATED_BLEED
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: an embedding with no terminator bleeding the level onto later content
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "LRE + LRE nesting"
      NAME: DEEP_NESTING
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: nested embeddings crafting a multi-level reorder
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with LRE are central to visual-order deception.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: LRE reorders a nested run (structure masking), but does not imitate the existence of a verified entity. Its risks are visual/logical desync, not entity mimicry. (Filename spoof is more natural with override; see RLO/LRO.)
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of LRE with RLE (U+202B) / LRO (U+202D) to evade an LRE-only filter
  A2: percent-encoding "%E2%80%AA" to slip past a raw-byte scan
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: embedding code reorder value=safe <LRE> // danger? <PDF>
  B2: override-only filter gap (LRE survives an RLO/LRO strip)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "LRE ... PDF" (SC1) — scoped embedding span
  C2: "LRE (no PDF)" (SC2) — unterminated bleed
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: LRE presented as harmless nested LTR layout inside a code field
  D2: "%E2%80%AA" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: code reorder deceiving a reviewer
  E2: N/A — vector: nested-embedding reorder surviving a shallow single-level check
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: a bidi embedding is cosmetic display only
  EXPECTED: FAIL_RENDERING_COSMETIC_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: an invisible control char cannot be dangerous
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: embedding is weaker than override so it is safe
  EXPECTED: FAIL_WEAKER_MEANS_SAFE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E2%80%AA" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: stripping only overrides stops all bidi attacks
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: the presence of a bidi mark proves the input was sanitized
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to neutralize embeddings AND overrides AND isolates together (the whole Bidi_Control family) without breaking legitimate nested mixed-direction text?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (reject unterminated/nesting-violating bidi + render logical order for review + strip the full family, not just overrides — an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "weaker (embedding) is not safer; an override-only filter is insufficient".
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
