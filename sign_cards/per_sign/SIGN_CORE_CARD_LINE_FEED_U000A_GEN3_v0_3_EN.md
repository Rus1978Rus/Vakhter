PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_LINE_FEED_U000A_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_LINE_FEED_U000A_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_LINE_FEED_U000A_GEN3_v0_3_EN
CODEPOINT: U+000A
VISIBLE_FORM: ␊
UNICODE_NAME: <control> LINE FEED (LF)
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: line feed / newline (non-printing)
CATEGORY_ROADMAP: INJ (CRLF/header injection, log forging) · PHAGO: — (record boundary forgery)
GLYPH_NOTE: VISIBLE_FORM uses ␊ (U+240A SYMBOL FOR LINE FEED) as a printable picture; the sign itself (U+000A) is a non-printing control character.

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
VISIBLE_FORM: ␊
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: LINE_FEED_FORM ≠ EFFECT
SIGN_CATEGORY:
  - line terminator / newline in text and files
  - record boundary in logs / NDJSON / CSV
  - header/field terminator in wire protocols (HTTP, SMTP)
  - statement/line boundary in scripts

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_NEWLINE_ONLY — LF is not always "just a newline" (in a header it terminates/injects a line)
  2. NOT_BOUNDARY_SAFE — a record boundary lets an attacker forge a NEW record/line
  3. NOT_INVISIBLE_MEANS_HARMLESS — being non-printing does not make it inert
  4. NOT_ESCAPED_PROOF — a shown "\n" is not proof a real LF was neutralized
  5. NOT_ENCODED_SAFE — "%0A" / "\n" may be decoded back to LF later
  6. NOT_AUTHORITY — LF does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; context makes it split
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_HEADER_SAFE — LF in a header enables response/log/SMTP splitting
  10. NOT_SANITIZED_PROOF — the presence of a newline does not mean the input is sanitized
  11. NOT_OUTPUT_CONTEXT_PROOF — safety depends on the protocol/parse context

BASE_FORMULAS:
  LINE_FEED_FORM ≠ EFFECT
  LINE_FEED_FORM ≠ NEWLINE_ONLY_PROOF
  LINE_FEED_FORM ≠ BOUNDARY_SAFETY_PROOF
  LINE_FEED_FORM ≠ INVISIBLE_HARMLESS_PROOF
  LINE_FEED_FORM ≠ ESCAPED_PROOF
  LINE_FEED_FORM ≠ ENCODED_SAFETY_PROOF
  LINE_FEED_FORM ≠ AUTHORITY
  LINE_FEED_FORM ≠ EXECUTION_TRIGGER
  LINE_FEED_FORM ≠ HEADER_SAFETY_PROOF
  LINE_FEED_FORM ≠ SANITIZED_PROOF
  LINE_FEED_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: LF (ZONE_1) has parallel functions (text newline, record boundary, protocol terminator) co-existing without cultural precession. Polysemy of a stable control code.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a teletype control code with no gestural predecessor; the record/protocol-boundary functions are layered on by the digital epoch in parallel.

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
    INPUT: "line one\\nline two"
    CONTEXT: a newline shown as an escape in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: LINE_FEED_FORM ≠ NEWLINE_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "use \\n to break a line"
    CONTEXT: describing the escape sequence in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: LINE_FEED_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "printf('a\\nb')"
    CONTEXT: an escape inside a code example (as literal text)
    EXPECTED: INFO
    RISK: NONE
    GUARD: LINE_FEED_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "a multi-line note body"
    CONTEXT: legitimate multi-line free text in a text field
    EXPECTED: INFO
    RISK: NONE
    GUARD: LINE_FEED_FORM ≠ BOUNDARY_SAFETY_PROOF
  SAFE_CASE_005:
    INPUT: "CSV row with a quoted, newlined cell"
    CONTEXT: an LF inside a properly quoted CSV field
    EXPECTED: INFO
    RISK: NONE
    GUARD: LINE_FEED_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "LF is 0x0A on Unix"
    CONTEXT: naming the control code in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: LINE_FEED_FORM ≠ NEWLINE_ONLY_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: HTTP_RESPONSE_SPLITTING
    INPUT: "value%0ASet-Cookie:%20admin=1"
    CONTEXT: an injected LF starting a forged HTTP header
    RISK: CRITICAL
    ATTACK: "%0A" decodes to LF and injects an attacker-controlled header/body
    GUARD: LINE_FEED_FORM ≠ HEADER_SAFETY_PROOF
  RISK_CASE_002:
    NAME: LOG_FORGING
    INPUT: "user%0A2026-01-01 ADMIN login OK"
    CONTEXT: an injected LF forging a fake log line
    RISK: HIGH
    ATTACK: LF starts a new log record the attacker fully controls (audit poisoning)
    GUARD: LINE_FEED_FORM ≠ BOUNDARY_SAFETY_PROOF
  RISK_CASE_003:
    NAME: SMTP_HEADER_INJECTION
    INPUT: "addr@x.com%0ABcc:%20victim@y.com"
    CONTEXT: an injected LF adding an email header
    RISK: HIGH
    ATTACK: LF injects an extra SMTP header (Bcc) into a mail-sending field
    GUARD: LINE_FEED_FORM ≠ HEADER_SAFETY_PROOF
  RISK_CASE_004:
    NAME: NDJSON_RECORD_FORGERY
    INPUT: 'name%0A{"role":"admin"}'
    CONTEXT: an injected LF forging an extra NDJSON record
    RISK: HIGH
    ATTACK: LF closes the current record and injects a new one downstream
    GUARD: LINE_FEED_FORM ≠ EFFECT
  RISK_CASE_005:
    NAME: ENCODED_LF_BYPASS
    INPUT: "value\\u000aInjected (with a later decode)"
    CONTEXT: a \\u000a decoded back to LF before it hits the sink
    RISK: HIGH
    ATTACK: the encoded LF decodes AFTER the check → line injection
    GUARD: LINE_FEED_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: UNICODE_LINEBREAK_SUBSTITUTE
    INPUT: "value<U+2028>Injected (line separator)"
    CONTEXT: a Unicode line separator treated as a break by some parsers
    RISK: MEDIUM
    ATTACK: U+2028/U+2029 acts as a newline in JS/some parsers, bypassing an LF filter
    GUARD: LINE_FEED_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ␍
    CODEPOINT: U+000D
    NAME: CARRIAGE RETURN
    RISK: HIGH
    RULE: CARRIAGE_RETURN ≠ LINE_FEED (CR alone or CRLF can also split a line)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨NEL⟩
    CODEPOINT: U+0085
    NAME: NEXT LINE
    RISK: MEDIUM
    RULE: NEXT_LINE ≠ LINE_FEED (NEL is a C1 line break some parsers honor)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨LSEP⟩
    CODEPOINT: U+2028
    NAME: LINE SEPARATOR
    RISK: MEDIUM
    RULE: LINE_SEPARATOR ≠ LINE_FEED (a break in JS/some parsers, invisible to an LF filter)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨PSEP⟩
    CODEPOINT: U+2029
    NAME: PARAGRAPH SEPARATOR
    RISK: MEDIUM
    RULE: PARAGRAPH_SEPARATOR ≠ LINE_FEED
  CONFUSABLE_005:
    VISIBLE_FORM: ␋
    CODEPOINT: U+000B
    NAME: LINE TABULATION
    RISK: LOW
    RULE: LINE_TABULATION ≠ LINE_FEED (VT is a vertical break some tools treat as a newline)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "LF is always just a newline"
    RESPONSE: LINE_FEED_FORM ≠ NEWLINE_ONLY_PROOF
    RULE: in a header/log/protocol LF terminates a line and can inject a new one
  CG2:
    TRIGGER: "an invisible control char cannot be dangerous"
    RESPONSE: LINE_FEED_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: invisibility is orthogonal to effect; LF drives record/line boundaries
  CG3:
    TRIGGER: "a record boundary is safe by definition"
    RESPONSE: LINE_FEED_FORM ≠ BOUNDARY_SAFETY_PROOF
    RULE: the boundary lets an attacker forge a new record/header
  CG4:
    TRIGGER: "'%0A' / '\\n' is safe forever"
    RESPONSE: LINE_FEED_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to LF before the sink
  CG5:
    TRIGGER: "an LF filter catches all line breaks"
    RESPONSE: LINE_FEED_FORM ≠ EFFECT
    RULE: CR (U+000D), NEL (U+0085), U+2028/U+2029 also break lines in some parsers
  CG6:
    TRIGGER: "the presence of a newline means the input is sanitized"
    RESPONSE: LINE_FEED_FORM ≠ SANITIZED_PROOF
    RULE: the presence of the sign says nothing about sanitization

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "CR+LF"
      NAME: CRLF_HEADER_TERMINATOR
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: a CRLF pair terminating and injecting HTTP headers
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "LF+LF"
      NAME: HEADER_BODY_SPLIT
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: a blank line ending headers and starting an injected body
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "LF + log-timestamp"
      NAME: LOG_LINE_FORGERY
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: LF plus a forged timestamp faking an audit entry
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with LF are central to CRLF/header/log injection.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: LF forges a record/line BOUNDARY, but does not imitate the existence of a verified entity. Its risks are splitting/forgery, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of LF with a Unicode line separator U+2028 to bypass an LF filter
  A2: substitution with NEL (U+0085) as a C1 line break
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: HTTP response splitting value%0ASet-Cookie:%20admin=1
  B2: log forging user%0A<forged audit line>
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "CR+LF" (SC1) — HTTP header terminator injection
  C2: "LF+LF" (SC2) — header/body split
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: LF presented as a harmless newline inside a header field
  D2: "%0A" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: forged header injection into a response
  E2: N/A — vector: forged NDJSON record injection into a log pipeline
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: LF is always just a newline
  EXPECTED: FAIL_NEWLINE_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: an invisible control char cannot be dangerous
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: a record boundary is safe by definition
  EXPECTED: FAIL_BOUNDARY_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%0A" / "\n" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: an LF filter catches all line breaks
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: the presence of a newline proves the input was sanitized
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to strip/normalize LF per protocol (HTTP/SMTP/log) without false positives on legitimate multi-line text fields?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (header-value newline stripping + structured logging + protocol-aware encoding is an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "the safety of LF is decided by the protocol/parse context".
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
