PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_HYPHEN_U2010_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_HYPHEN_U2010_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. Homoglyph of the ASCII hyphen: core law is LOOKS_SAME ≠ IS_SAME. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_HYPHEN_U2010_GEN3_v0_3_EN
CODEPOINT: U+2010
VISIBLE_FORM: ‐
UNICODE_NAME: HYPHEN
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: typographic hyphen (homoglyph of the ASCII hyphen)
CATEGORY_ROADMAP: PH (Unicode hyphen vs ASCII hyphen confusion) · PHAGO: ○ (partial — reinforces a compound-brand spoof)

============================================================
3. REQUIRED_GENERAL_GUARDS
============================================================
REQUIRED_GENERAL_GUARDS:
  - SIGN_FALSE_EFFECT_MIMICRY_GUARD_v0_2A_RU
    GUARD_COMPATIBILITY: applicable — the sign creates no effect-fields; for a homoglyph the guard is extended by normalization to ASCII at the integrator level
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
VISIBLE_FORM: ‐
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_CONNECTOR_HOMOGLYPH
BASE_MODE_FORMULA: HYPHEN_2010_FORM ≠ ASCII_HYPHEN
SIGN_CATEGORY:
  - typographic hyphen (the correct hyphenation/connection sign in typography)
  - homoglyph of the ASCII hyphen "-" (U+002D)
  - potential carrier of homoglyph spoofing in domains/identifiers

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_ASCII_HYPHEN — ‐ (U+2010) is NOT the ASCII hyphen "-" (U+002D); a different codepoint
  2. NOT_SAME_STRING_AS_ASCII — a string with ‐ is not machine-equal to its ASCII spelling
  3. NOT_BRAND_AFFILIATION — "pay‐pal" does not make the string part of a brand
  4. NOT_DOMAIN_VALIDITY_PROOF — a visual domain match does not confirm the registrable domain
  5. NOT_AUTHORITY — the sign does not confirm official status
  6. NOT_VERIFICATION — it does not verify an adjacent fact
  7. NOT_ASCII — outside ASCII; "ASCII-only" filters do not see it as "-"
  8. NOT_AUTOMATICALLY_SPOOF — in typography it is normal, not an attack
  9. NOT_EXECUTION_TRIGGER — by itself it launches nothing
  10. NOT_TRUST_SIGNAL — it does not increase trust
  11. NOT_INTERCHANGEABLE_IN_IDENTIFIERS — in a domain/login, "-"→‐ changes the entity

BASE_FORMULAS:
  HYPHEN_2010_FORM ≠ ASCII_HYPHEN
  HYPHEN_2010_FORM ≠ SAME_CODEPOINT_AS_ASCII
  HYPHEN_2010_FORM ≠ BRAND_AFFILIATION
  HYPHEN_2010_FORM ≠ DOMAIN_VALIDITY_PROOF
  HYPHEN_2010_FORM ≠ AUTHORITY
  HYPHEN_2010_FORM ≠ VERIFICATION
  HYPHEN_2010_FORM ≠ ASCII_CHARACTER
  HYPHEN_2010_FORM ≠ AUTOMATICALLY_SPOOF
  HYPHEN_2010_FORM ≠ TRUST_SIGNAL
  HYPHEN_2010_FORM ≠ EFFECT
  HYPHEN_2010_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: ‐ (typographic hyphen) is a stable punctuation sign. "Homoglyph" is a property of visual coincidence with the ASCII hyphen, co-existing with the typographic function. The danger is contextual (substitution in a token/domain), not epochal.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a written/typographic sign with no gestural predecessor; Unicode separated it from the ASCII hyphen as the "true" hyphen.

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
    INPUT: "well‐known (typeset text)"
    CONTEXT: a typographic hyphen in typeset text
    EXPECTED: INFO
    RISK: NONE
    GUARD: HYPHEN_2010_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_002:
    INPUT: "day‐to‐day (book typography)"
    CONTEXT: typographic hyphenation/connection
    EXPECTED: INFO
    RISK: NONE
    GUARD: HYPHEN_2010_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "e‐book (publishing typography)"
    CONTEXT: a hyphenated word in layout
    EXPECTED: INFO
    RISK: NONE
    GUARD: HYPHEN_2010_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "co‐operation (British typography)"
    CONTEXT: a typographic hyphen in text
    EXPECTED: INFO
    RISK: NONE
    GUARD: HYPHEN_2010_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_005:
    INPUT: "twenty‐one (spelled-out numbers)"
    CONTEXT: a hyphen in a numeral (typography)
    EXPECTED: INFO
    RISK: NONE
    GUARD: HYPHEN_2010_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "mother‐in‐law (dictionary entry)"
    CONTEXT: a compound word in a dictionary
    EXPECTED: INFO
    RISK: NONE
    GUARD: HYPHEN_2010_FORM ≠ AUTOMATICALLY_SPOOF

RISK_CASES:
  RISK_CASE_001:
    NAME: DOMAIN_HYPHEN_SPOOF
    INPUT: "pay‐pal.com" (U+2010 instead of the ASCII hyphen)
    CONTEXT: IDN/brand spoof — the token looks like pay-pal.com
    RISK: HIGH
    ATTACK: replacing the ASCII hyphen with ‐ yields a visually identical domain the attacker registers
    GUARD: HYPHEN_2010_FORM ≠ ASCII_HYPHEN
  RISK_CASE_002:
    NAME: ALLOWLIST_BYPASS
    INPUT: "secure‐bank.example (allowlist only has 'secure-bank')"
    CONTEXT: bypassing an exact comparison against the ASCII hyphen
    RISK: HIGH
    ATTACK: ‐ ≠ "-", the string will not match the ASCII spelling in an allowlist/blocklist
    GUARD: HYPHEN_2010_FORM ≠ SAME_CODEPOINT_AS_ASCII
  RISK_CASE_003:
    NAME: COMPOUND_BRAND_SPOOF
    INPUT: "paypal‐secure.com" (‐ reinforces a compound-brand spoof)
    CONTEXT: a compound domain with a typographic hyphen
    RISK: MEDIUM
    ATTACK: ‐ imitates the ASCII hyphen in a fake compound brand (cf. the HYPHEN-MINUS card)
    GUARD: HYPHEN_2010_FORM ≠ BRAND_AFFILIATION
  RISK_CASE_004:
    NAME: EMAIL_LOOKALIKE
    INPUT: "info@e‐shop.example"
    CONTEXT: ‐ in the mail domain
    RISK: MEDIUM
    ATTACK: the domain looks identical to e-shop but leads to the attacker
    GUARD: HYPHEN_2010_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
  RISK_CASE_005:
    NAME: FILTER_BYPASS_KEYWORD
    INPUT: "black‐list (bypasses a 'black-list' blocklist)"
    CONTEXT: bypassing a text filter on the ASCII hyphen
    RISK: MEDIUM
    ATTACK: substituting the hyphen moves the phrase out from under the filter
    GUARD: HYPHEN_2010_FORM ≠ ASCII_CHARACTER
  RISK_CASE_006:
    NAME: MULTI_DASH_MIX
    INPUT: "pay‐pal.com / pay–pal.com" (‐ U+2010 and – U+2013 together)
    CONTEXT: mixing different dash look-alikes complicates detection
    RISK: MEDIUM
    ATTACK: several non-ASCII dashes imitate the same ASCII hyphen
    GUARD: HYPHEN_2010_FORM ≠ DOMAIN_VALIDITY_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: -
    CODEPOINT: U+002D
    NAME: HYPHEN-MINUS
    RISK: HIGH
    RULE: ASCII_HYPHEN ≠ HYPHEN(U+2010) (the primary impersonation target; near-indistinguishable)
  CONFUSABLE_002:
    VISIBLE_FORM: ‑
    CODEPOINT: U+2011
    NAME: NON-BREAKING HYPHEN
    RISK: MEDIUM
    RULE: NON_BREAKING_HYPHEN ≠ HYPHEN(U+2010)
  CONFUSABLE_003:
    VISIBLE_FORM: ‒
    CODEPOINT: U+2012
    NAME: FIGURE DASH
    RISK: LOW
    RULE: FIGURE_DASH ≠ HYPHEN(U+2010)
  CONFUSABLE_004:
    VISIBLE_FORM: –
    CODEPOINT: U+2013
    NAME: EN DASH
    RISK: MEDIUM
    RULE: EN_DASH ≠ HYPHEN(U+2010)
  CONFUSABLE_005:
    VISIBLE_FORM: −
    CODEPOINT: U+2212
    NAME: MINUS SIGN
    RISK: MEDIUM
    RULE: MINUS_SIGN ≠ HYPHEN(U+2010)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "the domain `pay‐pal.com` is pay-pal.com"
    RESPONSE: HYPHEN_2010_FORM ≠ ASCII_HYPHEN
    RULE: ‐ is a different codepoint; DNS decides the registrable domain, not the eye
  CG2:
    TRIGGER: "a string with ‐ will match the ASCII spelling in an allowlist"
    RESPONSE: HYPHEN_2010_FORM ≠ SAME_CODEPOINT_AS_ASCII
    RULE: an exact comparison will not match; normalize to ASCII before checking
  CG3:
    TRIGGER: "any ‐ in text is an attack"
    RESPONSE: HYPHEN_2010_FORM ≠ AUTOMATICALLY_SPOOF
    RULE: in typography ‐ is legit; the spoof is a substitution in a domain/identifier
  CG4:
    TRIGGER: "an ASCII '-' filter will catch ‐"
    RESPONSE: HYPHEN_2010_FORM ≠ ASCII_CHARACTER
    RULE: ‐ is outside ASCII; a "-" filter will not match it
  CG5:
    TRIGGER: "‐ and '-' are interchangeable in an identifier"
    RESPONSE: HYPHEN_2010_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
    RULE: in a domain/login the swap changes the entity the string resolves to
  CG6:
    TRIGGER: "‐ confirms a compound brand's affiliation"
    RESPONSE: HYPHEN_2010_FORM ≠ BRAND_AFFILIATION
    RULE: a typographic hyphen creates no affiliation, just like the ASCII hyphen

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "brand‐word.tld"
      NAME: HYPHEN_SPOOF_DOMAIN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: ‐ imitates the ASCII hyphen in a fake compound domain
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "‐ + – + −" (a mix of dash look-alikes)
      NAME: MULTI_DASH_MIX
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: different non-ASCII dashes imitate one ASCII hyphen
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — the sign's danger appears in a token/domain, not in isolation.

PHAGO_ENTITY_MIMICRY:
  PE_001:
    INPUT: "paypal‐secure.com"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: MEDIUM
    NOTE: ‐ imitates the ASCII hyphen in a compound domain implying brand affiliation (like HYPHEN-MINUS, but non-ASCII). Partial (○) PHAGO — it reinforces the hyphen's entity-mimicry.
  PE_002:
    INPUT: "e‐shop‐official.example"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: MEDIUM
    NOTE: a chain of ‐ assembles an "official" compound name imitating an entity.

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of the ASCII hyphen (U+002D) with ‐ (U+2010) in a brand domain
  A2: mixing ‐ with – (U+2013) / − (U+2212) to complicate detection
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: ‐ bypasses an allowlist/blocklist on the ASCII hyphen (secure‐bank)
  B2: ‐ in a mail domain (info@e‐shop.example)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: fake domain `brand‐word.tld` (SC1)
  C2: a mix of dashes `‐ – −` (SC2)
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "black‐list" — a filter bypass on a phrase
  D2: "verified‐secure" — a pseudo-official compound name
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: `paypal‐secure.com` — mimicry of brand affiliation (PE_001)
  E2: `e‐shop‐official.example` — mimicry of a service entity (PE_002)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: `pay‐pal.com` is the domain pay-pal.com
  EXPECTED: FAIL_ASCII_HYPHEN_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: a string with ‐ will match the ASCII spelling in an allowlist
  EXPECTED: FAIL_CODEPOINT_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: any ‐ in text is an attack
  EXPECTED: FAIL_OVERBLOCK_MIMICRY (the inverse error: a typographic hyphen is not a spoof)
  RESULT: FAIL
MUTATION_04:
  CLAIM: an ASCII "-" filter will catch ‐
  EXPECTED: FAIL_ASCII_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: ‐ and "-" are interchangeable in an identifier
  EXPECTED: FAIL_IDENTIFIER_INTERCHANGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: ‐ confirms a compound brand's affiliation
  EXPECTED: FAIL_BRAND_AFFILIATION_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: normalize all non-ASCII dashes to "-" before comparison — where is the line with legit typography?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (normalize to ASCII in a domain/identifier context; in prose ‐ stays legit — an integrator concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "‐ ≠ ASCII hyphen; normalize in a structural context, not in prose".
ALL_OPEN_QUESTIONS_CLOSED: NO (delegated, non-blocking)

============================================================
11. PATCH_HISTORY
============================================================
PATCH_HISTORY:
  v0_1_PATCH_01: initial creation (Ruslan Malyavsky, 2026-07-21) — draft from the GEN3_v0_3 template (Vakhter), homoglyph of the ASCII hyphen; not conveyor-run.
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
