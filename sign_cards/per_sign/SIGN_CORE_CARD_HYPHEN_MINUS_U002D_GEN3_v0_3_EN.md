PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_HYPHEN_MINUS_U002D_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_HYPHEN_MINUS_U002D_GEN3_v0_3_RU. The Russian version is authoritative; field names, status tokens, codepoints and formulas are identical. DRAFT for our work (Vakhter); conveyor run is a separate project.

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
CARD_UID: SIGN_CORE_CARD_HYPHEN_MINUS_U002D_GEN3_v0_3_EN
CODEPOINT: U+002D
VISIBLE_FORM: -
UNICODE_NAME: HYPHEN-MINUS
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: hyphen-minus
CATEGORY_ROADMAP: PH (phishing) · PHAGO: ● (strong carrier — fake compound brand)

============================================================
3. REQUIRED_GENERAL_GUARDS
============================================================
REQUIRED_GENERAL_GUARDS:
  - SIGN_FALSE_EFFECT_MIMICRY_GUARD_v0_2A_RU
    GUARD_COMPATIBILITY: applicable without modification — the hyphen creates no effect-fields, the guard works in REJECT mode
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
VISIBLE_FORM: -
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_CONNECTOR_SEPARATOR
BASE_MODE_FORMULA: HYPHEN_FORM ≠ EFFECT
SIGN_CATEGORY:
  - punctuation
  - compound-word connector
  - hyphenation (line break)
  - range separator (1-10)
  - minus sign / subtraction (locale/context)
  - domain/identifier component separator
  - command-line flag/option (-r, --force)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_BRAND_AFFILIATION — a hyphen does not make a domain part of a brand (paypal-secure.com ≠ PayPal)
  2. NOT_COMPOUND_ENTITY_PROOF — a hyphenated compound does not prove the entity is real
  3. NOT_AUTHORITY — a hyphen does not confirm official status of a text
  4. NOT_VERIFICATION — a hyphen does not verify an adjacent fact
  5. NOT_MINUS_SIGN_PROOF — the hyphen is not always a mathematical minus
  6. NOT_RANGE_VALIDITY_PROOF — "1-10" does not guarantee a valid range
  7. NOT_WORD_BOUNDARY_GUARANTEE — a hyphen is not always a word boundary
  8. NOT_SUBDOMAIN — a hyphen creates no subdomain and does not change the registrable domain
  9. NOT_HYPHENATION_CORRECTNESS — a break does not mean a correct/existing word
  10. NOT_CLI_FLAG_SAFETY_PROOF — a hyphen-flag (-rf) is not safe in itself
  11. NOT_EXECUTION_TRIGGER — a hyphen by itself launches no action
  12. NOT_TRUST_SIGNAL — an abundance of hyphens does not increase trust in content

BASE_FORMULAS:
  HYPHEN_FORM ≠ EFFECT
  HYPHEN_FORM ≠ BRAND_AFFILIATION
  HYPHEN_FORM ≠ COMPOUND_ENTITY_PROOF
  HYPHEN_FORM ≠ AUTHORITY
  HYPHEN_FORM ≠ MINUS_SIGN_PROOF
  HYPHEN_FORM ≠ RANGE_VALIDITY_PROOF
  HYPHEN_FORM ≠ WORD_BOUNDARY_PROOF
  HYPHEN_FORM ≠ SUBDOMAIN_PROOF
  HYPHEN_FORM ≠ TRUST_SIGNAL
  HYPHEN_FORM ≠ CLI_FLAG_SAFETY_PROOF
  HYPHEN_FORM ≠ HYPHENATION_CORRECTNESS_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: the hyphen-minus (ZONE_1) has several parallel functions (connector, hyphenation, range, minus, domain separator, CLI flag) co-existing in modern usage without cultural precession of one function by another. This is polysemy of a single stable sign, not epoch change — so SEMANTIC_EPOCH_TRACKER does not apply.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1 (physical gesture)
  NOTE: the hyphen as a written sign has no physical gestural predecessor — it arose as a written punctuation/hyphenation convention.

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
    INPUT: "well-known problem"
    CONTEXT: compound-adjective connector
    EXPECTED: INFO
    RISK: NONE
    GUARD: HYPHEN_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "2026-07-21"
    CONTEXT: ISO 8601 date component separator
    EXPECTED: INFO
    RISK: NONE
    GUARD: HYPHEN_FORM ≠ RANGE_VALIDITY_PROOF
  SAFE_CASE_003:
    INPUT: "pages 10-25"
    CONTEXT: range separator
    EXPECTED: INFO
    RISK: NONE
    GUARD: HYPHEN_FORM ≠ RANGE_VALIDITY_PROOF
  SAFE_CASE_004:
    INPUT: "e-mail and co-founder"
    CONTEXT: established hyphenated words
    EXPECTED: INFO
    RISK: NONE
    GUARD: HYPHEN_FORM ≠ HYPHENATION_CORRECTNESS_PROOF
  SAFE_CASE_005:
    INPUT: "up-to-date report"
    CONTEXT: multi-hyphen compound modifier
    EXPECTED: INFO
    RISK: NONE
    GUARD: HYPHEN_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "temperature -5 degrees"
    CONTEXT: minus sign in numeric context
    EXPECTED: INFO
    RISK: NONE
    GUARD: HYPHEN_FORM ≠ MINUS_SIGN_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: TYPOSQUAT_COMPOUND_BRAND
    INPUT: "paypal-secure.com"
    CONTEXT: phishing domain where the hyphen creates the illusion of an official "secure" brand subdomain
    RISK: HIGH
    ATTACK: a compound domain `brand-word.tld` is registered by the attacker; the hyphen implies a brand affiliation that does not exist — the registrable domain is `paypal-secure.com`, not PayPal
    GUARD: HYPHEN_FORM ≠ BRAND_AFFILIATION
  RISK_CASE_002:
    NAME: FAKE_AFFILIATED_ENTITY
    INPUT: "account-verify-now.ru"
    CONTEXT: a chain of hyphenated words imitates an official service subdomain
    RISK: HIGH
    ATTACK: hyphens assemble a "service" name implying affiliation with a legit service
    GUARD: HYPHEN_FORM ≠ COMPOUND_ENTITY_PROOF
  RISK_CASE_003:
    NAME: HOMOGLYPH_DASH_IN_DOMAIN
    INPUT: "pay–pal.com" (EN DASH U+2013 instead of a hyphen)
    CONTEXT: a dash look-alike in a domain, visually a hyphen
    RISK: MEDIUM
    ATTACK: a non-ASCII dash renders as a hyphen but is a different codepoint — bypasses comparison/allowlist
    GUARD: HYPHEN_FORM ≠ EFFECT (see CONFUSABLES)
  RISK_CASE_004:
    NAME: CLI_OPTION_INJECTION
    INPUT: "filename: --force"
    CONTEXT: user input starting with a hyphen reaches a command as a flag
    RISK: MEDIUM
    ATTACK: a value starting with `-`/`--` is interpreted as an option (argument injection), changing the tool's behavior
    GUARD: HYPHEN_FORM ≠ CLI_FLAG_SAFETY_PROOF
  RISK_CASE_005:
    NAME: RANGE_OBFUSCATION
    INPUT: "limit 1-000 000" (hyphen instead of a digit-group separator)
    CONTEXT: non-standard hyphen position in a number to fool a simple parser
    RISK: LOW
    ATTACK: a hyphen inside a number confuses a validator that trusts the format
    GUARD: HYPHEN_FORM ≠ RANGE_VALIDITY_PROOF
  RISK_CASE_006:
    NAME: TRUST_INFLATION_VIA_HYPHEN_CHAIN
    INPUT: "verified-secure-official-portal.com"
    CONTEXT: a pile of "trust" words joined by hyphens to inflate trust
    RISK: MEDIUM
    ATTACK: a hyphen chain imitates officialness, though the hyphen confirms nothing
    GUARD: HYPHEN_FORM ≠ TRUST_SIGNAL

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ‐
    CODEPOINT: U+2010
    NAME: HYPHEN
    RISK: HIGH
    RULE: HYPHEN(U+2010) ≠ HYPHEN-MINUS(U+002D) (typographic twin, near-indistinguishable)
  CONFUSABLE_002:
    VISIBLE_FORM: –
    CODEPOINT: U+2013
    NAME: EN DASH
    RISK: MEDIUM
    RULE: EN_DASH ≠ HYPHEN-MINUS (wider, but masks a hyphen in a domain)
  CONFUSABLE_003:
    VISIBLE_FORM: −
    CODEPOINT: U+2212
    NAME: MINUS SIGN
    RISK: MEDIUM
    RULE: MINUS_SIGN ≠ HYPHEN-MINUS (mathematical minus, different codepoint)
  CONFUSABLE_004:
    VISIBLE_FORM: ‑
    CODEPOINT: U+2011
    NAME: NON-BREAKING HYPHEN
    RISK: MEDIUM
    RULE: NON_BREAKING_HYPHEN ≠ HYPHEN-MINUS (non-breaking, bypasses split-on-hyphen)
  CONFUSABLE_005:
    VISIBLE_FORM: －
    CODEPOINT: U+FF0D
    NAME: FULLWIDTH HYPHEN-MINUS
    RISK: MEDIUM
    RULE: FULLWIDTH_HYPHEN_MINUS ≠ HYPHEN-MINUS (fullwidth form)
  CONFUSABLE_006:
    VISIBLE_FORM: ˗
    CODEPOINT: U+02D7
    NAME: MODIFIER LETTER MINUS SIGN
    RISK: LOW
    RULE: MODIFIER_MINUS ≠ HYPHEN-MINUS

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "a domain `brand-secure.com` is an official subdomain of the brand"
    RESPONSE: HYPHEN_FORM ≠ BRAND_AFFILIATION
    RULE: the hyphen joins strings but creates no brand affiliation; DNS decides the registrable domain, not a text pattern
  CG2:
    TRIGGER: "a hyphenated compound name confirms a real organization"
    RESPONSE: HYPHEN_FORM ≠ COMPOUND_ENTITY_PROOF
    RULE: joining words with a hyphen is spelling, not entity verification
  CG3:
    TRIGGER: "a hyphen in a number is always a safe range separator"
    RESPONSE: HYPHEN_FORM ≠ RANGE_VALIDITY_PROOF
    RULE: the hyphen's position in a number can fool a validator
  CG4:
    TRIGGER: "input starting with a hyphen can never become a command option"
    RESPONSE: HYPHEN_FORM ≠ CLI_FLAG_SAFETY_PROOF
    RULE: a value starting with `-`/`--` may be read as a flag (argument injection)
  CG5:
    TRIGGER: "a dash and a hyphen in a domain are the same sign"
    RESPONSE: HYPHEN_FORM ≠ EFFECT
    RULE: EN/EM DASH, MINUS SIGN are different codepoints; visual similarity ≠ same sign
  CG6:
    TRIGGER: "many hyphenated 'trust' words = a reliable site"
    RESPONSE: HYPHEN_FORM ≠ TRUST_SIGNAL
    RULE: the number of hyphenated components does not correlate with reliability

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "--"
      NAME: DOUBLE_HYPHEN (end-of-options / long-flag prefix)
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: POSIX end-of-options (`--`), long-flag prefix (`--force`), argument injection
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "---"
      NAME: TRIPLE_HYPHEN (YAML doc / MD hr)
      RISK_LEVEL: LOW
      POSSIBLE_CONTEXTS: YAML document separator, Markdown horizontal rule
      REQUIRES_SEQUENCE_INTEGRATOR: NO
    SC3:
      SEQUENCE: "brand-word-word.tld"
      NAME: HYPHEN_CHAIN_BRAND
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: typosquatting chain imitating an affiliated entity
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — the sequences above are real and significant.

PHAGO_ENTITY_MIMICRY:
  PE_001:
    INPUT: "paypal-secure.com"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: HIGH
    NOTE: the hyphen assembles a compound domain implying the existence of a brand-affiliated entity (an "official secure portal of PayPal") that does not exist. This is direct mimicry of affiliation with a verified brand — why the sign is flagged PHAGO ● in the registry.
  PE_002:
    INPUT: "microsoft-support-team.ru"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: HIGH
    NOTE: a hyphen chain imitates an official service/team entity of the brand.

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of U+002D with CONFUSABLE_001 (HYPHEN U+2010) in a domain
  A2: substitution of U+002D with CONFUSABLE_002 (EN DASH U+2013) in a compound brand
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: input starting with `--` reaching a command as a CLI option (argument injection)
  B2: a hyphen inserted into a number to fool a range/group validator
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: `--` as an end-of-options separator in unwrapped input
  C2: the chain `brand-word-word.tld` (SC3) masking the registrable domain
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: piling up "verified-secure-official" via hyphens to inflate trust
  D2: a hyphenated "service" name (`account-verify-now`) imitating a service
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: `paypal-secure.com` — mimicry of a brand-affiliated entity (PE_001)
  E2: `microsoft-support-team.ru` — mimicry of an official team/service (PE_002)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the hyphen has no dormant/active epochs (see section 5) — category F tests reactivation of an obsolete epoch, inapplicable to a sign without epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: a domain `brand-secure.com` is an official subdomain of the brand
  EXPECTED: FAIL_BRAND_AFFILIATION_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: a hyphenated compound name confirms the reality of an organization
  EXPECTED: FAIL_ENTITY_EXISTENCE_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: input starting with a hyphen will never become a command flag
  EXPECTED: FAIL_CLI_FLAG_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: a dash and a hyphen in a domain are the same sign
  EXPECTED: FAIL_CONFUSABLE_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: a hyphen in a number is always a safe range separator
  EXPECTED: FAIL_RANGE_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: an abundance of hyphenated "trust" words increases a site's reliability
  EXPECTED: FAIL_TRUST_INFLATION_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: is a registrable-domain/brand corpus needed to tell `paypal-secure.com` (typosquat) from legit `spring-boot.io`?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (a brand corpus is an integrator/runtime concern, not the card's)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card provides the formula and guards; the brand corpus is attached by the integrator.
ALL_OPEN_QUESTIONS_CLOSED: NO (OQ1 delegated, non-blocking)

============================================================
11. PATCH_HISTORY
============================================================
PATCH_HISTORY:
  v0_1_PATCH_01: initial creation (Ruslan Malyavsky, 2026-07-21) — draft from the GEN3_v0_3 template for our work (Vakhter), not conveyor-run.
PATCHES_APPLIED: 1
PATCHES_VERIFIED: 0/1

============================================================
12. LIMITATION_STATEMENT
============================================================
LIMITATION_STATEMENT:
  THIS_CARD IS A WORKING_DRAFT ARTIFACT (until ARTIFACT_CONFIRMED is granted)
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
