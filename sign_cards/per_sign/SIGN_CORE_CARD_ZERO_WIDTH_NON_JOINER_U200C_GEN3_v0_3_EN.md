PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_ZERO_WIDTH_NON_JOINER_U200C_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_ZERO_WIDTH_NON_JOINER_U200C_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_ZERO_WIDTH_NON_JOINER_U200C_GEN3_v0_3_EN
CODEPOINT: U+200C
VISIBLE_FORM: ⟨ZWNJ⟩
UNICODE_NAME: ZERO WIDTH NON-JOINER
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: zero width non-joiner / script-required joining control (cannot be blindly stripped)
CATEGORY_ROADMAP: LLM (invisible zero-width injection) · PHAGO: — (token masking)
GLYPH_NOTE: VISIBLE_FORM uses the marker ⟨ZWNJ⟩; the sign itself (U+200C) is an invisible Format char (Cf) and is NEVER written literally here. Examples use ⟨ZWNJ⟩/%E2%80%8C, never the byte. Unlike a pure-noise invisible, ZWNJ is REQUIRED by some scripts, so it cannot be blindly deleted.

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
VISIBLE_FORM: ⟨ZWNJ⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: ZWNJ_FORM ≠ EFFECT
SIGN_CATEGORY:
  - invisible Format char that PREVENTS cursive joining / ligature formation between neighbours
  - legitimate and REQUIRED in Persian, Arabic and some Indic scripts (semantically significant)
  - (misused) invisible char inserted into an ASCII identifier/keyword to defeat matching
  - (misused) confusable with ZWSP/ZWJ/WJ — a naive filter conflates the whole invisible family

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — being non-printing does not make it inert
  2. NOT_SAFE_TO_BLINDLY_STRIP — it is script-required; deleting it corrupts legitimate Persian/Indic text
  3. NOT_ZWSP — it controls joining, it is NOT a break opportunity; different function, same invisibility
  4. NOT_DISPLAY_ONLY — the reader may see no glyph, but the byte carries through parsing and comparison
  5. NOT_ENCODED_SAFE — "%E2%80%8C" may be decoded back to the ZWNJ later
  6. NOT_AUTHORITY — it does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; it deceives filters and readers
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_MEANINGLESS_NOISE — in the wrong context it is an attack char, in the right context it is required orthography
  10. NOT_SANITIZED_PROOF — the presence of the char does not mean the input is sanitized
  11. NOT_SINGLE_TOKEN_PROOF — "ad⟨ZWNJ⟩min" may render as "admin" yet compare unequal

BASE_FORMULAS:
  ZWNJ_FORM ≠ EFFECT
  ZWNJ_FORM ≠ SAFE_TO_BLINDLY_STRIP_PROOF
  ZWNJ_FORM ≠ ZWSP_EQUIVALENCE_PROOF
  ZWNJ_FORM ≠ DISPLAY_ONLY_PROOF
  ZWNJ_FORM ≠ ENCODED_SAFETY_PROOF
  ZWNJ_FORM ≠ AUTHORITY
  ZWNJ_FORM ≠ EXECUTION_TRIGGER
  ZWNJ_FORM ≠ MEANINGLESS_NOISE_PROOF
  ZWNJ_FORM ≠ INVISIBLE_HARMLESS_PROOF
  ZWNJ_FORM ≠ SANITIZED_PROOF
  ZWNJ_FORM ≠ SINGLE_TOKEN_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: ZWNJ (ZONE_1) has parallel functions (required orthographic joining control vs. invisible identifier-injection) co-existing without cultural precession. Polysemy of a stable Format char; its dual role makes blind stripping unsafe.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a joining-control with a real orthographic role but no gestural predecessor; the identifier-injection misuse is layered on by the digital epoch in parallel with required script use.

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
    INPUT: "ZWNJ is U+200C in Unicode"
    CONTEXT: naming the char in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWNJ_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "ZWNJ prevents cursive joining between letters"
    CONTEXT: describing the joining-control function in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWNJ_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <ZWNJ> here"
    CONTEXT: a documentation marker, not the byte
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWNJ_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "Persian and some Indic scripts require ZWNJ"
    CONTEXT: describing legitimate required orthography in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWNJ_FORM ≠ SAFE_TO_BLINDLY_STRIP_PROOF
  SAFE_CASE_005:
    INPUT: "it is not the same as a break opportunity"
    CONTEXT: distinguishing it from ZWSP in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWNJ_FORM ≠ ZWSP_EQUIVALENCE_PROOF
  SAFE_CASE_006:
    INPUT: "a normalizer may need an allowlist for it"
    CONTEXT: describing careful sanitization in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWNJ_FORM ≠ MEANINGLESS_NOISE_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: INVISIBLE_IN_IDENTIFIER
    INPUT: "ad<ZWNJ>min vs admin (look-alike username)"
    CONTEXT: a ZWNJ inside an ASCII identifier making it compare unequal while looking identical
    RISK: HIGH
    ATTACK: "ad<ZWNJ>min" registers as a look-alike of "admin" for impersonation
    GUARD: ZWNJ_FORM ≠ SINGLE_TOKEN_PROOF
  RISK_CASE_002:
    NAME: KEYWORD_SPLIT
    INPUT: "jav<ZWNJ>ascript: in a URL scheme check"
    CONTEXT: a ZWNJ splitting a keyword so a substring blocklist fails to match
    RISK: HIGH
    ATTACK: the blocklist misses "javascript" while a lenient parser ignores the ZWNJ
    GUARD: ZWNJ_FORM ≠ SINGLE_TOKEN_PROOF
  RISK_CASE_003:
    NAME: OVERBROAD_STRIP_CORRUPTS_TEXT
    INPUT: "a filter deletes all ZWNJ, breaking legitimate Persian input"
    CONTEXT: a blind strip that damages required orthography (a false-positive harm)
    RISK: MEDIUM
    ATTACK: an over-eager sanitizer corrupts real text, causing data loss or a different word
    GUARD: ZWNJ_FORM ≠ SAFE_TO_BLINDLY_STRIP_PROOF
  RISK_CASE_004:
    NAME: ENCODED_ZWNJ_BYPASS
    INPUT: "value%E2%80%8Ctail (with a later decode)"
    CONTEXT: a percent-encoded ZWNJ decoded back before use
    RISK: HIGH
    ATTACK: "%E2%80%8C" decodes to the ZWNJ AFTER a check → hidden split reappears
    GUARD: ZWNJ_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: INVISIBLE_FAMILY_CONFLATION
    INPUT: "a filter treating ZWNJ, ZWJ and ZWSP as one class"
    CONTEXT: a naive filter conflating the whole invisible family, mishandling one of them
    RISK: MEDIUM
    ATTACK: a rule tuned for ZWSP mis-handles ZWNJ (either misses the attack or corrupts required text)
    GUARD: ZWNJ_FORM ≠ ZWSP_EQUIVALENCE_PROOF
  RISK_CASE_006:
    NAME: HOMOGLYPH_STACK
    INPUT: "раy<ZWNJ>раl (invisible split + confusable letters combined)"
    CONTEXT: a ZWNJ stacked with confusable letters to deepen a spoof
    RISK: MEDIUM
    ATTACK: the invisible char plus look-alike letters make a hostile string pass a shallow review
    GUARD: ZWNJ_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨ZWSP⟩
    CODEPOINT: U+200B
    NAME: ZERO WIDTH SPACE
    RISK: HIGH
    RULE: ZERO_WIDTH_SPACE ≠ ZERO_WIDTH_NON_JOINER (ZWSP is a break opportunity; ZWNJ controls joining — different function, both invisible)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨ZWJ⟩
    CODEPOINT: U+200D
    NAME: ZERO WIDTH JOINER
    RISK: HIGH
    RULE: ZERO_WIDTH_JOINER ≠ ZERO_WIDTH_NON_JOINER (ZWJ forces joining; ZWNJ forbids it — exact opposites, both invisible)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨WJ⟩
    CODEPOINT: U+2060
    NAME: WORD JOINER
    RISK: MEDIUM
    RULE: WORD_JOINER ≠ ZERO_WIDTH_NON_JOINER (WJ forbids a line break; ZWNJ forbids cursive joining — different layers, both zero-width)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨ZWNBSP⟩
    CODEPOINT: U+FEFF
    NAME: ZERO WIDTH NO-BREAK SPACE
    RISK: MEDIUM
    RULE: ZERO_WIDTH_NO_BREAK_SPACE ≠ ZERO_WIDTH_NON_JOINER (U+FEFF also serves as a BOM; different role, both invisible)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨SHY⟩
    CODEPOINT: U+00AD
    NAME: SOFT HYPHEN
    RISK: LOW
    RULE: SOFT_HYPHEN ≠ ZERO_WIDTH_NON_JOINER (a conditional hyphen, usually invisible; not a joining control)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "just strip every ZWNJ, it is invisible junk"
    RESPONSE: ZWNJ_FORM ≠ SAFE_TO_BLINDLY_STRIP_PROOF
    RULE: it is required by some scripts; blind stripping corrupts legitimate text
  CG2:
    TRIGGER: "an invisible char cannot be dangerous"
    RESPONSE: ZWNJ_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: invisibility is orthogonal to effect; ZWNJ drives identifier and filter desync
  CG3:
    TRIGGER: "treat ZWNJ the same as a zero width space"
    RESPONSE: ZWNJ_FORM ≠ ZWSP_EQUIVALENCE_PROOF
    RULE: they have different functions; conflating them mishandles one
  CG4:
    TRIGGER: "'%E2%80%8C' is safe forever"
    RESPONSE: ZWNJ_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to the ZWNJ before use
  CG5:
    TRIGGER: "a ZWNJ is meaningless noise"
    RESPONSE: ZWNJ_FORM ≠ MEANINGLESS_NOISE_PROOF
    RULE: in the right context it is required orthography; in the wrong context it is an attack char
  CG6:
    TRIGGER: "the string looks like admin, so it is admin"
    RESPONSE: ZWNJ_FORM ≠ SINGLE_TOKEN_PROOF
    RULE: display unity does not imply byte equality; an invisible char may hide inside

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "ASCII identifier with an interior ZWNJ"
      NAME: SPLIT_IDENTIFIER
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: a ZWNJ inside an ASCII name/keyword to defeat matching or impersonate
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "ZWNJ in a required-script context"
      NAME: LEGITIMATE_ORTHOGRAPHY
      RISK_LEVEL: LOW
      POSSIBLE_CONTEXTS: required Persian/Indic joining control that must be preserved
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "ZWNJ + confusable letters"
      NAME: INVISIBLE_HOMOGLYPH_STACK
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: an invisible char combined with look-alike letters for a spoof
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — ZWNJ's risk is exactly context-dependent (required vs. injected).

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: ZWNJ masks/splits tokens (token masking), but does not imitate the existence of a verified entity. Its risks are identifier confusion and filter desync, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of ZWNJ with ZWSP (U+200B) / ZWJ (U+200D) / WJ (U+2060) to vary the invisible byte / evade a ZWNJ-only filter
  A2: percent-encoding "%E2%80%8C" to slip past a raw-byte scan
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: identifier split "ad<ZWNJ>min" impersonating "admin"
  B2: overbroad strip corrupts legitimate Persian input (false-positive harm)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "ASCII identifier with an interior ZWNJ" (SC1) — split identifier
  C2: "ZWNJ + confusable letters" (SC3) — invisible homoglyph stack
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: ZWNJ presented as "meaningless invisible noise" so it is ignored, then abused
  D2: "%E2%80%8C" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: invisible identifier confusion (ad<ZWNJ>min vs admin)
  E2: N/A — vector: invisible-family conflation mishandling ZWNJ
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: it is safe to blindly strip every ZWNJ
  EXPECTED: FAIL_SAFE_TO_BLINDLY_STRIP_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: an invisible char cannot be dangerous
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: ZWNJ is equivalent to a zero width space
  EXPECTED: FAIL_ZWSP_EQUIVALENCE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E2%80%8C" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: a ZWNJ is meaningless noise
  EXPECTED: FAIL_MEANINGLESS_NOISE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: a string that looks like admin is admin
  EXPECTED: FAIL_SINGLE_TOKEN_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to block ZWNJ used as an invisible identifier/keyword injector while preserving it where Persian/Arabic/Indic orthography requires it — i.e. a context-aware rather than blanket policy?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (a context-aware normalizer: reject/flag ZWNJ inside ASCII-only identifiers and blocked keywords, preserve it inside required-script runs — an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "ZWNJ is context-dependent: required orthography in one place, an attack char in another; blind stripping is itself a harm".
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
