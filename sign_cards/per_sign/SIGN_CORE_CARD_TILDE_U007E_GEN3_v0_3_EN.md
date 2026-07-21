PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_TILDE_U007E_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_TILDE_U007E_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_TILDE_U007E_GEN3_v0_3_EN
CODEPOINT: U+007E
VISIBLE_FORM: ~
UNICODE_NAME: TILDE
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: tilde
CATEGORY_ROADMAP: PH (home-dir paths, tilde expansion) · PHAGO: — (structure masking)

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
VISIBLE_FORM: ~
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_MARKER
BASE_MODE_FORMULA: TILDE_FORM ≠ EFFECT
SIGN_CATEGORY:
  - home-directory marker (~/, ~user) in shell/URL
  - "approximately" sign (~5 minutes)
  - bitwise NOT in programming languages (~x)
  - backup/temp-file marker (file~)
  - tilde expansion in the shell
WHAT_THIS_SIGN_IS_NOT:
  1. NOT_HOME_PATH_SAFE — "~/…" does not guarantee a safe path (traversal is possible)
  2. NOT_USER_ENUM_SAFE — "~user" can reveal user existence
  3. NOT_APPROX_PROOF — "~5" does not confirm the approximate value is correct
  4. NOT_BACKUP_HIDDEN — "file~" (an editor backup) can disclose the source
  5. NOT_AUTHORITY — "~" does not confirm officialness
  6. NOT_EXECUTION_TRIGGER — by itself it executes nothing
  7. NOT_TRUST_SIGNAL — it does not increase trust
  8. NOT_EXPANSION_SAFE — "~" in the shell expands to a path (not a literal)
  9. NOT_PATH_END — "~" does not mark the end of a path
  10. NOT_BITWISE_SAFE — "~x" changes the value (bitwise NOT)
  11. NOT_TILDE_LITERAL — "~" is not always a literal char (the shell expands it)

BASE_FORMULAS:
  TILDE_FORM ≠ EFFECT
  TILDE_FORM ≠ HOME_PATH_SAFETY_PROOF
  TILDE_FORM ≠ USER_ENUMERATION_SAFETY_PROOF
  TILDE_FORM ≠ APPROX_VALIDITY_PROOF
  TILDE_FORM ≠ BACKUP_CONCEALMENT_PROOF
  TILDE_FORM ≠ AUTHORITY
  TILDE_FORM ≠ TRUST_SIGNAL
  TILDE_FORM ≠ EXPANSION_SAFETY_PROOF
  TILDE_FORM ≠ PATH_END_PROOF
  TILDE_FORM ≠ BITWISE_SAFETY_PROOF
  TILDE_FORM ≠ TILDE_LITERAL_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "~" (ZONE_1) has parallel functions (home dir, approximately, bitwise NOT, backup marker) co-existing without cultural precession. Polysemy of a stable sign.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a written/diacritic sign with no gestural predecessor; the path/expansion functions are layered on by the digital epoch in parallel.

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
    INPUT: "about ~5 minutes"
    CONTEXT: "approximately" sign
    EXPECTED: INFO
    RISK: NONE
    GUARD: TILDE_FORM ≠ APPROX_VALIDITY_PROOF
  SAFE_CASE_002:
    INPUT: "cd ~/documents"
    CONTEXT: the user's home directory
    EXPECTED: INFO
    RISK: NONE
    GUARD: TILDE_FORM ≠ HOME_PATH_SAFETY_PROOF
  SAFE_CASE_003:
    INPUT: "mask = ~x"
    CONTEXT: bitwise NOT
    EXPECTED: INFO
    RISK: NONE
    GUARD: TILDE_FORM ≠ BITWISE_SAFETY_PROOF
  SAFE_CASE_004:
    INPUT: "range 3 ~ 4"
    CONTEXT: an approximate range (stylistic)
    EXPECTED: INFO
    RISK: NONE
    GUARD: TILDE_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "a swung dash ~ in text"
    CONTEXT: a typographic mark
    EXPECTED: INFO
    RISK: NONE
    GUARD: TILDE_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "config.txt~ (editor backup)"
    CONTEXT: a local temp file (in a trusted environment)
    EXPECTED: INFO
    RISK: NONE
    GUARD: TILDE_FORM ≠ BACKUP_CONCEALMENT_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: HOME_PATH_TRAVERSAL
    INPUT: "~/../../etc/passwd"
    CONTEXT: "~" expands to the home path + traversal upward
    RISK: HIGH
    ATTACK: "~" expands to the home directory, "../../" climbs out of it
    GUARD: TILDE_FORM ≠ HOME_PATH_SAFETY_PROOF
  RISK_CASE_002:
    NAME: USER_ENUMERATION
    INPUT: "https://site.com/~admin/"
    CONTEXT: mod_userdir reveals a user's existence
    RISK: MEDIUM
    ATTACK: different responses for "~admin" vs "~nouser" enumerate users
    GUARD: TILDE_FORM ≠ USER_ENUMERATION_SAFETY_PROOF
  RISK_CASE_003:
    NAME: BACKUP_SOURCE_DISCLOSURE
    INPUT: "https://site.com/config.php~"
    CONTEXT: an editor backup file is served as text
    RISK: HIGH
    ATTACK: "config.php~" is not executed as PHP → the server returns the SOURCE (secret leak)
    GUARD: TILDE_FORM ≠ BACKUP_CONCEALMENT_PROOF
  RISK_CASE_004:
    NAME: UNSAFE_TILDE_EXPANSION
    INPUT: "rm ~/*"
    CONTEXT: "~" expansion in the shell under unsafe substitution
    RISK: HIGH
    ATTACK: "~" expands to the home path; unexpected deletion of contents
    GUARD: TILDE_FORM ≠ EXPANSION_SAFETY_PROOF
  RISK_CASE_005:
    NAME: ROOT_HOME_ACCESS
    INPUT: "/~root/.ssh/"
    CONTEXT: an attempt to reach root's home directory
    RISK: HIGH
    ATTACK: "~root" points to a private directory; an attempt to read keys
    GUARD: TILDE_FORM ≠ HOME_PATH_SAFETY_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_TILDE_BYPASS
    INPUT: "～/etc" (fullwidth ～ U+FF5E)
    CONTEXT: a tilde look-alike to bypass a path filter
    RISK: LOW
    ATTACK: a filter looks for ASCII "~", a normalizer may fold ～ to "~"
    GUARD: TILDE_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ～
    CODEPOINT: U+FF5E
    NAME: FULLWIDTH TILDE
    RISK: MEDIUM
    RULE: FULLWIDTH_TILDE ≠ TILDE (bypasses a filter looking for ASCII "~")
  CONFUSABLE_002:
    VISIBLE_FORM: ∼
    CODEPOINT: U+223C
    NAME: TILDE OPERATOR
    RISK: LOW
    RULE: TILDE_OPERATOR ≠ TILDE (mathematical operator)
  CONFUSABLE_003:
    VISIBLE_FORM: ⁓
    CODEPOINT: U+2053
    NAME: SWUNG DASH
    RISK: LOW
    RULE: SWUNG_DASH ≠ TILDE
  CONFUSABLE_004:
    VISIBLE_FORM: ˜
    CODEPOINT: U+02DC
    NAME: SMALL TILDE
    RISK: LOW
    RULE: SMALL_TILDE ≠ TILDE
  CONFUSABLE_005:
    VISIBLE_FORM: 〜
    CODEPOINT: U+301C
    NAME: WAVE DASH
    RISK: LOW
    RULE: WAVE_DASH ≠ TILDE

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "'~/…' always stays inside the home directory"
    RESPONSE: TILDE_FORM ≠ HOME_PATH_SAFETY_PROOF
    RULE: "../" after "~" climbs out of home; normalize the path after expansion
  CG2:
    TRIGGER: "'~admin' is a harmless link"
    RESPONSE: TILDE_FORM ≠ USER_ENUMERATION_SAFETY_PROOF
    RULE: different responses for existing/non-existing "~user" enumerate accounts
  CG3:
    TRIGGER: "'file~' is just a name, the server will not serve it"
    RESPONSE: TILDE_FORM ≠ BACKUP_CONCEALMENT_PROOF
    RULE: a backup "*.php~" may be served as text → source disclosure
  CG4:
    TRIGGER: "'~' in a command is a literal char"
    RESPONSE: TILDE_FORM ≠ TILDE_LITERAL_PROOF
    RULE: the shell expands "~" to the home path; escape it for a literal meaning
  CG5:
    TRIGGER: "'~' marks the end of a path"
    RESPONSE: TILDE_FORM ≠ PATH_END_PROOF
    RULE: "~" is a prefix/marker, not the end of a path
  CG6:
    TRIGGER: "an ASCII '~' filter catches all tildes"
    RESPONSE: TILDE_FORM ≠ EFFECT
    RULE: fullwidth ～ (U+FF5E) is a different codepoint

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "~/.."
      NAME: HOME_TRAVERSAL
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: home expansion + upward traversal (access beyond home)
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "~user"
      NAME: USERDIR
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: mod_userdir / user enumeration
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "*~"
      NAME: BACKUP_SUFFIX
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: editor backup file → source disclosure
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with "~" are central to paths/files.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "~" masks path/file STRUCTURE (home directory, backup, expansion) but does not imitate the existence of a verified entity (brand/account). Its risks are path traversal/disclosure, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of ASCII "~" with fullwidth ～ (U+FF5E) to bypass a path filter
  A2: mixing "~" with ∼ (U+223C) in a filter
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: "~/../../etc/passwd" — traversal via home expansion
  B2: "rm ~/*" — unsafe tilde expansion in the shell
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "~/.." (SC1) — climbing beyond home
  C2: "*.php~" (SC3) — source disclosure via a backup
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "/~admin/" — user enumeration (mod_userdir)
  D2: "~5% guarantee" — pseudo-precision via the "approximately" sign
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: access to "~root/.ssh"
  E2: N/A — vector: backup disclosure with secrets (config~)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: "~/…" always stays inside the home directory
  EXPECTED: FAIL_HOME_PATH_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: "~admin" is a harmless link with no user disclosure
  EXPECTED: FAIL_USER_ENUMERATION_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: the server will never serve "file~" as text
  EXPECTED: FAIL_BACKUP_DISCLOSURE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "~" in a command is a literal char
  EXPECTED: FAIL_TILDE_EXPANSION_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: "~" marks the end of a path
  EXPECTED: FAIL_PATH_END_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: an ASCII "~" filter catches all variants of the sign
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to safely expand "~"/"~user" and normalize the path without traversal?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (normalize the path AFTER expansion + forbid "~user" outside an allowlist — an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "expanding '~' + '../' can climb out of home".
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
