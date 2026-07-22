PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_PARAGRAPH_SEPARATOR_U2029_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_PARAGRAPH_SEPARATOR_U2029_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_PARAGRAPH_SEPARATOR_U2029_GEN3_v0_3_EN
CODEPOINT: U+2029
VISIBLE_FORM: ⟨PSEP⟩
UNICODE_NAME: PARAGRAPH SEPARATOR
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: paragraph separator / a paragraph break that is not LF, and a bidi paragraph boundary
CATEGORY_ROADMAP: LLM (invisible paragraph-break injection) · PHAGO: — (paragraph-structure masking)
GLYPH_NOTE: VISIBLE_FORM uses the marker ⟨PSEP⟩; the sign itself (U+2029) is a Paragraph Separator (Zp) and is NEVER written literally here — a literal U+2029 would be treated as a new paragraph/line by Unicode-aware tools and could corrupt block parsing of this document. Examples use ⟨PSEP⟩/%E2%80%A9, never the byte.

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
VISIBLE_FORM: ⟨PSEP⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: PSEP_FORM ≠ EFFECT
SIGN_CATEGORY:
  - a Unicode paragraph terminator (category Zp) that ends a paragraph to Unicode-aware code
  - legitimate paragraph break in Unicode text
  - is NOT U+000A (LF); an LF-only parser does not treat it as a break, and it is a PARAGRAPH boundary, not just a line break
  - (misused) a near-invisible paragraph break that resets bidi paragraph state and that a \n-only parser misses → parser/log desync, JS-literal break, and bidi-paragraph reset

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_NEWLINE_LF — it is a break but a DIFFERENT codepoint than LF (U+000A)
  2. NOT_SEEN_BY_EVERY_PARSER — an LF/CR-only splitter does not break on U+2029; a Unicode splitlines() does → disagreement
  3. NOT_VISIBLE — it usually renders as nothing or a gap, so a human review may not notice the break
  4. NOT_LSEP — U+2029 is a PARAGRAPH separator (Zp); U+2028 is a LINE separator (Zl); handling one is not handling the other
  5. NOT_BIDI_NEUTRAL — it defines the paragraph boundary that terminates any open bidi embedding/override/isolate; where it lands changes bidi resolution
  6. NOT_ENCODED_SAFE — "%E2%80%A9" may be decoded back to the U+2029 later
  7. NOT_AUTHORITY — it does not confirm officialness
  8. NOT_EXECUTION_TRIGGER — by itself it executes nothing; it deceives paragraph/line logic
  9. NOT_JS_STRING_SAFE — historically (pre-ES2019) a raw U+2029 was illegal in a JavaScript string literal, breaking JSON embedded in <script>
  10. NOT_SANITIZED_PROOF — the presence of the char does not mean the input is sanitized
  11. NOT_SINGLE_PARAGRAPH_PROOF — a value that "looks like one paragraph" may contain a U+2029 that splits it downstream

BASE_FORMULAS:
  PSEP_FORM ≠ EFFECT
  PSEP_FORM ≠ NEWLINE_LF_PROOF
  PSEP_FORM ≠ SEEN_BY_EVERY_PARSER_PROOF
  PSEP_FORM ≠ VISIBLE_PROOF
  PSEP_FORM ≠ LSEP_EQUIVALENCE_PROOF
  PSEP_FORM ≠ BIDI_NEUTRAL_PROOF
  PSEP_FORM ≠ ENCODED_SAFETY_PROOF
  PSEP_FORM ≠ AUTHORITY
  PSEP_FORM ≠ EXECUTION_TRIGGER
  PSEP_FORM ≠ JS_STRING_SAFE_PROOF
  PSEP_FORM ≠ SANITIZED_PROOF
  PSEP_FORM ≠ SINGLE_PARAGRAPH_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: PSEP (ZONE_1) has parallel functions (legitimate Unicode paragraph break vs. parser-disagreement / bidi-reset injection) co-existing without cultural precession. Polysemy of a stable separator char.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a Unicode-era paragraph terminator with no gestural predecessor; the parser-desync and bidi-reset misuse is layered on by the digital epoch in parallel with legitimate paragraph-break use.

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
    INPUT: "PSEP is U+2029 in Unicode"
    CONTEXT: naming the char in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: PSEP_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "a paragraph separator ends a paragraph in Unicode text"
    CONTEXT: describing the legitimate function in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: PSEP_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <PSEP> here"
    CONTEXT: a documentation marker, not the byte
    EXPECTED: INFO
    RISK: NONE
    GUARD: PSEP_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "it is a different codepoint from LF"
    CONTEXT: distinguishing it from U+000A in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: PSEP_FORM ≠ NEWLINE_LF_PROOF
  SAFE_CASE_005:
    INPUT: "a paragraph separator differs from a line separator"
    CONTEXT: distinguishing it from U+2028 in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: PSEP_FORM ≠ LSEP_EQUIVALENCE_PROOF
  SAFE_CASE_006:
    INPUT: "it marks a bidi paragraph boundary"
    CONTEXT: describing the bidi role in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: PSEP_FORM ≠ BIDI_NEUTRAL_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: LOG_INJECTION
    INPUT: "a field value containing a U+2029 written into a log"
    CONTEXT: a Unicode-aware log viewer showing a forged extra paragraph/line the \n-based writer did not intend
    RISK: HIGH
    ATTACK: the U+2029 injects a fake log entry invisible to an LF-only review
    GUARD: PSEP_FORM ≠ SINGLE_PARAGRAPH_PROOF
  RISK_CASE_002:
    NAME: PARSER_BREAK_DESYNC
    INPUT: "record<PSEP>second half processed as one unit by an LF-only parser"
    CONTEXT: an LF-only splitter keeping one record where a Unicode splitter sees two
    RISK: HIGH
    ATTACK: the check and the executor disagree on boundaries → a smuggled second record
    GUARD: PSEP_FORM ≠ SEEN_BY_EVERY_PARSER_PROOF
  RISK_CASE_003:
    NAME: BIDI_PARAGRAPH_RESET
    INPUT: "an open bidi override followed by a U+2029"
    CONTEXT: the paragraph separator terminating the bidi paragraph, changing where an override/isolate ends
    RISK: MEDIUM
    ATTACK: the attacker uses the paragraph boundary to control the extent of a bidi reorder (see the override/isolate cards)
    GUARD: PSEP_FORM ≠ BIDI_NEUTRAL_PROOF
  RISK_CASE_004:
    NAME: ENCODED_PSEP_BYPASS
    INPUT: "value%E2%80%A9tail (with a later decode)"
    CONTEXT: a percent-encoded U+2029 decoded back before use
    RISK: HIGH
    ATTACK: "%E2%80%A9" decodes to the U+2029 AFTER a check → the hidden break reappears
    GUARD: PSEP_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: SEPARATOR_FAMILY_GAP
    INPUT: "input using U+2028 (LSEP) or U+0085 (NEL) where only U+2029 is filtered"
    CONTEXT: other Unicode line/paragraph terminators slipping past a PSEP-only filter
    RISK: MEDIUM
    ATTACK: filtering only U+2029 misses U+2028/U+0085 and other break codepoints
    GUARD: PSEP_FORM ≠ LSEP_EQUIVALENCE_PROOF
  RISK_CASE_006:
    NAME: JS_STRING_LITERAL_BREAK
    INPUT: "JSON containing a raw U+2029 embedded in a <script> block"
    CONTEXT: a pre-ES2019 JS engine treating the raw U+2029 as a line terminator inside a string literal
    RISK: MEDIUM
    ATTACK: the raw separator breaks the string literal, turning data into code (an XSS/parse break)
    GUARD: PSEP_FORM ≠ JS_STRING_SAFE_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨LSEP⟩
    CODEPOINT: U+2028
    NAME: LINE SEPARATOR
    RISK: HIGH
    RULE: LINE_SEPARATOR ≠ PARAGRAPH_SEPARATOR (a line break (Zl) vs a paragraph break (Zp); a filter handling one may miss the other)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨LF⟩
    CODEPOINT: U+000A
    NAME: LINE FEED
    RISK: HIGH
    RULE: LINE_FEED ≠ PARAGRAPH_SEPARATOR (the ASCII newline; the LF/CR-only world does not treat U+2029 as a break)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨NEL⟩
    CODEPOINT: U+0085
    NAME: NEXT LINE
    RISK: MEDIUM
    RULE: NEXT_LINE ≠ PARAGRAPH_SEPARATOR (another Unicode line terminator, from the C1 controls; different codepoint, similar effect)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨CR⟩
    CODEPOINT: U+000D
    NAME: CARRIAGE RETURN
    RISK: MEDIUM
    RULE: CARRIAGE_RETURN ≠ PARAGRAPH_SEPARATOR (the classic CR line ending; not U+2029)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨FF⟩
    CODEPOINT: U+000C
    NAME: FORM FEED
    RISK: LOW
    RULE: FORM_FEED ≠ PARAGRAPH_SEPARATOR (a page/section break control that some parsers treat as a break; a distinct control)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "it is a newline, so it is LF"
    RESPONSE: PSEP_FORM ≠ NEWLINE_LF_PROOF
    RULE: it is a break but a different codepoint than U+000A
  CG2:
    TRIGGER: "our parser handles newlines, so it sees this"
    RESPONSE: PSEP_FORM ≠ SEEN_BY_EVERY_PARSER_PROOF
    RULE: an LF/CR-only splitter does not break on U+2029; a Unicode splitter does — they disagree
  CG3:
    TRIGGER: "a human would see the break"
    RESPONSE: PSEP_FORM ≠ VISIBLE_PROOF
    RULE: it usually renders as nothing/a gap; a reviewer may miss the break
  CG4:
    TRIGGER: "line and paragraph separators are the same"
    RESPONSE: PSEP_FORM ≠ LSEP_EQUIVALENCE_PROOF
    RULE: U+2029 (Zp) is a paragraph boundary; U+2028 (Zl) is a line boundary; they differ
  CG5:
    TRIGGER: "a paragraph break has nothing to do with bidi"
    RESPONSE: PSEP_FORM ≠ BIDI_NEUTRAL_PROOF
    RULE: it terminates the bidi paragraph, bounding any open override/embedding/isolate
  CG6:
    TRIGGER: "'%E2%80%A9' is safe forever"
    RESPONSE: PSEP_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to the U+2029 before use
  CG7:
    TRIGGER: "the string looks like one paragraph, so it is one"
    RESPONSE: PSEP_FORM ≠ SINGLE_PARAGRAPH_PROOF
    RULE: a near-invisible U+2029 can split it downstream

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "field value with an interior U+2029"
      NAME: PARAGRAPH_SPLIT_INJECTION
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: an interior paragraph separator forging an extra log/record
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "open bidi control then U+2029"
      NAME: BIDI_PARAGRAPH_BOUND
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: a paragraph separator bounding an open override/isolate to control the reorder extent
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "mixed U+2029 + U+2028 + U+0085"
      NAME: BREAK_FAMILY_MIX
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: several break codepoints combined to evade a PSEP-only filter
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — PSEP's risk is exactly about where a paragraph boundary lands in a sequence.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: U+2029 forges paragraph/record structure (paragraph-structure masking), but does not imitate the existence of a verified entity. Its risks are parser/log desync and bidi-extent control, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of U+2029 with U+2028 (LSEP) / U+0085 (NEL) to vary the break codepoint / evade a PSEP-only filter
  A2: percent-encoding "%E2%80%A9" to slip past a raw-byte scan
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: log injection (a U+2029 forging an extra log entry)
  B2: parser break desync (LF-only vs Unicode splitter disagree)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "open bidi control then U+2029" (SC2) — bidi paragraph bound
  C2: "mixed U+2029 + U+2028 + U+0085" (SC3) — break-family mix
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: U+2029 presented as "just a newline" so it is treated like LF and normalized wrong (or not at all)
  D2: "%E2%80%A9" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: forged record/paragraph structure via an invisible break
  E2: N/A — vector: PSEP-only filter missing the wider line/paragraph break family
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: a paragraph separator is the same as LF
  EXPECTED: FAIL_NEWLINE_LF_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: every newline-aware parser sees U+2029
  EXPECTED: FAIL_SEEN_BY_EVERY_PARSER_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: line and paragraph separators are interchangeable
  EXPECTED: FAIL_LSEP_EQUIVALENCE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E2%80%A9" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: a paragraph break is bidi-neutral
  EXPECTED: FAIL_BIDI_NEUTRAL_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: a raw U+2029 is safe inside a JS string literal
  EXPECTED: FAIL_JS_STRING_SAFE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to normalize the whole Unicode line/paragraph break family (U+2028, U+2029, U+0085, U+000B, U+000C …) consistently before splitting, logging, JSON/JS embedding and record parsing, while accounting for the bidi paragraph reset U+2029 causes, without breaking legitimate paragraph breaks?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (a Unicode-aware break normalizer applied once before split, log-write, embed and parse; escape/reject raw separators in JS/JSON; account for bidi paragraph boundaries — an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "U+2029 is a paragraph break (not LF, not U+2028) that also resets the bidi paragraph; LF-only and Unicode-aware parsers disagree".
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
