PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_INTERLINEAR_ANNOTATION_SEPARATOR_UFFFA_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_INTERLINEAR_ANNOTATION_SEPARATOR_UFFFA_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_INTERLINEAR_ANNOTATION_SEPARATOR_UFFFA_GEN3_v0_3_EN
CODEPOINT: U+FFFA
VISIBLE_FORM: ⟨IAS⟩
UNICODE_NAME: INTERLINEAR ANNOTATION SEPARATOR
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: interlinear annotation separator / the boundary where base text ends and hidden annotation begins
CATEGORY_ROADMAP: LLM (invisible annotation-payload injection) · PHAGO: — (hidden-payload masking)
GLYPH_NOTE: VISIBLE_FORM uses the marker ⟨IAS⟩; the sign itself (U+FFFA) is an invisible Format char (Cf) and is NEVER written literally here. Examples use ⟨IAS⟩/%EF%BF%BA, never the byte. It divides the base text from the annotation inside an anchor (U+FFF9) … terminator (U+FFFB) span; everything after it up to the terminator is the hidden annotation.

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
VISIBLE_FORM: ⟨IAS⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: IAS_FORM ≠ EFFECT
SIGN_CATEGORY:
  - an invisible Format char that DIVIDES the annotated base text from the annotation inside an annotation span
  - legitimate (internal) use: mark the transition from base to annotation, between anchor and terminator
  - it is explicitly NOT intended for plain-text interchange (an internal, out-of-band construct)
  - (misused) the boundary after which the smuggled annotation payload begins — the carrier edge a display-only review does not cross

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — being non-printing does not make it inert
  2. NOT_FOR_INTERCHANGE — it is defined for internal use; its presence in interchanged text is anomalous, not normal
  3. NOT_BASE_IS_WHOLE — text before the separator is only the base; the annotation after it is real content
  4. NOT_ANCHOR — U+FFFA is the separator, not the opener (U+FFF9); it presumes an already-open span
  5. NOT_ENCODED_SAFE — "%EF%BF%BA" may be decoded back to the separator later
  6. NOT_AUTHORITY — it does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; it delimits a hidden payload
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_TERMINATOR — it does not close the span; a TERMINATOR (U+FFFB) does, and its absence leaves the annotation open
  10. NOT_SANITIZED_PROOF — the presence of the char does not mean the input is sanitized
  11. NOT_SINGLE_TEXT_PROOF — the visible base text is not the whole content; a hidden annotation follows the separator

BASE_FORMULAS:
  IAS_FORM ≠ EFFECT
  IAS_FORM ≠ FOR_INTERCHANGE_PROOF
  IAS_FORM ≠ BASE_IS_WHOLE_PROOF
  IAS_FORM ≠ ANCHOR_PROOF
  IAS_FORM ≠ ENCODED_SAFETY_PROOF
  IAS_FORM ≠ AUTHORITY
  IAS_FORM ≠ EXECUTION_TRIGGER
  IAS_FORM ≠ TERMINATOR_PROOF
  IAS_FORM ≠ INVISIBLE_HARMLESS_PROOF
  IAS_FORM ≠ SANITIZED_PROOF
  IAS_FORM ≠ SINGLE_TEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: IAS (ZONE_1) has parallel functions (internal base/annotation division vs. invisible payload-boundary injection) co-existing without cultural precession. Polysemy of a stable Format char.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: an annotation-dividing control with no gestural predecessor; the payload-boundary misuse is layered on by the digital epoch in parallel with the internal annotation use.

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
    INPUT: "IAS is U+FFFA in Unicode"
    CONTEXT: naming the char in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAS_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "the separator divides base text from annotation"
    CONTEXT: describing the internal function in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAS_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <IAS> here"
    CONTEXT: a documentation marker, not the byte
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAS_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "it is not intended for plain-text interchange"
    CONTEXT: describing its intended scope in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAS_FORM ≠ FOR_INTERCHANGE_PROOF
  SAFE_CASE_005:
    INPUT: "it is the separator, not the anchor"
    CONTEXT: distinguishing it from U+FFF9 in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAS_FORM ≠ ANCHOR_PROOF
  SAFE_CASE_006:
    INPUT: "it does not close the span"
    CONTEXT: distinguishing it from the terminator in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAS_FORM ≠ TERMINATOR_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: PAYLOAD_AFTER_SEPARATOR
    INPUT: "base<IAS>hidden annotation payload up to the terminator"
    CONTEXT: the annotation after the separator carrying content a display-only review does not read
    RISK: HIGH
    ATTACK: the payload after the separator smuggles data/instructions past a look-only step
    GUARD: IAS_FORM ≠ BASE_IS_WHOLE_PROOF
  RISK_CASE_002:
    NAME: RENDER_DISAGREEMENT
    INPUT: "one consumer shows the base (before IAS), another the annotation (after IAS)"
    CONTEXT: two components resolving the span differently around the separator
    RISK: HIGH
    ATTACK: the check reads the base, the executor the annotation → a bypass in the gap
    GUARD: IAS_FORM ≠ SINGLE_TEXT_PROOF
  RISK_CASE_003:
    NAME: SEPARATOR_WITHOUT_ANCHOR
    INPUT: "an IAS with no preceding anchor"
    CONTEXT: a stray separator that a lenient parser may still act on
    RISK: MEDIUM
    ATTACK: an out-of-context separator triggers annotation handling where none was opened
    GUARD: IAS_FORM ≠ ANCHOR_PROOF
  RISK_CASE_004:
    NAME: ENCODED_IAS_BYPASS
    INPUT: "value%EF%BF%BAtail (with a later decode)"
    CONTEXT: a percent-encoded separator decoded back before use
    RISK: HIGH
    ATTACK: "%EF%BF%BA" decodes to the separator AFTER a check → the hidden payload boundary reappears
    GUARD: IAS_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: UNTERMINATED_ANNOTATION
    INPUT: "an IAS whose annotation is never closed by a terminator"
    CONTEXT: an open annotation whose extent depends on the consumer
    RISK: MEDIUM
    ATTACK: the unterminated annotation swallows following text differently across parsers
    GUARD: IAS_FORM ≠ TERMINATOR_PROOF
  RISK_CASE_006:
    NAME: INVISIBLE_HOMOGLYPH_STACK
    INPUT: "раyраl<IAS>... (annotation control + confusable letters combined)"
    CONTEXT: a separator stacked with confusable letters to deepen a spoof
    RISK: MEDIUM
    ATTACK: the invisible control plus look-alike letters make a hostile string pass a shallow review
    GUARD: IAS_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨IAA⟩
    CODEPOINT: U+FFF9
    NAME: INTERLINEAR ANNOTATION ANCHOR
    RISK: HIGH
    RULE: INTERLINEAR_ANNOTATION_ANCHOR ≠ INTERLINEAR_ANNOTATION_SEPARATOR (the opener of the span; the separator presumes it and divides base from annotation)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨IAT⟩
    CODEPOINT: U+FFFB
    NAME: INTERLINEAR ANNOTATION TERMINATOR
    RISK: HIGH
    RULE: INTERLINEAR_ANNOTATION_TERMINATOR ≠ INTERLINEAR_ANNOTATION_SEPARATOR (the closer; the separator only divides, it does not close)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨TAG-SP⟩
    CODEPOINT: U+E0020
    NAME: TAG SPACE
    RISK: MEDIUM
    RULE: TAG_SPACE ≠ INTERLINEAR_ANNOTATION_SEPARATOR (a tag-block invisible carrying ASCII; a different smuggling mechanism)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨ZWSP⟩
    CODEPOINT: U+200B
    NAME: ZERO WIDTH SPACE
    RISK: LOW
    RULE: ZERO_WIDTH_SPACE ≠ INTERLINEAR_ANNOTATION_SEPARATOR (a single break-opportunity invisible, not an annotation divider)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨OBJ⟩
    CODEPOINT: U+FFFC
    NAME: OBJECT REPLACEMENT CHARACTER
    RISK: LOW
    RULE: OBJECT_REPLACEMENT_CHARACTER ≠ INTERLINEAR_ANNOTATION_SEPARATOR (a neighbouring special standing in for an embedded object; different purpose)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "it is a normal interchange character"
    RESPONSE: IAS_FORM ≠ FOR_INTERCHANGE_PROOF
    RULE: it is defined for internal use; in interchanged text it is anomalous
  CG2:
    TRIGGER: "an invisible char cannot be dangerous"
    RESPONSE: IAS_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: invisibility is orthogonal to effect; the separator bounds a hidden payload
  CG3:
    TRIGGER: "the base text is the whole content"
    RESPONSE: IAS_FORM ≠ BASE_IS_WHOLE_PROOF
    RULE: the annotation after the separator is real content, not nothing
  CG4:
    TRIGGER: "'%EF%BF%BA' is safe forever"
    RESPONSE: IAS_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to the separator before use
  CG5:
    TRIGGER: "the separator opens the span"
    RESPONSE: IAS_FORM ≠ ANCHOR_PROOF
    RULE: the anchor (U+FFF9) opens; the separator only divides an already-open span
  CG6:
    TRIGGER: "the separator closes the annotation"
    RESPONSE: IAS_FORM ≠ TERMINATOR_PROOF
    RULE: the terminator (U+FFFB) closes; without it the annotation stays open

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "IAA ... IAS <payload> IAT"
      NAME: HIDDEN_ANNOTATION_PAYLOAD
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: the payload after the separator hidden from a display-only review
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "IAS with no anchor or no terminator"
      NAME: MALFORMED_SPAN
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: a stray/unbalanced separator handled inconsistently across parsers
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "IAS + confusable letters"
      NAME: INVISIBLE_HOMOGLYPH_STACK
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: an annotation control combined with look-alike letters for a spoof
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — the separator's meaning is inherently about the span it divides.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: IAS bounds a hidden annotation payload (hidden-payload masking), but does not imitate the existence of a verified entity. Its risks are hidden-payload smuggling and render disagreement, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution/combination with ANCHOR (U+FFF9) / TERMINATOR (U+FFFB) or other invisibles to vary the construct
  A2: percent-encoding "%EF%BF%BA" to slip past a raw-byte scan
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: payload after separator (hidden annotation a display-only review misses)
  B2: render disagreement (one consumer reads base, another the annotation)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "IAS with no anchor or no terminator" (SC2) — malformed span
  C2: "IAA ... IAS <payload> IAT" (SC1) — hidden annotation payload
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: IAS presented as a "normal interchange character" so its payload is not treated as anomalous
  D2: "%EF%BF%BA" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: hidden-payload smuggling invisible to a reviewer
  E2: N/A — vector: separator without anchor triggering annotation handling out of context
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: it is a normal interchange character
  EXPECTED: FAIL_FOR_INTERCHANGE_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: an invisible char cannot be dangerous
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: the base text is the whole content
  EXPECTED: FAIL_BASE_IS_WHOLE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%EF%BF%BA" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: the separator opens the span
  EXPECTED: FAIL_ANCHOR_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: the separator closes the annotation
  EXPECTED: FAIL_TERMINATOR_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to treat the interlinear annotation controls (U+FFF9/FFFA/FFFB) as out-of-band anomalies in interchanged text — stripping or rejecting the whole span, surfacing the annotation after the separator, and rejecting malformed/unbalanced spans — without breaking a legitimate internal annotation pipeline?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (a normalizer that pairs anchor-separator-terminator, rejects stray/unbalanced controls, and decodes-and-shows the annotation payload to the reviewer/model boundary — an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "the separator marks where the base ends and the hidden annotation begins; the base text is not the whole content".
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
