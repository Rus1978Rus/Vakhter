PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_LINE_SEPARATOR_U2028_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_LINE_SEPARATOR_U2028_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_LINE_SEPARATOR_U2028_GEN3_v0_3_EN
CODEPOINT: U+2028
VISIBLE_FORM: ⟨LSEP⟩
UNICODE_NAME: LINE SEPARATOR
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: line separator / a line break that is not LF or CR (parser disagreement, JS-literal break)
CATEGORY_ROADMAP: LLM (invisible line-break injection) · PHAGO: — (line-structure masking)
GLYPH_NOTE: VISIBLE_FORM uses the marker ⟨LSEP⟩; the sign itself (U+2028) is a Line Separator (Zl) and is NEVER written literally here — a literal U+2028 would be treated as a new line by Unicode-aware tools and could corrupt block parsing of this document. Examples use ⟨LSEP⟩/%E2%80%A8, never the byte.

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
VISIBLE_FORM: ⟨LSEP⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: LSEP_FORM ≠ EFFECT
SIGN_CATEGORY:
  - a Unicode line terminator (category Zl) that starts a new line to Unicode-aware code
  - legitimate line break in Unicode text (an alternative to LF)
  - is NOT U+000A (LF) or U+000D (CR); an LF/CR-only parser does not treat it as a line break
  - (misused) invisible-ish line break that a \n-only parser misses → line-count / log / record desync, and historically a JavaScript string-literal break

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_NEWLINE_LF — it is a line break but a DIFFERENT codepoint than LF (U+000A)
  2. NOT_SEEN_BY_EVERY_PARSER — an LF/CR-only splitter does not break on U+2028; a Unicode splitlines() does → disagreement
  3. NOT_VISIBLE — it usually renders as nothing or a small gap, so a human review may not notice a new line
  4. NOT_PSEP — U+2028 is a LINE separator (Zl); U+2029 is a PARAGRAPH separator (Zp); handling one is not handling the other
  5. NOT_ENCODED_SAFE — "%E2%80%A8" may be decoded back to the U+2028 later
  6. NOT_AUTHORITY — it does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; it deceives line-based logic
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_JS_STRING_SAFE — historically (pre-ES2019) a raw U+2028 was illegal in a JavaScript string literal, breaking JSON embedded in <script>
  10. NOT_SANITIZED_PROOF — the presence of the char does not mean the input is sanitized
  11. NOT_SINGLE_LINE_PROOF — a value that "looks like one line" may contain a U+2028 that splits it downstream

BASE_FORMULAS:
  LSEP_FORM ≠ EFFECT
  LSEP_FORM ≠ NEWLINE_LF_PROOF
  LSEP_FORM ≠ SEEN_BY_EVERY_PARSER_PROOF
  LSEP_FORM ≠ VISIBLE_PROOF
  LSEP_FORM ≠ PSEP_EQUIVALENCE_PROOF
  LSEP_FORM ≠ ENCODED_SAFETY_PROOF
  LSEP_FORM ≠ AUTHORITY
  LSEP_FORM ≠ EXECUTION_TRIGGER
  LSEP_FORM ≠ JS_STRING_SAFE_PROOF
  LSEP_FORM ≠ SANITIZED_PROOF
  LSEP_FORM ≠ SINGLE_LINE_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: LSEP (ZONE_1) has parallel functions (legitimate Unicode line break vs. parser-disagreement injection) co-existing without cultural precession. Polysemy of a stable separator char.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a Unicode-era line terminator with no gestural predecessor; the parser-desync and log-injection misuse is layered on by the digital epoch in parallel with legitimate line-break use.

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
    INPUT: "LSEP is U+2028 in Unicode"
    CONTEXT: naming the char in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: LSEP_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "a line separator starts a new line in Unicode text"
    CONTEXT: describing the legitimate function in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: LSEP_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <LSEP> here"
    CONTEXT: a documentation marker, not the byte
    EXPECTED: INFO
    RISK: NONE
    GUARD: LSEP_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "it is a different codepoint from LF"
    CONTEXT: distinguishing it from U+000A in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: LSEP_FORM ≠ NEWLINE_LF_PROOF
  SAFE_CASE_005:
    INPUT: "a line separator differs from a paragraph separator"
    CONTEXT: distinguishing it from U+2029 in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: LSEP_FORM ≠ PSEP_EQUIVALENCE_PROOF
  SAFE_CASE_006:
    INPUT: "a Unicode-aware splitlines can normalize it"
    CONTEXT: describing careful handling in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: LSEP_FORM ≠ SEEN_BY_EVERY_PARSER_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: LOG_INJECTION
    INPUT: "a field value containing a U+2028 written into a log"
    CONTEXT: a Unicode-aware log viewer showing a forged extra line the \n-based writer did not intend
    RISK: HIGH
    ATTACK: the U+2028 injects a fake log line (spoofed entry) invisible to an LF-only review
    GUARD: LSEP_FORM ≠ SINGLE_LINE_PROOF
  RISK_CASE_002:
    NAME: PARSER_LINE_DESYNC
    INPUT: "record<LSEP>second half processed as one line by an LF-only parser"
    CONTEXT: an LF-only splitter keeping one line where a Unicode splitter sees two (or vice versa)
    RISK: HIGH
    ATTACK: the check and the executor disagree on line boundaries → a smuggled second line
    GUARD: LSEP_FORM ≠ SEEN_BY_EVERY_PARSER_PROOF
  RISK_CASE_003:
    NAME: JS_STRING_LITERAL_BREAK
    INPUT: "JSON containing a raw U+2028 embedded in a <script> block"
    CONTEXT: a pre-ES2019 JS engine treating the raw U+2028 as a line terminator inside a string literal
    RISK: MEDIUM
    ATTACK: the raw separator breaks the string literal, turning data into code (an XSS/parse break)
    GUARD: LSEP_FORM ≠ JS_STRING_SAFE_PROOF
  RISK_CASE_004:
    NAME: ENCODED_LSEP_BYPASS
    INPUT: "value%E2%80%A8tail (with a later decode)"
    CONTEXT: a percent-encoded U+2028 decoded back before use
    RISK: HIGH
    ATTACK: "%E2%80%A8" decodes to the U+2028 AFTER a check → the hidden line break reappears
    GUARD: LSEP_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: SEPARATOR_FAMILY_GAP
    INPUT: "input using U+2029 (PSEP) or U+0085 (NEL) where only U+2028 is filtered"
    CONTEXT: other Unicode line/paragraph terminators slipping past an LSEP-only filter
    RISK: MEDIUM
    ATTACK: filtering only U+2028 misses U+2029/U+0085 and other break codepoints
    GUARD: LSEP_FORM ≠ PSEP_EQUIVALENCE_PROOF
  RISK_CASE_006:
    NAME: INVISIBLE_BREAK_REVIEW_BYPASS
    INPUT: "a value that looks like one line but splits when rendered"
    CONTEXT: a U+2028 passing a single-line visual review then splitting downstream
    RISK: MEDIUM
    ATTACK: the near-invisible break makes a multi-line payload read as one harmless line
    GUARD: LSEP_FORM ≠ VISIBLE_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨PSEP⟩
    CODEPOINT: U+2029
    NAME: PARAGRAPH SEPARATOR
    RISK: HIGH
    RULE: PARAGRAPH_SEPARATOR ≠ LINE_SEPARATOR (a paragraph break (Zp) vs a line break (Zl); a filter handling one may miss the other)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨LF⟩
    CODEPOINT: U+000A
    NAME: LINE FEED
    RISK: HIGH
    RULE: LINE_FEED ≠ LINE_SEPARATOR (the ASCII newline; the LF/CR-only world does not treat U+2028 as a break)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨NEL⟩
    CODEPOINT: U+0085
    NAME: NEXT LINE
    RISK: MEDIUM
    RULE: NEXT_LINE ≠ LINE_SEPARATOR (another Unicode line terminator, from the C1 controls; different codepoint, similar effect)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨CR⟩
    CODEPOINT: U+000D
    NAME: CARRIAGE RETURN
    RISK: MEDIUM
    RULE: CARRIAGE_RETURN ≠ LINE_SEPARATOR (the classic CR line ending; not U+2028)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨VT⟩
    CODEPOINT: U+000B
    NAME: LINE TABULATION
    RISK: LOW
    RULE: LINE_TABULATION ≠ LINE_SEPARATOR (a vertical tab that some parsers treat as a break; a distinct control)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "it is a newline, so it is LF"
    RESPONSE: LSEP_FORM ≠ NEWLINE_LF_PROOF
    RULE: it is a line break but a different codepoint than U+000A
  CG2:
    TRIGGER: "our parser handles newlines, so it sees this"
    RESPONSE: LSEP_FORM ≠ SEEN_BY_EVERY_PARSER_PROOF
    RULE: an LF/CR-only splitter does not break on U+2028; a Unicode splitter does — they disagree
  CG3:
    TRIGGER: "a human would see the new line"
    RESPONSE: LSEP_FORM ≠ VISIBLE_PROOF
    RULE: it usually renders as nothing/a gap; a reviewer may miss the break
  CG4:
    TRIGGER: "'%E2%80%A8' is safe forever"
    RESPONSE: LSEP_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to the U+2028 before use
  CG5:
    TRIGGER: "we filter U+2028, so all Unicode breaks are handled"
    RESPONSE: LSEP_FORM ≠ PSEP_EQUIVALENCE_PROOF
    RULE: U+2029 (PSEP), U+0085 (NEL) and others are separate break codepoints
  CG6:
    TRIGGER: "the string looks like one line, so it is one line"
    RESPONSE: LSEP_FORM ≠ SINGLE_LINE_PROOF
    RULE: a near-invisible U+2028 can split it into two lines downstream

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "field value with an interior U+2028"
      NAME: LINE_SPLIT_INJECTION
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: an interior line separator forging an extra log/record line
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "raw U+2028 inside a JS/JSON string"
      NAME: STRING_LITERAL_BREAK
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: a raw separator breaking a pre-ES2019 string literal
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "mixed U+2028 + U+2029 + U+0085"
      NAME: BREAK_FAMILY_MIX
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: several break codepoints combined to evade an LSEP-only filter
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — LSEP's risk is exactly about where a break lands in a sequence.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: U+2028 forges line/record structure (line-structure masking), but does not imitate the existence of a verified entity. Its risks are parser/log desync, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of U+2028 with U+2029 (PSEP) / U+0085 (NEL) to vary the break codepoint / evade an LSEP-only filter
  A2: percent-encoding "%E2%80%A8" to slip past a raw-byte scan
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: log injection (a U+2028 forging an extra log line)
  B2: parser line desync (LF-only vs Unicode splitter disagree)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "raw U+2028 inside a JS/JSON string" (SC2) — string-literal break
  C2: "mixed U+2028 + U+2029 + U+0085" (SC3) — break-family mix
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: U+2028 presented as "just a newline" so it is treated like LF and normalized wrong (or not at all)
  D2: "%E2%80%A8" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: forged record/line structure via an invisible break
  E2: N/A — vector: LSEP-only filter missing the wider line/paragraph break family
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: a line separator is the same as LF
  EXPECTED: FAIL_NEWLINE_LF_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: every newline-aware parser sees U+2028
  EXPECTED: FAIL_SEEN_BY_EVERY_PARSER_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: a reviewer always sees the new line
  EXPECTED: FAIL_VISIBLE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E2%80%A8" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: filtering U+2028 handles all Unicode breaks
  EXPECTED: FAIL_PSEP_EQUIVALENCE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: a raw U+2028 is safe inside a JS string literal
  EXPECTED: FAIL_JS_STRING_SAFE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to normalize the whole Unicode line/paragraph break family (U+2028, U+2029, U+0085, U+000B, U+000C …) consistently before line-splitting, logging, JSON/JS embedding and record parsing, without breaking legitimate Unicode line breaks?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (a Unicode-aware line normalizer applied once before split, log-write, embed and parse; escape or reject raw separators in JS/JSON contexts — an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "U+2028 is a line break but not LF; LF-only and Unicode-aware parsers disagree, and it is only one of a wider break family".
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
