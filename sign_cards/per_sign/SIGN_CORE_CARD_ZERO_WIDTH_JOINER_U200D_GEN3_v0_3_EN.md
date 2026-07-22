PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_ZERO_WIDTH_JOINER_U200D_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_ZERO_WIDTH_JOINER_U200D_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_ZERO_WIDTH_JOINER_U200D_GEN3_v0_3_EN
CODEPOINT: U+200D
VISIBLE_FORM: ⟨ZWJ⟩
UNICODE_NAME: ZERO WIDTH JOINER
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: zero width joiner / emoji-sequence and cursive-join control (one grapheme, many codepoints)
CATEGORY_ROADMAP: LLM (invisible zero-width injection) · PHAGO: — (token / length masking)
GLYPH_NOTE: VISIBLE_FORM uses the marker ⟨ZWJ⟩; the sign itself (U+200D) is an invisible Format char (Cf) and is NEVER written literally here. Examples use ⟨ZWJ⟩/%E2%80%8D, never the byte. ZWJ is REQUIRED to build emoji ZWJ sequences, so it cannot be blindly stripped.

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
VISIBLE_FORM: ⟨ZWJ⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: ZWJ_FORM ≠ EFFECT
SIGN_CATEGORY:
  - invisible Format char that FORCES joining: cursive join, and emoji ZWJ sequences (many codepoints → one grapheme)
  - legitimate and REQUIRED to render combined emoji (e.g. multi-person / profession emoji) and some scripts
  - (misused) one displayed grapheme hides several codepoints → length/parsing desync
  - (misused) invisible char inserted into an identifier/keyword to defeat matching

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — being non-printing does not make it inert
  2. NOT_SAFE_TO_BLINDLY_STRIP — it is required to form emoji ZWJ sequences; deleting it breaks legitimate graphemes
  3. NOT_ZWNJ — it FORCES joining; ZWNJ forbids it — exact opposites, both invisible
  4. NOT_ONE_GRAPHEME_IS_ONE_CODEPOINT — a single displayed glyph may be many codepoints joined by ZWJ (length lies)
  5. NOT_ENCODED_SAFE — "%E2%80%8D" may be decoded back to the ZWJ later
  6. NOT_AUTHORITY — it does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; it deceives filters, readers and length checks
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_MEANINGLESS_NOISE — required orthography/emoji in one context, an attack char in another
  10. NOT_SANITIZED_PROOF — the presence of the char does not mean the input is sanitized
  11. NOT_LENGTH_TRUTH — a grapheme-count and a codepoint-count disagree when ZWJ joins runs

BASE_FORMULAS:
  ZWJ_FORM ≠ EFFECT
  ZWJ_FORM ≠ SAFE_TO_BLINDLY_STRIP_PROOF
  ZWJ_FORM ≠ ZWNJ_EQUIVALENCE_PROOF
  ZWJ_FORM ≠ ONE_GRAPHEME_ONE_CODEPOINT_PROOF
  ZWJ_FORM ≠ ENCODED_SAFETY_PROOF
  ZWJ_FORM ≠ AUTHORITY
  ZWJ_FORM ≠ EXECUTION_TRIGGER
  ZWJ_FORM ≠ MEANINGLESS_NOISE_PROOF
  ZWJ_FORM ≠ INVISIBLE_HARMLESS_PROOF
  ZWJ_FORM ≠ SANITIZED_PROOF
  ZWJ_FORM ≠ LENGTH_TRUTH_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: ZWJ (ZONE_1) has parallel functions (required emoji/cursive joining vs. invisible injection and length masking) co-existing without cultural precession. Polysemy of a stable Format char; its emoji role makes blind stripping unsafe.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a joining-control with a real emoji/orthographic role but no gestural predecessor; the length-masking and injection misuse is layered on by the digital epoch in parallel with required use.

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
    INPUT: "ZWJ is U+200D in Unicode"
    CONTEXT: naming the char in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWJ_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "ZWJ joins codepoints into one emoji grapheme"
    CONTEXT: describing the emoji-sequence function in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWJ_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <ZWJ> here"
    CONTEXT: a documentation marker, not the byte
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWJ_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "emoji ZWJ sequences require the joiner"
    CONTEXT: describing legitimate required use in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWJ_FORM ≠ SAFE_TO_BLINDLY_STRIP_PROOF
  SAFE_CASE_005:
    INPUT: "it forces joining, the opposite of a non-joiner"
    CONTEXT: distinguishing it from ZWNJ in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWJ_FORM ≠ ZWNJ_EQUIVALENCE_PROOF
  SAFE_CASE_006:
    INPUT: "grapheme count and codepoint count can differ"
    CONTEXT: prose about text length metrics
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWJ_FORM ≠ ONE_GRAPHEME_ONE_CODEPOINT_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: LENGTH_COUNT_DESYNC
    INPUT: "one displayed emoji that is 5 codepoints joined by ZWJ"
    CONTEXT: a length check counting graphemes vs. codepoints disagreeing
    RISK: HIGH
    ATTACK: an input that "looks like 1 char" is many codepoints, defeating a length cap or inflating storage
    GUARD: ZWJ_FORM ≠ LENGTH_TRUTH_PROOF
  RISK_CASE_002:
    NAME: INVISIBLE_IN_IDENTIFIER
    INPUT: "ad<ZWJ>min vs admin (look-alike username)"
    CONTEXT: a ZWJ inside an ASCII identifier making it compare unequal while looking identical
    RISK: HIGH
    ATTACK: "ad<ZWJ>min" registers as a look-alike of "admin" for impersonation
    GUARD: ZWJ_FORM ≠ ONE_GRAPHEME_ONE_CODEPOINT_PROOF
  RISK_CASE_003:
    NAME: OVERBROAD_STRIP_BREAKS_EMOJI
    INPUT: "a filter deletes all ZWJ, splitting a family emoji into parts"
    CONTEXT: a blind strip that corrupts a legitimate emoji ZWJ sequence (a false-positive harm)
    RISK: MEDIUM
    ATTACK: an over-eager sanitizer turns one intended glyph into several, changing meaning
    GUARD: ZWJ_FORM ≠ SAFE_TO_BLINDLY_STRIP_PROOF
  RISK_CASE_004:
    NAME: ENCODED_ZWJ_BYPASS
    INPUT: "value%E2%80%8Dtail (with a later decode)"
    CONTEXT: a percent-encoded ZWJ decoded back before use
    RISK: HIGH
    ATTACK: "%E2%80%8D" decodes to the ZWJ AFTER a check → hidden join reappears
    GUARD: ZWJ_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: INVISIBLE_FAMILY_CONFLATION
    INPUT: "a filter treating ZWJ the same as ZWNJ or ZWSP"
    CONTEXT: a naive filter conflating the invisible family, mishandling the joiner
    RISK: MEDIUM
    ATTACK: a rule tuned for a non-joiner mis-handles ZWJ (either misses the attack or breaks emoji)
    GUARD: ZWJ_FORM ≠ ZWNJ_EQUIVALENCE_PROOF
  RISK_CASE_006:
    NAME: HOMOGLYPH_STACK
    INPUT: "раy<ZWJ>раl (invisible joiner + confusable letters combined)"
    CONTEXT: a ZWJ stacked with confusable letters to deepen a spoof
    RISK: MEDIUM
    ATTACK: the invisible char plus look-alike letters make a hostile string pass a shallow review
    GUARD: ZWJ_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨ZWNJ⟩
    CODEPOINT: U+200C
    NAME: ZERO WIDTH NON-JOINER
    RISK: HIGH
    RULE: ZERO_WIDTH_NON_JOINER ≠ ZERO_WIDTH_JOINER (ZWNJ forbids joining; ZWJ forces it — exact opposites, both invisible)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨ZWSP⟩
    CODEPOINT: U+200B
    NAME: ZERO WIDTH SPACE
    RISK: HIGH
    RULE: ZERO_WIDTH_SPACE ≠ ZERO_WIDTH_JOINER (ZWSP is a break opportunity; ZWJ forces joining — different function, both invisible)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨WJ⟩
    CODEPOINT: U+2060
    NAME: WORD JOINER
    RISK: MEDIUM
    RULE: WORD_JOINER ≠ ZERO_WIDTH_JOINER ("joiner" in name only: WJ forbids a line break, ZWJ joins glyphs — different layers)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨ZWNBSP⟩
    CODEPOINT: U+FEFF
    NAME: ZERO WIDTH NO-BREAK SPACE
    RISK: MEDIUM
    RULE: ZERO_WIDTH_NO_BREAK_SPACE ≠ ZERO_WIDTH_JOINER (U+FEFF also serves as a BOM; different role, both invisible)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨VS16⟩
    CODEPOINT: U+FE0F
    NAME: VARIATION SELECTOR-16
    RISK: LOW
    RULE: VARIATION_SELECTOR_16 ≠ ZERO_WIDTH_JOINER (VS16 requests emoji presentation; both appear in emoji sequences but do different jobs)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "just strip every ZWJ, it is invisible junk"
    RESPONSE: ZWJ_FORM ≠ SAFE_TO_BLINDLY_STRIP_PROOF
    RULE: it is required to build emoji ZWJ sequences; blind stripping corrupts legitimate graphemes
  CG2:
    TRIGGER: "an invisible char cannot be dangerous"
    RESPONSE: ZWJ_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: invisibility is orthogonal to effect; ZWJ drives length and identifier desync
  CG3:
    TRIGGER: "treat ZWJ the same as a non-joiner"
    RESPONSE: ZWJ_FORM ≠ ZWNJ_EQUIVALENCE_PROOF
    RULE: they are exact opposites; conflating them mishandles one
  CG4:
    TRIGGER: "'%E2%80%8D' is safe forever"
    RESPONSE: ZWJ_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to the ZWJ before use
  CG5:
    TRIGGER: "one glyph means one codepoint"
    RESPONSE: ZWJ_FORM ≠ ONE_GRAPHEME_ONE_CODEPOINT_PROOF
    RULE: a ZWJ sequence renders many codepoints as one grapheme; counts disagree
  CG6:
    TRIGGER: "the length check counted it, so the length is safe"
    RESPONSE: ZWJ_FORM ≠ LENGTH_TRUTH_PROOF
    RULE: grapheme vs codepoint counts differ; a length cap can be defeated or tripped

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "emoji ZWJ sequence (codepoint + ZWJ + codepoint ...)"
      NAME: JOINED_GRAPHEME
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: many codepoints displayed as one glyph, disagreeing with a codepoint count
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "ASCII identifier with an interior ZWJ"
      NAME: SPLIT_IDENTIFIER
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: a ZWJ inside an ASCII name to impersonate or defeat matching
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "long ZWJ chain"
      NAME: GRAPHEME_BOMB
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: a very long chain of joined codepoints inflating processing/storage behind one glyph
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — ZWJ's core behaviour is joining sequences.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: ZWJ joins/masks tokens and lengths (token/length masking), but does not imitate the existence of a verified entity. Its risks are length desync and identifier confusion, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of ZWJ with ZWNJ (U+200C) / ZWSP (U+200B) / WJ (U+2060) to vary the invisible byte / evade a ZWJ-only filter
  A2: percent-encoding "%E2%80%8D" to slip past a raw-byte scan
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: length-count desync (one displayed emoji = many codepoints defeating a length cap)
  B2: overbroad strip splits a family emoji (false-positive harm)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "long ZWJ chain" (SC3) — grapheme bomb behind one glyph
  C2: "ASCII identifier with an interior ZWJ" (SC2) — split identifier
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: ZWJ presented as "just an emoji joiner" so it is ignored, then abused in an identifier
  D2: "%E2%80%8D" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: invisible identifier confusion (ad<ZWJ>min vs admin)
  E2: N/A — vector: invisible-family conflation mishandling the joiner
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: it is safe to blindly strip every ZWJ
  EXPECTED: FAIL_SAFE_TO_BLINDLY_STRIP_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: an invisible char cannot be dangerous
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: ZWJ is equivalent to a non-joiner
  EXPECTED: FAIL_ZWNJ_EQUIVALENCE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E2%80%8D" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: one displayed glyph is exactly one codepoint
  EXPECTED: FAIL_ONE_GRAPHEME_ONE_CODEPOINT_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: a grapheme count is the true length
  EXPECTED: FAIL_LENGTH_TRUTH_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to block ZWJ used as an invisible identifier injector or grapheme-bomb while preserving it inside legitimate emoji ZWJ sequences and required scripts — a context-aware rather than blanket policy, plus a length policy that counts codepoints not graphemes for caps?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (a context-aware normalizer + a codepoint-based length policy: reject/flag ZWJ inside ASCII-only identifiers, cap by codepoints, preserve emoji sequences — an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "one grapheme is not one codepoint; ZWJ is required for emoji yet an attack char in identifiers; blind stripping is itself a harm".
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
