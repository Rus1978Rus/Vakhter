PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_ROMAN_SMALL_C_U217D_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_ROMAN_SMALL_C_U217D_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. Homoglyph sign: core law is LOOKS_SAME ≠ IS_SAME. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_ROMAN_SMALL_C_U217D_GEN3_v0_3_EN
CODEPOINT: U+217D
VISIBLE_FORM: ⅽ
UNICODE_NAME: SMALL ROMAN NUMERAL ONE HUNDRED
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: Roman numeral "ⅽ" small one hundred (homoglyph of Latin small c)
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
VISIBLE_FORM: ⅽ
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_LETTER_HOMOGLYPH
BASE_MODE_FORMULA: ROMAN_SMALL_C_FORM ≠ LATIN_C
SIGN_CATEGORY:
  - Roman-numeral letter-form "small roman numeral one hundred" (means 100 as a standalone numeral; a Number Forms character)
  - homoglyph of Latin small "c" (U+0063)
  - potential carrier of homoglyph spoofing when mixed INTO a Latin word

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_LATIN_C — Roman ⅽ (U+217D) is NOT Latin c (U+0063); a different codepoint AND a numeral (value 100), not a letter
  2. NOT_SAME_STRING_AS_LATIN — a string with Roman ⅽ is not machine-equal to its Latin twin
  3. NOT_BRAND_NAME_PROOF — "ⅽisco" does not prove a link to the Cisco brand
  4. NOT_DOMAIN_VALIDITY_PROOF — a visual domain match does not confirm the registrable domain
  5. NOT_AUTHORITY — the form does not confirm official status
  6. NOT_VERIFICATION — it does not verify an adjacent fact
  7. NOT_ASCII — not in ASCII; "ASCII-only" filters do not see it as c
  8. NOT_AUTOMATICALLY_SPOOF — as a standalone Roman numeral it is normal, not an attack
  9. NOT_EXECUTION_TRIGGER — by itself it launches nothing
  10. NOT_TRUST_SIGNAL — it does not increase trust in content
  11. NOT_EFFECT — the numeral form creates no effect
  12. NOT_INTERCHANGEABLE_IN_IDENTIFIERS — in an identifier/domain, c→ⅽ changes the entity

BASE_FORMULAS:
  ROMAN_SMALL_C_FORM ≠ LATIN_C
  ROMAN_SMALL_C_FORM ≠ SAME_CODEPOINT_AS_LATIN
  ROMAN_SMALL_C_FORM ≠ BRAND_NAME_PROOF
  ROMAN_SMALL_C_FORM ≠ DOMAIN_VALIDITY_PROOF
  ROMAN_SMALL_C_FORM ≠ AUTHORITY
  ROMAN_SMALL_C_FORM ≠ VERIFICATION
  ROMAN_SMALL_C_FORM ≠ ASCII_LETTER
  ROMAN_SMALL_C_FORM ≠ AUTOMATICALLY_SPOOF
  ROMAN_SMALL_C_FORM ≠ TRUST_SIGNAL
  ROMAN_SMALL_C_FORM ≠ EFFECT
  ROMAN_SMALL_C_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: Roman "ⅽ" small one hundred is a stable numeral form with no cultural precession of functions. "Homoglyph" is not an epoch but a property of visual coincidence with Latin c, co-existing with the form's legit numeral function. The danger is contextual (embedded in a Latin word), not epochal — so SEMANTIC_EPOCH_TRACKER does not apply.
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
    INPUT: "ⅽ years" (100 years, Roman numeral)
    CONTEXT: a standalone Roman numeral (its own token)
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_SMALL_C_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_002:
    INPUT: "Page ⅽ" (page 100, Roman numeral)
    CONTEXT: a Roman numeral as a whole token, not inside a word
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_SMALL_C_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "ⅽⅼ guests" (150 guests, Roman numeral)
    CONTEXT: an all-Roman-numeral token
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_SMALL_C_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_004:
    INPUT: "chapter ⅽ" (chapter 100, Roman numeral)
    CONTEXT: an all-Roman-numeral token beside a Latin word
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_SMALL_C_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "ⅾⅽ soldiers" (600 soldiers, Roman numeral)
    CONTEXT: an all-Roman-numeral token
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_SMALL_C_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_006:
    INPUT: "ⅽⅽ pages" (200 pages, Roman numeral)
    CONTEXT: an all-Roman-numeral token
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_SMALL_C_FORM ≠ AUTOMATICALLY_SPOOF

RISK_CASES:
  RISK_CASE_001:
    NAME: BRAND_HOMOGLYPH
    INPUT: "ⅽisco-support.com" (Roman ⅽ at the start of a brand)
    CONTEXT: IDN/brand spoof — the token looks like cisco but the first char is a Roman numeral
    RISK: CRITICAL
    ATTACK: replacing Latin c with Roman ⅽ yields a visually identical brand the attacker registers
    GUARD: ROMAN_SMALL_C_FORM ≠ LATIN_C
  RISK_CASE_002:
    NAME: MIDTOKEN_BRAND_SUBSTITUTION
    INPUT: "faⅽebook-login.com" (Roman ⅽ inside a brand)
    CONTEXT: mid-token substitution in a brand phrase
    RISK: CRITICAL
    ATTACK: the string is machine-≠ facebook, but a human sees no difference
    GUARD: ROMAN_SMALL_C_FORM ≠ DOMAIN_VALIDITY_PROOF
  RISK_CASE_003:
    NAME: HANDLE_IMPERSONATION
    INPUT: "@ⅽostcoHelp" (Roman ⅽ in a handle)
    CONTEXT: impersonating a brand account in a chat/social platform
    RISK: HIGH
    ATTACK: the look-alike handle appears as costcoHelp but is a different account
    GUARD: ROMAN_SMALL_C_FORM ≠ VERIFICATION
  RISK_CASE_004:
    NAME: FILTER_BYPASS_KEYWORD
    INPUT: "ⅽlick" (Roman ⅽ bypasses a "click" blocklist)
    CONTEXT: bypassing a text filter looking for a Latin word
    RISK: HIGH
    ATTACK: one substituted character moves the word out from under the blocklist
    GUARD: ROMAN_SMALL_C_FORM ≠ ASCII_LETTER
  RISK_CASE_005:
    NAME: EMAIL_LOOKALIKE
    INPUT: "no-reply@ⅽhase-secure.example" (Roman ⅽ in the mail domain)
    CONTEXT: a phishing email from the "same" company
    RISK: HIGH
    ATTACK: the domain looks identical but leads to the attacker
    GUARD: ROMAN_SMALL_C_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
  RISK_CASE_006:
    NAME: MULTI_HOMOGLYPH_ON_TARGET
    INPUT: "ⅽostⅽo" (two Roman ⅽ among Latin letters, imitating costco)
    CONTEXT: multiple substitutions in one token (ⅽ Roman, ost/o Latin — a numeral-in-word mix)
    RISK: HIGH
    ATTACK: a chain of look-alikes imitates the whole Latin brand name
    GUARD: ROMAN_SMALL_C_FORM ≠ BRAND_NAME_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: c
    CODEPOINT: U+0063
    NAME: LATIN SMALL LETTER C
    RISK: CRITICAL
    RULE: LATIN_C ≠ ROMAN_SMALL_C (the primary impersonation target; visually identical in many fonts)
  CONFUSABLE_002:
    VISIBLE_FORM: с
    CODEPOINT: U+0441
    NAME: CYRILLIC SMALL LETTER ES
    RISK: HIGH
    RULE: CYRILLIC_ES ≠ ROMAN_SMALL_C (another script with the same c-shape; complicates detection)
  CONFUSABLE_003:
    VISIBLE_FORM: ｃ
    CODEPOINT: U+FF43
    NAME: FULLWIDTH LATIN SMALL LETTER C
    RISK: MEDIUM
    RULE: FULLWIDTH_SMALL_C ≠ ROMAN_SMALL_C (a full-width Latin c; a different compatibility form)
  CONFUSABLE_004:
    VISIBLE_FORM: 𝖼
    CODEPOINT: U+1D5BC
    NAME: MATHEMATICAL SANS-SERIF SMALL C
    RISK: MEDIUM
    RULE: MATH_SANS_SMALL_C ≠ ROMAN_SMALL_C (a math-alphanumeric styled Latin c used to dodge simple filters)
  CONFUSABLE_005:
    VISIBLE_FORM: 𝐜
    CODEPOINT: U+1D41C
    NAME: MATHEMATICAL BOLD SMALL C
    RISK: LOW
    RULE: MATH_BOLD_SMALL_C ≠ ROMAN_SMALL_C (a bold-styled Latin c)
  CONFUSABLE_006:
    VISIBLE_FORM: 𝑐
    CODEPOINT: U+1D450
    NAME: MATHEMATICAL ITALIC SMALL C
    RISK: LOW
    RULE: MATH_ITALIC_SMALL_C ≠ ROMAN_SMALL_C (an italic-styled Latin c)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "the brand `ⅽisco` is Cisco"
    RESPONSE: ROMAN_SMALL_C_FORM ≠ LATIN_C
    RULE: the first char is a Roman numeral (100); the registrable domain/name is different — DNS decides, not the eye
  CG2:
    TRIGGER: "a string with Roman ⅽ equals its Latin spelling"
    RESPONSE: ROMAN_SMALL_C_FORM ≠ SAME_CODEPOINT_AS_LATIN
    RULE: different codepoints → machine-different strings
  CG3:
    TRIGGER: "any Roman ⅽ in text is an attack"
    RESPONSE: ROMAN_SMALL_C_FORM ≠ AUTOMATICALLY_SPOOF
    RULE: a standalone Roman numeral is legit; the spoof is a numeral-form embedded INSIDE a Latin word
  CG4:
    TRIGGER: "an ASCII filter will catch the substituted word"
    RESPONSE: ROMAN_SMALL_C_FORM ≠ ASCII_LETTER
    RULE: Roman ⅽ is outside ASCII; a Latin filter will not match it
  CG5:
    TRIGGER: "the handle `@ⅽostcoHelp` is the same account as @costcoHelp"
    RESPONSE: ROMAN_SMALL_C_FORM ≠ VERIFICATION
    RULE: visual similarity does not identify an account
  CG6:
    TRIGGER: "swapping c→ⅽ in an identifier is harmless"
    RESPONSE: ROMAN_SMALL_C_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
    RULE: in a domain/login/token the swap changes the entity the string resolves to

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "ⅽisco" (Roman ⅽ + Latin in one token)
      NAME: NUMERAL_IN_WORD_TOKEN
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: IDN/brand spoof; the key signal is a Roman-numeral form INSIDE an ASCII-Latin word
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "ⅽostⅽo" (two Roman ⅽ among Latin letters)
      NAME: MULTI_HOMOGLYPH_TOKEN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: multiple substitution onto a target brand
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — the sign's danger appears precisely in a sequence (a token), not in isolation.

PHAGO_ENTITY_MIMICRY:
  PE_001:
    INPUT: "ⅽisco-support.com"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: CRITICAL
    NOTE: Roman ⅽ mimics the NAME itself of a verified brand (not merely structure) — direct mimicry of an entity's existence. This is why the registry flags the sign PHAGO ●; commercial lookalike defenses often miss this class.
  PE_002:
    INPUT: "@ⅽostcoHelp"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: HIGH
    NOTE: impersonating an official brand support account via a look-alike in the name.

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of Latin c (U+0063) with Roman ⅽ (U+217D) in a brand domain
  A2: mixing Roman ⅽ with Cyrillic es с / math sans-serif c to complicate detection
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: Roman ⅽ bypasses a Latin-keyword blocklist (ⅽlick)
  B2: Roman ⅽ in a mail domain (no-reply@ⅽhase-secure.example) for phishing
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: the numeral-in-word token `ⅽisco` (SC1) — a Roman form inside one word
  C2: multiple substitution `ⅽostⅽo` (SC2) onto a target brand
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: the handle `@ⅽostcoHelp` imitates a brand account
  D2: "ⅽhase-secure" — a look-alike in a pseudo-official name
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: `ⅽisco-support.com` — mimicry of a brand name (PE_001)
  E2: `@ⅽostcoHelp` — mimicry of an official account (PE_002)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the form has no dormant/active epochs (see section 5).
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: `ⅽisco-support.com` with Roman ⅽ is Cisco's domain
  EXPECTED: FAIL_BRAND_NAME_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: a string with Roman ⅽ is machine-equal to its Latin spelling
  EXPECTED: FAIL_CODEPOINT_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: any Roman ⅽ in text is an attack
  EXPECTED: FAIL_OVERBLOCK_MIMICRY (the inverse error: a standalone Roman numeral is not a spoof)
  RESULT: FAIL
MUTATION_04:
  CLAIM: an ASCII filter on "click" will catch "ⅽlick"
  EXPECTED: FAIL_ASCII_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: the handle `@ⅽostcoHelp` is the same account as `@costcoHelp`
  EXPECTED: FAIL_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: swapping c→ⅽ in an identifier is harmless
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
