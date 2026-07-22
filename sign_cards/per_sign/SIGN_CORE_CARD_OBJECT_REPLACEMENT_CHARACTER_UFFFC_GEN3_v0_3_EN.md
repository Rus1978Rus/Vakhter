PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_OBJECT_REPLACEMENT_CHARACTER_UFFFC_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_OBJECT_REPLACEMENT_CHARACTER_UFFFC_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_OBJECT_REPLACEMENT_CHARACTER_UFFFC_GEN3_v0_3_EN
CODEPOINT: U+FFFC
VISIBLE_FORM: ⟨OBJ⟩
UNICODE_NAME: OBJECT REPLACEMENT CHARACTER
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: object replacement character / a placeholder standing in for out-of-band embedded content
CATEGORY_ROADMAP: LLM (embedded-object placeholder injection) · PHAGO: — (embedded-payload masking)
GLYPH_NOTE: VISIBLE_FORM uses the marker ⟨OBJ⟩; the sign itself (U+FFFC) is a Symbol (category So) usually shown as a placeholder box and is NOT written literally here — a literal U+FFFC would drop a placeholder into this document. Examples use ⟨OBJ⟩/%EF%BF%BC, never the byte. It marks the position of an embedded object (image/OLE/attachment) whose real content rides out-of-band.

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
VISIBLE_FORM: ⟨OBJ⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: OBJ_FORM ≠ EFFECT
SIGN_CATEGORY:
  - a placeholder Symbol (category So) marking WHERE an embedded object sits in text
  - legitimate use: represent the position of an inline image / OLE object / attachment in a rich-text stream
  - the placeholder glyph is NOT the object; the real embedded content is carried out-of-band
  - (misused) a marker for hidden embedded content a plain-text view does not show, or a token a consumer resolves by fetching/rendering an object

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_THE_OBJECT — the placeholder stands in for an object; the actual content (image/OLE/attachment) is elsewhere
  2. NOT_EMPTY — its presence means embedded content is attached, not that the text is complete on its own
  3. NOT_PLAIN_TEXT_COMPLETE — a plain-text extraction shows the placeholder but drops the embedded payload
  4. NOT_INERT_ON_RESOLVE — resolving the placeholder may fetch or render an object with its own risks (SSRF, macro, parser)
  5. NOT_ENCODED_SAFE — "%EF%BF%BC" may be decoded back to the placeholder later
  6. NOT_AUTHORITY — it does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; the object it points to may
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_A_SPACE — although often rendered as a box/gap, it is a content placeholder, not whitespace
  10. NOT_SANITIZED_PROOF — the presence of the char does not mean the input (or the embedded object) is sanitized
  11. NOT_SINGLE_STREAM_PROOF — the visible text and the embedded object are two streams; the placeholder ties them but is not the whole

BASE_FORMULAS:
  OBJ_FORM ≠ EFFECT
  OBJ_FORM ≠ THE_OBJECT_PROOF
  OBJ_FORM ≠ EMPTY_PROOF
  OBJ_FORM ≠ PLAIN_TEXT_COMPLETE_PROOF
  OBJ_FORM ≠ INERT_ON_RESOLVE_PROOF
  OBJ_FORM ≠ ENCODED_SAFETY_PROOF
  OBJ_FORM ≠ AUTHORITY
  OBJ_FORM ≠ EXECUTION_TRIGGER
  OBJ_FORM ≠ A_SPACE_PROOF
  OBJ_FORM ≠ SANITIZED_PROOF
  OBJ_FORM ≠ SINGLE_STREAM_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: OBJ (ZONE_1) has parallel functions (legitimate embedded-object placeholder vs. hidden-embedded-content injection) co-existing without cultural precession. Polysemy of a stable placeholder symbol.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a content-placeholder symbol with no gestural predecessor; the hidden-embedded-content misuse is layered on by the digital epoch in parallel with legitimate rich-text embedding.

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
    INPUT: "OBJ is U+FFFC in Unicode"
    CONTEXT: naming the char in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: OBJ_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "the object replacement character marks an embedded object position"
    CONTEXT: describing the legitimate function in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: OBJ_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <OBJ> here"
    CONTEXT: a documentation marker, not the byte
    EXPECTED: INFO
    RISK: NONE
    GUARD: OBJ_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "the placeholder is not the embedded object itself"
    CONTEXT: describing the placeholder relationship in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: OBJ_FORM ≠ THE_OBJECT_PROOF
  SAFE_CASE_005:
    INPUT: "a plain-text extract shows the placeholder but not the object"
    CONTEXT: describing extraction behaviour in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: OBJ_FORM ≠ PLAIN_TEXT_COMPLETE_PROOF
  SAFE_CASE_006:
    INPUT: "it is a content placeholder, not whitespace"
    CONTEXT: distinguishing it from a space in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: OBJ_FORM ≠ A_SPACE_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: HIDDEN_EMBEDDED_CONTENT
    INPUT: "visible text plus an OBJ pointing to an out-of-band object"
    CONTEXT: an embedded object a plain-text review never sees
    RISK: HIGH
    ATTACK: the object carries data/an exploit the text view drops, smuggling it past a look-only step
    GUARD: OBJ_FORM ≠ PLAIN_TEXT_COMPLETE_PROOF
  RISK_CASE_002:
    NAME: RESOLVE_SIDE_EFFECT
    INPUT: "a consumer that fetches/renders the object referenced by the placeholder"
    CONTEXT: resolving the placeholder triggering a network fetch or a parser
    RISK: HIGH
    ATTACK: resolving the object causes SSRF, a macro run, or a document-parser exploit
    GUARD: OBJ_FORM ≠ INERT_ON_RESOLVE_PROOF
  RISK_CASE_003:
    NAME: STREAM_DESYNC
    INPUT: "the text stream and the object stream disagreeing on what is present"
    CONTEXT: a check reading the text but not the embedded object
    RISK: HIGH
    ATTACK: the checker sees benign text, the renderer/executor sees a hostile object → bypass
    GUARD: OBJ_FORM ≠ SINGLE_STREAM_PROOF
  RISK_CASE_004:
    NAME: ENCODED_OBJ_BYPASS
    INPUT: "value%EF%BF%BCtail (with a later decode)"
    CONTEXT: a percent-encoded placeholder decoded back before use
    RISK: MEDIUM
    ATTACK: "%EF%BF%BC" decodes to the placeholder AFTER a check → the embedded-object reference reappears
    GUARD: OBJ_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: PLACEHOLDER_ASSUMED_EMPTY
    INPUT: "a pipeline treating an OBJ as an empty/whitespace slot"
    CONTEXT: assuming the placeholder carries nothing
    RISK: MEDIUM
    ATTACK: the assumed-empty slot actually anchors real embedded content that is processed elsewhere
    GUARD: OBJ_FORM ≠ EMPTY_PROOF
  RISK_CASE_006:
    NAME: INVISIBLE_HOMOGLYPH_STACK
    INPUT: "раyраl<OBJ>... (placeholder + confusable letters combined)"
    CONTEXT: a placeholder stacked with confusable letters to deepen a spoof
    RISK: LOW
    ATTACK: the placeholder plus look-alike letters make a crafted string read as a normal entry
    GUARD: OBJ_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨REPL⟩
    CODEPOINT: U+FFFD
    NAME: REPLACEMENT CHARACTER
    RISK: HIGH
    RULE: REPLACEMENT_CHARACTER ≠ OBJECT_REPLACEMENT_CHARACTER (U+FFFD marks a decode error / invalid byte; U+FFFC marks a valid embedded object — opposite meanings, adjacent codepoints)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨IAT⟩
    CODEPOINT: U+FFFB
    NAME: INTERLINEAR ANNOTATION TERMINATOR
    RISK: MEDIUM
    RULE: INTERLINEAR_ANNOTATION_TERMINATOR ≠ OBJECT_REPLACEMENT_CHARACTER (a neighbouring annotation control; not an object placeholder)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨SUB⟩
    CODEPOINT: U+001A
    NAME: SUBSTITUTE
    RISK: MEDIUM
    RULE: SUBSTITUTE ≠ OBJECT_REPLACEMENT_CHARACTER (a C0 control historically used as a replacement; a different mechanism)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨NBSP⟩
    CODEPOINT: U+00A0
    NAME: NO-BREAK SPACE
    RISK: LOW
    RULE: NO_BREAK_SPACE ≠ OBJECT_REPLACEMENT_CHARACTER (a space that may render as a similar gap; not a content placeholder)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨GEOM-BOX⟩
    CODEPOINT: U+25A1
    NAME: WHITE SQUARE
    RISK: LOW
    RULE: WHITE_SQUARE ≠ OBJECT_REPLACEMENT_CHARACTER (a visible box glyph the placeholder is often mistaken for; a plain geometric symbol)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "the placeholder is the object"
    RESPONSE: OBJ_FORM ≠ THE_OBJECT_PROOF
    RULE: it stands in for an object carried out-of-band; the glyph is not the content
  CG2:
    TRIGGER: "the text extract is the whole message"
    RESPONSE: OBJ_FORM ≠ PLAIN_TEXT_COMPLETE_PROOF
    RULE: the extract drops the embedded object; the placeholder marks what is missing
  CG3:
    TRIGGER: "resolving the placeholder is harmless"
    RESPONSE: OBJ_FORM ≠ INERT_ON_RESOLVE_PROOF
    RULE: fetching/rendering the object can trigger SSRF, a macro, or a parser exploit
  CG4:
    TRIGGER: "'%EF%BF%BC' is safe forever"
    RESPONSE: OBJ_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to the placeholder before use
  CG5:
    TRIGGER: "an OBJ is an empty slot"
    RESPONSE: OBJ_FORM ≠ EMPTY_PROOF
    RULE: it anchors real embedded content processed elsewhere
  CG6:
    TRIGGER: "text and object are one stream, so checking text is enough"
    RESPONSE: OBJ_FORM ≠ SINGLE_STREAM_PROOF
    RULE: the object is a separate stream; checking text alone misses it

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "text + OBJ + out-of-band object"
      NAME: EMBEDDED_PAYLOAD
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: an embedded object hidden from a plain-text review and resolved by a renderer
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "OBJ with a dangling/attacker-controlled object reference"
      NAME: RESOLVE_TARGET_ABUSE
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: a placeholder pointing at a fetch/parse target an attacker controls
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "OBJ + confusable letters"
      NAME: PLACEHOLDER_HOMOGLYPH_STACK
      RISK_LEVEL: LOW
      POSSIBLE_CONTEXTS: a placeholder combined with look-alike letters for a spoof
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — the placeholder's meaning is inherently about the embedded object it ties in.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: OBJ anchors an out-of-band embedded payload (embedded-payload masking), but does not imitate the existence of a verified entity. Its risks are hidden embedded content and resolve-time side effects, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: confusion with REPLACEMENT CHARACTER (U+FFFD) / a box glyph (U+25A1) to disguise the placeholder's meaning
  A2: percent-encoding "%EF%BF%BC" to slip past a raw-byte scan
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: hidden embedded content (an OBJ pointing to an object a text review misses)
  B2: resolve side effect (fetching/rendering the object triggers SSRF/macro/parser)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "OBJ with a dangling/attacker-controlled object reference" (SC2) — resolve-target abuse
  C2: "text + OBJ + out-of-band object" (SC1) — embedded payload
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: OBJ presented as an "empty box" so a reviewer treats the slot as harmless
  D2: "%EF%BF%BC" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: embedded-payload smuggling invisible to a text-only review
  E2: N/A — vector: stream desync (text checked, object executed)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: the placeholder is the embedded object
  EXPECTED: FAIL_THE_OBJECT_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: the plain-text extract is the whole message
  EXPECTED: FAIL_PLAIN_TEXT_COMPLETE_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: resolving the placeholder is inert
  EXPECTED: FAIL_INERT_ON_RESOLVE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%EF%BF%BC" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: an OBJ is an empty slot
  EXPECTED: FAIL_EMPTY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: text and object are a single stream
  EXPECTED: FAIL_SINGLE_STREAM_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to treat an object replacement character as a pointer to a separate, untrusted embedded stream — validating the object with the same rigor as the text, and never fetching/rendering it implicitly — without breaking legitimate rich-text embedding?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (an integrator that binds each OBJ to its embedded object, validates/scans the object stream, and gates any fetch/render behind explicit policy — an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "the placeholder is not the object and not empty; the real embedded content is a separate stream a text-only check and an implicit resolve both mishandle".
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
