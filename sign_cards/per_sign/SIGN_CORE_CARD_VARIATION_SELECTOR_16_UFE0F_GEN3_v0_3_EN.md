PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_VARIATION_SELECTOR_16_UFE0F_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_VARIATION_SELECTOR_16_UFE0F_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_VARIATION_SELECTOR_16_UFE0F_GEN3_v0_3_EN
CODEPOINT: U+FE0F
VISIBLE_FORM: ⟨VS16⟩
UNICODE_NAME: VARIATION SELECTOR-16
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: variation selector-16 / emoji presentation & invisible carrier
CATEGORY_ROADMAP: LLM (invisible Mn carrier, presentation confusion) · PHAGO: — (carrier / presentation modifier)
GLYPH_NOTE: VISIBLE_FORM uses the marker ⟨VS16⟩; the sign itself (U+FE0F) is an invisible nonspacing mark (Mn, Default_Ignorable) and is NEVER written literally here. Examples use ⟨VS16⟩/%EF%B8%8F, never the byte.

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
VISIBLE_FORM: ⟨VS16⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: VS16_FORM ≠ EFFECT
SIGN_CATEGORY:
  - emoji-presentation selector (forces the emoji rendering of a base character)
  - invisible nonspacing mark (Mn), Default_Ignorable
  - component of ZWJ emoji sequences (family/flag/profession emoji)
  - (misused) invisible carrier appended to smuggle or pad a token

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — being non-printing does not make it inert
  2. NOT_PRESENTATION_ONLY — it can flip a base char between text and emoji rendering (display desync)
  3. NOT_ZERO_LENGTH — it is a real codepoint that changes byte length, hashes, and comparisons
  4. NOT_TRIM_PROOF — a "clean" token may carry an invisible trailing VS16
  5. NOT_ENCODED_SAFE — "%EF%B8%8F" may be decoded back to VS16 later
  6. NOT_AUTHORITY — it does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; it pads/modifies rendering
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_IDENTIFIER_SAFE — an appended VS16 makes two "identical-looking" identifiers differ
  10. NOT_SANITIZED_PROOF — the presence of VS16 does not mean the input is sanitized
  11. NOT_NORMALIZE_STABLE — presence/absence changes emoji-sequence identity across systems

BASE_FORMULAS:
  VS16_FORM ≠ EFFECT
  VS16_FORM ≠ PRESENTATION_ONLY_PROOF
  VS16_FORM ≠ ZERO_LENGTH_PROOF
  VS16_FORM ≠ TRIM_SAFETY_PROOF
  VS16_FORM ≠ ESCAPED_PROOF
  VS16_FORM ≠ ENCODED_SAFETY_PROOF
  VS16_FORM ≠ AUTHORITY
  VS16_FORM ≠ EXECUTION_TRIGGER
  VS16_FORM ≠ INVISIBLE_HARMLESS_PROOF
  VS16_FORM ≠ IDENTIFIER_EQUALITY_PROOF
  VS16_FORM ≠ SANITIZED_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: VS16 (ZONE_1) has parallel functions (legitimate emoji presentation vs. invisible carrier/padding) co-existing without cultural precession. Polysemy of a stable variation selector.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a presentation-control mark with no gestural predecessor; the carrier/smuggle use is layered on by the digital epoch in parallel with legitimate emoji rendering.

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
    INPUT: "VS16 is U+FE0F in Unicode"
    CONTEXT: naming the selector in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: VS16_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "the heart emoji uses a base char + VS16"
    CONTEXT: describing legitimate emoji presentation in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: VS16_FORM ≠ PRESENTATION_ONLY_PROOF
  SAFE_CASE_003:
    INPUT: "the marker is written as <VS16> here"
    CONTEXT: a documentation marker, not the byte
    EXPECTED: INFO
    RISK: NONE
    GUARD: VS16_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "variation selectors pick a glyph variant"
    CONTEXT: prose about variation selectors
    EXPECTED: INFO
    RISK: NONE
    GUARD: VS16_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "ZWJ emoji sequences may include VS16"
    CONTEXT: describing legitimate emoji sequence structure
    EXPECTED: INFO
    RISK: NONE
    GUARD: VS16_FORM ≠ ZERO_LENGTH_PROOF
  SAFE_CASE_006:
    INPUT: "VS15 selects text, VS16 selects emoji"
    CONTEXT: prose contrasting the two selectors
    EXPECTED: INFO
    RISK: NONE
    GUARD: VS16_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: INVISIBLE_CARRIER_SMUGGLE
    INPUT: "admin<VS16><VS16><VS16> (invisible padding after a token)"
    CONTEXT: VS16 repeated to smuggle invisible content past a visual review
    RISK: HIGH
    ATTACK: the invisible marks carry/pad content a human never sees but the machine stores/matches on
    GUARD: VS16_FORM ≠ INVISIBLE_HARMLESS_PROOF
  RISK_CASE_002:
    NAME: IDENTIFIER_LOOKALIKE_SPLIT
    INPUT: "user<VS16> vs user (two look-identical, byte-different names)"
    CONTEXT: an appended VS16 making two identical-looking identifiers differ
    RISK: HIGH
    ATTACK: "user<VS16>" and "user" render the same but bypass a uniqueness/allow-list check
    GUARD: VS16_FORM ≠ IDENTIFIER_EQUALITY_PROOF
  RISK_CASE_003:
    NAME: PRESENTATION_FLIP_DECEPTION
    INPUT: "digit<VS16> rendered as an emoji instead of text"
    CONTEXT: VS16 flipping a base char's rendering to hide/alter its meaning
    RISK: MEDIUM
    ATTACK: a base char displays as an emoji, mismatching what a filter/reader assumes
    GUARD: VS16_FORM ≠ PRESENTATION_ONLY_PROOF
  RISK_CASE_004:
    NAME: TRIM_BYPASS_TRAILING_VS
    INPUT: "value<VS16> (invisible trailing selector survives an edge-trim)"
    CONTEXT: a trailing VS16 an outer trim misses
    RISK: MEDIUM
    ATTACK: trimming whitespace leaves the invisible VS16, so the "cleaned" value still differs
    GUARD: VS16_FORM ≠ TRIM_SAFETY_PROOF
  RISK_CASE_005:
    NAME: ENCODED_VS_BYPASS
    INPUT: "token%EF%B8%8F (with a later decode)"
    CONTEXT: a percent-encoded VS16 decoded back after a check
    RISK: MEDIUM
    ATTACK: "%EF%B8%8F" decodes to VS16 AFTER validation → carrier/identifier split
    GUARD: VS16_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: EMOJI_SEQUENCE_TAMPER
    INPUT: "base<ZWJ>base<VS16> (manipulated ZWJ+VS sequence)"
    CONTEXT: VS16 combined with ZWJ to craft an ambiguous/oversized emoji sequence
    RISK: MEDIUM
    ATTACK: the tampered sequence renders differently across systems, desyncing display from bytes
    GUARD: VS16_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨VS15⟩
    CODEPOINT: U+FE0E
    NAME: VARIATION SELECTOR-15
    RISK: HIGH
    RULE: VARIATION_SELECTOR_15 ≠ VARIATION_SELECTOR_16 (text vs emoji presentation; opposite render, same invisibility)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨VS1⟩
    CODEPOINT: U+FE00
    NAME: VARIATION SELECTOR-1
    RISK: MEDIUM
    RULE: VARIATION_SELECTOR_1 ≠ VARIATION_SELECTOR_16 (a different selector a VS16-only filter misses)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨ZWJ⟩
    CODEPOINT: U+200D
    NAME: ZERO WIDTH JOINER
    RISK: HIGH
    RULE: ZERO_WIDTH_JOINER ≠ VARIATION_SELECTOR_16 (Cf joiner in the same emoji sequences; different mechanism, same invisibility)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨VS17⟩
    CODEPOINT: U+E0100
    NAME: VARIATION SELECTOR-17
    RISK: LOW
    RULE: VARIATION_SELECTOR_17 ≠ VARIATION_SELECTOR_16 (ideographic variation selector, another invisible carrier)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨ZWSP⟩
    CODEPOINT: U+200B
    NAME: ZERO WIDTH SPACE
    RISK: MEDIUM
    RULE: ZERO_WIDTH_SPACE ≠ VARIATION_SELECTOR_16 (a different invisible a shallow "strip invisibles" pass may treat identically)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "VS16 only changes presentation, so it is cosmetic"
    RESPONSE: VS16_FORM ≠ PRESENTATION_ONLY_PROOF
    RULE: it flips text↔emoji rendering and pads bytes; display and identity both shift
  CG2:
    TRIGGER: "an invisible mark cannot be dangerous"
    RESPONSE: VS16_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: invisibility is orthogonal to effect; VS16 is a real carrier codepoint
  CG3:
    TRIGGER: "two strings that look identical are equal"
    RESPONSE: VS16_FORM ≠ IDENTIFIER_EQUALITY_PROOF
    RULE: an appended VS16 makes look-alike strings byte-different (uniqueness bypass)
  CG4:
    TRIGGER: "'%EF%B8%8F' is safe forever"
    RESPONSE: VS16_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to VS16 before the sink
  CG5:
    TRIGGER: "trimming a value removes the selector"
    RESPONSE: VS16_FORM ≠ TRIM_SAFETY_PROOF
    RULE: edge-trimming leaves an invisible trailing VS16
  CG6:
    TRIGGER: "the presence of VS16 means the input is sanitized"
    RESPONSE: VS16_FORM ≠ SANITIZED_PROOF
    RULE: the presence of the sign says nothing about sanitization

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "base + VS16"
      NAME: PRESENTATION_FLIP
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: forcing an emoji rendering of a base char to alter its read meaning
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "ZWJ + base + VS16"
      NAME: EMOJI_SEQUENCE_CRAFT
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: crafting an ambiguous/oversized ZWJ emoji sequence
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "VS16 x N"
      NAME: INVISIBLE_PADDING
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: repeated invisible marks smuggling/padding content
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with VS16 are central to invisible carrier / presentation deception.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: VS16 modifies presentation or carries invisible content, but does not imitate the existence of a verified entity. Its risks are carrier/identifier-split/presentation-desync, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of VS16 with VS15 (U+FE0E) / VS1 (U+FE00) to evade a VS16-only filter
  A2: percent-encoding "%EF%B8%8F" to slip past a raw-byte scan
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: invisible carrier smuggle admin<VS16><VS16><VS16>
  B2: identifier look-alike split user<VS16> vs user
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "base + VS16" (SC1) — presentation flip
  C2: "VS16 x N" (SC3) — invisible padding
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: VS16 presented as harmless emoji presentation inside an identifier field
  D2: "%EF%B8%8F" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: invisible-split uniqueness bypass on a username
  E2: N/A — vector: presentation flip desyncing a filter's assumption from the render
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: VS16 is cosmetic presentation only
  EXPECTED: FAIL_PRESENTATION_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: an invisible mark cannot be dangerous
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: two look-identical strings are equal
  EXPECTED: FAIL_IDENTIFIER_EQUALITY_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%EF%B8%8F" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: trimming removes the selector
  EXPECTED: FAIL_TRIM_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: the presence of VS16 proves the input was sanitized
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to normalize/reject VS16 in identifiers and credentials (byte-equality after NFC, strip stray selectors) without breaking legitimate emoji rendering in display text?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (identifier canonicalization + emoji-aware allow context + strip stray selectors outside valid emoji sequences — an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "VS16 is a real invisible carrier; look-alike ≠ byte-equal".
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
