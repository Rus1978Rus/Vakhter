PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_REPLACEMENT_CHARACTER_UFFFD_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_REPLACEMENT_CHARACTER_UFFFD_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_REPLACEMENT_CHARACTER_UFFFD_GEN3_v0_3_EN
CODEPOINT: U+FFFD
VISIBLE_FORM: ⟨REPL⟩
UNICODE_NAME: REPLACEMENT CHARACTER
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: replacement character / the decode-error marker (content was already invalid or lost)
CATEGORY_ROADMAP: LLM (lossy-decode / mojibake injection) · PHAGO: — (corruption masking)
GLYPH_NOTE: VISIBLE_FORM uses the marker ⟨REPL⟩; the sign itself (U+FFFD) is a Symbol (category So), usually shown as a black diamond with a question mark, and is NOT written literally here. Examples use ⟨REPL⟩/%EF%BF%BD, never the byte. It is what a decoder substitutes for an invalid/undecodable byte sequence.

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
VISIBLE_FORM: ⟨REPL⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: REPL_FORM ≠ EFFECT
SIGN_CATEGORY:
  - a Symbol a decoder substitutes for an invalid / undecodable byte sequence
  - legitimate use: signal that a byte could not be decoded (a visible marker of a decode error)
  - its presence means content was ALREADY changed or lost at an earlier decode step
  - (misused) a fingerprint of lossy transcoding an attacker exploits — deliberate mojibake so a check-before-decode and a use-after-decode disagree

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_ORIGINAL_CONTENT — it is a substitution; the original byte(s) it replaced are gone or altered
  2. NOT_ONE_BYTE — a decoder may emit one U+FFFD per invalid byte or one per bad sequence; the count is decoder-dependent, not the original length
  3. NOT_HARMLESS_NOISE — its presence signals a decode error upstream that may have dropped or reshaped meaningful data
  4. NOT_OBJECT_REPLACEMENT — U+FFFD marks a decode error; U+FFFC marks a valid embedded object — opposite meanings, adjacent codepoints
  5. NOT_ENCODED_SAFE — "%EF%BF%BD" may be decoded back to the replacement character later
  6. NOT_AUTHORITY — it does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; it marks corruption
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_STABLE_DECODE — different decoders substitute differently (count/position), so check-before-decode ≠ use-after-decode
  10. NOT_SANITIZED_PROOF — the presence of the char does not mean the input is sanitized; it may hide a stripped payload
  11. NOT_ROUNDTRIP_PROOF — once substituted, the data cannot round-trip back to the original bytes

BASE_FORMULAS:
  REPL_FORM ≠ EFFECT
  REPL_FORM ≠ ORIGINAL_CONTENT_PROOF
  REPL_FORM ≠ ONE_BYTE_PROOF
  REPL_FORM ≠ HARMLESS_NOISE_PROOF
  REPL_FORM ≠ OBJECT_REPLACEMENT_PROOF
  REPL_FORM ≠ ENCODED_SAFETY_PROOF
  REPL_FORM ≠ AUTHORITY
  REPL_FORM ≠ EXECUTION_TRIGGER
  REPL_FORM ≠ STABLE_DECODE_PROOF
  REPL_FORM ≠ SANITIZED_PROOF
  REPL_FORM ≠ ROUNDTRIP_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: REPL (ZONE_1) has parallel functions (legitimate decode-error signal vs. lossy-transcode / mojibake injection fingerprint) co-existing without cultural precession. Polysemy of a stable substitution symbol.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a decode-error substitution symbol with no gestural predecessor; the lossy-transcode misuse is layered on by the digital epoch in parallel with legitimate error signalling.

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
    INPUT: "REPL is U+FFFD in Unicode"
    CONTEXT: naming the char in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: REPL_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "a decoder emits U+FFFD for an invalid byte"
    CONTEXT: describing the legitimate function in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: REPL_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <REPL> here"
    CONTEXT: a documentation marker, not the byte
    EXPECTED: INFO
    RISK: NONE
    GUARD: REPL_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "it is a substitution, not the original content"
    CONTEXT: describing what it replaced in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: REPL_FORM ≠ ORIGINAL_CONTENT_PROOF
  SAFE_CASE_005:
    INPUT: "it marks a decode error, not an embedded object"
    CONTEXT: distinguishing it from U+FFFC in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: REPL_FORM ≠ OBJECT_REPLACEMENT_PROOF
  SAFE_CASE_006:
    INPUT: "its presence signals earlier corruption to investigate"
    CONTEXT: describing it as a diagnostic in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: REPL_FORM ≠ HARMLESS_NOISE_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: DECODE_TIMING_DESYNC
    INPUT: "a check run on raw bytes and a use run after decoding to U+FFFD"
    CONTEXT: check-before-decode and use-after-decode seeing different strings
    RISK: HIGH
    ATTACK: an invalid sequence passes a raw-byte check, then decodes to a different string the executor uses
    GUARD: REPL_FORM ≠ STABLE_DECODE_PROOF
  RISK_CASE_002:
    NAME: MOJIBAKE_FILTER_EVASION
    INPUT: "deliberately malformed bytes that decode to REPL, splitting a keyword"
    CONTEXT: crafted invalid bytes inserted so a substring match fails after substitution
    RISK: HIGH
    ATTACK: the malformed sequence breaks "javascript" into pieces around a REPL a lenient stage rejoins/ignores
    GUARD: REPL_FORM ≠ ORIGINAL_CONTENT_PROOF
  RISK_CASE_003:
    NAME: SUBSTITUTION_COUNT_SHIFT
    INPUT: "a bad sequence one decoder replaces with 1 REPL and another with 3"
    CONTEXT: decoders disagreeing on how many U+FFFD to emit
    RISK: MEDIUM
    ATTACK: a length/offset computed on one decoder mis-indexes on another → a parsing shift
    GUARD: REPL_FORM ≠ ONE_BYTE_PROOF
  RISK_CASE_004:
    NAME: ENCODED_REPL_BYPASS
    INPUT: "value%EF%BF%BDtail (with a later decode)"
    CONTEXT: a percent-encoded replacement character decoded back before use
    RISK: MEDIUM
    ATTACK: "%EF%BF%BD" decodes to a literal U+FFFD AFTER a check, mimicking a decode error to confuse handling
    GUARD: REPL_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: HIDDEN_STRIPPED_PAYLOAD
    INPUT: "a REPL where meaningful bytes were dropped during transcode"
    CONTEXT: treating the REPL as harmless while it masks removed content
    RISK: MEDIUM
    ATTACK: the substitution hides that data (e.g. a control or delimiter) was silently lost, changing meaning
    GUARD: REPL_FORM ≠ HARMLESS_NOISE_PROOF
  RISK_CASE_006:
    NAME: OBJECT_CONFUSION
    INPUT: "a pipeline treating U+FFFD like U+FFFC (embedded object)"
    CONTEXT: confusing the decode-error marker with the object placeholder
    RISK: LOW
    ATTACK: mishandling one as the other mis-routes error vs embedded-object logic
    GUARD: REPL_FORM ≠ OBJECT_REPLACEMENT_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨OBJ⟩
    CODEPOINT: U+FFFC
    NAME: OBJECT REPLACEMENT CHARACTER
    RISK: HIGH
    RULE: OBJECT_REPLACEMENT_CHARACTER ≠ REPLACEMENT_CHARACTER (U+FFFC marks a valid embedded object; U+FFFD marks a decode error — opposite meanings, adjacent codepoints)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨SUB⟩
    CODEPOINT: U+001A
    NAME: SUBSTITUTE
    RISK: MEDIUM
    RULE: SUBSTITUTE ≠ REPLACEMENT_CHARACTER (a C0 control historically used for a substitute character; a different, older mechanism)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨QMARK⟩
    CODEPOINT: U+003F
    NAME: QUESTION MARK
    RISK: MEDIUM
    RULE: QUESTION_MARK ≠ REPLACEMENT_CHARACTER (some transcoders substitute an ASCII "?" for undecodable chars; a different, ambiguous substitution)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨BLACK-DIAMOND⟩
    CODEPOINT: U+25C6
    NAME: BLACK DIAMOND
    RISK: LOW
    RULE: BLACK_DIAMOND ≠ REPLACEMENT_CHARACTER (the diamond glyph REPL is often drawn as; a plain geometric symbol)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨NULL⟩
    CODEPOINT: U+0000
    NAME: NULL
    RISK: LOW
    RULE: NULL ≠ REPLACEMENT_CHARACTER (a NUL is sometimes substituted or truncated on; a different corruption mechanism)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "the REPL is the original content"
    RESPONSE: REPL_FORM ≠ ORIGINAL_CONTENT_PROOF
    RULE: it is a substitution; the bytes it replaced are gone or altered
  CG2:
    TRIGGER: "one REPL means one lost byte"
    RESPONSE: REPL_FORM ≠ ONE_BYTE_PROOF
    RULE: decoders emit a decoder-dependent count of U+FFFD; it is not the original length
  CG3:
    TRIGGER: "a REPL is just harmless noise"
    RESPONSE: REPL_FORM ≠ HARMLESS_NOISE_PROOF
    RULE: it signals an upstream decode error that may have dropped meaningful data
  CG4:
    TRIGGER: "'%EF%BF%BD' is safe forever"
    RESPONSE: REPL_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to a literal U+FFFD before use
  CG5:
    TRIGGER: "check-before-decode equals use-after-decode"
    RESPONSE: REPL_FORM ≠ STABLE_DECODE_PROOF
    RULE: decoding to U+FFFD changes the string; the two stages disagree
  CG6:
    TRIGGER: "U+FFFD and U+FFFC are the same replacement char"
    RESPONSE: REPL_FORM ≠ OBJECT_REPLACEMENT_PROOF
    RULE: one marks a decode error, the other a valid embedded object — opposite meanings

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "malformed bytes -> REPL inside a keyword"
      NAME: MOJIBAKE_SPLIT
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: an invalid sequence decoding to a REPL that splits a blocked keyword
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "raw check then decode-to-REPL"
      NAME: DECODE_TIMING_GAP
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: a check on bytes and a use on the decoded string disagreeing
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "REPL count varying across decoders"
      NAME: OFFSET_SHIFT
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: a length/offset computed on one decoder mis-indexing on another
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — REPL's risk is exactly about decode timing and substitution across a sequence.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: REPL marks/masks corruption (corruption masking), but does not imitate the existence of a verified entity. Its risks are decode-timing desync and hidden data loss, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: confusion with OBJECT REPLACEMENT (U+FFFC) / an ASCII "?" substitution to disguise a decode error
  A2: percent-encoding "%EF%BF%BD" to inject a literal replacement character past a raw-byte scan
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: decode-timing desync (raw-byte check vs decoded-string use)
  B2: mojibake filter evasion (malformed bytes decode to a REPL splitting a keyword)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "REPL count varying across decoders" (SC3) — offset shift
  C2: "malformed bytes -> REPL inside a keyword" (SC1) — mojibake split
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: REPL presented as "harmless noise" while it masks stripped/lost bytes
  D2: "%EF%BF%BD" as a "safe" encoded decode-error marker with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: hidden data loss behind a substitution
  E2: N/A — vector: decode-error/embedded-object confusion (U+FFFD vs U+FFFC)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: the REPL is the original content
  EXPECTED: FAIL_ORIGINAL_CONTENT_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: one REPL equals one lost byte
  EXPECTED: FAIL_ONE_BYTE_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: a REPL is harmless noise
  EXPECTED: FAIL_HARMLESS_NOISE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%EF%BF%BD" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: check-before-decode equals use-after-decode
  EXPECTED: FAIL_STABLE_DECODE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: U+FFFD is the same as U+FFFC
  EXPECTED: FAIL_OBJECT_REPLACEMENT_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to decode once to a canonical form before any check or use (never checking raw bytes then using a decoded string), and to treat any U+FFFD as a hard signal of upstream corruption to reject or investigate — without breaking legitimate error reporting?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (a pipeline that decodes-then-checks on one canonical string and flags/rejects inputs containing decode-error markers — an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "U+FFFD is a lossy substitution, not the original; its count is decoder-dependent and check-before-decode disagrees with use-after-decode".
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
