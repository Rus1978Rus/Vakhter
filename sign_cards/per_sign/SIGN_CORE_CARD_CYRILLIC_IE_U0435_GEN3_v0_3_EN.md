PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_CYRILLIC_IE_U0435_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_CYRILLIC_IE_U0435_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. Homoglyph sign: core law is LOOKS_SAME ≠ IS_SAME. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_CYRILLIC_IE_U0435_GEN3_v0_3_EN
CODEPOINT: U+0435
VISIBLE_FORM: е
UNICODE_NAME: CYRILLIC SMALL LETTER IE
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: Cyrillic "е" (homoglyph of Latin e)
CATEGORY_ROADMAP: PH (phishing) · PHAGO: ● (strong carrier — mimics the brand name itself)

============================================================
3. REQUIRED_GENERAL_GUARDS
============================================================
REQUIRED_GENERAL_GUARDS:
  - SIGN_FALSE_EFFECT_MIMICRY_GUARD_v0_2A_RU
    GUARD_COMPATIBILITY: applicable — the sign creates no effect-fields; for a homoglyph the guard is extended by a mixed-script check at the integrator level
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
VISIBLE_FORM: е
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_LETTER_HOMOGLYPH
BASE_MODE_FORMULA: CYRILLIC_IE_FORM ≠ LATIN_E
SIGN_CATEGORY:
  - Cyrillic letter (legitimate in Russian / other Cyrillic scripts)
  - homoglyph of Latin small "e" (U+0065)
  - potential carrier of homoglyph / IDN spoofing when scripts are mixed

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_LATIN_E — Cyrillic е (U+0435) is NOT Latin e (U+0065); a different codepoint
  2. NOT_SAME_STRING_AS_LATIN — a string with Cyrillic е is not machine-equal to its Latin twin
  3. NOT_BRAND_NAME_PROOF — "googlе.com" does not prove a link to the Google brand
  4. NOT_DOMAIN_VALIDITY_PROOF — a visual domain match does not confirm the registrable domain
  5. NOT_AUTHORITY — the letter does not confirm official status
  6. NOT_VERIFICATION — it does not verify an adjacent fact
  7. NOT_ASCII — not in ASCII; "ASCII-only" filters do not see it as e
  8. NOT_AUTOMATICALLY_SPOOF — in single-script Russian text it is normal, not an attack
  9. NOT_EXECUTION_TRIGGER — by itself it launches nothing
  10. NOT_TRUST_SIGNAL — it does not increase trust in content
  11. NOT_EFFECT — the letter form creates no effect
  12. NOT_INTERCHANGEABLE_IN_IDENTIFIERS — in an identifier/domain, e→е changes the entity

BASE_FORMULAS:
  CYRILLIC_IE_FORM ≠ LATIN_E
  CYRILLIC_IE_FORM ≠ SAME_CODEPOINT_AS_LATIN
  CYRILLIC_IE_FORM ≠ BRAND_NAME_PROOF
  CYRILLIC_IE_FORM ≠ DOMAIN_VALIDITY_PROOF
  CYRILLIC_IE_FORM ≠ AUTHORITY
  CYRILLIC_IE_FORM ≠ VERIFICATION
  CYRILLIC_IE_FORM ≠ ASCII_LETTER
  CYRILLIC_IE_FORM ≠ AUTOMATICALLY_SPOOF
  CYRILLIC_IE_FORM ≠ TRUST_SIGNAL
  CYRILLIC_IE_FORM ≠ EFFECT
  CYRILLIC_IE_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: Cyrillic "е" is a stable letter with no cultural precession of functions. "Homoglyph" is not an epoch but a property of visual coincidence with Latin e, co-existing with the letter's legit function. The danger is contextual (mixed scripts), not epochal — so SEMANTIC_EPOCH_TRACKER does not apply.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1 (physical gesture)
  NOTE: a letter is a written sign with no gestural predecessor; Cyrillic descends from Greek uncial (written genealogy).

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
    INPUT: "если день ясный" (if the day is clear, Russian)
    CONTEXT: ordinary Russian text (single script)
    EXPECTED: INFO
    RISK: NONE
    GUARD: CYRILLIC_IE_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_002:
    INPUT: "Елена Летова" (a Russian name)
    CONTEXT: Russian proper name
    EXPECTED: INFO
    RISK: NONE
    GUARD: CYRILLIC_IE_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "белое море" (the White Sea)
    CONTEXT: Russian words where "е" is an ordinary letter
    EXPECTED: INFO
    RISK: NONE
    GUARD: CYRILLIC_IE_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_004:
    INPUT: "неделя отдыха" (a week of rest)
    CONTEXT: a Russian phrase
    EXPECTED: INFO
    RISK: NONE
    GUARD: CYRILLIC_IE_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "дерево в лесу" (a tree in the forest)
    CONTEXT: single-script Cyrillic phrase
    EXPECTED: INFO
    RISK: NONE
    GUARD: CYRILLIC_IE_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_006:
    INPUT: "еле-еле" (barely)
    CONTEXT: a word rich in "е", yet all Cyrillic
    EXPECTED: INFO
    RISK: NONE
    GUARD: CYRILLIC_IE_FORM ≠ AUTOMATICALLY_SPOOF

RISK_CASES:
  RISK_CASE_001:
    NAME: GOOGLE_HOMOGLYPH
    INPUT: "googlе.com" (Cyrillic е at the end of a brand)
    CONTEXT: IDN/brand spoof — the token looks like google.com but the last char is Cyrillic
    RISK: CRITICAL
    ATTACK: replacing Latin e with Cyrillic е yields a visually identical domain the attacker registers
    GUARD: CYRILLIC_IE_FORM ≠ LATIN_E
  RISK_CASE_002:
    NAME: MEDIAL_BRAND_SUBSTITUTION
    INPUT: "amazоn-sеcure.com" (Cyrillic е in the middle of a brand phrase)
    CONTEXT: medial substitution in a brand domain
    RISK: CRITICAL
    ATTACK: the string is machine-≠ its Latin spelling, but a human sees no difference
    GUARD: CYRILLIC_IE_FORM ≠ DOMAIN_VALIDITY_PROOF
  RISK_CASE_003:
    NAME: HANDLE_IMPERSONATION
    INPUT: "@hеlpdesk" (Cyrillic е in a handle)
    CONTEXT: impersonating a helpdesk account in a chat/social platform
    RISK: HIGH
    ATTACK: the look-alike handle appears as helpdesk but is a different account
    GUARD: CYRILLIC_IE_FORM ≠ VERIFICATION
  RISK_CASE_004:
    NAME: FILTER_BYPASS_KEYWORD
    INPUT: "frее-money" (Cyrillic е bypasses a "free" blocklist)
    CONTEXT: bypassing a text filter looking for a Latin word
    RISK: HIGH
    ATTACK: one substituted letter moves the word out from under the blocklist
    GUARD: CYRILLIC_IE_FORM ≠ ASCII_LETTER
  RISK_CASE_005:
    NAME: EMAIL_LOOKALIKE
    INPUT: "service@securе-pay.example" (Cyrillic е in the mail domain)
    CONTEXT: a phishing email from the "same" service
    RISK: HIGH
    ATTACK: the domain looks identical but leads to the attacker
    GUARD: CYRILLIC_IE_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
  RISK_CASE_006:
    NAME: MULTI_HOMOGLYPH_ON_TARGET
    INPUT: "еxprеss" (several Cyrillic е imitating a brand)
    CONTEXT: multiple substitutions in one token
    RISK: HIGH
    ATTACK: a chain of look-alikes imitates the whole Latin brand name
    GUARD: CYRILLIC_IE_FORM ≠ BRAND_NAME_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: e
    CODEPOINT: U+0065
    NAME: LATIN SMALL LETTER E
    RISK: CRITICAL
    RULE: LATIN_E ≠ CYRILLIC_IE (the primary impersonation target; visually identical in many fonts)
  CONFUSABLE_002:
    VISIBLE_FORM: ё
    CODEPOINT: U+0451
    NAME: CYRILLIC SMALL LETTER IO
    RISK: MEDIUM
    RULE: CYRILLIC_IO ≠ CYRILLIC_IE (same script, a diaeresis form; distinct letter)
  CONFUSABLE_003:
    VISIBLE_FORM: 𝖾
    CODEPOINT: U+1D5BE
    NAME: MATHEMATICAL SANS-SERIF SMALL E
    RISK: MEDIUM
    RULE: MATH_SANS_E ≠ CYRILLIC_IE (a math-alphanumeric styled Latin e used to dodge simple filters)
  CONFUSABLE_004:
    VISIBLE_FORM: é
    CODEPOINT: U+00E9
    NAME: LATIN SMALL LETTER E WITH ACUTE
    RISK: LOW
    RULE: LATIN_E_ACUTE ≠ CYRILLIC_IE (an accented Latin twin)
  CONFUSABLE_005:
    VISIBLE_FORM: ｅ
    CODEPOINT: U+FF45
    NAME: FULLWIDTH LATIN SMALL LETTER E
    RISK: LOW
    RULE: FULLWIDTH_E ≠ CYRILLIC_IE (a full-width Latin e; a different compatibility form)
  CONFUSABLE_006:
    VISIBLE_FORM: ẹ
    CODEPOINT: U+1EB9
    NAME: LATIN SMALL LETTER E WITH DOT BELOW
    RISK: LOW
    RULE: LATIN_E_DOT_BELOW ≠ CYRILLIC_IE (a decorated Latin twin)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "the domain `googlе.com` is Google"
    RESPONSE: CYRILLIC_IE_FORM ≠ LATIN_E
    RULE: the last char is Cyrillic; the registrable domain is different — DNS decides, not the eye
  CG2:
    TRIGGER: "a string with Cyrillic е equals its Latin spelling"
    RESPONSE: CYRILLIC_IE_FORM ≠ SAME_CODEPOINT_AS_LATIN
    RULE: different codepoints → machine-different strings
  CG3:
    TRIGGER: "any Cyrillic е in text is an attack"
    RESPONSE: CYRILLIC_IE_FORM ≠ AUTOMATICALLY_SPOOF
    RULE: in single-script Russian text the letter is legit; the spoof is a MIX of scripts in one token
  CG4:
    TRIGGER: "an ASCII filter will catch the substituted word"
    RESPONSE: CYRILLIC_IE_FORM ≠ ASCII_LETTER
    RULE: Cyrillic е is outside ASCII; a Latin filter will not match it
  CG5:
    TRIGGER: "the handle `@hеlpdesk` is the same account as @helpdesk"
    RESPONSE: CYRILLIC_IE_FORM ≠ VERIFICATION
    RULE: visual similarity does not identify an account
  CG6:
    TRIGGER: "swapping e→е in an identifier is harmless"
    RESPONSE: CYRILLIC_IE_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
    RULE: in a domain/login/token the swap changes the entity the string resolves to

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "googlе" (Cyrillic е + Latin in one token)
      NAME: MIXED_SCRIPT_TOKEN
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: IDN/brand spoof; the key signal is a SCRIPT MIX within one token
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "еxprеss" (several Cyrillic among Latin)
      NAME: MULTI_HOMOGLYPH_TOKEN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: multiple substitution onto a target brand
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — the sign's danger appears precisely in a sequence (a token), not in isolation.

PHAGO_ENTITY_MIMICRY:
  PE_001:
    INPUT: "googlе.com"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: CRITICAL
    NOTE: Cyrillic е mimics the NAME itself of a verified brand (not merely structure) — direct mimicry of an entity's existence. This is why the registry flags the sign PHAGO ●; commercial lookalike defenses often miss this class.
  PE_002:
    INPUT: "@amazоn_hеlp"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: HIGH
    NOTE: impersonating an official brand account via a look-alike in the name.

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of Latin e (U+0065) with Cyrillic е (U+0435) in a brand domain
  A2: mixing Cyrillic е with math sans-serif e / accented Latin é to complicate detection
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: Cyrillic е bypasses a Latin-keyword blocklist (frее-money)
  B2: Cyrillic е in a mail domain (service@securе-pay.example) for phishing
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: the mixed token `googlе` (SC1) — scripts within one word
  C2: multiple substitution `еxprеss` (SC2) onto a target brand
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: the handle `@hеlpdesk` imitates a service account
  D2: "sеcure-official" — a look-alike in a pseudo-official name
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: `googlе.com` — mimicry of a brand name (PE_001)
  E2: `@amazоn_hеlp` — mimicry of an official account (PE_002)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the letter has no dormant/active epochs (see section 5).
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: `googlе.com` with Cyrillic е is Google's domain
  EXPECTED: FAIL_BRAND_NAME_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: a string with Cyrillic е is machine-equal to its Latin spelling
  EXPECTED: FAIL_CODEPOINT_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: any Cyrillic е in text is an attack
  EXPECTED: FAIL_OVERBLOCK_MIMICRY (the inverse error: genuine Russian is not a spoof)
  RESULT: FAIL
MUTATION_04:
  CLAIM: an ASCII filter on "free" will catch "frее"
  EXPECTED: FAIL_ASCII_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: the handle `@hеlpdesk` is the same account as `@helpdesk`
  EXPECTED: FAIL_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: swapping e→е in an identifier is harmless
  EXPECTED: FAIL_IDENTIFIER_INTERCHANGE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to distinguish legit single-script Russian text from a spoof without false positives?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (the "script mix within one token" rule is an integrator concern; see the Vakhter prototype confusable_cards.py)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the LOOKS_SAME ≠ IS_SAME formula and the "spoof = mix, not presence" rule.
OQ2:
  QUESTION: is the full UTS #39 confusables table + a brand corpus needed for the whole-script case?
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
