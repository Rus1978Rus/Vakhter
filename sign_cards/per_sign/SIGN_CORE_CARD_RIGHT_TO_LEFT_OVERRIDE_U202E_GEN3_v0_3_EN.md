PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_RIGHT_TO_LEFT_OVERRIDE_U202E_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_RIGHT_TO_LEFT_OVERRIDE_U202E_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_RIGHT_TO_LEFT_OVERRIDE_U202E_GEN3_v0_3_EN
CODEPOINT: U+202E
VISIBLE_FORM: ⟨RLO⟩
UNICODE_NAME: RIGHT-TO-LEFT OVERRIDE
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: right-to-left override / Trojan Source
CATEGORY_ROADMAP: LLM (bidi visual reorder, Trojan Source) · PHAGO: ○ (partial — filename/type spoof)
GLYPH_NOTE: VISIBLE_FORM uses the marker ⟨RLO⟩; the sign itself (U+202E) is an invisible Bidi_Control (Cf) and is NEVER written literally here — a literal RLO would reorder this document. All examples use ⟨RLO⟩/⟨PDF⟩/%E2%80%AE, never the byte.

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
VISIBLE_FORM: ⟨RLO⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: RLO_FORM ≠ EFFECT
SIGN_CATEGORY:
  - bidirectional override (forces RTL display order of following characters)
  - Unicode Bidi_Control (part of the Bidirectional Algorithm)
  - legitimate mixed LTR/RTL text layout
  - (misused) Trojan Source token reorder / filename-extension spoof

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — being non-printing does not make it inert
  2. NOT_DISPLAY_ONLY — it reorders the VISUAL run while logical bytes are unchanged (desync)
  3. NOT_RENDERING_COSMETIC — the reorder changes what a human approves vs what executes/stores
  4. NOT_ESCAPED_PROOF — the presence of a bidi mark does not mean it is quoted/escaped
  5. NOT_ENCODED_SAFE — "%E2%80%AE" may be decoded back to the override later
  6. NOT_AUTHORITY — it does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; it deceives the reader
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_BALANCED_PROOF — an unterminated override (no PDF/PDI) bleeds RTL onto the rest
  10. NOT_SANITIZED_PROOF — the presence of the override does not mean the input is sanitized
  11. NOT_LTR_CONTEXT_SAFE — even inside an LTR document it forces an RTL run

BASE_FORMULAS:
  RLO_FORM ≠ EFFECT
  RLO_FORM ≠ DISPLAY_ONLY_PROOF
  RLO_FORM ≠ RENDERING_COSMETIC_PROOF
  RLO_FORM ≠ LOGICAL_ORDER_PROOF
  RLO_FORM ≠ ESCAPED_PROOF
  RLO_FORM ≠ ENCODED_SAFETY_PROOF
  RLO_FORM ≠ AUTHORITY
  RLO_FORM ≠ EXECUTION_TRIGGER
  RLO_FORM ≠ INVISIBLE_HARMLESS_PROOF
  RLO_FORM ≠ SANITIZED_PROOF
  RLO_FORM ≠ BALANCED_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: RLO (ZONE_1) has parallel functions (legitimate RTL layout vs. visual-order deception) co-existing without cultural precession. Polysemy of a stable Bidi_Control.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a formatting control with no gestural predecessor; the reorder-deception use is layered on by the digital epoch in parallel with legitimate RTL layout.

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
    INPUT: "RLO is U+202E in Unicode"
    CONTEXT: naming the control in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLO_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "bidi controls lay out mixed Hebrew/English"
    CONTEXT: describing legitimate RTL layout in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLO_FORM ≠ RENDERING_COSMETIC_PROOF
  SAFE_CASE_003:
    INPUT: "the marker is written as <RLO> here"
    CONTEXT: a documentation marker, not the byte
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLO_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "Arabic and Hebrew are right-to-left scripts"
    CONTEXT: prose about RTL scripts (no control byte)
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLO_FORM ≠ DISPLAY_ONLY_PROOF
  SAFE_CASE_005:
    INPUT: "a properly terminated RTL run (RLO...PDF) in an editor"
    CONTEXT: describing balanced legitimate usage
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLO_FORM ≠ BALANCED_PROOF
  SAFE_CASE_006:
    INPUT: "the Bidirectional Algorithm handles direction"
    CONTEXT: prose about the UBA
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLO_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: TROJAN_SOURCE_COMMENT_REORDER
    INPUT: 'isAdmin = true <RLO> // safe? <PDF>'
    CONTEXT: an override making executable code render as if inside a comment
    RISK: CRITICAL
    ATTACK: the override reorders the visual run so a reviewer approves code they misread (logic ≠ display)
    GUARD: RLO_FORM ≠ RENDERING_COSMETIC_PROOF
  RISK_CASE_002:
    NAME: FILENAME_EXTENSION_SPOOF
    INPUT: "resume<RLO>cod.exe"
    CONTEXT: an override reversing the tail so ".exe" displays as ".doc"
    RISK: HIGH
    ATTACK: "cod.exe" renders reversed as "exe.doc" — a dangerous file looks like a document
    GUARD: RLO_FORM ≠ DISPLAY_ONLY_PROOF
  RISK_CASE_003:
    NAME: UNTERMINATED_OVERRIDE_BLEED
    INPUT: "label<RLO>rest of the line with no PDF"
    CONTEXT: an override with no PDF/PDI, forcing RTL onto everything after
    RISK: HIGH
    ATTACK: the unterminated override bleeds RTL past its intended span, corrupting later fields
    GUARD: RLO_FORM ≠ BALANCED_PROOF
  RISK_CASE_004:
    NAME: IDENTIFIER_LOGIC_SPOOF
    INPUT: "if (user<RLO>nimda<PDF>) grant()"
    CONTEXT: an override making an identifier read differently than it is stored
    RISK: HIGH
    ATTACK: the visible identifier differs from the logical one, hiding a privileged branch
    GUARD: RLO_FORM ≠ LOGICAL_ORDER_PROOF
  RISK_CASE_005:
    NAME: ENCODED_BIDI_BYPASS
    INPUT: "value%E2%80%AEtail (with a later decode)"
    CONTEXT: a percent-encoded RLO decoded back before display
    RISK: HIGH
    ATTACK: "%E2%80%AE" decodes to the override AFTER a check → reorder deception
    GUARD: RLO_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: BIDI_HOMOGLYPH_STACK
    INPUT: "раyраl<RLO> ... (bidi + confusable letters combined)"
    CONTEXT: an override stacked with confusable letters to deepen the spoof
    RISK: MEDIUM
    ATTACK: the override plus look-alike letters make a hostile string pass a shallow visual review
    GUARD: RLO_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨LRO⟩
    CODEPOINT: U+202D
    NAME: LEFT-TO-RIGHT OVERRIDE
    RISK: HIGH
    RULE: LEFT_TO_RIGHT_OVERRIDE ≠ RIGHT_TO_LEFT_OVERRIDE (mirror override, reorders the other way; a naive filter conflates them)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨RLE⟩
    CODEPOINT: U+202B
    NAME: RIGHT-TO-LEFT EMBEDDING
    RISK: HIGH
    RULE: RIGHT_TO_LEFT_EMBEDDING ≠ RIGHT_TO_LEFT_OVERRIDE (embedding vs override; different strength, similar reorder)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨LRE⟩
    CODEPOINT: U+202A
    NAME: LEFT-TO-RIGHT EMBEDDING
    RISK: MEDIUM
    RULE: LEFT_TO_RIGHT_EMBEDDING ≠ RIGHT_TO_LEFT_OVERRIDE
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨RLI⟩
    CODEPOINT: U+2067
    NAME: RIGHT-TO-LEFT ISOLATE
    RISK: MEDIUM
    RULE: RIGHT_TO_LEFT_ISOLATE ≠ RIGHT_TO_LEFT_OVERRIDE (isolate scopes direction; a filter that strips only RLO misses it)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨ALM⟩
    CODEPOINT: U+061C
    NAME: ARABIC LETTER MARK
    RISK: LOW
    RULE: ARABIC_LETTER_MARK ≠ RIGHT_TO_LEFT_OVERRIDE (a bidi mark that also affects order, invisible to an RLO-only filter)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "a bidi override only changes display, so it is cosmetic"
    RESPONSE: RLO_FORM ≠ RENDERING_COSMETIC_PROOF
    RULE: the reorder changes what a human approves vs what executes/stores (logic ≠ display)
  CG2:
    TRIGGER: "an invisible control char cannot be dangerous"
    RESPONSE: RLO_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: invisibility is orthogonal to effect; RLO drives visual/logical desync
  CG3:
    TRIGGER: "the logical byte order is what matters, so display is safe"
    RESPONSE: RLO_FORM ≠ LOGICAL_ORDER_PROOF
    RULE: reviewers approve the DISPLAY; the attack lives in the display↔logic gap
  CG4:
    TRIGGER: "'%E2%80%AE' is safe forever"
    RESPONSE: RLO_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to the override before display
  CG5:
    TRIGGER: "stripping RLO stops bidi attacks"
    RESPONSE: RLO_FORM ≠ EFFECT
    RULE: LRO/RLE/LRE/RLI/ALM also reorder; a single-char strip misses the family
  CG6:
    TRIGGER: "the presence of a bidi mark means the input is sanitized"
    RESPONSE: RLO_FORM ≠ SANITIZED_PROOF
    RULE: the presence of the sign says nothing about sanitization

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "RLO ... PDF"
      NAME: BALANCED_OVERRIDE_SPAN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: a scoped reorder span used to reorder a specific token (Trojan Source)
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "RLO (no PDF)"
      NAME: UNTERMINATED_BLEED
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: an override with no terminator bleeding RTL onto later content
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "RLO + confusable letters"
      NAME: STACKED_SPOOF
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: an override combined with homoglyphs for a deeper visual spoof
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with RLO are central to visual-order deception.

PHAGO_ENTITY_MIMICRY:
  PARTIAL:
    LEVEL: ○
    REASON: RLO's core mechanism is visual/logical DESYNC (structure masking), but the filename/
      extension spoof (a ".exe" that displays as ".doc") partially mimics the IDENTITY of a benign
      file type — a hostile entity wearing a safe entity's visible name. Partial entity-mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of RLO with LRO (U+202D) / RLE (U+202B) to evade an RLO-only filter
  A2: percent-encoding "%E2%80%AE" to slip past a raw-byte scan
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: Trojan Source comment reorder isAdmin=true <RLO> // safe? <PDF>
  B2: filename extension spoof resume<RLO>cod.exe
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "RLO ... PDF" (SC1) — scoped Trojan Source span
  C2: "RLO (no PDF)" (SC2) — unterminated bleed
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: RLO presented as harmless RTL layout inside a code/identifier field
  D2: "%E2%80%AE" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: filename/type spoof — a ".exe" wearing a ".doc" visible identity (partial entity-mimicry)
  E2: identifier spoof — a privileged branch wearing a benign-looking name
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: a bidi override is cosmetic display only
  EXPECTED: FAIL_RENDERING_COSMETIC_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: an invisible control char cannot be dangerous
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: only the logical byte order matters, display is safe
  EXPECTED: FAIL_LOGICAL_ORDER_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E2%80%AE" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: stripping RLO stops all bidi attacks
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
  QUESTION: how to detect/neutralize bidi reorder (reject unbalanced runs, normalize spans) without false positives on legitimate mixed RTL/LTR text?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (reject unterminated/nesting-violating bidi in code/identifiers/filenames + render logical order for review + strip the whole Bidi_Control family, not just RLO — an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "RLO deceives via the display↔logic gap; safety is decided by the render/parse context".
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
