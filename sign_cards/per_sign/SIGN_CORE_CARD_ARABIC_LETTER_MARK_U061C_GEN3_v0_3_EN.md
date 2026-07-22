PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_ARABIC_LETTER_MARK_U061C_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_ARABIC_LETTER_MARK_U061C_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_ARABIC_LETTER_MARK_U061C_GEN3_v0_3_EN
CODEPOINT: U+061C
VISIBLE_FORM: ⟨ALM⟩
UNICODE_NAME: ARABIC LETTER MARK
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: arabic letter mark / invisible strong RTL mark outside the U+200x block
CATEGORY_ROADMAP: LLM (invisible bidi direction injection) · PHAGO: — (order masking)
GLYPH_NOTE: VISIBLE_FORM uses the marker ⟨ALM⟩; the sign itself (U+061C) is an invisible Bidi_Control (Cf) in the Arabic block and is NEVER written literally here — a literal ALM could reorder this document. Examples use ⟨ALM⟩/%D8%9C, never the byte. ALM is a strong mark like RLM but sits at U+061C, not in the U+200x invisibles range.

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
VISIBLE_FORM: ⟨ALM⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: ALM_FORM ≠ EFFECT
SIGN_CATEGORY:
  - an invisible zero-width character that acts as a STRONG right-to-left (Arabic-type) character
  - legitimate bidi use: making a following number/neutral take Arabic-script direction handling
  - it sets direction WITHOUT any embedding/override/isolate — no format opener or terminator involved
  - (misused) invisible direction injection that lives at U+061C, so a filter scanning only the U+200x/202x/206x invisibles misses it entirely

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — being non-printing does not make it inert
  2. NOT_A_FORMAT_CONTROL — it is a strong character, not an embedding/override/isolate; no terminator, no nesting
  3. NOT_IN_THE_U200X_RANGE — it sits at U+061C in the Arabic block, not among the U+200B–200F invisibles a scanner may focus on
  4. NOT_DIRECTIONLESS — it carries strong RTL directionality that can flip the resolved order of adjacent neutrals/numbers
  5. NOT_RLM — it behaves like RLM but is a distinct codepoint (U+061C ≠ U+200F); handling one is not handling the other
  6. NOT_ARABIC_TEXT_ONLY — its risk is not limited to Arabic content; it can be dropped into any string to steer direction
  7. NOT_ENCODED_SAFE — "%D8%9C" may be decoded back to the ALM later
  8. NOT_AUTHORITY — it does not confirm officialness
  9. NOT_EXECUTION_TRIGGER — by itself it executes nothing; it deceives visual order
  10. NOT_SANITIZED_PROOF — the presence of the char does not mean the input is sanitized
  11. NOT_SINGLE_ORDER_PROOF — a string that "reads one way" may reorder around a hidden ALM

BASE_FORMULAS:
  ALM_FORM ≠ EFFECT
  ALM_FORM ≠ FORMAT_CONTROL_PROOF
  ALM_FORM ≠ IN_U200X_RANGE_PROOF
  ALM_FORM ≠ DIRECTIONLESS_PROOF
  ALM_FORM ≠ RLM_EQUIVALENCE_PROOF
  ALM_FORM ≠ ARABIC_TEXT_ONLY_PROOF
  ALM_FORM ≠ ENCODED_SAFETY_PROOF
  ALM_FORM ≠ AUTHORITY
  ALM_FORM ≠ EXECUTION_TRIGGER
  ALM_FORM ≠ INVISIBLE_HARMLESS_PROOF
  ALM_FORM ≠ SANITIZED_PROOF
  ALM_FORM ≠ SINGLE_ORDER_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: ALM (ZONE_1) has parallel functions (legitimate Arabic-context direction fixing vs. invisible direction injection) co-existing without cultural precession. Polysemy of a stable Bidi_Control mark.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: an invisible strong-direction mark (Unicode 6.3) with no gestural predecessor; the direction-injection misuse is layered on by the digital epoch in parallel with legitimate Arabic-context use.

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
    INPUT: "ALM is U+061C in Unicode"
    CONTEXT: naming the char in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: ALM_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "ALM sets Arabic-script direction for a following number"
    CONTEXT: describing the legitimate bidi function in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: ALM_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <ALM> here"
    CONTEXT: a documentation marker, not the byte
    EXPECTED: INFO
    RISK: NONE
    GUARD: ALM_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "it is a strong character, not a format control"
    CONTEXT: distinguishing it from overrides/isolates in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: ALM_FORM ≠ FORMAT_CONTROL_PROOF
  SAFE_CASE_005:
    INPUT: "it sits at U+061C, not in the U+200x block"
    CONTEXT: describing its codepoint location in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: ALM_FORM ≠ IN_U200X_RANGE_PROOF
  SAFE_CASE_006:
    INPUT: "a bidi-aware normalizer can handle the marks too"
    CONTEXT: describing careful sanitization in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: ALM_FORM ≠ RLM_EQUIVALENCE_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: RANGE_SCAN_GAP
    INPUT: "input passing a scanner that only checks U+200B-200F and 202x/206x"
    CONTEXT: an ALM slipping past a filter focused on the U+200x invisibles
    RISK: HIGH
    ATTACK: the mark at U+061C is outside the scanned range, so the reorder survives
    GUARD: ALM_FORM ≠ IN_U200X_RANGE_PROOF
  RISK_CASE_002:
    NAME: NEUTRAL_REORDER
    INPUT: "digits/punctuation around a hidden ALM flipping visible order"
    CONTEXT: an ALM setting the direction of adjacent neutrals so the display order changes
    RISK: HIGH
    ATTACK: an amount, date or path reads in a different order than it is stored
    GUARD: ALM_FORM ≠ SINGLE_ORDER_PROOF
  RISK_CASE_003:
    NAME: RLM_ONLY_FILTER_GAP
    INPUT: "a filter that removes RLM (U+200F) but not ALM (U+061C)"
    CONTEXT: a mark-aware filter that still misses the Arabic-block mark
    RISK: MEDIUM
    ATTACK: ALM does the same RTL steering RLM would, but the filter only modelled RLM
    GUARD: ALM_FORM ≠ RLM_EQUIVALENCE_PROOF
  RISK_CASE_004:
    NAME: ENCODED_ALM_BYPASS
    INPUT: "value%D8%9Ctail (with a later decode)"
    CONTEXT: a percent-encoded ALM decoded back before display
    RISK: HIGH
    ATTACK: "%D8%9C" decodes to the ALM AFTER a check → the reorder reappears
    GUARD: ALM_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: NON_ARABIC_CONTEXT_INJECTION
    INPUT: "an ALM dropped into an otherwise Latin/ASCII string"
    CONTEXT: an ALM steering direction in content that is not Arabic at all
    RISK: MEDIUM
    ATTACK: assuming ALM only matters in Arabic text, a filter ignores it in Latin input where it still reorders
    GUARD: ALM_FORM ≠ ARABIC_TEXT_ONLY_PROOF
  RISK_CASE_006:
    NAME: BIDI_HOMOGLYPH_STACK
    INPUT: "раyраl<ALM> ... (mark + confusable letters combined)"
    CONTEXT: an ALM stacked with confusable letters to deepen a spoof
    RISK: MEDIUM
    ATTACK: the invisible mark plus look-alike letters make a hostile string pass a shallow visual review
    GUARD: ALM_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨RLM⟩
    CODEPOINT: U+200F
    NAME: RIGHT-TO-LEFT MARK
    RISK: HIGH
    RULE: RIGHT_TO_LEFT_MARK ≠ ARABIC_LETTER_MARK (same RTL steering, but RLM is at U+200F while ALM is at U+061C — a filter may model only one)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨LRM⟩
    CODEPOINT: U+200E
    NAME: LEFT-TO-RIGHT MARK
    RISK: HIGH
    RULE: LEFT_TO_RIGHT_MARK ≠ ARABIC_LETTER_MARK (the opposite-direction invisible strong mark; a naive filter conflates them)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨RLO⟩
    CODEPOINT: U+202E
    NAME: RIGHT-TO-LEFT OVERRIDE
    RISK: MEDIUM
    RULE: RIGHT_TO_LEFT_OVERRIDE ≠ ARABIC_LETTER_MARK (an override forces direction and has a terminator; the mark is a strong char with neither)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨ARABIC-SEMI⟩
    CODEPOINT: U+061B
    NAME: ARABIC SEMICOLON
    RISK: LOW
    RULE: ARABIC_SEMICOLON ≠ ARABIC_LETTER_MARK (a visible punctuation mark next to ALM in the block; visible, not an invisible direction mark)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨ZWSP⟩
    CODEPOINT: U+200B
    NAME: ZERO WIDTH SPACE
    RISK: LOW
    RULE: ZERO_WIDTH_SPACE ≠ ARABIC_LETTER_MARK (both invisible, but ZWSP is a break opportunity carrying no direction)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "our scanner covers the U+200x invisibles, so we are covered"
    RESPONSE: ALM_FORM ≠ IN_U200X_RANGE_PROOF
    RULE: ALM is at U+061C, outside the U+200x range a scanner may focus on
  CG2:
    TRIGGER: "an invisible char cannot be dangerous"
    RESPONSE: ALM_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: invisibility is orthogonal to effect; ALM reorders neutrals invisibly
  CG3:
    TRIGGER: "it is an override, so look for a terminator"
    RESPONSE: ALM_FORM ≠ FORMAT_CONTROL_PROOF
    RULE: it is a strong character with no terminator and no nesting
  CG4:
    TRIGGER: "'%D8%9C' is safe forever"
    RESPONSE: ALM_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to the ALM before display
  CG5:
    TRIGGER: "ALM only matters inside Arabic text"
    RESPONSE: ALM_FORM ≠ ARABIC_TEXT_ONLY_PROOF
    RULE: it can steer direction dropped into any string, including Latin/ASCII
  CG6:
    TRIGGER: "we strip RLM, so this direction mark is handled"
    RESPONSE: ALM_FORM ≠ RLM_EQUIVALENCE_PROOF
    RULE: ALM (U+061C) is a distinct codepoint from RLM (U+200F)

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "neutrals + interior ALM"
      NAME: NEUTRAL_ORDER_FLIP
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: an ALM flipping the visible order of digits/punctuation around it
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "ALM used where a U+200x-only scanner runs"
      NAME: RANGE_SCAN_GAP
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: a mark surviving because only the U+200x range is scanned
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "mixed ALM + RLM + LRM"
      NAME: MARK_FAMILY_MIX
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: several direction marks combined to evade a single-codepoint filter
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — ALM's effect is on the order of the surrounding sequence.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: ALM reorders neutral runs (order masking), but does not imitate the existence of a verified entity. Its risks are visual-order desync, not entity mimicry. (Filename spoof is more natural with an override; see RLO/LRO.)
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of ALM with RLM (U+200F) / LRM (U+200E) to vary the direction mark / evade a single-codepoint filter
  A2: percent-encoding "%D8%9C" to slip past a raw-byte scan
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: range-scan gap (ALM at U+061C survives a U+200x-only scan)
  B2: non-Arabic context injection (ALM reorders inside Latin/ASCII where it is assumed irrelevant)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "neutrals + interior ALM" (SC1) — neutral order flip
  C2: "mixed ALM + RLM + LRM" (SC3) — mark-family mix
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: ALM presented as an "Arabic-only" direction fix while it reorders a non-Arabic payload
  D2: "%D8%9C" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: invisible neutral reorder deceiving a reviewer
  E2: N/A — vector: mark outside the scanned range bypassing a U+200x-focused filter
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: scanning the U+200x invisibles covers ALM too
  EXPECTED: FAIL_IN_U200X_RANGE_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: an invisible char cannot be dangerous
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: ALM is a format control with a terminator
  EXPECTED: FAIL_FORMAT_CONTROL_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%D8%9C" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: ALM only matters inside Arabic text
  EXPECTED: FAIL_ARABIC_TEXT_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: stripping RLM handles ALM too
  EXPECTED: FAIL_RLM_EQUIVALENCE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to enumerate ALL invisible direction marks and controls by property (Bidi_Control) rather than by codepoint range, so a mark like ALM at U+061C is caught alongside the U+200x/202x/206x family, without false positives on legitimate Arabic-context direction fixing?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (a bidi normalizer keyed on the Bidi_Control property, not a hardcoded range, covering U+061C together with the U+200x/202x/206x set — an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "ALM is a strong RTL mark outside the U+200x range; a range-based scanner misses it, and it is not Arabic-text-only".
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
