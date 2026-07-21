PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_RIGHT_SQUARE_BRACKET_U005D_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_RIGHT_SQUARE_BRACKET_U005D_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_RIGHT_SQUARE_BRACKET_U005D_GEN3_v0_3_EN
CODEPOINT: U+005D
VISIBLE_FORM: ]
UNICODE_NAME: RIGHT SQUARE BRACKET
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: right square bracket / index & array close
CATEGORY_ROADMAP: INJ (param-array/nested-key close, regex class close) · PHAGO: — (nested-key close forgery)

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
VISIBLE_FORM: ]
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: RIGHT_SQUARE_BRACKET_FORM ≠ EFFECT
SIGN_CATEGORY:
  - array/index accessor closer (arr[i], obj[key])
  - JSON array closer ([1, 2, 3])
  - regex character-class closer ([a-z])
  - query-string nested-key closer (a[b]=1)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INDEX_ONLY — "]" is not always benign closing (it completes a nested key / array)
  2. NOT_ARRAY_SAFE — a "]" completes an injected nested key/array structure
  3. NOT_KEY_SCOPED — "]" finishes "[__proto__]"/"[role]" so the key takes effect
  4. NOT_ESCAPED_PROOF — the presence of "]" does not mean it is quoted/escaped
  5. NOT_ENCODED_SAFE — "%5D" may be decoded back to "]" later
  6. NOT_AUTHORITY — "]" does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; context makes it complete a key/array
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_REGEX_CLASS_SAFE — "]" closes a character class; a misplaced "]" changes what it matches
  10. NOT_SANITIZED_PROOF — the presence of "]" does not mean the input is sanitized
  11. NOT_OUTPUT_CONTEXT_PROOF — safety depends on the parse/binding context

BASE_FORMULAS:
  RIGHT_SQUARE_BRACKET_FORM ≠ EFFECT
  RIGHT_SQUARE_BRACKET_FORM ≠ INDEX_ONLY_PROOF
  RIGHT_SQUARE_BRACKET_FORM ≠ ARRAY_SAFETY_PROOF
  RIGHT_SQUARE_BRACKET_FORM ≠ KEY_SCOPE_PROOF
  RIGHT_SQUARE_BRACKET_FORM ≠ ESCAPED_PROOF
  RIGHT_SQUARE_BRACKET_FORM ≠ ENCODED_SAFETY_PROOF
  RIGHT_SQUARE_BRACKET_FORM ≠ AUTHORITY
  RIGHT_SQUARE_BRACKET_FORM ≠ EXECUTION_TRIGGER
  RIGHT_SQUARE_BRACKET_FORM ≠ REGEX_CLASS_SAFETY_PROOF
  RIGHT_SQUARE_BRACKET_FORM ≠ SANITIZED_PROOF
  RIGHT_SQUARE_BRACKET_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "]" (ZONE_1) has parallel functions (array/index close, JSON array close, regex class close, nested query key close) co-existing without cultural precession. Polysemy of a stable sign.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a punctuation/mathematical bracket with no gestural predecessor; the index/array/class functions are layered on by the digital epoch in parallel.

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
    INPUT: "arr[0] returns the first item"
    CONTEXT: array indexing shown as text
    EXPECTED: INFO
    RISK: NONE
    GUARD: RIGHT_SQUARE_BRACKET_FORM ≠ INDEX_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "JSON [1, 2, 3]"
    CONTEXT: a well-formed JSON array shown as text
    EXPECTED: INFO
    RISK: NONE
    GUARD: RIGHT_SQUARE_BRACKET_FORM ≠ ARRAY_SAFETY_PROOF
  SAFE_CASE_003:
    INPUT: "regex [a-z]+ matches letters"
    CONTEXT: describing a regex character class
    EXPECTED: INFO
    RISK: NONE
    GUARD: RIGHT_SQUARE_BRACKET_FORM ≠ REGEX_CLASS_SAFETY_PROOF
  SAFE_CASE_004:
    INPUT: "see reference [12] in the bibliography"
    CONTEXT: a citation number in brackets
    EXPECTED: INFO
    RISK: NONE
    GUARD: RIGHT_SQUARE_BRACKET_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "the ] key on a keyboard"
    CONTEXT: naming the bracket key in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: RIGHT_SQUARE_BRACKET_FORM ≠ INDEX_ONLY_PROOF
  SAFE_CASE_006:
    INPUT: "[INFO] log line prefix"
    CONTEXT: a bracketed log-level tag
    EXPECTED: INFO
    RISK: NONE
    GUARD: RIGHT_SQUARE_BRACKET_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: PROTOTYPE_POLLUTION_CLOSE
    INPUT: "obj[__proto__][isAdmin]=true"
    CONTEXT: "]" completing a nested key that reaches the prototype
    RISK: CRITICAL
    ATTACK: "]" finalizes "[__proto__]" so Object.prototype is polluted
    GUARD: RIGHT_SQUARE_BRACKET_FORM ≠ KEY_SCOPE_PROOF
  RISK_CASE_002:
    NAME: MASS_ASSIGN_CLOSE
    INPUT: "user[role]=admin"
    CONTEXT: "]" completing a nested parameter bound to a model
    RISK: HIGH
    ATTACK: "]" finishes "user[role]" so the privileged field is mass-assigned
    GUARD: RIGHT_SQUARE_BRACKET_FORM ≠ ARRAY_SAFETY_PROOF
  RISK_CASE_003:
    NAME: ARRAY_TYPE_CLOSE
    INPUT: "id[]=1 (completing an array where a scalar is expected)"
    CONTEXT: "]" completing an array parameter
    RISK: MEDIUM
    ATTACK: "]" finalizes "id[]" so the value is an array (type confusion)
    GUARD: RIGHT_SQUARE_BRACKET_FORM ≠ EFFECT
  RISK_CASE_004:
    NAME: REGEX_CLASS_CLOSE_SHIFT
    INPUT: "[a-z]] (a stray ] shifting the class boundary)"
    CONTEXT: a misplaced "]" changing where the character class ends
    RISK: MEDIUM
    ATTACK: an early/late "]" alters the class so it matches unintended characters
    GUARD: RIGHT_SQUARE_BRACKET_FORM ≠ REGEX_CLASS_SAFETY_PROOF
  RISK_CASE_005:
    NAME: ENCODED_BRACKET_BYPASS
    INPUT: "obj%5B__proto__%5D (with a later decode)"
    CONTEXT: an encoded "]" decoded back before the binder
    RISK: HIGH
    ATTACK: %5D decodes to "]" AFTER the check → completes nested-key binding
    GUARD: RIGHT_SQUARE_BRACKET_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_BRACKET_BYPASS
    INPUT: "obj［key］ (fullwidth ］ U+FF3D)"
    CONTEXT: a look-alike to bypass a "]" filter
    RISK: MEDIUM
    ATTACK: a filter looks for ASCII "]", a normalizer may fold ］ to "]"
    GUARD: RIGHT_SQUARE_BRACKET_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ］
    CODEPOINT: U+FF3D
    NAME: FULLWIDTH RIGHT SQUARE BRACKET
    RISK: HIGH
    RULE: FULLWIDTH_RIGHT_SQUARE_BRACKET ≠ RIGHT_SQUARE_BRACKET (bypasses a filter looking for ASCII "]")
  CONFUSABLE_002:
    VISIBLE_FORM: ﹈
    CODEPOINT: U+FE48
    NAME: PRESENTATION FORM FOR VERTICAL RIGHT SQUARE BRACKET
    RISK: MEDIUM
    RULE: PRESENTATION_VERTICAL_RIGHT_SQUARE_BRACKET ≠ RIGHT_SQUARE_BRACKET
  CONFUSABLE_003:
    VISIBLE_FORM: ⁆
    CODEPOINT: U+2046
    NAME: RIGHT SQUARE BRACKET WITH QUILL
    RISK: LOW
    RULE: RIGHT_SQUARE_BRACKET_WITH_QUILL ≠ RIGHT_SQUARE_BRACKET
  CONFUSABLE_004:
    VISIBLE_FORM: ❳
    CODEPOINT: U+2773
    NAME: LIGHT RIGHT TORTOISE SHELL BRACKET ORNAMENT
    RISK: LOW
    RULE: LIGHT_RIGHT_TORTOISE_SHELL_BRACKET_ORNAMENT ≠ RIGHT_SQUARE_BRACKET
  CONFUSABLE_005:
    VISIBLE_FORM: 〛
    CODEPOINT: U+301B
    NAME: RIGHT WHITE SQUARE BRACKET
    RISK: LOW
    RULE: RIGHT_WHITE_SQUARE_BRACKET ≠ RIGHT_SQUARE_BRACKET

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "']' is always benign closing"
    RESPONSE: RIGHT_SQUARE_BRACKET_FORM ≠ INDEX_ONLY_PROOF
    RULE: "]" completes nested keys, arrays, and regex classes
  CG2:
    TRIGGER: "closing an array/key cannot be dangerous"
    RESPONSE: RIGHT_SQUARE_BRACKET_FORM ≠ ARRAY_SAFETY_PROOF
    RULE: "]" finishes "[role]"/"[__proto__]" so the injected key takes effect
  CG3:
    TRIGGER: "']' just finishes a string key"
    RESPONSE: RIGHT_SQUARE_BRACKET_FORM ≠ KEY_SCOPE_PROOF
    RULE: the completed nested key can pollute the prototype or mass-assign
  CG4:
    TRIGGER: "'%5D' is safe forever"
    RESPONSE: RIGHT_SQUARE_BRACKET_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to "]" before the binder
  CG5:
    TRIGGER: "an ASCII ']' filter catches all brackets"
    RESPONSE: RIGHT_SQUARE_BRACKET_FORM ≠ EFFECT
    RULE: fullwidth ］ (U+FF3D) is a different codepoint
  CG6:
    TRIGGER: "the presence of ']' means the input is sanitized"
    RESPONSE: RIGHT_SQUARE_BRACKET_FORM ≠ SANITIZED_PROOF
    RULE: the presence of the sign says nothing about sanitization

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "__proto__]"
      NAME: PROTOTYPE_POLLUTION_CLOSE
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: completing a nested key that reaches the object prototype
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "role]"
      NAME: MASS_ASSIGNMENT_CLOSE
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: completing a privileged nested field for binding
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "]]"
      NAME: REGEX_CLASS_SHIFT
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: a stray "]" shifting a regex class boundary
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with "]" are central to nested-key/array injection.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "]" closes an index/array/nested key, but does not imitate the existence of a verified entity. Its risks are nested-key/array injection, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of ASCII "]" with fullwidth ］ (U+FF3D) to bypass a filter
  A2: substitution with presentation form ﹈ (U+FE48)
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: prototype pollution close obj[__proto__][isAdmin]=true
  B2: mass-assignment close user[role]=admin
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "__proto__]" (SC1) — prototype pollution close
  C2: "]]" (SC3) — regex class boundary shift
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "]" presented as harmless index close inside a parameter field
  D2: "%5D" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: prototype pollution completion into a JS object graph
  E2: N/A — vector: mass-assignment completion into a model
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: "]" is always benign closing
  EXPECTED: FAIL_INDEX_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: closing an array/key cannot be dangerous
  EXPECTED: FAIL_ARRAY_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: "]" just finishes a string key
  EXPECTED: FAIL_KEY_SCOPE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%5D" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: an ASCII "]" filter catches all bracket look-alikes
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: the presence of "]" proves the input was sanitized
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to bind "]"-completed nested keys safely (query/JSON/regex) without false positives on indexing/arrays/citations/log tags?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (block __proto__/constructor keys + explicit allow-listed binding + safe regex-class construction is an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "the safety of ']' is decided by the parse/binding context".
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
