PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_GREEK_OMICRON_U03BF_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_GREEK_OMICRON_U03BF_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. Homoglyph sign: core law is LOOKS_SAME ≠ IS_SAME. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_GREEK_OMICRON_U03BF_GEN3_v0_3_EN
CODEPOINT: U+03BF
VISIBLE_FORM: ο
UNICODE_NAME: GREEK SMALL LETTER OMICRON
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: Greek "omicron" (homoglyph of Latin o)
CATEGORY_ROADMAP: PH (homoglyph of 'o') · PHAGO: ● (strong carrier — mimics the brand name itself)

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
VISIBLE_FORM: ο
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_LETTER_HOMOGLYPH
BASE_MODE_FORMULA: OMICRON_FORM ≠ LATIN_O
SIGN_CATEGORY:
  - Greek letter (legitimate in Greek text)
  - homoglyph of Latin small "o" (U+006F)
  - potential carrier of homoglyph / IDN spoofing when scripts are mixed

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_LATIN_O — Greek ο (U+03BF) is NOT Latin o (U+006F); a different codepoint
  2. NOT_SAME_STRING_AS_LATIN — a string with ο is not machine-equal to its Latin twin
  3. NOT_BRAND_NAME_PROOF — "gοogle" does not prove a link to the Google brand
  4. NOT_DOMAIN_VALIDITY_PROOF — a visual domain match does not confirm the registrable domain
  5. NOT_AUTHORITY — the letter does not confirm official status
  6. NOT_VERIFICATION — it does not verify an adjacent fact
  7. NOT_ASCII — outside ASCII; "ASCII-only" filters do not see it as o
  8. NOT_AUTOMATICALLY_SPOOF — in single-script Greek text it is normal, not an attack
  9. NOT_EXECUTION_TRIGGER — by itself it launches nothing
  10. NOT_TRUST_SIGNAL — it does not increase trust
  11. NOT_INTERCHANGEABLE_IN_IDENTIFIERS — in an identifier, o→ο changes the entity

BASE_FORMULAS:
  OMICRON_FORM ≠ LATIN_O
  OMICRON_FORM ≠ SAME_CODEPOINT_AS_LATIN
  OMICRON_FORM ≠ BRAND_NAME_PROOF
  OMICRON_FORM ≠ DOMAIN_VALIDITY_PROOF
  OMICRON_FORM ≠ AUTHORITY
  OMICRON_FORM ≠ VERIFICATION
  OMICRON_FORM ≠ ASCII_LETTER
  OMICRON_FORM ≠ AUTOMATICALLY_SPOOF
  OMICRON_FORM ≠ TRUST_SIGNAL
  OMICRON_FORM ≠ EFFECT
  OMICRON_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: Greek "omicron" is a stable letter with no cultural precession. "Homoglyph" is a property of visual coincidence with Latin o, co-existing with the letter's legit function. The danger is contextual (mixed scripts), not epochal.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a letter is a written sign with no gestural predecessor; the Greek alphabet descends from Phoenician (written genealogy).

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
    INPUT: "λόγος" (logos)
    CONTEXT: a Greek word (single script)
    EXPECTED: INFO
    RISK: NONE
    GUARD: OMICRON_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_002:
    INPUT: "ο κόσμος" (the world)
    CONTEXT: a Greek phrase
    EXPECTED: INFO
    RISK: NONE
    GUARD: OMICRON_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "φιλοσοφία" (philosophy)
    CONTEXT: a Greek word
    EXPECTED: INFO
    RISK: NONE
    GUARD: OMICRON_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_004:
    INPUT: "Αθήνα, ο άνθρωπος"
    CONTEXT: single-script Greek text
    EXPECTED: INFO
    RISK: NONE
    GUARD: OMICRON_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_005:
    INPUT: "χρόνος" (time)
    CONTEXT: a Greek word
    EXPECTED: INFO
    RISK: NONE
    GUARD: OMICRON_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "Καλημέρα κόσμε"
    CONTEXT: a greeting in Greek
    EXPECTED: INFO
    RISK: NONE
    GUARD: OMICRON_FORM ≠ AUTOMATICALLY_SPOOF

RISK_CASES:
  RISK_CASE_001:
    NAME: MIXED_SCRIPT_BRAND_SPOOF
    INPUT: "gοogle.com" (Greek ο among Latin)
    CONTEXT: IDN/brand spoof — the token looks like google.com
    RISK: CRITICAL
    ATTACK: replacing Latin o with Greek ο yields a visually identical domain the attacker registers
    GUARD: OMICRON_FORM ≠ LATIN_O
  RISK_CASE_002:
    NAME: MICROSOFT_HOMOGLYPH
    INPUT: "micrοsοft.com" (two Greek ο)
    CONTEXT: multiple substitution in a brand
    RISK: CRITICAL
    ATTACK: the string is machine-≠ microsoft.com, but a human sees no difference
    GUARD: OMICRON_FORM ≠ DOMAIN_VALIDITY_PROOF
  RISK_CASE_003:
    NAME: HANDLE_IMPERSONATION
    INPUT: "@rοot" (Greek ο in a handle)
    CONTEXT: impersonating a root/rooot account
    RISK: HIGH
    ATTACK: the look-alike handle appears as "root" but is a different account
    GUARD: OMICRON_FORM ≠ VERIFICATION
  RISK_CASE_004:
    NAME: FILTER_BYPASS_KEYWORD
    INPUT: "prοmo" (Greek ο bypasses a "promo" blocklist)
    CONTEXT: bypassing a text filter
    RISK: HIGH
    ATTACK: one substituted letter moves the word out from under the blocklist
    GUARD: OMICRON_FORM ≠ ASCII_LETTER
  RISK_CASE_005:
    NAME: EMAIL_LOOKALIKE
    INPUT: "billing@shοp.example" (Greek ο in the mail domain)
    CONTEXT: a phishing email from the "same" shop
    RISK: HIGH
    ATTACK: the domain looks identical but leads to the attacker
    GUARD: OMICRON_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
  RISK_CASE_006:
    NAME: MULTI_HOMOGLYPH_MIX
    INPUT: "gοοgle" (Greek ο + Latin + possibly Cyrillic о)
    CONTEXT: mixing look-alike sources complicates detection
    RISK: HIGH
    ATTACK: one target imitated by letters from different scripts
    GUARD: OMICRON_FORM ≠ BRAND_NAME_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: o
    CODEPOINT: U+006F
    NAME: LATIN SMALL LETTER O
    RISK: CRITICAL
    RULE: LATIN_O ≠ OMICRON (the primary impersonation target; visually identical)
  CONFUSABLE_002:
    VISIBLE_FORM: о
    CODEPOINT: U+043E
    NAME: CYRILLIC SMALL LETTER O
    RISK: CRITICAL
    RULE: CYRILLIC_O ≠ OMICRON (a third twin of the same shape)
  CONFUSABLE_003:
    VISIBLE_FORM: 0
    CODEPOINT: U+0030
    NAME: DIGIT ZERO
    RISK: MEDIUM
    RULE: DIGIT_ZERO ≠ OMICRON (close in some fonts)
  CONFUSABLE_004:
    VISIBLE_FORM: σ
    CODEPOINT: U+03C3
    NAME: GREEK SMALL LETTER SIGMA
    RISK: LOW
    RULE: GREEK_SIGMA ≠ OMICRON (a neighboring Greek letter, different)
  CONFUSABLE_005:
    VISIBLE_FORM: ᴏ
    CODEPOINT: U+1D0F
    NAME: LATIN LETTER SMALL CAPITAL O
    RISK: LOW
    RULE: SMALL_CAPITAL_O ≠ OMICRON

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "the domain `gοogle.com` is Google"
    RESPONSE: OMICRON_FORM ≠ LATIN_O
    RULE: the letter is Greek; the registrable domain is different — DNS decides, not the eye
  CG2:
    TRIGGER: "a string with Greek ο equals its Latin spelling"
    RESPONSE: OMICRON_FORM ≠ SAME_CODEPOINT_AS_LATIN
    RULE: different codepoints → machine-different strings
  CG3:
    TRIGGER: "any Greek ο in text is an attack"
    RESPONSE: OMICRON_FORM ≠ AUTOMATICALLY_SPOOF
    RULE: in single-script Greek text the letter is legit; the spoof is a MIX of scripts in one token
  CG4:
    TRIGGER: "an ASCII filter will catch the substituted word"
    RESPONSE: OMICRON_FORM ≠ ASCII_LETTER
    RULE: Greek ο is outside ASCII; a Latin filter will not match it
  CG5:
    TRIGGER: "the handle `@rοot` is the same account as @root"
    RESPONSE: OMICRON_FORM ≠ VERIFICATION
    RULE: visual similarity does not identify an account
  CG6:
    TRIGGER: "swapping o→ο in an identifier is harmless"
    RESPONSE: OMICRON_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
    RULE: in a domain/login the swap changes the entity the string resolves to

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "gοogle" (Greek ο + Latin in one token)
      NAME: MIXED_SCRIPT_TOKEN
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: IDN/brand spoof; the key signal is a SCRIPT MIX within one token
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "micrοsοft" (several Greek among Latin)
      NAME: MULTI_HOMOGLYPH_TOKEN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: multiple substitution onto a target brand
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — the sign's danger appears in a sequence (a token), not in isolation.

PHAGO_ENTITY_MIMICRY:
  PE_001:
    INPUT: "gοogle.com"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: CRITICAL
    NOTE: Greek ο mimics the NAME itself of a verified brand — direct mimicry of an entity's existence. The registry flags the sign PHAGO ●; commercial defenses often miss this class.
  PE_002:
    INPUT: "@micrοsοft_help"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: HIGH
    NOTE: impersonating an official brand account via a look-alike in the name.

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of Latin o (U+006F) with Greek ο (U+03BF) in a brand domain
  A2: mixing Greek ο with Cyrillic о (U+043E) to complicate detection
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: Greek ο bypasses a Latin-keyword blocklist (prοmo)
  B2: Greek ο in a mail domain (billing@shοp.example)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: the mixed token `gοogle` (SC1)
  C2: multiple substitution `micrοsοft` (SC2)
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: the handle `@rοot` imitates a service account
  D2: "prοmο-official" — a look-alike in a pseudo-official name
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: `gοogle.com` — mimicry of a brand name (PE_001)
  E2: `@micrοsοft_help` — mimicry of an official account (PE_002)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the letter has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: `gοogle.com` with Greek ο is Google's domain
  EXPECTED: FAIL_BRAND_NAME_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: a string with Greek ο is machine-equal to its Latin spelling
  EXPECTED: FAIL_CODEPOINT_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: any Greek ο in text is an attack
  EXPECTED: FAIL_OVERBLOCK_MIMICRY (the inverse error: genuine Greek is not a spoof)
  RESULT: FAIL
MUTATION_04:
  CLAIM: an ASCII filter on "promo" will catch "prοmo"
  EXPECTED: FAIL_ASCII_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: the handle `@rοot` is the same account as `@root`
  EXPECTED: FAIL_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: swapping o→ο in an identifier is harmless
  EXPECTED: FAIL_IDENTIFIER_INTERCHANGE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to distinguish legit single-script Greek text from a spoof without false positives?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (the "script mix within one token" rule is an integrator concern; see the Vakhter prototype confusable_cards.py)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the LOOKS_SAME ≠ IS_SAME formula and the "spoof = mix, not presence" rule.
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
