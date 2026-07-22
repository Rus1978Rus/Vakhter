PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_ZERO_WIDTH_SPACE_U200B_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_ZERO_WIDTH_SPACE_U200B_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_ZERO_WIDTH_SPACE_U200B_GEN3_v0_3_EN
CODEPOINT: U+200B
VISIBLE_FORM: ⟨ZWSP⟩
UNICODE_NAME: ZERO WIDTH SPACE
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: zero width space / invisible token splitter (blocklist evasion)
CATEGORY_ROADMAP: LLM (invisible zero-width injection) · PHAGO: — (token masking)
GLYPH_NOTE: VISIBLE_FORM uses the marker ⟨ZWSP⟩; the sign itself (U+200B) is an invisible Format char (Cf) with zero advance width and is NEVER written literally here — a literal ZWSP would silently split tokens in this document. Examples use ⟨ZWSP⟩/%E2%80%8B, never the byte.

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
VISIBLE_FORM: ⟨ZWSP⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: ZWSP_FORM ≠ EFFECT
SIGN_CATEGORY:
  - zero-width, zero-advance invisible Format char (a line-break opportunity)
  - legitimate typographic use (allow a break inside a long unbreakable token/URL)
  - (misused) invisible token splitter that breaks a keyword so a blocklist match fails
  - (misused) invisible payload that survives a display-only review while a parser ignores it

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — being non-printing does not make it inert
  2. NOT_ZERO_WIDTH_MEANS_ABSENT — zero advance width does not mean the byte is not there
  3. NOT_WHITESPACE_EQUIVALENT — it is not a normal space; a blocklist/tokenizer treating it as a separator or ignoring it disagree, causing desync
  4. NOT_DISPLAY_ONLY — the reader sees nothing, but the bytes carry through parsing
  5. NOT_ENCODED_SAFE — "%E2%80%8B" may be decoded back to the ZWSP later
  6. NOT_AUTHORITY — it does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; it deceives filters and readers
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_NORMALIZED_AWAY_PROOF — presence of the sign does not mean normalization removed it
  10. NOT_SANITIZED_PROOF — the presence of the char does not mean the input is sanitized
  11. NOT_SINGLE_TOKEN_PROOF — "jav⟨ZWSP⟩ascript" may render as one word yet parse as two (or vice versa)

BASE_FORMULAS:
  ZWSP_FORM ≠ EFFECT
  ZWSP_FORM ≠ ZERO_WIDTH_MEANS_ABSENT_PROOF
  ZWSP_FORM ≠ WHITESPACE_EQUIVALENT_PROOF
  ZWSP_FORM ≠ DISPLAY_ONLY_PROOF
  ZWSP_FORM ≠ ENCODED_SAFETY_PROOF
  ZWSP_FORM ≠ AUTHORITY
  ZWSP_FORM ≠ EXECUTION_TRIGGER
  ZWSP_FORM ≠ NORMALIZED_AWAY_PROOF
  ZWSP_FORM ≠ INVISIBLE_HARMLESS_PROOF
  ZWSP_FORM ≠ SANITIZED_PROOF
  ZWSP_FORM ≠ SINGLE_TOKEN_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: ZWSP (ZONE_1) has parallel functions (legitimate break opportunity vs. invisible token splitting) co-existing without cultural precession. Polysemy of a stable Format char.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a zero-advance formatting control with no gestural predecessor; the token-splitting evasion is layered on by the digital epoch in parallel with legitimate break-opportunity typography.

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
    INPUT: "ZWSP is U+200B in Unicode"
    CONTEXT: naming the char in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWSP_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "a zero width space is a line-break opportunity"
    CONTEXT: describing legitimate typographic use in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWSP_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <ZWSP> here"
    CONTEXT: a documentation marker, not the byte
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWSP_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "it lets a long URL wrap without a visible space"
    CONTEXT: describing the break-opportunity property in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWSP_FORM ≠ WHITESPACE_EQUIVALENT_PROOF
  SAFE_CASE_005:
    INPUT: "normalization or stripping may remove it"
    CONTEXT: describing a sanitizer in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWSP_FORM ≠ NORMALIZED_AWAY_PROOF
  SAFE_CASE_006:
    INPUT: "it has zero advance width when rendered"
    CONTEXT: prose about the glyph metric
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWSP_FORM ≠ ZERO_WIDTH_MEANS_ABSENT_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: BLOCKLIST_KEYWORD_SPLIT
    INPUT: "jav<ZWSP>ascript: in a URL scheme check"
    CONTEXT: a ZWSP splitting a keyword so a substring blocklist fails to match
    RISK: HIGH
    ATTACK: the blocklist sees "jav" + "ascript" and misses "javascript", while a lenient parser rejoins it
    GUARD: ZWSP_FORM ≠ SINGLE_TOKEN_PROOF
  RISK_CASE_002:
    NAME: INVISIBLE_IN_IDENTIFIER
    INPUT: "admin<ZWSP> vs admin (two distinct usernames)"
    CONTEXT: an invisible char making two identifiers compare unequal while looking identical
    RISK: HIGH
    ATTACK: "admin<ZWSP>" registers as a look-alike of "admin" for impersonation
    GUARD: ZWSP_FORM ≠ ZERO_WIDTH_MEANS_ABSENT_PROOF
  RISK_CASE_003:
    NAME: FILTER_PARSER_DESYNC
    INPUT: "a filter strips ZWSP but the downstream parser does not (or vice versa)"
    CONTEXT: two stages disagreeing on whether the ZWSP is present
    RISK: HIGH
    ATTACK: the check sees one string, the executor sees another → bypass
    GUARD: ZWSP_FORM ≠ WHITESPACE_EQUIVALENT_PROOF
  RISK_CASE_004:
    NAME: ENCODED_ZWSP_BYPASS
    INPUT: "value%E2%80%8Btail (with a later decode)"
    CONTEXT: a percent-encoded ZWSP decoded back before use
    RISK: HIGH
    ATTACK: "%E2%80%8B" decodes to the ZWSP AFTER a check → token split reappears
    GUARD: ZWSP_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: HOMOGLYPH_STACK
    INPUT: "раy<ZWSP>раl (invisible split + confusable letters combined)"
    CONTEXT: a ZWSP stacked with confusable letters to deepen a spoof
    RISK: MEDIUM
    ATTACK: the invisible split plus look-alike letters make a hostile string pass a shallow review
    GUARD: ZWSP_FORM ≠ EFFECT
  RISK_CASE_006:
    NAME: INVISIBLE_FLOOD
    INPUT: "a run of many ZWSP inserted between every character"
    CONTEXT: mass invisible insertion to defeat naive matching and inflate length
    RISK: MEDIUM
    ATTACK: every keyword is shredded into single chars, so no substring rule matches
    GUARD: ZWSP_FORM ≠ SINGLE_TOKEN_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨ZWNJ⟩
    CODEPOINT: U+200C
    NAME: ZERO WIDTH NON-JOINER
    RISK: HIGH
    RULE: ZERO_WIDTH_NON_JOINER ≠ ZERO_WIDTH_SPACE (ZWNJ controls ligature joining; ZWSP is a break opportunity — different function, both invisible)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨ZWJ⟩
    CODEPOINT: U+200D
    NAME: ZERO WIDTH JOINER
    RISK: HIGH
    RULE: ZERO_WIDTH_JOINER ≠ ZERO_WIDTH_SPACE (ZWJ forces joining/emoji sequences; ZWSP breaks — opposite intent, both invisible)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨WJ⟩
    CODEPOINT: U+2060
    NAME: WORD JOINER
    RISK: HIGH
    RULE: WORD_JOINER ≠ ZERO_WIDTH_SPACE (WJ forbids a break; ZWSP allows one — inverse semantics, both zero-width)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨ZWNBSP⟩
    CODEPOINT: U+FEFF
    NAME: ZERO WIDTH NO-BREAK SPACE
    RISK: MEDIUM
    RULE: ZERO_WIDTH_NO_BREAK_SPACE ≠ ZERO_WIDTH_SPACE (U+FEFF also serves as a BOM; different role, both invisible)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨SP⟩
    CODEPOINT: U+0020
    NAME: SPACE
    RISK: LOW
    RULE: SPACE ≠ ZERO_WIDTH_SPACE (an ordinary visible-advance space, not a zero-width control)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "it has zero width, so it is effectively not there"
    RESPONSE: ZWSP_FORM ≠ ZERO_WIDTH_MEANS_ABSENT_PROOF
    RULE: zero advance width is a display metric; the byte is present in the data
  CG2:
    TRIGGER: "an invisible char cannot be dangerous"
    RESPONSE: ZWSP_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: invisibility is orthogonal to effect; ZWSP drives filter/parser desync
  CG3:
    TRIGGER: "it is just a space, treat it like whitespace"
    RESPONSE: ZWSP_FORM ≠ WHITESPACE_EQUIVALENT_PROOF
    RULE: it is not a normal space; stages disagree on it, causing desync
  CG4:
    TRIGGER: "'%E2%80%8B' is safe forever"
    RESPONSE: ZWSP_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to the ZWSP before use
  CG5:
    TRIGGER: "normalization always strips it"
    RESPONSE: ZWSP_FORM ≠ NORMALIZED_AWAY_PROOF
    RULE: not all pipelines normalize; presence does not imply it will be removed
  CG6:
    TRIGGER: "the string looks like one word, so it is one token"
    RESPONSE: ZWSP_FORM ≠ SINGLE_TOKEN_PROOF
    RULE: display unity does not imply token unity; an invisible split may hide inside

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "keyword with an interior ZWSP"
      NAME: SPLIT_KEYWORD
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: a ZWSP inside a blocked keyword to defeat a substring match
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "ZWSP between every character"
      NAME: INVISIBLE_FLOOD
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: mass insertion shredding all tokens
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "ZWSP + confusable letters"
      NAME: INVISIBLE_HOMOGLYPH_STACK
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: an invisible split combined with look-alike letters for a spoof
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with ZWSP are central to invisible token-splitting.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: ZWSP splits/masks tokens (token masking), but does not imitate the existence of a verified entity. Its risks are filter/parser desync and identifier confusion, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of ZWSP with ZWNJ (U+200C) / WJ (U+2060) / ZWNBSP (U+FEFF) to vary the invisible byte / evade a ZWSP-only filter
  A2: percent-encoding "%E2%80%8B" to slip past a raw-byte scan
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: keyword split "jav<ZWSP>ascript:" defeating a substring blocklist
  B2: filter/parser desync (one stage strips ZWSP, the other does not)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "ZWSP between every character" (SC2) — invisible flood shredding tokens
  C2: "keyword with an interior ZWSP" (SC1) — split keyword
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: ZWSP presented as a harmless "line-break opportunity" inside a hostile field
  D2: "%E2%80%8B" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: invisible identifier confusion (admin<ZWSP> vs admin)
  E2: N/A — vector: invisible split defeating a naive matcher
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: zero width means the char is effectively absent
  EXPECTED: FAIL_ZERO_WIDTH_MEANS_ABSENT_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: an invisible char cannot be dangerous
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: a ZWSP is equivalent to ordinary whitespace
  EXPECTED: FAIL_WHITESPACE_EQUIVALENT_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E2%80%8B" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: normalization always strips the ZWSP
  EXPECTED: FAIL_NORMALIZED_AWAY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: a string that looks like one word is one token
  EXPECTED: FAIL_SINGLE_TOKEN_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to detect invisible zero-width chars (200B-200D, 2060, FEFF) inside tokens and enforce a single normalization decision across filter and parser, without false positives on legitimate break opportunities and script-required joiners?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (a normalizer that decides once — strip-or-reject invisibles before both the check and the executor, with an allowlist for scripts that require ZWNJ/ZWJ — an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "zero width is a display metric, not absence; invisible splits break substring matching and desync stages".
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
