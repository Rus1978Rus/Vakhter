PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_MONGOLIAN_VOWEL_SEPARATOR_U180E_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_MONGOLIAN_VOWEL_SEPARATOR_U180E_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_MONGOLIAN_VOWEL_SEPARATOR_U180E_GEN3_v0_3_EN
CODEPOINT: U+180E
VISIBLE_FORM: ⟨MVS⟩
UNICODE_NAME: MONGOLIAN VOWEL SEPARATOR
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: mongolian vowel separator / an invisible whose Unicode category CHANGED across versions
CATEGORY_ROADMAP: LLM (invisible version-dependent injection) · PHAGO: — (token / whitespace masking)
GLYPH_NOTE: VISIBLE_FORM uses the marker ⟨MVS⟩; the sign itself (U+180E) is an invisible char (now category Cf) and is NEVER written literally here. Examples use ⟨MVS⟩/%E1%A0%8E, never the byte. Its property changed across Unicode versions (once space-like Zs, now a zero-width Cf format char), so different components disagree about it.

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
VISIBLE_FORM: ⟨MVS⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: MVS_FORM ≠ EFFECT
SIGN_CATEGORY:
  - an invisible Mongolian-script control (now category Cf, zero-width)
  - legitimate use: a vowel separator in Mongolian text shaping
  - its Unicode property CHANGED across versions (historically treated as a space, Zs; later reclassified Cf)
  - (misused) an invisible interior char whose meaning depends on the Unicode version a component ships — a version-skew gap between checker and executor

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — being non-printing does not make it inert
  2. NOT_STABLE_PROPERTY — its category/width changed across Unicode versions; two libraries may classify it differently
  3. NOT_ALWAYS_A_SPACE — older tables treated it as whitespace; newer ones do not, so a whitespace rule disagrees by version
  4. NOT_DISPLAY_ONLY — it has (now) zero width, but the byte carries through matching and comparison
  5. NOT_ENCODED_SAFE — "%E1%A0%8E" may be decoded back to the MVS later
  6. NOT_AUTHORITY — it does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; it deceives version-sensitive logic
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_MONGOLIAN_TEXT_ONLY — its injection risk is not limited to Mongolian content
  10. NOT_SANITIZED_PROOF — the presence of the char does not mean the input is sanitized
  11. NOT_SAME_ACROSS_STACK — a checker on one Unicode version and an executor on another can treat it differently → desync

BASE_FORMULAS:
  MVS_FORM ≠ EFFECT
  MVS_FORM ≠ STABLE_PROPERTY_PROOF
  MVS_FORM ≠ ALWAYS_A_SPACE_PROOF
  MVS_FORM ≠ DISPLAY_ONLY_PROOF
  MVS_FORM ≠ ENCODED_SAFETY_PROOF
  MVS_FORM ≠ AUTHORITY
  MVS_FORM ≠ EXECUTION_TRIGGER
  MVS_FORM ≠ MONGOLIAN_TEXT_ONLY_PROOF
  MVS_FORM ≠ INVISIBLE_HARMLESS_PROOF
  MVS_FORM ≠ SANITIZED_PROOF
  MVS_FORM ≠ SAME_ACROSS_STACK_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: MVS (ZONE_1) has parallel functions (legitimate Mongolian vowel separation vs. invisible version-skew injection) co-existing without cultural precession. Its Unicode-property change is a versioning artifact, not a semantic epoch of the sign.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: an invisible shaping control with no gestural predecessor; the version-skew misuse is layered on by the digital epoch in parallel with legitimate Mongolian use.

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
    INPUT: "MVS is U+180E in Unicode"
    CONTEXT: naming the char in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: MVS_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "the Mongolian vowel separator shapes Mongolian text"
    CONTEXT: describing the legitimate function in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: MVS_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <MVS> here"
    CONTEXT: a documentation marker, not the byte
    EXPECTED: INFO
    RISK: NONE
    GUARD: MVS_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "its Unicode category changed between versions"
    CONTEXT: describing the versioning history in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: MVS_FORM ≠ STABLE_PROPERTY_PROOF
  SAFE_CASE_005:
    INPUT: "older tables treated it as whitespace"
    CONTEXT: describing the former classification in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: MVS_FORM ≠ ALWAYS_A_SPACE_PROOF
  SAFE_CASE_006:
    INPUT: "a normalizer can strip it consistently across the stack"
    CONTEXT: describing careful sanitization in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: MVS_FORM ≠ SAME_ACROSS_STACK_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: VERSION_SKEW_DESYNC
    INPUT: "a checker on an old Unicode version and an executor on a new one disagreeing on U+180E"
    CONTEXT: one component treats it as whitespace, the other as a zero-width format char
    RISK: HIGH
    ATTACK: the check normalizes/splits differently than the executor → a bypass in the gap
    GUARD: MVS_FORM ≠ SAME_ACROSS_STACK_PROOF
  RISK_CASE_002:
    NAME: WHITESPACE_ASSUMPTION_GAP
    INPUT: "a trim/blank check assuming U+180E is whitespace"
    CONTEXT: a rule built on the old Zs classification mis-handling the now-Cf char
    RISK: HIGH
    ATTACK: the field is treated as blank/space by one layer but as content by another
    GUARD: MVS_FORM ≠ ALWAYS_A_SPACE_PROOF
  RISK_CASE_003:
    NAME: INVISIBLE_IN_IDENTIFIER
    INPUT: "ad<MVS>min vs admin (look-alike username)"
    CONTEXT: an invisible char inside an ASCII identifier making it compare unequal while looking identical
    RISK: MEDIUM
    ATTACK: "ad<MVS>min" registers as a look-alike of "admin" for impersonation
    GUARD: MVS_FORM ≠ EFFECT
  RISK_CASE_004:
    NAME: ENCODED_MVS_BYPASS
    INPUT: "value%E1%A0%8Etail (with a later decode)"
    CONTEXT: a percent-encoded MVS decoded back before use
    RISK: HIGH
    ATTACK: "%E1%A0%8E" decodes to the MVS AFTER a check → the hidden char reappears
    GUARD: MVS_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: NON_MONGOLIAN_CONTEXT_INJECTION
    INPUT: "an MVS dropped into an otherwise Latin/ASCII string"
    CONTEXT: an MVS used as a generic invisible where it has no legitimate role
    RISK: MEDIUM
    ATTACK: assuming MVS only matters in Mongolian text, a filter ignores it in Latin input
    GUARD: MVS_FORM ≠ MONGOLIAN_TEXT_ONLY_PROOF
  RISK_CASE_006:
    NAME: INVISIBLE_HOMOGLYPH_STACK
    INPUT: "раy<MVS>раl (invisible char + confusable letters combined)"
    CONTEXT: an MVS stacked with confusable letters to deepen a spoof
    RISK: MEDIUM
    ATTACK: the invisible char plus look-alike letters make a hostile string pass a shallow review
    GUARD: MVS_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨ZWSP⟩
    CODEPOINT: U+200B
    NAME: ZERO WIDTH SPACE
    RISK: HIGH
    RULE: ZERO_WIDTH_SPACE ≠ MONGOLIAN_VOWEL_SEPARATOR (both invisible zero-width, but MVS carries a version-changed property and a script role)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨NBSP⟩
    CODEPOINT: U+00A0
    NAME: NO-BREAK SPACE
    RISK: MEDIUM
    RULE: NO_BREAK_SPACE ≠ MONGOLIAN_VOWEL_SEPARATOR (a visible-advance space; MVS is now zero-width and was formerly space-classified)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨WJ⟩
    CODEPOINT: U+2060
    NAME: WORD JOINER
    RISK: MEDIUM
    RULE: WORD_JOINER ≠ MONGOLIAN_VOWEL_SEPARATOR (an invisible no-break glue, not a Mongolian shaping control)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨FVS1⟩
    CODEPOINT: U+180B
    NAME: MONGOLIAN FREE VARIATION SELECTOR ONE
    RISK: MEDIUM
    RULE: MONGOLIAN_FREE_VARIATION_SELECTOR_ONE ≠ MONGOLIAN_VOWEL_SEPARATOR (a neighbouring invisible Mongolian selector; different shaping role)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨ZWNBSP⟩
    CODEPOINT: U+FEFF
    NAME: ZERO WIDTH NO-BREAK SPACE
    RISK: LOW
    RULE: ZERO_WIDTH_NO_BREAK_SPACE ≠ MONGOLIAN_VOWEL_SEPARATOR (a zero-width no-break space / BOM; a different invisible with its own dual role)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "its Unicode property is fixed, so all libs agree"
    RESPONSE: MVS_FORM ≠ STABLE_PROPERTY_PROOF
    RULE: its category/width changed across versions; libraries on different versions disagree
  CG2:
    TRIGGER: "an invisible char cannot be dangerous"
    RESPONSE: MVS_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: invisibility is orthogonal to effect; MVS drives version-skew desync
  CG3:
    TRIGGER: "it is whitespace, trim will drop it"
    RESPONSE: MVS_FORM ≠ ALWAYS_A_SPACE_PROOF
    RULE: only older tables classed it as whitespace; newer ones make it a zero-width format char
  CG4:
    TRIGGER: "'%E1%A0%8E' is safe forever"
    RESPONSE: MVS_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to the MVS before use
  CG5:
    TRIGGER: "it only matters inside Mongolian text"
    RESPONSE: MVS_FORM ≠ MONGOLIAN_TEXT_ONLY_PROOF
    RULE: it can be dropped into any string as a generic invisible
  CG6:
    TRIGGER: "checker and executor treat it the same"
    RESPONSE: MVS_FORM ≠ SAME_ACROSS_STACK_PROOF
    RULE: components on different Unicode versions can classify it differently → desync

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "U+180E across a version-skewed checker/executor"
      NAME: VERSION_SKEW_GAP
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: an MVS classified differently by two components in a pipeline
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "identifier with an interior MVS"
      NAME: SPLIT_IDENTIFIER
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: an MVS inside an ASCII name to impersonate or defeat matching
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "MVS + confusable letters"
      NAME: INVISIBLE_HOMOGLYPH_STACK
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: an invisible char combined with look-alike letters for a spoof
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — MVS's key risk is exactly cross-component version disagreement.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: MVS masks tokens/whitespace across version skew (token/whitespace masking), but does not imitate the existence of a verified entity. Its risks are version-skew desync, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of MVS with ZWSP (U+200B) / WJ (U+2060) to vary the invisible char / evade an MVS-only filter
  A2: percent-encoding "%E1%A0%8E" to slip past a raw-byte scan
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: version-skew desync (checker vs executor classify U+180E differently)
  B2: whitespace-assumption gap (a trim built on the old Zs classification)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "identifier with an interior MVS" (SC2) — split identifier
  C2: "MVS + confusable letters" (SC3) — invisible homoglyph stack
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: MVS presented as "harmless Mongolian shaping" while used as a generic invisible in Latin input
  D2: "%E1%A0%8E" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: invisible identifier confusion (ad<MVS>min vs admin)
  E2: N/A — vector: version-skew gap between components on different Unicode versions
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: its Unicode property is stable across versions
  EXPECTED: FAIL_STABLE_PROPERTY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: an invisible char cannot be dangerous
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: it is always whitespace
  EXPECTED: FAIL_ALWAYS_A_SPACE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E1%A0%8E" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: it only matters inside Mongolian text
  EXPECTED: FAIL_MONGOLIAN_TEXT_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: every component in the stack treats it the same
  EXPECTED: FAIL_SAME_ACROSS_STACK_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to pin one Unicode version (or one explicit invisible-character policy) across every component of a pipeline so a version-changed char like U+180E is classified identically by checker and executor, without depending on each library's shipped tables?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (a single normalization policy with an explicit invisible set applied before every stage, independent of per-library Unicode versions — an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "U+180E's Unicode property changed across versions; treating it as stable or always-whitespace invites a checker/executor desync".
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
