PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_LEFT_TO_RIGHT_MARK_U200E_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_LEFT_TO_RIGHT_MARK_U200E_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_LEFT_TO_RIGHT_MARK_U200E_GEN3_v0_3_EN
CODEPOINT: U+200E
VISIBLE_FORM: ⟨LRM⟩
UNICODE_NAME: LEFT-TO-RIGHT MARK
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: left-to-right mark / invisible strong LTR character (mirror of RLM)
CATEGORY_ROADMAP: LLM (invisible bidi direction injection) · PHAGO: — (order masking)
GLYPH_NOTE: VISIBLE_FORM uses the marker ⟨LRM⟩; the sign itself (U+200E) is an invisible Bidi_Control (Cf) and is NEVER written literally here — a literal LRM could reorder this document. Examples use ⟨LRM⟩/%E2%80%8E, never the byte. Like RLM, LRM is a strong CHARACTER, not a format opener/closer.

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
VISIBLE_FORM: ⟨LRM⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: LRM_FORM ≠ EFFECT
SIGN_CATEGORY:
  - an invisible zero-width character that acts as a STRONG left-to-right character
  - legitimate bidi use: fixing neutral characters to LTR, or restoring LTR context after an RTL run
  - it sets direction WITHOUT any embedding/override/isolate — no format opener or terminator involved
  - (misused) invisible direction injection that a format-only filter (202x/206x) misses; the "default-looking" LTR makes it easy to overlook

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — being non-printing does not make it inert
  2. NOT_A_FORMAT_CONTROL — it is a strong character, not an embedding/override/isolate; no terminator, no nesting
  3. NOT_CAUGHT_BY_FORMAT_ONLY_FILTER — a filter stripping only U+202A–202E / U+2066–2069 does not touch U+200E
  4. NOT_DIRECTIONLESS — it carries strong LTR directionality that can fix or flip the resolved order of adjacent neutrals/numbers
  5. NOT_RLM — U+200E is LTR; U+200F (RLM) is RTL; they are opposite-direction marks
  6. NOT_DEFAULT_MEANS_NOOP — "looks like the normal LTR default" does not mean it does nothing; it can override an inherited RTL context
  7. NOT_ENCODED_SAFE — "%E2%80%8E" may be decoded back to the LRM later
  8. NOT_AUTHORITY — it does not confirm officialness
  9. NOT_EXECUTION_TRIGGER — by itself it executes nothing; it deceives visual order
  10. NOT_SANITIZED_PROOF — the presence of the char does not mean the input is sanitized
  11. NOT_SINGLE_ORDER_PROOF — a string that "reads one way" may reorder around a hidden LRM

BASE_FORMULAS:
  LRM_FORM ≠ EFFECT
  LRM_FORM ≠ FORMAT_CONTROL_PROOF
  LRM_FORM ≠ CAUGHT_BY_FORMAT_ONLY_FILTER_PROOF
  LRM_FORM ≠ DIRECTIONLESS_PROOF
  LRM_FORM ≠ RLM_EQUIVALENCE_PROOF
  LRM_FORM ≠ DEFAULT_MEANS_NOOP_PROOF
  LRM_FORM ≠ ENCODED_SAFETY_PROOF
  LRM_FORM ≠ AUTHORITY
  LRM_FORM ≠ EXECUTION_TRIGGER
  LRM_FORM ≠ INVISIBLE_HARMLESS_PROOF
  LRM_FORM ≠ SANITIZED_PROOF
  LRM_FORM ≠ SINGLE_ORDER_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: LRM (ZONE_1) has parallel functions (legitimate neutral-direction fixing vs. invisible direction injection) co-existing without cultural precession. Polysemy of a stable Bidi_Control mark.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: an invisible strong-direction mark with no gestural predecessor; the direction-injection misuse is layered on by the digital epoch in parallel with legitimate neutral-fixing use.

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
    INPUT: "LRM is U+200E in Unicode"
    CONTEXT: naming the char in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: LRM_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "LRM fixes neutral characters to left-to-right"
    CONTEXT: describing the legitimate bidi function in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: LRM_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <LRM> here"
    CONTEXT: a documentation marker, not the byte
    EXPECTED: INFO
    RISK: NONE
    GUARD: LRM_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "it is a strong character, not a format control"
    CONTEXT: distinguishing it from LRO/LRE/LRI in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: LRM_FORM ≠ FORMAT_CONTROL_PROOF
  SAFE_CASE_005:
    INPUT: "LRM is left-to-right, RLM is right-to-left"
    CONTEXT: distinguishing it from U+200F in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: LRM_FORM ≠ RLM_EQUIVALENCE_PROOF
  SAFE_CASE_006:
    INPUT: "a bidi-aware normalizer can handle the marks too"
    CONTEXT: describing careful sanitization in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: LRM_FORM ≠ CAUGHT_BY_FORMAT_ONLY_FILTER_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: FORMAT_ONLY_FILTER_GAP
    INPUT: "input passing a strip that removes only 202A-202E and 2066-2069"
    CONTEXT: an LRM slipping past a filter that only knows the format controls
    RISK: HIGH
    ATTACK: the strong mark reorders neutrals with no format opener for the filter to catch
    GUARD: LRM_FORM ≠ CAUGHT_BY_FORMAT_ONLY_FILTER_PROOF
  RISK_CASE_002:
    NAME: RTL_CONTEXT_NEUTRALIZE
    INPUT: "an LRM forcing LTR inside an otherwise RTL run"
    CONTEXT: an LRM overriding an inherited RTL context so neutrals resolve LTR
    RISK: HIGH
    ATTACK: the invisible mark changes how an amount/path/label reads inside RTL text
    GUARD: LRM_FORM ≠ DEFAULT_MEANS_NOOP_PROOF
  RISK_CASE_003:
    NAME: MARK_VS_OVERRIDE_CONFUSION
    INPUT: "a reviewer expecting an LRO but the payload uses an LRM"
    CONTEXT: an analysis keyed on overrides missing the mark-based reorder
    RISK: MEDIUM
    ATTACK: because LRM is a mark (no terminator), an override-focused check does not model it
    GUARD: LRM_FORM ≠ FORMAT_CONTROL_PROOF
  RISK_CASE_004:
    NAME: ENCODED_LRM_BYPASS
    INPUT: "value%E2%80%8Etail (with a later decode)"
    CONTEXT: a percent-encoded LRM decoded back before display
    RISK: HIGH
    ATTACK: "%E2%80%8E" decodes to the LRM AFTER a check → the reorder reappears
    GUARD: LRM_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: MARK_PAIR_GAP
    INPUT: "input using U+200F (RLM) or U+061C (ALM) where only U+200E is filtered"
    CONTEXT: the other invisible direction marks slipping past an LRM-only filter
    RISK: MEDIUM
    ATTACK: filtering only U+200E misses RLM/ALM, which inject the opposite/derived direction
    GUARD: LRM_FORM ≠ RLM_EQUIVALENCE_PROOF
  RISK_CASE_006:
    NAME: BIDI_HOMOGLYPH_STACK
    INPUT: "раyраl<LRM> ... (mark + confusable letters combined)"
    CONTEXT: an LRM stacked with confusable letters to deepen a spoof
    RISK: MEDIUM
    ATTACK: the invisible mark plus look-alike letters make a hostile string pass a shallow visual review
    GUARD: LRM_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨RLM⟩
    CODEPOINT: U+200F
    NAME: RIGHT-TO-LEFT MARK
    RISK: HIGH
    RULE: RIGHT_TO_LEFT_MARK ≠ LEFT_TO_RIGHT_MARK (the opposite-direction invisible strong mark; a naive filter conflates them)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨ALM⟩
    CODEPOINT: U+061C
    NAME: ARABIC LETTER MARK
    RISK: HIGH
    RULE: ARABIC_LETTER_MARK ≠ LEFT_TO_RIGHT_MARK (a strong RTL mark in the Arabic block; opposite direction and a different neighbourhood a filter may miss)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨LRO⟩
    CODEPOINT: U+202D
    NAME: LEFT-TO-RIGHT OVERRIDE
    RISK: MEDIUM
    RULE: LEFT_TO_RIGHT_OVERRIDE ≠ LEFT_TO_RIGHT_MARK (an override forces direction and has a terminator; the mark is a strong char with neither)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨LRI⟩
    CODEPOINT: U+2066
    NAME: LEFT-TO-RIGHT ISOLATE
    RISK: MEDIUM
    RULE: LEFT_TO_RIGHT_ISOLATE ≠ LEFT_TO_RIGHT_MARK (an isolate scopes and needs a PDI; the mark scopes nothing and needs no terminator)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨ZWSP⟩
    CODEPOINT: U+200B
    NAME: ZERO WIDTH SPACE
    RISK: LOW
    RULE: ZERO_WIDTH_SPACE ≠ LEFT_TO_RIGHT_MARK (both invisible, but ZWSP is a break opportunity carrying no direction)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "our bidi filter strips the format controls, so we are covered"
    RESPONSE: LRM_FORM ≠ CAUGHT_BY_FORMAT_ONLY_FILTER_PROOF
    RULE: LRM is a strong mark, not a 202x/206x control; a format-only strip misses it
  CG2:
    TRIGGER: "an invisible char cannot be dangerous"
    RESPONSE: LRM_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: invisibility is orthogonal to effect; LRM reorders neutrals invisibly
  CG3:
    TRIGGER: "it just sets the normal LTR default, so it is a no-op"
    RESPONSE: LRM_FORM ≠ DEFAULT_MEANS_NOOP_PROOF
    RULE: it can override an inherited RTL context; "default-looking" is not "no effect"
  CG4:
    TRIGGER: "'%E2%80%8E' is safe forever"
    RESPONSE: LRM_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to the LRM before display
  CG5:
    TRIGGER: "an invisible mark carries no direction"
    RESPONSE: LRM_FORM ≠ DIRECTIONLESS_PROOF
    RULE: LRM is a strong LTR character; it fixes/flips the order of adjacent neutrals
  CG6:
    TRIGGER: "we filter U+200E, so the marks are handled"
    RESPONSE: LRM_FORM ≠ RLM_EQUIVALENCE_PROOF
    RULE: RLM (U+200F) and ALM (U+061C) are separate direction marks

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "RTL run + interior LRM"
      NAME: RTL_CONTEXT_FLIP
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: an LRM forcing LTR on neutrals inside RTL text
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "LRM used where a format-only filter runs"
      NAME: FORMAT_FILTER_GAP
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: a mark surviving because only the 202x/206x controls are stripped
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "mixed LRM + RLM + ALM"
      NAME: MARK_FAMILY_MIX
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: several direction marks combined to evade an LRM-only filter
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — LRM's effect is on the order of the surrounding sequence.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: LRM reorders neutral runs (order masking), but does not imitate the existence of a verified entity. Its risks are visual-order desync, not entity mimicry. (Filename spoof is more natural with an override; see RLO/LRO.)
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of LRM with RLM (U+200F) / ALM (U+061C) to vary the direction mark / evade an LRM-only filter
  A2: percent-encoding "%E2%80%8E" to slip past a raw-byte scan
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: format-only filter gap (LRM survives a 202A-202E / 2066-2069 strip)
  B2: RTL context neutralize (LRM forces LTR inside an RTL run)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "RTL run + interior LRM" (SC1) — RTL context flip
  C2: "mixed LRM + RLM + ALM" (SC3) — mark-family mix
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: LRM presented as a harmless "default direction" while it neutralizes an RTL context
  D2: "%E2%80%8E" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: invisible neutral reorder deceiving a reviewer
  E2: N/A — vector: mark-based reorder bypassing a format-control-only filter
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: stripping the format controls covers LRM too
  EXPECTED: FAIL_CAUGHT_BY_FORMAT_ONLY_FILTER_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: an invisible char cannot be dangerous
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: LRM just sets the default so it is a no-op
  EXPECTED: FAIL_DEFAULT_MEANS_NOOP_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E2%80%8E" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: an invisible mark carries no direction
  EXPECTED: FAIL_DIRECTIONLESS_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: filtering U+200E handles all direction marks
  EXPECTED: FAIL_RLM_EQUIVALENCE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to model the invisible direction marks (U+200E LRM, U+200F RLM, U+061C ALM) alongside the bidi format controls, so a bidi filter catches mark-based reorders too, without false positives on legitimate neutral-direction fixing?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (a bidi normalizer covering marks AND format controls, resolving order deterministically and flagging suspicious mark-driven reorders — an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "LRM is a strong direction mark, not a format control, and not a no-op; a filter that strips only 202x/206x misses it".
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
