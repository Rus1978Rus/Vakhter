PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_INTERLINEAR_ANNOTATION_ANCHOR_UFFF9_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_INTERLINEAR_ANNOTATION_ANCHOR_UFFF9_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_INTERLINEAR_ANNOTATION_ANCHOR_UFFF9_GEN3_v0_3_EN
CODEPOINT: U+FFF9
VISIBLE_FORM: ⟨IAA⟩
UNICODE_NAME: INTERLINEAR ANNOTATION ANCHOR
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: interlinear annotation anchor / opener of a hidden-annotation span (not for interchange)
CATEGORY_ROADMAP: LLM (invisible annotation-span injection) · PHAGO: — (hidden-payload masking)
GLYPH_NOTE: VISIBLE_FORM uses the marker ⟨IAA⟩; the sign itself (U+FFF9) is an invisible Format char (Cf) and is NEVER written literally here. Examples use ⟨IAA⟩/%EF%BF%B9, never the byte. It opens an interlinear-annotation span (with SEPARATOR U+FFFA and TERMINATOR U+FFFB) that is NOT intended for plain-text interchange.

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
VISIBLE_FORM: ⟨IAA⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: IAA_FORM ≠ EFFECT
SIGN_CATEGORY:
  - an invisible Format char that OPENS an interlinear annotation span
  - legitimate (internal) use: mark where annotated base text begins, paired with SEPARATOR and TERMINATOR
  - it is explicitly NOT intended for plain-text interchange (an internal, out-of-band construct)
  - (misused) opens a hidden span whose annotation content different consumers show, hide, or drop inconsistently → a Trojan-annotation vector

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — being non-printing does not make it inert
  2. NOT_FOR_INTERCHANGE — it is defined for internal use; its presence in interchanged text is anomalous, not normal
  3. NOT_EMPTY_SPAN — it opens a span that can carry hidden annotation content, not nothing
  4. NOT_RENDERED_UNIFORMLY — some consumers show the base text, some the annotation, some drop the span → display disagreement
  5. NOT_ENCODED_SAFE — "%EF%BF%B9" may be decoded back to the anchor later
  6. NOT_AUTHORITY — it does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; it frames a hidden span
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_SELF_CLOSING — an unterminated anchor (no TERMINATOR) leaves an open span whose extent depends on the consumer
  10. NOT_SANITIZED_PROOF — the presence of the char does not mean the input is sanitized
  11. NOT_SINGLE_TEXT_PROOF — the visible base text is not the whole content; a hidden annotation rides inside the span

BASE_FORMULAS:
  IAA_FORM ≠ EFFECT
  IAA_FORM ≠ FOR_INTERCHANGE_PROOF
  IAA_FORM ≠ EMPTY_SPAN_PROOF
  IAA_FORM ≠ RENDERED_UNIFORMLY_PROOF
  IAA_FORM ≠ ENCODED_SAFETY_PROOF
  IAA_FORM ≠ AUTHORITY
  IAA_FORM ≠ EXECUTION_TRIGGER
  IAA_FORM ≠ SELF_CLOSING_PROOF
  IAA_FORM ≠ INVISIBLE_HARMLESS_PROOF
  IAA_FORM ≠ SANITIZED_PROOF
  IAA_FORM ≠ SINGLE_TEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: IAA (ZONE_1) has parallel functions (internal annotation framing vs. invisible hidden-span injection) co-existing without cultural precession. Polysemy of a stable Format char.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: an annotation-framing control with no gestural predecessor; the hidden-span injection misuse is layered on by the digital epoch in parallel with the internal annotation use.

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
    INPUT: "IAA is U+FFF9 in Unicode"
    CONTEXT: naming the char in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAA_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "the anchor opens an interlinear annotation span"
    CONTEXT: describing the internal function in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAA_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <IAA> here"
    CONTEXT: a documentation marker, not the byte
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAA_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "it is not intended for plain-text interchange"
    CONTEXT: describing its intended scope in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAA_FORM ≠ FOR_INTERCHANGE_PROOF
  SAFE_CASE_005:
    INPUT: "it pairs with a separator and a terminator"
    CONTEXT: describing the span structure in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAA_FORM ≠ SELF_CLOSING_PROOF
  SAFE_CASE_006:
    INPUT: "a filter can strip the annotation controls"
    CONTEXT: describing careful sanitization in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAA_FORM ≠ SANITIZED_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: HIDDEN_ANNOTATION_SMUGGLING
    INPUT: "visible base text plus a hidden annotation inside an IAA...SEP...TERM span"
    CONTEXT: an annotation span carrying content some consumers do not display
    RISK: HIGH
    ATTACK: the hidden annotation smuggles data/instructions past a display-only review
    GUARD: IAA_FORM ≠ SINGLE_TEXT_PROOF
  RISK_CASE_002:
    NAME: RENDER_DISAGREEMENT
    INPUT: "one consumer shows the base text, another the annotation"
    CONTEXT: two components resolving the span differently
    RISK: HIGH
    ATTACK: the check sees one string, the executor/renderer another → a bypass in the gap
    GUARD: IAA_FORM ≠ RENDERED_UNIFORMLY_PROOF
  RISK_CASE_003:
    NAME: UNTERMINATED_ANCHOR_BLEED
    INPUT: "an IAA with no TERMINATOR"
    CONTEXT: an open annotation span whose extent depends on the consumer
    RISK: MEDIUM
    ATTACK: the unterminated span swallows following text differently across parsers
    GUARD: IAA_FORM ≠ SELF_CLOSING_PROOF
  RISK_CASE_004:
    NAME: ENCODED_IAA_BYPASS
    INPUT: "value%EF%BF%B9tail (with a later decode)"
    CONTEXT: a percent-encoded anchor decoded back before use
    RISK: HIGH
    ATTACK: "%EF%BF%B9" decodes to the anchor AFTER a check → the hidden span reappears
    GUARD: IAA_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: INTERCHANGE_ANOMALY_IGNORED
    INPUT: "an IAA appearing in interchanged plain text"
    CONTEXT: a pipeline that does not treat the out-of-band control as anomalous
    RISK: MEDIUM
    ATTACK: because it is not expected in interchange, handling is undefined and exploitable
    GUARD: IAA_FORM ≠ FOR_INTERCHANGE_PROOF
  RISK_CASE_006:
    NAME: INVISIBLE_HOMOGLYPH_STACK
    INPUT: "раyраl<IAA>... (annotation control + confusable letters combined)"
    CONTEXT: an anchor stacked with confusable letters to deepen a spoof
    RISK: MEDIUM
    ATTACK: the invisible control plus look-alike letters make a hostile string pass a shallow review
    GUARD: IAA_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨IAS⟩
    CODEPOINT: U+FFFA
    NAME: INTERLINEAR ANNOTATION SEPARATOR
    RISK: HIGH
    RULE: INTERLINEAR_ANNOTATION_SEPARATOR ≠ INTERLINEAR_ANNOTATION_ANCHOR (the divider that begins the hidden annotation; a different role in the same span)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨IAT⟩
    CODEPOINT: U+FFFB
    NAME: INTERLINEAR ANNOTATION TERMINATOR
    RISK: HIGH
    RULE: INTERLINEAR_ANNOTATION_TERMINATOR ≠ INTERLINEAR_ANNOTATION_ANCHOR (the closer; its presence marks, not proves, a balanced span)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨TAG⟩
    CODEPOINT: U+E0001
    NAME: LANGUAGE TAG
    RISK: MEDIUM
    RULE: LANGUAGE_TAG ≠ INTERLINEAR_ANNOTATION_ANCHOR (another out-of-band invisible smuggling mechanism; a different construct)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨ZWSP⟩
    CODEPOINT: U+200B
    NAME: ZERO WIDTH SPACE
    RISK: LOW
    RULE: ZERO_WIDTH_SPACE ≠ INTERLINEAR_ANNOTATION_ANCHOR (a single break-opportunity invisible, not a span opener)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨OBJ⟩
    CODEPOINT: U+FFFC
    NAME: OBJECT REPLACEMENT CHARACTER
    RISK: LOW
    RULE: OBJECT_REPLACEMENT_CHARACTER ≠ INTERLINEAR_ANNOTATION_ANCHOR (a neighbouring special that stands in for an embedded object; different purpose)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "it is a normal interchange character"
    RESPONSE: IAA_FORM ≠ FOR_INTERCHANGE_PROOF
    RULE: it is defined for internal use; in interchanged text it is anomalous
  CG2:
    TRIGGER: "an invisible char cannot be dangerous"
    RESPONSE: IAA_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: invisibility is orthogonal to effect; the anchor frames a hidden span
  CG3:
    TRIGGER: "the span is empty, so nothing is hidden"
    RESPONSE: IAA_FORM ≠ EMPTY_SPAN_PROOF
    RULE: it can carry real annotation content some consumers do not show
  CG4:
    TRIGGER: "'%EF%BF%B9' is safe forever"
    RESPONSE: IAA_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to the anchor before use
  CG5:
    TRIGGER: "every consumer renders the span the same way"
    RESPONSE: IAA_FORM ≠ RENDERED_UNIFORMLY_PROOF
    RULE: consumers show base, annotation, or nothing — they disagree
  CG6:
    TRIGGER: "the anchor closes itself"
    RESPONSE: IAA_FORM ≠ SELF_CLOSING_PROOF
    RULE: without a TERMINATOR the span is open and its extent is consumer-dependent

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "IAA ... IAS ... IAT (full annotation span)"
      NAME: HIDDEN_ANNOTATION
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: a balanced span whose annotation part is hidden from a display-only review
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "IAA with no IAT"
      NAME: UNTERMINATED_SPAN
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: an open span swallowing following text differently across parsers
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "IAA + confusable letters"
      NAME: INVISIBLE_HOMOGLYPH_STACK
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: an annotation control combined with look-alike letters for a spoof
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — the anchor's meaning is inherently about the span it opens.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: IAA frames a hidden annotation payload (hidden-payload masking), but does not imitate the existence of a verified entity. Its risks are hidden-span smuggling and render disagreement, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution/combination with SEPARATOR (U+FFFA) / TERMINATOR (U+FFFB) or other invisibles to vary the construct
  A2: percent-encoding "%EF%BF%B9" to slip past a raw-byte scan
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: hidden-annotation smuggling (content inside IAA...SEP...TERM a display-only review misses)
  B2: render disagreement (one consumer shows base, another the annotation)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "IAA with no IAT" (SC2) — unterminated span
  C2: "IAA ... IAS ... IAT" (SC1) — hidden annotation
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: IAA presented as a "normal interchange character" so its span is not treated as anomalous
  D2: "%EF%BF%B9" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: hidden-annotation smuggling invisible to a reviewer
  E2: N/A — vector: interchange-anomaly ignored, leaving handling undefined
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
  CLAIM: the annotation span is empty
  EXPECTED: FAIL_EMPTY_SPAN_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%EF%BF%B9" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: every consumer renders the span identically
  EXPECTED: FAIL_RENDERED_UNIFORMLY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: the anchor closes itself
  EXPECTED: FAIL_SELF_CLOSING_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to treat the interlinear annotation controls (U+FFF9/FFFA/FFFB) as out-of-band anomalies in interchanged text — stripping or rejecting the whole span and surfacing any hidden annotation — without breaking a legitimate internal annotation pipeline?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (a normalizer that rejects/flags annotation spans in interchange, pairs anchor-separator-terminator, and decodes-and-shows hidden annotation to the reviewer/model boundary — an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "the anchor opens a hidden, not-for-interchange annotation span; its content is not the visible text and consumers render it inconsistently".
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
