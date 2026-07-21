PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_LOW_LINE_U005F_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_LOW_LINE_U005F_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_LOW_LINE_U005F_GEN3_v0_3_EN
CODEPOINT: U+005F
VISIBLE_FORM: _
UNICODE_NAME: LOW LINE
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: underscore
CATEGORY_ROADMAP: PH (fake subdomains, look-alike separators) · PHAGO: ○ (partial — a fake subdomain may imply an official sub-entity)

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
VISIBLE_FORM: _
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_CONNECTOR
BASE_MODE_FORMULA: LOW_LINE_FORM ≠ EFFECT
SIGN_CATEGORY:
  - identifier connector (snake_case, user_name)
  - Markdown emphasis (_italic_)
  - single-char wildcard in SQL LIKE (a_c)
  - service DNS labels (_dmarc, _acme-challenge)
  - pseudo-separator in a domain/host (visual, not DNS hierarchy)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_SUBDOMAIN — "_" creates no subdomain and does not change the registrable domain
  2. NOT_BRAND_AFFILIATION — "paypal_secure" does not make the string part of a brand
  3. NOT_HOSTNAME_VALIDITY — "_" is not formally valid in a hostname (RFC 1123), yet appears
  4. NOT_WILDCARD_SAFE — "_" in SQL LIKE matches any single character
  5. NOT_EMPHASIS_SAFE — "_text_" (Markdown) does not guarantee the content is safe
  6. NOT_AUTHORITY — "_" does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_WORD_BOUNDARY_GUARANTEE — "_" is not always a word boundary (often inside a token)
  10. NOT_SEPARATOR_UNIQUENESS — "user_id" and "user__id" are different identifiers
  11. NOT_IDENTIFIER_VALIDITY_PROOF — "_" does not confirm an identifier exists / is authorized

BASE_FORMULAS:
  LOW_LINE_FORM ≠ EFFECT
  LOW_LINE_FORM ≠ SUBDOMAIN_PROOF
  LOW_LINE_FORM ≠ BRAND_AFFILIATION
  LOW_LINE_FORM ≠ HOSTNAME_VALIDITY_PROOF
  LOW_LINE_FORM ≠ WILDCARD_SAFETY_PROOF
  LOW_LINE_FORM ≠ EMPHASIS_SAFETY_PROOF
  LOW_LINE_FORM ≠ AUTHORITY
  LOW_LINE_FORM ≠ TRUST_SIGNAL
  LOW_LINE_FORM ≠ WORD_BOUNDARY_PROOF
  LOW_LINE_FORM ≠ SEPARATOR_UNIQUENESS_PROOF
  LOW_LINE_FORM ≠ IDENTIFIER_VALIDITY_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "_" (ZONE_1) has parallel functions (connector, emphasis, wildcard, DNS label) co-existing without cultural precession. Polysemy of a stable sign.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a written sign (low line/underscore) with no gestural predecessor; the identifier/DNS functions are layered on by the digital epoch in parallel.

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
    INPUT: "user_name"
    CONTEXT: snake_case identifier
    EXPECTED: INFO
    RISK: NONE
    GUARD: LOW_LINE_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "MAX_BUFFER_SIZE"
    CONTEXT: UPPER_SNAKE constant
    EXPECTED: INFO
    RISK: NONE
    GUARD: LOW_LINE_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "_italic_"
    CONTEXT: Markdown emphasis
    EXPECTED: INFO
    RISK: NONE
    GUARD: LOW_LINE_FORM ≠ EMPHASIS_SAFETY_PROOF
  SAFE_CASE_004:
    INPUT: "def __init__(self)"
    CONTEXT: Python dunder method
    EXPECTED: INFO
    RISK: NONE
    GUARD: LOW_LINE_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "SELECT * WHERE code LIKE 'a_c'"
    CONTEXT: an intended single-char wildcard
    EXPECTED: INFO
    RISK: NONE
    GUARD: LOW_LINE_FORM ≠ WILDCARD_SAFETY_PROOF
  SAFE_CASE_006:
    INPUT: "_dmarc.example.com"
    CONTEXT: a legitimate service DNS label
    EXPECTED: INFO
    RISK: NONE
    GUARD: LOW_LINE_FORM ≠ HOSTNAME_VALIDITY_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: FAKE_SUBDOMAIN_SEPARATOR
    INPUT: "paypal_com.evil.ru"
    CONTEXT: "_" imitates a dot separator, implying a brand subdomain
    RISK: HIGH
    ATTACK: "paypal_com" looks like a PayPal subdomain; the registrable domain is evil.ru
    GUARD: LOW_LINE_FORM ≠ SUBDOMAIN_PROOF
  RISK_CASE_002:
    NAME: SQL_LIKE_WILDCARD_BYPASS
    INPUT: "username LIKE 'admin_'"
    CONTEXT: "_" as a wildcard matches admin1/adminX
    RISK: HIGH
    ATTACK: an unescaped "_" in LIKE widens the match beyond the expected value
    GUARD: LOW_LINE_FORM ≠ WILDCARD_SAFETY_PROOF
  RISK_CASE_003:
    NAME: FAKE_AFFILIATED_LABEL
    INPUT: "login_secure_bank.example"
    CONTEXT: a chain of "_" implies an official sub-entity
    RISK: MEDIUM
    ATTACK: "_" separators assemble a "service" name imitating affiliation
    GUARD: LOW_LINE_FORM ≠ BRAND_AFFILIATION
  RISK_CASE_004:
    NAME: DNS_LABEL_SPOOF
    INPUT: "_dmarc.paypal.com.evil.ru"
    CONTEXT: a service label in a spoof domain for trust
    RISK: MEDIUM
    ATTACK: "_dmarc/_acme" before a look-alike domain imitates legit infrastructure
    GUARD: LOW_LINE_FORM ≠ IDENTIFIER_VALIDITY_PROOF
  RISK_CASE_005:
    NAME: IDENTIFIER_COLLISION
    INPUT: "user__id vs user_id"
    CONTEXT: a double "_" creates a similar but different identifier
    RISK: LOW
    ATTACK: visually close names lead to different entities/fields
    GUARD: LOW_LINE_FORM ≠ SEPARATOR_UNIQUENESS_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_UNDERSCORE_BYPASS
    INPUT: "paypal＿com" (fullwidth ＿ U+FF3F)
    CONTEXT: an underscore look-alike to bypass a filter
    RISK: LOW
    ATTACK: a filter looks for ASCII "_", a normalizer may fold ＿ to "_"
    GUARD: LOW_LINE_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ＿
    CODEPOINT: U+FF3F
    NAME: FULLWIDTH LOW LINE
    RISK: MEDIUM
    RULE: FULLWIDTH_LOW_LINE ≠ LOW_LINE (bypasses a filter looking for ASCII "_")
  CONFUSABLE_002:
    VISIBLE_FORM: ﹍
    CODEPOINT: U+FE4D
    NAME: DASHED LOW LINE
    RISK: LOW
    RULE: DASHED_LOW_LINE ≠ LOW_LINE
  CONFUSABLE_003:
    VISIBLE_FORM: ﹎
    CODEPOINT: U+FE4E
    NAME: CENTRELINE LOW LINE
    RISK: LOW
    RULE: CENTRELINE_LOW_LINE ≠ LOW_LINE
  CONFUSABLE_004:
    VISIBLE_FORM: ﹏
    CODEPOINT: U+FE4F
    NAME: WAVY LOW LINE
    RISK: LOW
    RULE: WAVY_LOW_LINE ≠ LOW_LINE
  CONFUSABLE_005:
    VISIBLE_FORM: ‿
    CODEPOINT: U+203F
    NAME: UNDERTIE
    RISK: LOW
    RULE: UNDERTIE ≠ LOW_LINE

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "'paypal_com' is a PayPal subdomain"
    RESPONSE: LOW_LINE_FORM ≠ SUBDOMAIN_PROOF
    RULE: "_" is not a DNS-hierarchy separator; DNS decides the registrable domain
  CG2:
    TRIGGER: "'_' in LIKE is just a literal underscore"
    RESPONSE: LOW_LINE_FORM ≠ WILDCARD_SAFETY_PROOF
    RULE: in SQL LIKE "_" matches any single char; escape it for a literal meaning
  CG3:
    TRIGGER: "a compound name via '_' confirms an organization"
    RESPONSE: LOW_LINE_FORM ≠ BRAND_AFFILIATION
    RULE: joining via "_" is identifier spelling, not entity verification
  CG4:
    TRIGGER: "'user_id' and 'user__id' are the same"
    RESPONSE: LOW_LINE_FORM ≠ SEPARATOR_UNIQUENESS_PROOF
    RULE: a different number of "_" → different identifiers
  CG5:
    TRIGGER: "'_dmarc' proves the domain's legit infrastructure"
    RESPONSE: LOW_LINE_FORM ≠ IDENTIFIER_VALIDITY_PROOF
    RULE: a service label does not confirm the parent domain's authenticity
  CG6:
    TRIGGER: "an ASCII '_' filter catches all underscores"
    RESPONSE: LOW_LINE_FORM ≠ EFFECT
    RULE: fullwidth ＿ (U+FF3F) is a different codepoint

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "brand_word.tld"
      NAME: FAKE_SUBDOMAIN_LABEL
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: "_" imitates a subdomain dot separator (phishing)
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "__dunder__"
      NAME: DOUBLE_UNDERSCORE
      RISK_LEVEL: LOW
      POSSIBLE_CONTEXTS: Python dunder names; usually legit, but name collision possible
      REQUIRES_SEQUENCE_INTEGRATOR: NO
    SC3:
      SEQUENCE: "a_c (in LIKE)"
      NAME: LIKE_WILDCARD
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: an unescaped wildcard in SQL LIKE
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with "_" matter (domain/SQL).

PHAGO_ENTITY_MIMICRY:
  PE_001:
    INPUT: "paypal_com.evil.ru"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: MEDIUM
    NOTE: "_" imitates a subdomain separator, implying an official brand sub-entity (e.g. "paypal_com"). Partial (○) PHAGO — structure masking with an entity-mimicry element.
  PE_002:
    INPUT: "support_official_paypal.example"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: MEDIUM
    NOTE: a chain of "_" assembles an "official" service entity of the brand.

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of ASCII "_" with fullwidth ＿ (U+FF3F) to bypass a filter
  A2: mixing "_" with ﹍ (U+FE4D) in a filter
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: an unescaped "_" as a wildcard in SQL LIKE (admin_)
  B2: a service DNS label "_dmarc" before a look-alike domain
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: fake subdomain "brand_word.tld" (SC1)
  C2: collision "user__id" vs "user_id"
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "login_secure_bank" — a pseudo-service name
  D2: "__verified__" as a pseudo-status (trust inflation)
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: "paypal_com.evil.ru" — mimicry of a brand sub-entity (PE_001)
  E2: "support_official_paypal" — mimicry of a service entity (PE_002)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: "paypal_com" is a PayPal subdomain
  EXPECTED: FAIL_SUBDOMAIN_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: "_" in SQL LIKE is just a literal underscore
  EXPECTED: FAIL_WILDCARD_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: a compound name via "_" confirms an organization
  EXPECTED: FAIL_ENTITY_EXISTENCE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "user_id" and "user__id" are one identifier
  EXPECTED: FAIL_SEPARATOR_UNIQUENESS_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: "_dmarc" proves the domain's legit infrastructure
  EXPECTED: FAIL_IDENTIFIER_VALIDITY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: an ASCII "_" filter catches all variants of the sign
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to distinguish a fake "_" subdomain from a legit DNS label (_dmarc) without false positives?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (registrable-domain parsing + a service-label allowlist is an integrator concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "'_' is not a DNS-hierarchy separator".
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
