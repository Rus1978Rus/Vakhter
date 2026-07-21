PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_QUESTION_MARK_U003F_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_QUESTION_MARK_U003F_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_QUESTION_MARK_U003F_GEN3_v0_3_EN
CODEPOINT: U+003F
VISIBLE_FORM: ?
UNICODE_NAME: QUESTION MARK
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: question mark
CATEGORY_ROADMAP: PH (query boundary, param smuggling) · PHAGO: — (structure masking)

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
VISIBLE_FORM: ?
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_SEPARATOR
BASE_MODE_FORMULA: QUESTION_MARK_FORM ≠ EFFECT
SIGN_CATEGORY:
  - punctuation (a question)
  - URL query-string start separator (?a=1&b=2)
  - ternary operator (a ? b : c)
  - "0 or 1" quantifier in regex (colou?r)
  - single-char glob wildcard in shell (file?.txt)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_QUERY_SAFE — a "?" query start does not make the parameters safe
  2. NOT_PARAM_VALIDITY_PROOF — the presence of "?" does not confirm the parameters are correct
  3. NOT_SINGLE_QUERY_BOUNDARY — a second "?" can confuse a parser about the query boundary
  4. NOT_REDIRECT_SAFE — "?next=…" does not guarantee a safe redirect
  5. NOT_AUTHORITY — "?" does not confirm officialness
  6. NOT_EXECUTION_TRIGGER — by itself it executes nothing
  7. NOT_TRUST_SIGNAL — it does not increase trust
  8. NOT_GLOB_SAFE — "?" as a wildcard can widen file access
  9. NOT_REGEX_SAFE — "?" in regex changes the pattern's semantics
  10. NOT_PARAM_UNIQUENESS_PROOF — a repeated parameter (?id=1&id=2) is not unambiguous
  11. NOT_URL_END_MARKER — "?" does not reliably mark the end of a URL/path

BASE_FORMULAS:
  QUESTION_MARK_FORM ≠ EFFECT
  QUESTION_MARK_FORM ≠ QUERY_SAFETY_PROOF
  QUESTION_MARK_FORM ≠ PARAM_VALIDITY_PROOF
  QUESTION_MARK_FORM ≠ SINGLE_QUERY_BOUNDARY_PROOF
  QUESTION_MARK_FORM ≠ REDIRECT_SAFETY_PROOF
  QUESTION_MARK_FORM ≠ AUTHORITY
  QUESTION_MARK_FORM ≠ TRUST_SIGNAL
  QUESTION_MARK_FORM ≠ GLOB_SAFETY_PROOF
  QUESTION_MARK_FORM ≠ REGEX_SAFETY_PROOF
  QUESTION_MARK_FORM ≠ PARAM_UNIQUENESS_PROOF
  QUESTION_MARK_FORM ≠ URL_END_MARKER_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "?" (ZONE_1) has parallel functions (question, query, ternary, regex, glob) co-existing without cultural precession. Polysemy of a stable sign.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a written punctuation sign with no gestural predecessor; the query/regex functions are layered on by the digital epoch in parallel.

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
    INPUT: "Are you sure?"
    CONTEXT: interrogative sentence
    EXPECTED: INFO
    RISK: NONE
    GUARD: QUESTION_MARK_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "https://site.com/search?q=cats"
    CONTEXT: ordinary query string
    EXPECTED: INFO
    RISK: NONE
    GUARD: QUESTION_MARK_FORM ≠ QUERY_SAFETY_PROOF
  SAFE_CASE_003:
    INPUT: "x = a ? b : c"
    CONTEXT: ternary operator
    EXPECTED: INFO
    RISK: NONE
    GUARD: QUESTION_MARK_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "regex: colou?r"
    CONTEXT: "0 or 1" quantifier
    EXPECTED: INFO
    RISK: NONE
    GUARD: QUESTION_MARK_FORM ≠ REGEX_SAFETY_PROOF
  SAFE_CASE_005:
    INPUT: "ls file?.txt"
    CONTEXT: single-char glob
    EXPECTED: INFO
    RISK: NONE
    GUARD: QUESTION_MARK_FORM ≠ GLOB_SAFETY_PROOF
  SAFE_CASE_006:
    INPUT: "is the issue open?"
    CONTEXT: a question in text
    EXPECTED: INFO
    RISK: NONE
    GUARD: QUESTION_MARK_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: OPEN_REDIRECT_PARAM
    INPUT: "https://site.com/login?next=//evil.com"
    CONTEXT: a redirect parameter points to an external host
    RISK: HIGH
    ATTACK: "?next=" with an external/protocol-relative URL — open redirect after login
    GUARD: QUESTION_MARK_FORM ≠ REDIRECT_SAFETY_PROOF
  RISK_CASE_002:
    NAME: PARAMETER_POLLUTION
    INPUT: "?id=1&id=2&id=admin"
    CONTEXT: repeated parameter (HTTP Parameter Pollution)
    RISK: HIGH
    ATTACK: different layers read different id values — auth/logic desync
    GUARD: QUESTION_MARK_FORM ≠ PARAM_UNIQUENESS_PROOF
  RISK_CASE_003:
    NAME: SECOND_QUESTION_MARK_SMUGGLE
    INPUT: "/path?a=1?b=2"
    CONTEXT: a second "?" confuses the parser about the query boundary
    RISK: MEDIUM
    ATTACK: an ambiguous query boundary smuggles a parameter past validation
    GUARD: QUESTION_MARK_FORM ≠ SINGLE_QUERY_BOUNDARY_PROOF
  RISK_CASE_004:
    NAME: JS_SCHEME_IN_PARAM
    INPUT: "?url=javascript:alert(1)"
    CONTEXT: a dangerous scheme as a redirect-parameter value
    RISK: HIGH
    ATTACK: the parameter value is placed into an href → XSS
    GUARD: QUESTION_MARK_FORM ≠ QUERY_SAFETY_PROOF
  RISK_CASE_005:
    NAME: SSRF_VIA_PARAM
    INPUT: "?image=http://169.254.169.254/latest/meta-data/"
    CONTEXT: a parameter with an internal URL (SSRF)
    RISK: HIGH
    ATTACK: the server fetches the URL from the parameter — access to metadata/internal network
    GUARD: QUESTION_MARK_FORM ≠ PARAM_VALIDITY_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_QM_BYPASS
    INPUT: "search？q=x" (fullwidth ？ U+FF1F)
    CONTEXT: a look-alike to bypass a query parser
    RISK: MEDIUM
    ATTACK: a filter looks for ASCII "?", a normalizer may fold ？ to "?"
    GUARD: QUESTION_MARK_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ？
    CODEPOINT: U+FF1F
    NAME: FULLWIDTH QUESTION MARK
    RISK: HIGH
    RULE: FULLWIDTH_QUESTION_MARK ≠ QUESTION_MARK (bypasses a query filter looking for ASCII "?")
  CONFUSABLE_002:
    VISIBLE_FORM: ⁇
    CODEPOINT: U+2047
    NAME: DOUBLE QUESTION MARK
    RISK: LOW
    RULE: DOUBLE_QUESTION_MARK ≠ QUESTION_MARK
  CONFUSABLE_003:
    VISIBLE_FORM: ¿
    CODEPOINT: U+00BF
    NAME: INVERTED QUESTION MARK
    RISK: LOW
    RULE: INVERTED_QUESTION_MARK ≠ QUESTION_MARK
  CONFUSABLE_004:
    VISIBLE_FORM: ‽
    CODEPOINT: U+203D
    NAME: INTERROBANG
    RISK: LOW
    RULE: INTERROBANG ≠ QUESTION_MARK
  CONFUSABLE_005:
    VISIBLE_FORM: ﹖
    CODEPOINT: U+FE56
    NAME: SMALL QUESTION MARK
    RISK: LOW
    RULE: SMALL_QUESTION_MARK ≠ QUESTION_MARK

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "since there is a '?', the query is safe"
    RESPONSE: QUESTION_MARK_FORM ≠ QUERY_SAFETY_PROOF
    RULE: parameter values may carry redirect/XSS/SSRF; check the values
  CG2:
    TRIGGER: "a URL parameter is unique"
    RESPONSE: QUESTION_MARK_FORM ≠ PARAM_UNIQUENESS_PROOF
    RULE: repetition is possible (HPP); different layers read different values
  CG3:
    TRIGGER: "one '?' in a URL means an unambiguous query boundary"
    RESPONSE: QUESTION_MARK_FORM ≠ SINGLE_QUERY_BOUNDARY_PROOF
    RULE: a second "?" can confuse the parser
  CG4:
    TRIGGER: "'?next=URL' only leads inside the site"
    RESPONSE: QUESTION_MARK_FORM ≠ REDIRECT_SAFETY_PROOF
    RULE: the redirect value must be validated against a host allowlist
  CG5:
    TRIGGER: "an ASCII '?' filter catches all queries"
    RESPONSE: QUESTION_MARK_FORM ≠ EFFECT
    RULE: fullwidth ？ (U+FF1F) is a different codepoint
  CG6:
    TRIGGER: "'?' marks the end of a URL"
    RESPONSE: QUESTION_MARK_FORM ≠ URL_END_MARKER_PROOF
    RULE: after "?" comes the query, then possibly a "#" fragment; "?" is not the end

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "?a=1&b=2"
      NAME: QUERY_STRING
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: query parameters; the danger is in the values (redirect/SSRF/XSS)
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "?a=1?b=2"
      NAME: DOUBLE_QUERY_DELIMITER
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: ambiguous query boundary, parameter smuggling
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "id=1&id=2"
      NAME: PARAM_POLLUTION
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: HTTP Parameter Pollution, layer desync
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — query sequences are central to this sign.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "?" masks URL STRUCTURE (query boundary, param smuggling) but does not imitate the existence of a verified entity. Its risks are obfuscation/logic, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of ASCII "?" with fullwidth ？ (U+FF1F) to bypass a query parser
  A2: mixing "?" with the twin ⁇ (U+2047) in a filter
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: open redirect "?next=//evil.com"
  B2: SSRF "?image=http://169.254.169.254/…"
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: double "?" "/path?a=1?b=2" (SC2)
  C2: parameter pollution "id=1&id=2&id=admin" (SC3)
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "?url=javascript:…" — a dangerous scheme in a parameter
  D2: cache-buster "?v=12345" as pseudo-legit cover for tracking
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: a redirect parameter to a brand look-alike
  E2: N/A — vector: a parameter with an internal URL (SSRF)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: the presence of "?" makes query parameters safe
  EXPECTED: FAIL_QUERY_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: a URL parameter is always unique
  EXPECTED: FAIL_PARAM_UNIQUENESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: one "?" means an unambiguous query boundary
  EXPECTED: FAIL_QUERY_BOUNDARY_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "?next=URL" only leads inside the site
  EXPECTED: FAIL_REDIRECT_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: an ASCII "?" filter catches all variants of the sign
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: "?" marks the end of a URL
  EXPECTED: FAIL_URL_END_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to validate parameter values (redirect/SSRF/XSS) without false positives on legit queries?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (host/scheme allowlist + output context is an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "check parameter values, not the mere '?'".
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
