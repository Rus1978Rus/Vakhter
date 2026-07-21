PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_NUMBER_SIGN_U0023_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_NUMBER_SIGN_U0023_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_NUMBER_SIGN_U0023_GEN3_v0_3_EN
CODEPOINT: U+0023
VISIBLE_FORM: #
UNICODE_NAME: NUMBER SIGN
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: number sign (hash)
CATEGORY_ROADMAP: PH (fragment hiding, URL truncation) · PHAGO: — (structure masking)

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
VISIBLE_FORM: #
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_SEPARATOR
BASE_MODE_FORMULA: NUMBER_SIGN_FORM ≠ EFFECT
SIGN_CATEGORY:
  - URL fragment separator (#section, #/route)
  - social hashtag (#news)
  - CSS id (#id) / number (#5)
  - comment (shell/python/yaml: # ...)
  - preprocessor directive (#include) / Markdown heading (# Title)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_FRAGMENT_SAFE — a "#" fragment does not make what follows it safe
  2. NOT_SERVER_VISIBLE — the part after "#" is not sent to the server (client only)
  3. NOT_URL_END — "#" does not mark the end of a URL; a fragment follows it
  4. NOT_COMMENT_SAFE — "#" as a comment does not guarantee the line is safe
  5. NOT_AUTHORITY — "#" does not confirm officialness
  6. NOT_EXECUTION_TRIGGER — by itself it executes nothing
  7. NOT_TRUST_SIGNAL — it does not increase trust
  8. NOT_HASHTAG_VALIDITY — "#tag" does not confirm the topic exists/is official
  9. NOT_ID_UNIQUENESS — "#id" does not guarantee uniqueness on a page
  10. NOT_ROUTE_SAFE — "#/admin" (SPA route) is not safe just because a "#" is present
  11. NOT_TRUNCATION_SAFE — "#" can visually truncate perception of a URL

BASE_FORMULAS:
  NUMBER_SIGN_FORM ≠ EFFECT
  NUMBER_SIGN_FORM ≠ FRAGMENT_SAFETY_PROOF
  NUMBER_SIGN_FORM ≠ SERVER_VISIBILITY_PROOF
  NUMBER_SIGN_FORM ≠ URL_END_MARKER_PROOF
  NUMBER_SIGN_FORM ≠ COMMENT_SAFETY_PROOF
  NUMBER_SIGN_FORM ≠ AUTHORITY
  NUMBER_SIGN_FORM ≠ TRUST_SIGNAL
  NUMBER_SIGN_FORM ≠ HASHTAG_VALIDITY_PROOF
  NUMBER_SIGN_FORM ≠ ID_UNIQUENESS_PROOF
  NUMBER_SIGN_FORM ≠ ROUTE_SAFETY_PROOF
  NUMBER_SIGN_FORM ≠ TRUNCATION_SAFETY_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "#" (ZONE_1) has parallel functions (fragment, hashtag, id, number, comment, heading) co-existing without cultural precession. Polysemy of a stable sign.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a written sign with no gestural predecessor; the URL/hashtag functions are layered on by the digital epoch in parallel.

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
    INPUT: "#news"
    CONTEXT: hashtag
    EXPECTED: INFO
    RISK: NONE
    GUARD: NUMBER_SIGN_FORM ≠ HASHTAG_VALIDITY_PROOF
  SAFE_CASE_002:
    INPUT: "issue #42"
    CONTEXT: item number
    EXPECTED: INFO
    RISK: NONE
    GUARD: NUMBER_SIGN_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "#include <stdio.h>"
    CONTEXT: C preprocessor directive
    EXPECTED: INFO
    RISK: NONE
    GUARD: NUMBER_SIGN_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "# Heading"
    CONTEXT: Markdown heading
    EXPECTED: INFO
    RISK: NONE
    GUARD: NUMBER_SIGN_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "count = 5  # comment"
    CONTEXT: Python/shell comment
    EXPECTED: INFO
    RISK: NONE
    GUARD: NUMBER_SIGN_FORM ≠ COMMENT_SAFETY_PROOF
  SAFE_CASE_006:
    INPUT: "https://site.com/doc#section-3"
    CONTEXT: legitimate anchor fragment
    EXPECTED: INFO
    RISK: NONE
    GUARD: NUMBER_SIGN_FORM ≠ FRAGMENT_SAFETY_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: FRAGMENT_HIDES_REAL_TARGET
    INPUT: "https://good.com/login#@evil.com"
    CONTEXT: the fragment masks perception of the real host
    RISK: HIGH
    ATTACK: everything after "#" is the (client) fragment; "@evil.com" in it creates an illusion/confusion about the target
    GUARD: NUMBER_SIGN_FORM ≠ SERVER_VISIBILITY_PROOF
  RISK_CASE_002:
    NAME: URL_TRUNCATION_TRICK
    INPUT: "https://evil.com#good.com/verify"
    CONTEXT: the real host is evil.com, "good.com" only in the fragment
    RISK: HIGH
    ATTACK: the eye reads "good.com", but the request goes to evil.com; the fragment is not sent
    GUARD: NUMBER_SIGN_FORM ≠ TRUNCATION_SAFETY_PROOF
  RISK_CASE_003:
    NAME: COMMENT_INJECTION
    INPUT: "value # rm -rf /"
    CONTEXT: "#" moves the rest of the line into a comment (or reveals it)
    RISK: MEDIUM
    ATTACK: injecting "#" changes what the interpreter treats as code vs comment
    GUARD: NUMBER_SIGN_FORM ≠ COMMENT_SAFETY_PROOF
  RISK_CASE_004:
    NAME: SPA_ROUTE_BYPASS
    INPUT: "https://app.com/#/admin/users"
    CONTEXT: a client route after "#" bypassing a server check
    RISK: MEDIUM
    ATTACK: "#/admin" is client navigation; authorization must be server-side, not by "#"
    GUARD: NUMBER_SIGN_FORM ≠ ROUTE_SAFETY_PROOF
  RISK_CASE_005:
    NAME: HASHBANG_UPLOAD
    INPUT: "#!/bin/sh" (at the start of an uploaded file)
    CONTEXT: the shebang makes the uploaded file an executable script
    RISK: HIGH
    ATTACK: "#!" at the file start + an executable bit → execution of an arbitrary script
    GUARD: NUMBER_SIGN_FORM ≠ EXECUTION_TRIGGER
  RISK_CASE_006:
    NAME: FULLWIDTH_HASH_BYPASS
    INPUT: "＃/admin" (fullwidth ＃ U+FF03)
    CONTEXT: a hash look-alike to bypass a fragment/route filter
    RISK: LOW
    ATTACK: a filter looks for ASCII "#", a normalizer may fold ＃ to "#"
    GUARD: NUMBER_SIGN_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ＃
    CODEPOINT: U+FF03
    NAME: FULLWIDTH NUMBER SIGN
    RISK: MEDIUM
    RULE: FULLWIDTH_NUMBER_SIGN ≠ NUMBER_SIGN (bypasses a filter looking for ASCII "#")
  CONFUSABLE_002:
    VISIBLE_FORM: ♯
    CODEPOINT: U+266F
    NAME: MUSIC SHARP SIGN
    RISK: LOW
    RULE: MUSIC_SHARP_SIGN ≠ NUMBER_SIGN
  CONFUSABLE_003:
    VISIBLE_FORM: ﹟
    CODEPOINT: U+FE5F
    NAME: SMALL NUMBER SIGN
    RISK: LOW
    RULE: SMALL_NUMBER_SIGN ≠ NUMBER_SIGN
  CONFUSABLE_004:
    VISIBLE_FORM: ⌗
    CODEPOINT: U+2317
    NAME: VIEWDATA SQUARE
    RISK: LOW
    RULE: VIEWDATA_SQUARE ≠ NUMBER_SIGN
  CONFUSABLE_005:
    VISIBLE_FORM: №
    CODEPOINT: U+2116
    NAME: NUMERO SIGN
    RISK: LOW
    RULE: NUMERO_SIGN ≠ NUMBER_SIGN (a different "number" sign, not ASCII "#")

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "what follows '#' is safe, since it is only a fragment"
    RESPONSE: NUMBER_SIGN_FORM ≠ FRAGMENT_SAFETY_PROOF
    RULE: the fragment drives the client (route/scroll/DOM); not automatically safe
  CG2:
    TRIGGER: "'good.com' in the URL means the request goes to good.com"
    RESPONSE: NUMBER_SIGN_FORM ≠ SERVER_VISIBILITY_PROOF
    RULE: the part after "#" is not sent; the real host is before "#"
  CG3:
    TRIGGER: "'#' marks the end of a URL"
    RESPONSE: NUMBER_SIGN_FORM ≠ URL_END_MARKER_PROOF
    RULE: a fragment follows "#" — it is part of the URL, not the end
  CG4:
    TRIGGER: "'#/admin' is safe since it is a client route"
    RESPONSE: NUMBER_SIGN_FORM ≠ ROUTE_SAFETY_PROOF
    RULE: authorization must be server-side; a client route does not replace it
  CG5:
    TRIGGER: "'#' at the start of a file is just a comment"
    RESPONSE: NUMBER_SIGN_FORM ≠ EXECUTION_TRIGGER
    RULE: "#!" (shebang) + an executable bit makes the file a script
  CG6:
    TRIGGER: "an ASCII '#' filter catches all hashes"
    RESPONSE: NUMBER_SIGN_FORM ≠ EFFECT
    RULE: fullwidth ＃ (U+FF03) is a different codepoint

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "#@host" (fragment with @)
      NAME: FRAGMENT_USERINFO_CONFUSION
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: confusion about the URL target (together with @); the fragment masks perception
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "#!"
      NAME: SHEBANG_OR_HASHBANG
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: shebang of an executable file; hashbang route in old SPAs
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "#/route"
      NAME: CLIENT_ROUTE
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: SPA navigation; bypass when trusting a client route
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with "#" are central to URL/execution.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "#" masks URL/code STRUCTURE (fragment, comment, route) but does not imitate the existence of a verified entity. Its risks are obfuscation/logic, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of ASCII "#" with fullwidth ＃ (U+FF03) to bypass a fragment filter
  A2: mixing "#" with ♯ (U+266F) in a filter
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: comment injection "value # rm -rf /"
  B2: shebang "#!/bin/sh" at the start of an uploaded file
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: fragment "#@evil.com" (SC1) — confusion about the URL target
  C2: client route "#/admin" (SC3) bypassing a server check
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: URL truncation "evil.com#good.com" — the eye reads good.com
  D2: "#verified" as a pseudo-status (trust inflation by hashtag)
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: the fragment masks the real host
  E2: N/A — vector: comment injection into a config/script
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: what follows "#" is safe (only a fragment)
  EXPECTED: FAIL_FRAGMENT_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: "good.com" in the URL means the request goes to good.com
  EXPECTED: FAIL_SERVER_VISIBILITY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: "#" marks the end of a URL
  EXPECTED: FAIL_URL_END_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: a client route "#/admin" is safe in itself
  EXPECTED: FAIL_ROUTE_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: "#" at the start of a file is always a harmless comment
  EXPECTED: FAIL_SHEBANG_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: an ASCII "#" filter catches all variants of the sign
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to treat the fragment in URL-security context (client vs server)?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (parsing the real host before "#" + a client-route policy is an integrator concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "the real host is before '#'; the fragment is not sent to the server".
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
