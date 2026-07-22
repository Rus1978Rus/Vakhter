PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_INTERLINEAR_ANNOTATION_TERMINATOR_UFFFB_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_INTERLINEAR_ANNOTATION_TERMINATOR_UFFFB_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_INTERLINEAR_ANNOTATION_TERMINATOR_UFFFB_GEN3_v0_3_EN
CODEPOINT: U+FFFB
VISIBLE_FORM: ⟨IAT⟩
UNICODE_NAME: INTERLINEAR ANNOTATION TERMINATOR
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: interlinear annotation terminator / the closer of an annotation span (presence != balance)
CATEGORY_ROADMAP: LLM (invisible annotation-span injection) · PHAGO: — (hidden-payload masking)
GLYPH_NOTE: VISIBLE_FORM uses the marker ⟨IAT⟩; the sign itself (U+FFFB) is an invisible Format char (Cf) and is NEVER written literally here. Examples use ⟨IAT⟩/%EF%BF%BB, never the byte. It closes an interlinear-annotation span opened by an anchor (U+FFF9) and divided by a separator (U+FFFA); it is NOT for plain-text interchange.

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
VISIBLE_FORM: ⟨IAT⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: IAT_FORM ≠ EFFECT
SIGN_CATEGORY:
  - an invisible Format char that CLOSES an interlinear annotation span
  - legitimate (internal) use: end the annotation opened by an anchor and divided by a separator
  - it is explicitly NOT intended for plain-text interchange (an internal, out-of-band construct)
  - (misused) a terminator whose presence does not prove a balanced span, and whose absence leaves an annotation open

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — being non-printing does not make it inert
  2. NOT_FOR_INTERCHANGE — it is defined for internal use; its presence in interchanged text is anomalous, not normal
  3. NOT_BALANCED_PROOF — a terminator does not prove a matching anchor/separator preceded it; presence is not balance
  4. NOT_ANCHOR — U+FFFB is the closer, not the opener (U+FFF9)
  5. NOT_ENCODED_SAFE — "%EF%BF%BB" may be decoded back to the terminator later
  6. NOT_AUTHORITY — it does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; it ends a hidden span
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_SEPARATOR — it does not divide base from annotation; a SEPARATOR (U+FFFA) does
  10. NOT_SANITIZED_PROOF — the presence of the char does not mean the input is sanitized
  11. NOT_CONTENT_CLEARED_PROOF — closing the span does not remove the hidden annotation the span carried

BASE_FORMULAS:
  IAT_FORM ≠ EFFECT
  IAT_FORM ≠ FOR_INTERCHANGE_PROOF
  IAT_FORM ≠ BALANCED_PROOF
  IAT_FORM ≠ ANCHOR_PROOF
  IAT_FORM ≠ ENCODED_SAFETY_PROOF
  IAT_FORM ≠ AUTHORITY
  IAT_FORM ≠ EXECUTION_TRIGGER
  IAT_FORM ≠ SEPARATOR_PROOF
  IAT_FORM ≠ INVISIBLE_HARMLESS_PROOF
  IAT_FORM ≠ SANITIZED_PROOF
  IAT_FORM ≠ CONTENT_CLEARED_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: IAT (ZONE_1) has parallel functions (internal annotation closing vs. invisible unbalanced-span injection) co-existing without cultural precession. Polysemy of a stable Format char.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: an annotation-closing control with no gestural predecessor; the unbalanced-span misuse is layered on by the digital epoch in parallel with the internal annotation use.

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
    INPUT: "IAT is U+FFFB in Unicode"
    CONTEXT: naming the char in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAT_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "the terminator closes an interlinear annotation span"
    CONTEXT: describing the internal function in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAT_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <IAT> here"
    CONTEXT: a documentation marker, not the byte
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAT_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "it is not intended for plain-text interchange"
    CONTEXT: describing its intended scope in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAT_FORM ≠ FOR_INTERCHANGE_PROOF
  SAFE_CASE_005:
    INPUT: "it is the terminator, not the anchor"
    CONTEXT: distinguishing it from U+FFF9 in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAT_FORM ≠ ANCHOR_PROOF
  SAFE_CASE_006:
    INPUT: "it does not divide base from annotation"
    CONTEXT: distinguishing it from the separator in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAT_FORM ≠ SEPARATOR_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: STRAY_TERMINATOR
    INPUT: "an IAT with no preceding anchor/separator"
    CONTEXT: a lone terminator a lenient parser may still act on
    RISK: HIGH
    ATTACK: an out-of-context terminator ends an annotation state that was never opened, mis-tracking parsing
    GUARD: IAT_FORM ≠ BALANCED_PROOF
  RISK_CASE_002:
    NAME: PRESENCE_NOT_BALANCE
    INPUT: "a span that has a terminator but a mismatched or missing anchor"
    CONTEXT: treating the presence of a terminator as proof of a well-formed span
    RISK: HIGH
    ATTACK: the terminator is taken as a balance signal, so a malformed span is accepted
    GUARD: IAT_FORM ≠ BALANCED_PROOF
  RISK_CASE_003:
    NAME: CONTENT_NOT_CLEARED
    INPUT: "an annotation closed by IAT whose hidden payload still rode through"
    CONTEXT: assuming closing the span removes the smuggled annotation
    RISK: MEDIUM
    ATTACK: the payload was already carried; the terminator only ends the span, it does not delete content
    GUARD: IAT_FORM ≠ CONTENT_CLEARED_PROOF
  RISK_CASE_004:
    NAME: ENCODED_IAT_BYPASS
    INPUT: "value%EF%BF%BBtail (with a later decode)"
    CONTEXT: a percent-encoded terminator decoded back before use
    RISK: HIGH
    ATTACK: "%EF%BF%BB" decodes to the terminator AFTER a check → the span structure reappears
    GUARD: IAT_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: INTERCHANGE_ANOMALY_IGNORED
    INPUT: "an IAT appearing in interchanged plain text"
    CONTEXT: a pipeline that does not treat the out-of-band control as anomalous
    RISK: MEDIUM
    ATTACK: because it is not expected in interchange, handling is undefined and exploitable
    GUARD: IAT_FORM ≠ FOR_INTERCHANGE_PROOF
  RISK_CASE_006:
    NAME: INVISIBLE_HOMOGLYPH_STACK
    INPUT: "раyраl<IAT>... (annotation control + confusable letters combined)"
    CONTEXT: a terminator stacked with confusable letters to deepen a spoof
    RISK: MEDIUM
    ATTACK: the invisible control plus look-alike letters make a hostile string pass a shallow review
    GUARD: IAT_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨IAA⟩
    CODEPOINT: U+FFF9
    NAME: INTERLINEAR ANNOTATION ANCHOR
    RISK: HIGH
    RULE: INTERLINEAR_ANNOTATION_ANCHOR ≠ INTERLINEAR_ANNOTATION_TERMINATOR (the opener; the terminator closes what the anchor opened)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨IAS⟩
    CODEPOINT: U+FFFA
    NAME: INTERLINEAR ANNOTATION SEPARATOR
    RISK: HIGH
    RULE: INTERLINEAR_ANNOTATION_SEPARATOR ≠ INTERLINEAR_ANNOTATION_TERMINATOR (the divider between base and annotation; the terminator only closes)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨OBJ⟩
    CODEPOINT: U+FFFC
    NAME: OBJECT REPLACEMENT CHARACTER
    RISK: MEDIUM
    RULE: OBJECT_REPLACEMENT_CHARACTER ≠ INTERLINEAR_ANNOTATION_TERMINATOR (a neighbouring special standing in for an embedded object; not a span terminator)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨PDI⟩
    CODEPOINT: U+2069
    NAME: POP DIRECTIONAL ISOLATE
    RISK: LOW
    RULE: POP_DIRECTIONAL_ISOLATE ≠ INTERLINEAR_ANNOTATION_TERMINATOR (a bidi isolate terminator; a different closing construct where presence also is not balance)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨ZWSP⟩
    CODEPOINT: U+200B
    NAME: ZERO WIDTH SPACE
    RISK: LOW
    RULE: ZERO_WIDTH_SPACE ≠ INTERLINEAR_ANNOTATION_TERMINATOR (a single break-opportunity invisible, not a span closer)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "it is a normal interchange character"
    RESPONSE: IAT_FORM ≠ FOR_INTERCHANGE_PROOF
    RULE: it is defined for internal use; in interchanged text it is anomalous
  CG2:
    TRIGGER: "an invisible char cannot be dangerous"
    RESPONSE: IAT_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: invisibility is orthogonal to effect; a stray terminator mis-tracks span parsing
  CG3:
    TRIGGER: "a terminator means the span is balanced"
    RESPONSE: IAT_FORM ≠ BALANCED_PROOF
    RULE: presence of a terminator does not prove a matching anchor/separator preceded it
  CG4:
    TRIGGER: "'%EF%BF%BB' is safe forever"
    RESPONSE: IAT_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to the terminator before use
  CG5:
    TRIGGER: "the terminator opens or divides the span"
    RESPONSE: IAT_FORM ≠ ANCHOR_PROOF
    RULE: the anchor opens and the separator divides; the terminator only closes
  CG6:
    TRIGGER: "closing the span removes the hidden annotation"
    RESPONSE: IAT_FORM ≠ CONTENT_CLEARED_PROOF
    RULE: the payload already rode through; closing does not delete content

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "IAA ... IAS ... IAT (balanced span)"
      NAME: CLOSED_ANNOTATION
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: a well-formed span whose annotation part is still hidden from a display-only review
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "IAT with no anchor"
      NAME: STRAY_CLOSE
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: a lone terminator mis-tracking annotation state across parsers
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "IAT + confusable letters"
      NAME: INVISIBLE_HOMOGLYPH_STACK
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: an annotation control combined with look-alike letters for a spoof
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — the terminator's meaning is inherently about the span it closes.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: IAT closes a hidden annotation span (hidden-payload masking), but does not imitate the existence of a verified entity. Its risks are unbalanced-span parsing and payload persistence, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution/combination with ANCHOR (U+FFF9) / SEPARATOR (U+FFFA) or other invisibles to vary the construct
  A2: percent-encoding "%EF%BF%BB" to slip past a raw-byte scan
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: presence-not-balance (a terminator accepted as proof of a well-formed span)
  B2: content-not-cleared (closing the span assumed to remove the smuggled annotation)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "IAT with no anchor" (SC2) — stray close
  C2: "IAA ... IAS ... IAT" (SC1) — closed annotation still hiding payload
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: IAT presented as a "normal interchange character" so its span is not treated as anomalous
  D2: "%EF%BF%BB" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: unbalanced-span parsing via a stray terminator
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
  CLAIM: a terminator proves the span is balanced
  EXPECTED: FAIL_BALANCED_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%EF%BF%BB" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: the terminator opens or divides the span
  EXPECTED: FAIL_ANCHOR_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: closing the span removes the hidden annotation
  EXPECTED: FAIL_CONTENT_CLEARED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to enforce well-formed anchor-separator-terminator triples in interchanged text — rejecting stray or unbalanced terminators and not treating a terminator as balance proof — while surfacing any annotation the closed span carried?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (a stack-based checker that pairs anchor-separator-terminator, rejects unbalanced/stray controls, and decodes-and-shows the annotation payload to the reviewer/model boundary — an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "a terminator closes but does not prove balance; its presence is not a well-formed span and closing does not delete the carried annotation".
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
