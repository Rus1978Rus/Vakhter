PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_ROMAN_CAPITAL_L_U216C_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_ROMAN_CAPITAL_L_U216C_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. Homoglyph sign: core law is LOOKS_SAME ≠ IS_SAME. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_ROMAN_CAPITAL_L_U216C_GEN3_v0_3_EN
CODEPOINT: U+216C
VISIBLE_FORM: Ⅼ
UNICODE_NAME: ROMAN NUMERAL FIFTY
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: Roman numeral "Ⅼ" fifty (homoglyph of Latin capital L)
CATEGORY_ROADMAP: PH (phishing) · PHAGO: ● (strong carrier — mimics the brand name itself)

============================================================
3. REQUIRED_GENERAL_GUARDS
============================================================
REQUIRED_GENERAL_GUARDS:
  - SIGN_FALSE_EFFECT_MIMICRY_GUARD_v0_2A_RU
    GUARD_COMPATIBILITY: applicable — the sign creates no effect-fields; for a numeral-letterform homoglyph the guard is extended by a "Roman-numeral form inside a Latin word" check at the integrator level
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
VISIBLE_FORM: Ⅼ
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_LETTER_HOMOGLYPH
BASE_MODE_FORMULA: ROMAN_CAP_L_FORM ≠ LATIN_CAP_L
SIGN_CATEGORY:
  - Roman-numeral letter-form "roman numeral fifty" (means 50 as a standalone numeral; a Number Forms character)
  - homoglyph of Latin capital "L" (U+004C)
  - potential carrier of homoglyph spoofing when mixed INTO a Latin word

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_LATIN_CAP_L — Roman Ⅼ (U+216C) is NOT Latin L (U+004C); a different codepoint AND a numeral (value 50), not a letter
  2. NOT_SAME_STRING_AS_LATIN — a string with Roman Ⅼ is not machine-equal to its Latin twin
  3. NOT_BRAND_NAME_PROOF — "ⅬEGO" does not prove a link to the Lego brand
  4. NOT_DOMAIN_VALIDITY_PROOF — a visual domain match does not confirm the registrable domain
  5. NOT_AUTHORITY — the form does not confirm official status
  6. NOT_VERIFICATION — it does not verify an adjacent fact
  7. NOT_ASCII — not in ASCII; "ASCII-only" filters do not see it as L
  8. NOT_AUTOMATICALLY_SPOOF — as a standalone Roman numeral it is normal, not an attack
  9. NOT_EXECUTION_TRIGGER — by itself it launches nothing
  10. NOT_TRUST_SIGNAL — it does not increase trust in content
  11. NOT_EFFECT — the numeral form creates no effect
  12. NOT_INTERCHANGEABLE_IN_IDENTIFIERS — in an identifier/domain, L→Ⅼ changes the entity

BASE_FORMULAS:
  ROMAN_CAP_L_FORM ≠ LATIN_CAP_L
  ROMAN_CAP_L_FORM ≠ SAME_CODEPOINT_AS_LATIN
  ROMAN_CAP_L_FORM ≠ BRAND_NAME_PROOF
  ROMAN_CAP_L_FORM ≠ DOMAIN_VALIDITY_PROOF
  ROMAN_CAP_L_FORM ≠ AUTHORITY
  ROMAN_CAP_L_FORM ≠ VERIFICATION
  ROMAN_CAP_L_FORM ≠ ASCII_LETTER
  ROMAN_CAP_L_FORM ≠ AUTOMATICALLY_SPOOF
  ROMAN_CAP_L_FORM ≠ TRUST_SIGNAL
  ROMAN_CAP_L_FORM ≠ EFFECT
  ROMAN_CAP_L_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: Roman "Ⅼ" fifty is a stable numeral form with no cultural precession of functions. "Homoglyph" is not an epoch but a property of visual coincidence with Latin L, co-existing with the form's legit numeral function. The danger is contextual (embedded in a Latin word), not epochal — so SEMANTIC_EPOCH_TRACKER does not apply.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1 (physical gesture)
  NOTE: a numeral form is a written sign with no gestural predecessor; the Roman numeral letter-forms are a Number Forms encoding of the Latin letters used as numerals.

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
    INPUT: "Ⅼ years" (50 years, Roman numeral)
    CONTEXT: a standalone Roman numeral (its own token)
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_CAP_L_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_002:
    INPUT: "Page Ⅼ" (page 50, Roman numeral)
    CONTEXT: a Roman numeral as a whole token, not inside a word
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_CAP_L_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "Volume Ⅼ" (volume 50, Roman numeral)
    CONTEXT: a standalone Roman numeral token beside a Latin word
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_CAP_L_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_004:
    INPUT: "Chapter Ⅼ" (chapter 50, Roman numeral)
    CONTEXT: a standalone Roman numeral token beside a Latin word
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_CAP_L_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "ⅭⅬ guests" (150 guests, Roman numeral)
    CONTEXT: an all-Roman-numeral token
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_CAP_L_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_006:
    INPUT: "Super Bowl Ⅼ" (Super Bowl 50, Roman numeral)
    CONTEXT: a standalone Roman numeral token
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_CAP_L_FORM ≠ AUTOMATICALLY_SPOOF

RISK_CASES:
  RISK_CASE_001:
    NAME: BRAND_HOMOGLYPH
    INPUT: "ⅬEGO-shop.com" (Roman Ⅼ at the start of a brand)
    CONTEXT: IDN/brand spoof — the token looks like LEGO but the first char is a Roman numeral
    RISK: CRITICAL
    ATTACK: replacing Latin L with Roman Ⅼ yields a visually identical brand the attacker registers
    GUARD: ROMAN_CAP_L_FORM ≠ LATIN_CAP_L
  RISK_CASE_002:
    NAME: ALLCAPS_BRAND_SUBSTITUTION
    INPUT: "ⅬG-electronics-deal.com" (Roman Ⅼ in an all-caps brand)
    CONTEXT: leading substitution in an all-caps brand phrase
    RISK: CRITICAL
    ATTACK: the string is machine-≠ LG, but a human sees no difference
    GUARD: ROMAN_CAP_L_FORM ≠ DOMAIN_VALIDITY_PROOF
  RISK_CASE_003:
    NAME: HANDLE_IMPERSONATION
    INPUT: "@ⅬinkedInHelp" (Roman Ⅼ in a handle)
    CONTEXT: impersonating a brand account in a chat/social platform
    RISK: HIGH
    ATTACK: the look-alike handle appears as LinkedInHelp but is a different account
    GUARD: ROMAN_CAP_L_FORM ≠ VERIFICATION
  RISK_CASE_004:
    NAME: FILTER_BYPASS_KEYWORD
    INPUT: "ⅬOGIN" (Roman Ⅼ bypasses a "LOGIN" blocklist)
    CONTEXT: bypassing a text filter looking for a Latin word
    RISK: HIGH
    ATTACK: one substituted character moves the word out from under the blocklist
    GUARD: ROMAN_CAP_L_FORM ≠ ASCII_LETTER
  RISK_CASE_005:
    NAME: EMAIL_LOOKALIKE
    INPUT: "no-reply@ⅬLOYDS-secure.example" (Roman Ⅼ in the mail domain)
    CONTEXT: a phishing email from the "same" company
    RISK: HIGH
    ATTACK: the domain looks identical but leads to the attacker
    GUARD: ROMAN_CAP_L_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
  RISK_CASE_006:
    NAME: MULTI_HOMOGLYPH_ON_TARGET
    INPUT: "ⅬOREAⅬ" (two Roman Ⅼ around Latin letters, imitating LOREAL)
    CONTEXT: multiple substitutions in one all-caps token (Ⅼ Roman, OREA Latin — a numeral-in-word mix)
    RISK: HIGH
    ATTACK: a chain of look-alikes imitates the whole Latin brand name
    GUARD: ROMAN_CAP_L_FORM ≠ BRAND_NAME_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: L
    CODEPOINT: U+004C
    NAME: LATIN CAPITAL LETTER L
    RISK: CRITICAL
    RULE: LATIN_CAP_L ≠ ROMAN_CAP_L (the primary impersonation target; visually identical in many fonts)
  CONFUSABLE_002:
    VISIBLE_FORM: Ｌ
    CODEPOINT: U+FF2C
    NAME: FULLWIDTH LATIN CAPITAL LETTER L
    RISK: MEDIUM
    RULE: FULLWIDTH_CAP_L ≠ ROMAN_CAP_L (a full-width Latin L; a different compatibility form)
  CONFUSABLE_003:
    VISIBLE_FORM: 𝗟
    CODEPOINT: U+1D5DF
    NAME: MATHEMATICAL SANS-SERIF BOLD CAPITAL L
    RISK: MEDIUM
    RULE: MATH_SANS_CAP_L ≠ ROMAN_CAP_L (a math-alphanumeric styled Latin L used to dodge simple filters)
  CONFUSABLE_004:
    VISIBLE_FORM: 𝕃
    CODEPOINT: U+1D543
    NAME: MATHEMATICAL DOUBLE-STRUCK CAPITAL L
    RISK: MEDIUM
    RULE: DOUBLE_STRUCK_L ≠ ROMAN_CAP_L (a double-struck styled Latin L)
  CONFUSABLE_005:
    VISIBLE_FORM: 𝐋
    CODEPOINT: U+1D40B
    NAME: MATHEMATICAL BOLD CAPITAL L
    RISK: LOW
    RULE: MATH_BOLD_CAP_L ≠ ROMAN_CAP_L (a bold-styled Latin L)
  CONFUSABLE_006:
    VISIBLE_FORM: 𝐿
    CODEPOINT: U+1D43F
    NAME: MATHEMATICAL ITALIC CAPITAL L
    RISK: LOW
    RULE: MATH_ITALIC_CAP_L ≠ ROMAN_CAP_L (an italic-styled Latin L)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "the brand `ⅬEGO` is Lego"
    RESPONSE: ROMAN_CAP_L_FORM ≠ LATIN_CAP_L
    RULE: the first char is a Roman numeral (50); the registrable domain/name is different — DNS decides, not the eye
  CG2:
    TRIGGER: "a string with Roman Ⅼ equals its Latin spelling"
    RESPONSE: ROMAN_CAP_L_FORM ≠ SAME_CODEPOINT_AS_LATIN
    RULE: different codepoints → machine-different strings
  CG3:
    TRIGGER: "any Roman Ⅼ in text is an attack"
    RESPONSE: ROMAN_CAP_L_FORM ≠ AUTOMATICALLY_SPOOF
    RULE: a standalone Roman numeral is legit; the spoof is a numeral-form embedded INSIDE a Latin word
  CG4:
    TRIGGER: "an ASCII filter will catch the substituted word"
    RESPONSE: ROMAN_CAP_L_FORM ≠ ASCII_LETTER
    RULE: Roman Ⅼ is outside ASCII; a Latin filter will not match it
  CG5:
    TRIGGER: "the handle `@ⅬinkedInHelp` is the same account as @LinkedInHelp"
    RESPONSE: ROMAN_CAP_L_FORM ≠ VERIFICATION
    RULE: visual similarity does not identify an account
  CG6:
    TRIGGER: "swapping L→Ⅼ in an identifier is harmless"
    RESPONSE: ROMAN_CAP_L_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
    RULE: in a domain/login/token the swap changes the entity the string resolves to

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "ⅬEGO" (Roman Ⅼ + Latin in one token)
      NAME: NUMERAL_IN_WORD_TOKEN
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: IDN/brand spoof; the key signal is a Roman-numeral form INSIDE an ASCII-Latin word
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "ⅬOREAⅬ" (two Roman Ⅼ among Latin capitals)
      NAME: MULTI_HOMOGLYPH_TOKEN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: multiple substitution onto a target all-caps brand
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — the sign's danger appears precisely in a sequence (a token), not in isolation.

PHAGO_ENTITY_MIMICRY:
  PE_001:
    INPUT: "ⅬEGO-shop.com"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: CRITICAL
    NOTE: Roman Ⅼ mimics the NAME itself of a verified brand (not merely structure) — direct mimicry of an entity's existence. This is why the registry flags the sign PHAGO ●; commercial lookalike defenses often miss this class.
  PE_002:
    INPUT: "@ⅬinkedInHelp"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: HIGH
    NOTE: impersonating an official brand support account via a look-alike in the name.

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of Latin L (U+004C) with Roman Ⅼ (U+216C) in a brand domain
  A2: mixing Roman Ⅼ with double-struck 𝕃 / math sans-serif L to complicate detection
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: Roman Ⅼ bypasses a Latin-keyword blocklist (ⅬOGIN)
  B2: Roman Ⅼ in a mail domain (no-reply@ⅬLOYDS-secure.example) for phishing
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: the numeral-in-word token `ⅬEGO` (SC1) — a Roman form inside one word
  C2: multiple substitution `ⅬOREAⅬ` (SC2) onto a target brand
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: the handle `@ⅬinkedInHelp` imitates a brand account
  D2: "ⅬLOYDS-secure" — a look-alike in a pseudo-official name
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: `ⅬEGO-shop.com` — mimicry of a brand name (PE_001)
  E2: `@ⅬinkedInHelp` — mimicry of an official account (PE_002)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the form has no dormant/active epochs (see section 5).
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: `ⅬEGO-shop.com` with Roman Ⅼ is Lego's domain
  EXPECTED: FAIL_BRAND_NAME_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: a string with Roman Ⅼ is machine-equal to its Latin spelling
  EXPECTED: FAIL_CODEPOINT_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: any Roman Ⅼ in text is an attack
  EXPECTED: FAIL_OVERBLOCK_MIMICRY (the inverse error: a standalone Roman numeral is not a spoof)
  RESULT: FAIL
MUTATION_04:
  CLAIM: an ASCII filter on "LOGIN" will catch "ⅬOGIN"
  EXPECTED: FAIL_ASCII_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: the handle `@ⅬinkedInHelp` is the same account as `@LinkedInHelp`
  EXPECTED: FAIL_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: swapping L→Ⅼ in an identifier is harmless
  EXPECTED: FAIL_IDENTIFIER_INTERCHANGE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to distinguish a legit standalone Roman numeral from a numeral-form embedded in a word without false positives?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (the "Roman-numeral form inside an ASCII-Latin word" rule is an integrator concern; see the Vakhter prototype confusable_cards.py)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the LOOKS_SAME ≠ IS_SAME formula and the "spoof = numeral-in-word, not standalone" rule.
OQ2:
  QUESTION: is the full UTS #39 confusables table + a brand corpus needed for the whole-word case?
  STATUS: OPEN
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: delegated to the runtime/integrator.
ALL_OPEN_QUESTIONS_CLOSED: NO (delegated, non-blocking)

============================================================
11. PATCH_HISTORY
============================================================
PATCH_HISTORY:
  v0_1_PATCH_01: initial creation (Ruslan Malyavsky, 2026-07-22) — draft from the GEN3_v0_3 template (Vakhter), homoglyph sign; not conveyor-run.
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
