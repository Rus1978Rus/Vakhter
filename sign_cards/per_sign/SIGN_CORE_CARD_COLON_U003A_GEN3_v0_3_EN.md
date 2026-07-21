PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_COLON_U003A_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_COLON_U003A_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_COLON_U003A_GEN3_v0_3_EN
CODEPOINT: U+003A
VISIBLE_FORM: :
UNICODE_NAME: COLON
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: colon
CATEGORY_ROADMAP: PH (port/protocol confusion) · PHAGO: ○ (partial — a scheme URI can imply an "official" resource)

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
VISIBLE_FORM: :
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_SEPARATOR
BASE_MODE_FORMULA: COLON_FORM ≠ EFFECT
SIGN_CATEGORY:
  - punctuation (explanation, enumeration)
  - time separator (12:30) and ratio (3:1)
  - key-value separator (key: value)
  - URI scheme separator (http:, javascript:, data:)
  - host:port and login:password separator in a URL
  - namespace separator (namespace::member)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_SCHEME_SAFE — a colon in "scheme:" does not make the scheme itself safe (javascript:, data:)
  2. NOT_PORT_VALIDITY_PROOF — "host:port" does not confirm the port is correct/safe
  3. NOT_TIME_PROOF — a colon does not guarantee "12:99" is a valid time
  4. NOT_KEYVALUE_PROOF — "key:value" does not confirm the pair is correct
  5. NOT_CREDENTIAL_PROOF — "user:pass" does not verify credentials
  6. NOT_AUTHORITY — a colon does not confirm officialness
  7. NOT_URL_STRUCTURE_PROOF — the presence of ":" does not prove a valid URL structure
  8. NOT_EXECUTION_TRIGGER — a colon by itself does not execute (the javascript: scheme does)
  9. NOT_TRUST_SIGNAL — it does not increase trust
  10. NOT_ALWAYS_SEPARATOR — "::" may be IPv6/namespace, not a pair
  11. NOT_SCHEME_PRESENCE_PROOF — ":" without a valid scheme before it is not a scheme

BASE_FORMULAS:
  COLON_FORM ≠ EFFECT
  COLON_FORM ≠ SCHEME_SAFETY_PROOF
  COLON_FORM ≠ PORT_VALIDITY_PROOF
  COLON_FORM ≠ TIME_VALIDITY_PROOF
  COLON_FORM ≠ KEYVALUE_VALIDITY_PROOF
  COLON_FORM ≠ CREDENTIAL_PROOF
  COLON_FORM ≠ AUTHORITY
  COLON_FORM ≠ URL_STRUCTURE_PROOF
  COLON_FORM ≠ EXECUTION_TRIGGER
  COLON_FORM ≠ TRUST_SIGNAL
  COLON_FORM ≠ SCHEME_PRESENCE_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: ":" (ZONE_1) has parallel functions (punctuation, time, ratio, key-value, scheme, host:port) co-existing without cultural precession. Polysemy of a stable sign.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a written punctuation sign with no gestural predecessor; the URI function is layered on by the digital epoch in parallel.

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
    INPUT: "meeting at 12:30"
    CONTEXT: time separator
    EXPECTED: INFO
    RISK: NONE
    GUARD: COLON_FORM ≠ TIME_VALIDITY_PROOF
  SAFE_CASE_002:
    INPUT: "ratio 3:1"
    CONTEXT: ratio
    EXPECTED: INFO
    RISK: NONE
    GUARD: COLON_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "name: Ivan"
    CONTEXT: key-value pair (YAML/JSON-like)
    EXPECTED: INFO
    RISK: NONE
    GUARD: COLON_FORM ≠ KEYVALUE_VALIDITY_PROOF
  SAFE_CASE_004:
    INPUT: "Important: read to the end"
    CONTEXT: punctuation-explanation
    EXPECTED: INFO
    RISK: NONE
    GUARD: COLON_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "https://example.com"
    CONTEXT: legitimate URL scheme
    EXPECTED: INFO
    RISK: NONE
    GUARD: COLON_FORM ≠ SCHEME_SAFETY_PROOF
  SAFE_CASE_006:
    INPUT: "std::vector<int>"
    CONTEXT: C++ namespace separator
    EXPECTED: INFO
    RISK: NONE
    GUARD: COLON_FORM ≠ ALWAYS_SEPARATOR

RISK_CASES:
  RISK_CASE_001:
    NAME: JAVASCRIPT_SCHEME_INJECTION
    INPUT: "javascript:alert(document.cookie)"
    CONTEXT: a dangerous scheme in an href/link
    RISK: CRITICAL
    ATTACK: the javascript: scheme executes code on navigation; the colon is the scheme separator, but the SCHEME executes, not ":"
    GUARD: COLON_FORM ≠ SCHEME_SAFETY_PROOF
  RISK_CASE_002:
    NAME: DATA_URI_PAYLOAD
    INPUT: "data:text/html,<script>...</script>"
    CONTEXT: a data URI with active content
    RISK: HIGH
    ATTACK: data: embeds executable/HTML content into a "link"
    GUARD: COLON_FORM ≠ URL_STRUCTURE_PROOF
  RISK_CASE_003:
    NAME: PORT_REDIRECT_CONFUSION
    INPUT: "http://trusted.com:evil.com/"
    CONTEXT: host:port confusion to mask the real host
    RISK: HIGH
    ATTACK: a non-standard ":" position confuses a naive URL parser about the real host/port
    GUARD: COLON_FORM ≠ PORT_VALIDITY_PROOF
  RISK_CASE_004:
    NAME: CREDENTIALS_IN_URL
    INPUT: "http://user:pass@evil.com"
    CONTEXT: login:password in userinfo (together with @)
    RISK: MEDIUM
    ATTACK: ":" separates the credentials, everything before "@" is userinfo; the real host is evil.com
    GUARD: COLON_FORM ≠ CREDENTIAL_PROOF
  RISK_CASE_005:
    NAME: FILE_SCHEME_LOCAL_READ
    INPUT: "file:///etc/passwd"
    CONTEXT: the file: scheme to read a local resource
    RISK: HIGH
    ATTACK: the file: scheme redirects the request to the local filesystem
    GUARD: COLON_FORM ≠ SCHEME_SAFETY_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_COLON_BYPASS
    INPUT: "javascript：alert(1)" (fullwidth ： U+FF1A)
    CONTEXT: a colon look-alike to bypass a scheme filter
    RISK: MEDIUM
    ATTACK: a filter looks for ASCII ":", while a normalizer/browser may fold ： to ":"
    GUARD: COLON_FORM ≠ EFFECT (see CONFUSABLES)

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ：
    CODEPOINT: U+FF1A
    NAME: FULLWIDTH COLON
    RISK: HIGH
    RULE: FULLWIDTH_COLON ≠ COLON (bypasses a scheme/port filter looking for ASCII ":")
  CONFUSABLE_002:
    VISIBLE_FORM: ∶
    CODEPOINT: U+2236
    NAME: RATIO
    RISK: MEDIUM
    RULE: RATIO ≠ COLON (mathematical ratio, different codepoint)
  CONFUSABLE_003:
    VISIBLE_FORM: ꞉
    CODEPOINT: U+A789
    NAME: MODIFIER LETTER COLON
    RISK: MEDIUM
    RULE: MODIFIER_COLON ≠ COLON
  CONFUSABLE_004:
    VISIBLE_FORM: ˸
    CODEPOINT: U+02F8
    NAME: MODIFIER LETTER RAISED COLON
    RISK: LOW
    RULE: RAISED_COLON ≠ COLON
  CONFUSABLE_005:
    VISIBLE_FORM: ։
    CODEPOINT: U+0589
    NAME: ARMENIAN FULL STOP
    RISK: LOW
    RULE: ARMENIAN_FULL_STOP ≠ COLON (visually similar to a colon)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "since there is a 'scheme:', the link is safe"
    RESPONSE: COLON_FORM ≠ SCHEME_SAFETY_PROOF
    RULE: javascript:/data:/file: are dangerous schemes; safety is decided by the scheme, not ":"
  CG2:
    TRIGGER: "'host:port' is always a correct host and port"
    RESPONSE: COLON_FORM ≠ PORT_VALIDITY_PROOF
    RULE: the ":" position can confuse a parser about the real host/port
  CG3:
    TRIGGER: "'12:99' is a valid time because there is a colon"
    RESPONSE: COLON_FORM ≠ TIME_VALIDITY_PROOF
    RULE: a separator does not check the range of the components
  CG4:
    TRIGGER: "'user:pass@host' is trusted credentials"
    RESPONSE: COLON_FORM ≠ CREDENTIAL_PROOF
    RULE: ":" only separates; everything before "@" is userinfo, the real host is after "@"
  CG5:
    TRIGGER: "an ASCII ':' filter catches all schemes"
    RESPONSE: COLON_FORM ≠ EFFECT
    RULE: fullwidth ： (U+FF1A) is a different codepoint; a normalizer may fold it to ":"
  CG6:
    TRIGGER: "the presence of ':' proves a valid URL"
    RESPONSE: COLON_FORM ≠ URL_STRUCTURE_PROOF
    RULE: ":" appears in time, ratio, key-value; it is not a sign of a valid URL

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "://"
      NAME: SCHEME_AUTHORITY_SEPARATOR
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: scheme/authority separator; a legit binding in itself (URL_CONTEXT), but it turns on stricter analysis of @ and the dot downstream (cf. legacy SOLIDUS_SCHEME_PATCH)
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "::"
      NAME: DOUBLE_COLON
      RISK_LEVEL: LOW
      POSSIBLE_CONTEXTS: IPv6 abbreviation, C++ namespace, YAML — usually legit
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "scheme:payload" (no //)
      NAME: OPAQUE_SCHEME
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: javascript:/data:/file: — opaque schemes with no authority, a frequent vector
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with ":" are central to URL structure.

PHAGO_ENTITY_MIMICRY:
  PE_001:
    INPUT: "http://microsoft.com:login@evil.com"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: MEDIUM
    NOTE: ":" together with "@" helps build a string where the brand sits in userinfo, implying an "official" resource. Partial (○) PHAGO — it amplifies the @ sign's entity-mimicry but by itself masks structure.
  PE_002:
    INPUT: "javascript:/* official portal */alert(1)"
    TYPE: SEMANTIC_AMBIGUITY (not PHAGO)
    RISK: LOW
    NOTE: a bait comment is not mimicry of a verified entity; flagged as ambiguity, not PHAGO.

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of ASCII ":" with fullwidth ： (U+FF1A) in the scheme javascript：
  A2: mixing ":" with RATIO (U+2236) to bypass a parser
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: javascript:/data: scheme in an href/URL field
  B2: userinfo user:pass@evil.com (together with @)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: opaque scheme scheme:payload with no // (SC3)
  C2: host:port confusion (http://trusted.com:evil.com/)
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: file:///etc/passwd — local read disguised as a "link"
  D2: "Important:" as a pseudo-authoritative explanation (significance inflation)
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: brand in userinfo via ":"+"@" (PE_001)
  E2: a bait scheme with an "official" comment (edge case, flagged as ambiguity)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: the presence of "scheme:" makes the link safe
  EXPECTED: FAIL_SCHEME_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: "host:port" guarantees a correct host and port
  EXPECTED: FAIL_PORT_VALIDITY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: "12:99" is a valid time because there is a colon
  EXPECTED: FAIL_TIME_VALIDITY_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "user:pass@host" is trusted credentials
  EXPECTED: FAIL_CREDENTIAL_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: an ASCII ":" filter catches all schemes
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: the presence of ":" proves a valid URL
  EXPECTED: FAIL_URL_STRUCTURE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to distinguish an opaque scheme (javascript:/data:) from a legit scheme:// without false positives on "12:30"/"key:value"?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (RFC 3986 §3.1 scheme validation + a safe-scheme allowlist is an integrator concern; cf. legacy SOLIDUS_SCHEME_PATCH)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the formulas and the rule "safety is decided by the scheme, not the colon".
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
