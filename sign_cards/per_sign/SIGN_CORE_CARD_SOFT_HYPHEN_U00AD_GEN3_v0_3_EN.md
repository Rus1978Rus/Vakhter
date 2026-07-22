PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_SOFT_HYPHEN_U00AD_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_SOFT_HYPHEN_U00AD_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_SOFT_HYPHEN_U00AD_GEN3_v0_3_EN
CODEPOINT: U+00AD
VISIBLE_FORM: ⟨SHY⟩
UNICODE_NAME: SOFT HYPHEN
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: soft hyphen / a conditional hyphen usually invisible mid-word (keyword-split evasion)
CATEGORY_ROADMAP: LLM (invisible-conditional token injection) · PHAGO: — (token masking)
GLYPH_NOTE: VISIBLE_FORM uses the marker ⟨SHY⟩; the sign itself (U+00AD) is an invisible Format char (Cf) that shows a hyphen ONLY at a line-break point, and is NEVER written literally here — a literal SHY would silently sit inside a word in this document. Examples use ⟨SHY⟩/%C2%AD, never the byte.

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
VISIBLE_FORM: ⟨SHY⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: SHY_FORM ≠ EFFECT
SIGN_CATEGORY:
  - an invisible Format char marking a permitted hyphenation point
  - it is CONDITIONAL: usually invisible mid-word, and renders as a hyphen only if a line break happens there
  - legitimate typography (allow a long word to break across lines)
  - (misused) an invisible interior char that breaks a keyword for a substring match while a lenient parser ignores it

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — being usually non-printing does not make it inert
  2. NOT_A_REAL_HYPHEN — it is NOT U+002D (hyphen-minus); it usually shows nothing, appearing as a hyphen only at a wrap point
  3. NOT_ALWAYS_INVISIBLE — it becomes a visible hyphen exactly when a line break lands on it, so it is a conditional, not a constant
  4. NOT_SEEN_BY_EVERY_CHECK — a substring/keyword check does not treat it as a separator, yet a lenient consumer may drop it
  5. NOT_ENCODED_SAFE — "%C2%AD" may be decoded back to the SHY later
  6. NOT_AUTHORITY — it does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; it deceives matching and readers
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_HYPHEN_MINUS — a filter looking for U+002D does not see U+00AD
  10. NOT_SANITIZED_PROOF — the presence of the char does not mean the input is sanitized
  11. NOT_SINGLE_TOKEN_PROOF — "jav⟨SHY⟩ascript" may render as one word yet compare/parse as split

BASE_FORMULAS:
  SHY_FORM ≠ EFFECT
  SHY_FORM ≠ REAL_HYPHEN_PROOF
  SHY_FORM ≠ ALWAYS_INVISIBLE_PROOF
  SHY_FORM ≠ SEEN_BY_EVERY_CHECK_PROOF
  SHY_FORM ≠ ENCODED_SAFETY_PROOF
  SHY_FORM ≠ AUTHORITY
  SHY_FORM ≠ EXECUTION_TRIGGER
  SHY_FORM ≠ HYPHEN_MINUS_PROOF
  SHY_FORM ≠ INVISIBLE_HARMLESS_PROOF
  SHY_FORM ≠ SANITIZED_PROOF
  SHY_FORM ≠ SINGLE_TOKEN_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: SHY (ZONE_1) has parallel functions (legitimate hyphenation point vs. invisible keyword splitting) co-existing without cultural precession. Polysemy of a stable Format char.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a conditional-hyphenation control with no gestural predecessor; the keyword-splitting misuse is layered on by the digital epoch in parallel with legitimate hyphenation.

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
    INPUT: "SHY is U+00AD in Unicode"
    CONTEXT: naming the char in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: SHY_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "a soft hyphen marks where a word may break"
    CONTEXT: describing legitimate typography in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: SHY_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <SHY> here"
    CONTEXT: a documentation marker, not the byte
    EXPECTED: INFO
    RISK: NONE
    GUARD: SHY_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "it usually shows nothing until a line wraps on it"
    CONTEXT: describing the conditional property in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: SHY_FORM ≠ ALWAYS_INVISIBLE_PROOF
  SAFE_CASE_005:
    INPUT: "it is not the same as a hyphen-minus"
    CONTEXT: distinguishing it from U+002D in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: SHY_FORM ≠ HYPHEN_MINUS_PROOF
  SAFE_CASE_006:
    INPUT: "a normalizer can strip soft hyphens"
    CONTEXT: describing careful sanitization in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: SHY_FORM ≠ SANITIZED_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: KEYWORD_SPLIT
    INPUT: "jav<SHY>ascript: in a URL scheme check"
    CONTEXT: a soft hyphen splitting a keyword so a substring blocklist fails to match
    RISK: HIGH
    ATTACK: the blocklist misses "javascript" while a lenient parser drops the SHY
    GUARD: SHY_FORM ≠ SINGLE_TOKEN_PROOF
  RISK_CASE_002:
    NAME: INVISIBLE_IN_IDENTIFIER
    INPUT: "ad<SHY>min vs admin (look-alike username)"
    CONTEXT: a soft hyphen inside an ASCII identifier making it compare unequal while looking identical
    RISK: HIGH
    ATTACK: "ad<SHY>min" registers as a look-alike of "admin" for impersonation
    GUARD: SHY_FORM ≠ SINGLE_TOKEN_PROOF
  RISK_CASE_003:
    NAME: CONDITIONAL_REVEAL
    INPUT: "a value that shows a stray hyphen only when the line wraps"
    CONTEXT: a SHY that appears as a hyphen at a wrap point, changing the read
    RISK: MEDIUM
    ATTACK: the char is invisible in review but reveals a hyphen at render, altering meaning (e.g. a code/serial)
    GUARD: SHY_FORM ≠ ALWAYS_INVISIBLE_PROOF
  RISK_CASE_004:
    NAME: ENCODED_SHY_BYPASS
    INPUT: "value%C2%ADtail (with a later decode)"
    CONTEXT: a percent-encoded SHY decoded back before use
    RISK: HIGH
    ATTACK: "%C2%AD" decodes to the SHY AFTER a check → the hidden split reappears
    GUARD: SHY_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: HYPHEN_FILTER_GAP
    INPUT: "a filter that normalizes U+002D but not U+00AD"
    CONTEXT: a hyphen-aware filter that misses the soft hyphen
    RISK: MEDIUM
    ATTACK: normalizing only the real hyphen leaves the invisible soft hyphen splitting tokens
    GUARD: SHY_FORM ≠ HYPHEN_MINUS_PROOF
  RISK_CASE_006:
    NAME: INVISIBLE_FLOOD
    INPUT: "a run of many SHY inserted between characters"
    CONTEXT: mass invisible insertion to defeat naive matching
    RISK: MEDIUM
    ATTACK: every keyword is shredded so no substring rule matches
    GUARD: SHY_FORM ≠ SINGLE_TOKEN_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨HYPHEN-MINUS⟩
    CODEPOINT: U+002D
    NAME: HYPHEN-MINUS
    RISK: HIGH
    RULE: HYPHEN_MINUS ≠ SOFT_HYPHEN (the visible ASCII hyphen; SHY is invisible mid-word and only shows at a wrap)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨ZWSP⟩
    CODEPOINT: U+200B
    NAME: ZERO WIDTH SPACE
    RISK: HIGH
    RULE: ZERO_WIDTH_SPACE ≠ SOFT_HYPHEN (both invisible splitters, but ZWSP never shows a glyph; SHY can show a hyphen at a wrap)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨HYPHEN⟩
    CODEPOINT: U+2010
    NAME: HYPHEN
    RISK: MEDIUM
    RULE: HYPHEN ≠ SOFT_HYPHEN (the unambiguous visible hyphen punctuation; not a conditional invisible)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨NB-HYPHEN⟩
    CODEPOINT: U+2011
    NAME: NON-BREAKING HYPHEN
    RISK: MEDIUM
    RULE: NON_BREAKING_HYPHEN ≠ SOFT_HYPHEN (a visible hyphen that forbids a break; SHY permits one and is usually invisible)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨ZWNJ⟩
    CODEPOINT: U+200C
    NAME: ZERO WIDTH NON-JOINER
    RISK: LOW
    RULE: ZERO_WIDTH_NON_JOINER ≠ SOFT_HYPHEN (a joining control, not a hyphenation point; both invisible)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "it is a hyphen, so it is U+002D"
    RESPONSE: SHY_FORM ≠ REAL_HYPHEN_PROOF
    RULE: it is U+00AD, usually invisible; it only shows a hyphen at a wrap
  CG2:
    TRIGGER: "an invisible char cannot be dangerous"
    RESPONSE: SHY_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: invisibility is orthogonal to effect; SHY splits keywords invisibly
  CG3:
    TRIGGER: "it is always invisible, so a reviewer never sees anything odd"
    RESPONSE: SHY_FORM ≠ ALWAYS_INVISIBLE_PROOF
    RULE: it reveals a hyphen exactly at a wrap point; it is conditional, not constant
  CG4:
    TRIGGER: "'%C2%AD' is safe forever"
    RESPONSE: SHY_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to the SHY before use
  CG5:
    TRIGGER: "we normalize hyphens, so this is handled"
    RESPONSE: SHY_FORM ≠ HYPHEN_MINUS_PROOF
    RULE: a U+002D-only normalizer does not touch U+00AD
  CG6:
    TRIGGER: "the string looks like one word, so it is one token"
    RESPONSE: SHY_FORM ≠ SINGLE_TOKEN_PROOF
    RULE: display unity does not imply token unity; an invisible SHY may split it

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "keyword with an interior SHY"
      NAME: SPLIT_KEYWORD
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: a soft hyphen inside a blocked keyword to defeat a substring match
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "SHY at a value that later wraps"
      NAME: CONDITIONAL_HYPHEN_REVEAL
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: a soft hyphen revealing a hyphen glyph at render time
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "SHY between every character"
      NAME: INVISIBLE_FLOOD
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: mass insertion shredding all tokens
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with SHY are central to invisible keyword splitting.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: SHY splits/masks tokens (token masking), but does not imitate the existence of a verified entity. Its risks are matching desync and identifier confusion, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of SHY with ZWSP (U+200B) / ZWNJ (U+200C) to vary the invisible splitter / evade a SHY-only filter
  A2: percent-encoding "%C2%AD" to slip past a raw-byte scan
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: keyword split "jav<SHY>ascript:" defeating a substring blocklist
  B2: hyphen filter gap (SHY survives a U+002D-only normalization)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "SHY between every character" (SC3) — invisible flood
  C2: "keyword with an interior SHY" (SC1) — split keyword
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: SHY presented as a harmless "hyphenation hint" inside a hostile field
  D2: "%C2%AD" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: invisible identifier confusion (ad<SHY>min vs admin)
  E2: N/A — vector: conditional reveal of a hyphen at a wrap point
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: a soft hyphen is a hyphen-minus
  EXPECTED: FAIL_REAL_HYPHEN_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: an invisible char cannot be dangerous
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: a soft hyphen is always invisible
  EXPECTED: FAIL_ALWAYS_INVISIBLE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%C2%AD" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: normalizing hyphen-minus handles the soft hyphen
  EXPECTED: FAIL_HYPHEN_MINUS_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: a string that looks like one word is one token
  EXPECTED: FAIL_SINGLE_TOKEN_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to strip or reject the soft hyphen (and the invisible-splitter family) inside tokens before substring matching and comparison, while preserving legitimate hyphenation hints in display text?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (a normalizer that removes soft hyphens from match/compare keys while keeping them only in a display layer — an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "SHY is a conditional invisible: not a real hyphen, not always invisible, and not caught by a U+002D-only filter".
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
