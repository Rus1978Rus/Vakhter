PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_SMALL_ROMAN_FIFTY_U217C_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_SMALL_ROMAN_FIFTY_U217C_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. Homoglyph sign: core law is LOOKS_SAME ≠ IS_SAME. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_SMALL_ROMAN_FIFTY_U217C_GEN3_v0_3_EN
CODEPOINT: U+217C
VISIBLE_FORM: ⅼ
UNICODE_NAME: SMALL ROMAN NUMERAL FIFTY
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: small Roman numeral fifty (homoglyph of Latin l)
CATEGORY_ROADMAP: PH (Roman numeral look-alike of 'l') · PHAGO: ○ (partial — rarer, but mimics a letter of the brand name)

============================================================
3. REQUIRED_GENERAL_GUARDS
============================================================
REQUIRED_GENERAL_GUARDS:
  - SIGN_FALSE_EFFECT_MIMICRY_GUARD_v0_2A_RU
    GUARD_COMPATIBILITY: applicable — the sign creates no effect-fields; for a homoglyph the guard is extended by a mixed-set check at the integrator level
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
VISIBLE_FORM: ⅼ
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_NUMERAL_HOMOGLYPH
BASE_MODE_FORMULA: ROMAN_FIFTY_FORM ≠ LATIN_L
SIGN_CATEGORY:
  - Roman numeral "50" (legitimate in Roman numbering)
  - homoglyph of Latin small "l" (U+006C)
  - potential carrier of homoglyph spoofing (a brand-name letter)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_LATIN_L — ⅼ (U+217C) is NOT Latin l (U+006C); a different codepoint
  2. NOT_SAME_STRING_AS_LATIN — a string with ⅼ is not machine-equal to its Latin twin
  3. NOT_BRAND_NAME_PROOF — "paypaⅼ" does not prove a link to the PayPal brand
  4. NOT_DOMAIN_VALIDITY_PROOF — a visual domain match does not confirm the registrable domain
  5. NOT_AUTHORITY — the sign does not confirm official status
  6. NOT_VERIFICATION — it does not verify an adjacent fact
  7. NOT_ASCII — outside ASCII; "ASCII-only" filters do not see it as l
  8. NOT_AUTOMATICALLY_SPOOF — in Roman numbering it is normal, not an attack
  9. NOT_EXECUTION_TRIGGER — by itself it launches nothing
  10. NOT_TRUST_SIGNAL — it does not increase trust
  11. NOT_INTERCHANGEABLE_IN_IDENTIFIERS — in an identifier, l→ⅼ changes the entity

BASE_FORMULAS:
  ROMAN_FIFTY_FORM ≠ LATIN_L
  ROMAN_FIFTY_FORM ≠ SAME_CODEPOINT_AS_LATIN
  ROMAN_FIFTY_FORM ≠ BRAND_NAME_PROOF
  ROMAN_FIFTY_FORM ≠ DOMAIN_VALIDITY_PROOF
  ROMAN_FIFTY_FORM ≠ AUTHORITY
  ROMAN_FIFTY_FORM ≠ VERIFICATION
  ROMAN_FIFTY_FORM ≠ ASCII_LETTER
  ROMAN_FIFTY_FORM ≠ AUTOMATICALLY_SPOOF
  ROMAN_FIFTY_FORM ≠ TRUST_SIGNAL
  ROMAN_FIFTY_FORM ≠ EFFECT
  ROMAN_FIFTY_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: ⅼ (small Roman fifty) is a stable numeric sign. "Homoglyph" is a property of visual coincidence with Latin l, co-existing with the numeric function. The danger is contextual (letter substitution in a token), not epochal.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a written numeric sign with no gestural predecessor; the Unicode number-form glyph is inherited from the Latin letter L.

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
    INPUT: "Ⅼ = 50 (Roman)"
    CONTEXT: Roman numeral 50 in a numeric context
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_FIFTY_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_002:
    INPUT: "numbering: ⅰ ⅴ ⅹ ⅼ"
    CONTEXT: a sequence of small Roman numerals
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_FIFTY_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "chapter Ⅼ"
    CONTEXT: chapter number in a Roman numeral
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_FIFTY_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_004:
    INPUT: "clock face: Ⅰ Ⅴ Ⅹ Ⅼ"
    CONTEXT: Roman numerals (typography)
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_FIFTY_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "volume ⅼ, page 3"
    CONTEXT: volume number in a small Roman numeral
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_FIFTY_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_006:
    INPUT: "list item Ⅼ"
    CONTEXT: a numbered list item in a Roman numeral
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_FIFTY_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: BRAND_LETTER_SPOOF
    INPUT: "paypaⅼ.com" (Roman ⅼ instead of l)
    CONTEXT: IDN/brand spoof — the token looks like paypal.com
    RISK: HIGH
    ATTACK: replacing Latin l with Roman ⅼ yields a visually identical domain the attacker registers
    GUARD: ROMAN_FIFTY_FORM ≠ LATIN_L
  RISK_CASE_002:
    NAME: LOGIN_HOMOGLYPH
    INPUT: "ⅼogin.example" (Roman ⅼ at the start)
    CONTEXT: substitution in a service name
    RISK: MEDIUM
    ATTACK: "ⅼogin" looks like "login" but is a different token
    GUARD: ROMAN_FIFTY_FORM ≠ DOMAIN_VALIDITY_PROOF
  RISK_CASE_003:
    NAME: FILTER_BYPASS_KEYWORD
    INPUT: "iⅼlegal" (Roman ⅼ bypasses an "illegal" blocklist)
    CONTEXT: bypassing a text filter
    RISK: MEDIUM
    ATTACK: one substituted letter moves the word out from under the blocklist
    GUARD: ROMAN_FIFTY_FORM ≠ ASCII_LETTER
  RISK_CASE_004:
    NAME: HANDLE_IMPERSONATION
    INPUT: "@nulⅼ_admin" (Roman ⅼ in a handle)
    CONTEXT: impersonating a service account
    RISK: MEDIUM
    ATTACK: the look-alike handle appears as "null_admin" but is a different account
    GUARD: ROMAN_FIFTY_FORM ≠ VERIFICATION
  RISK_CASE_005:
    NAME: EMAIL_LOOKALIKE
    INPUT: "billing@gⅼobal-bank.example"
    CONTEXT: Roman ⅼ in the mail domain
    RISK: MEDIUM
    ATTACK: the domain looks identical but leads to the attacker
    GUARD: ROMAN_FIFTY_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
  RISK_CASE_006:
    NAME: MULTI_HOMOGLYPH_MIX
    INPUT: "paypaⅼ" (Roman ⅼ + Latin + possibly a vertical bar)
    CONTEXT: mixing look-alike sources complicates detection
    RISK: MEDIUM
    ATTACK: one target letter imitated from different sets (digit/letter/punctuation)
    GUARD: ROMAN_FIFTY_FORM ≠ BRAND_NAME_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: l
    CODEPOINT: U+006C
    NAME: LATIN SMALL LETTER L
    RISK: HIGH
    RULE: LATIN_L ≠ ROMAN_FIFTY (the primary impersonation target; visually identical)
  CONFUSABLE_002:
    VISIBLE_FORM: 1
    CODEPOINT: U+0031
    NAME: DIGIT ONE
    RISK: MEDIUM
    RULE: DIGIT_ONE ≠ ROMAN_FIFTY (close to l/1 in some fonts)
  CONFUSABLE_003:
    VISIBLE_FORM: I
    CODEPOINT: U+0049
    NAME: LATIN CAPITAL LETTER I
    RISK: MEDIUM
    RULE: CAPITAL_I ≠ ROMAN_FIFTY
  CONFUSABLE_004:
    VISIBLE_FORM: |
    CODEPOINT: U+007C
    NAME: VERTICAL LINE
    RISK: LOW
    RULE: VERTICAL_LINE ≠ ROMAN_FIFTY
  CONFUSABLE_005:
    VISIBLE_FORM: ǀ
    CODEPOINT: U+01C0
    NAME: LATIN LETTER DENTAL CLICK
    RISK: LOW
    RULE: DENTAL_CLICK ≠ ROMAN_FIFTY

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "the domain `paypaⅼ.com` is PayPal"
    RESPONSE: ROMAN_FIFTY_FORM ≠ LATIN_L
    RULE: the sign is a Roman numeral; the registrable domain is different — DNS decides, not the eye
  CG2:
    TRIGGER: "a string with ⅼ equals its Latin spelling"
    RESPONSE: ROMAN_FIFTY_FORM ≠ SAME_CODEPOINT_AS_LATIN
    RULE: different codepoints → machine-different strings
  CG3:
    TRIGGER: "any ⅼ in text is an attack"
    RESPONSE: ROMAN_FIFTY_FORM ≠ AUTOMATICALLY_SPOOF
    RULE: in Roman numbering the sign is legit; the spoof is a LETTER substitution in a Latin token
  CG4:
    TRIGGER: "an ASCII filter will catch the substituted word"
    RESPONSE: ROMAN_FIFTY_FORM ≠ ASCII_LETTER
    RULE: ⅼ is outside ASCII; a Latin filter will not match it
  CG5:
    TRIGGER: "the handle `@nulⅼ_admin` is the same account"
    RESPONSE: ROMAN_FIFTY_FORM ≠ VERIFICATION
    RULE: visual similarity does not identify an account
  CG6:
    TRIGGER: "swapping l→ⅼ in an identifier is harmless"
    RESPONSE: ROMAN_FIFTY_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
    RULE: in a domain/login the swap changes the entity the string resolves to

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "paypaⅼ" (Roman ⅼ + Latin in one token)
      NAME: MIXED_SCRIPT_TOKEN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: brand spoof; the key signal is a number-form/other set within a Latin token
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "gⅼobaⅼ" (several ⅼ among Latin)
      NAME: MULTI_HOMOGLYPH_TOKEN
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: multiple substitution onto a target name
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — the sign's danger appears in a sequence (a token), not in isolation.

PHAGO_ENTITY_MIMICRY:
  PE_001:
    INPUT: "paypaⅼ.com"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: MEDIUM
    NOTE: ⅼ mimics a letter of a verified brand's NAME (paypal). Partial (○) PHAGO — rarer than the a/o homoglyphs, but the same entity-mimicry-by-name class.
  PE_002:
    INPUT: "@gⅼobal_support"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: MEDIUM
    NOTE: impersonating an official account via a look-alike letter in the name.

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of Latin l (U+006C) with Roman ⅼ (U+217C) in a brand domain
  A2: mixing ⅼ with a vertical bar | (U+007C) / digit 1 to complicate detection
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: Roman ⅼ bypasses a Latin-keyword blocklist (iⅼlegal)
  B2: Roman ⅼ in a mail domain (billing@gⅼobal-bank.example)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: the mixed token `paypaⅼ` (SC1)
  C2: multiple substitution `gⅼobaⅼ` (SC2)
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: the handle `@nulⅼ_admin` imitates a service account
  D2: "ⅼogin-official" — a look-alike in a pseudo-official name
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: `paypaⅼ.com` — mimicry of a brand name (PE_001)
  E2: `@gⅼobal_support` — mimicry of an official account (PE_002)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: `paypaⅼ.com` with Roman ⅼ is PayPal's domain
  EXPECTED: FAIL_BRAND_NAME_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: a string with ⅼ is machine-equal to its Latin spelling
  EXPECTED: FAIL_CODEPOINT_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: any ⅼ in text is an attack
  EXPECTED: FAIL_OVERBLOCK_MIMICRY (the inverse error: genuine Roman numbering is not a spoof)
  RESULT: FAIL
MUTATION_04:
  CLAIM: an ASCII filter on "illegal" will catch "iⅼlegal"
  EXPECTED: FAIL_ASCII_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: the handle `@nulⅼ_admin` is the same account as `@null_admin`
  EXPECTED: FAIL_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: swapping l→ⅼ in an identifier is harmless
  EXPECTED: FAIL_IDENTIFIER_INTERCHANGE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to distinguish legit Roman numbering from a letter substitution without false positives?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (the "number-form among Latin LETTERS in one token" rule is an integrator concern; cf. Vakhter confusable_cards.py)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the LOOKS_SAME ≠ IS_SAME formula and the "spoof = substitution in a token, not presence of a number-form" rule.
ALL_OPEN_QUESTIONS_CLOSED: NO (delegated, non-blocking)

============================================================
11. PATCH_HISTORY
============================================================
PATCH_HISTORY:
  v0_1_PATCH_01: initial creation (Ruslan Malyavsky, 2026-07-21) — draft from the GEN3_v0_3 template (Vakhter), homoglyph sign; not conveyor-run.
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
