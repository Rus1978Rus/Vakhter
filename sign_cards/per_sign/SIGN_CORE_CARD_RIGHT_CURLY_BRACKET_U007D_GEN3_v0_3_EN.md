PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_RIGHT_CURLY_BRACKET_U007D_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_RIGHT_CURLY_BRACKET_U007D_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_RIGHT_CURLY_BRACKET_U007D_GEN3_v0_3_EN
CODEPOINT: U+007D
VISIBLE_FORM: }
UNICODE_NAME: RIGHT CURLY BRACKET
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: right brace / template & object close
CATEGORY_ROADMAP: INJ (SSTI template close, object close) · PHAGO: — (structure close forgery)

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
VISIBLE_FORM: }
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: RIGHT_CURLY_BRACKET_FORM ≠ EFFECT
SIGN_CATEGORY:
  - code block closer ({ ... })
  - JSON/dict/set object closer ({"k": "v"})
  - template expression closer (}}, })
  - shell brace expansion closer ({a,b})

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_BLOCK_ONLY — "}" is not always a benign block close (it completes a template expression)
  2. NOT_TEMPLATE_SAFE — "}}" closes an expression the template engine then evaluates (SSTI/RCE)
  3. NOT_OBJECT_SAFE — a "}" closes an injected operator/key object (NoSQL/JSON)
  4. NOT_ESCAPED_PROOF — the presence of "}" does not mean it is quoted/escaped
  5. NOT_ENCODED_SAFE — "%7D" may be decoded back to "}" later
  6. NOT_AUTHORITY — "}" does not confirm officialness
  7. NOT_EXECUTION_TRIGGER — by itself it executes nothing; context makes it close/complete
  8. NOT_TRUST_SIGNAL — it does not increase trust
  9. NOT_BALANCED_PROOF — a placed "}" can rebalance a structure to the attacker's shape
  10. NOT_SANITIZED_PROOF — the presence of "}" does not mean the input is sanitized
  11. NOT_OUTPUT_CONTEXT_PROOF — safety depends on the parse/evaluation context

BASE_FORMULAS:
  RIGHT_CURLY_BRACKET_FORM ≠ EFFECT
  RIGHT_CURLY_BRACKET_FORM ≠ BLOCK_ONLY_PROOF
  RIGHT_CURLY_BRACKET_FORM ≠ TEMPLATE_SAFETY_PROOF
  RIGHT_CURLY_BRACKET_FORM ≠ OBJECT_SAFETY_PROOF
  RIGHT_CURLY_BRACKET_FORM ≠ ESCAPED_PROOF
  RIGHT_CURLY_BRACKET_FORM ≠ ENCODED_SAFETY_PROOF
  RIGHT_CURLY_BRACKET_FORM ≠ AUTHORITY
  RIGHT_CURLY_BRACKET_FORM ≠ EXECUTION_TRIGGER
  RIGHT_CURLY_BRACKET_FORM ≠ BALANCED_PROOF
  RIGHT_CURLY_BRACKET_FORM ≠ SANITIZED_PROOF
  RIGHT_CURLY_BRACKET_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "}" (ZONE_1) has parallel functions (block close, object close, template expression close, brace expansion close) co-existing without cultural precession. Polysemy of a stable sign.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: a punctuation/mathematical brace with no gestural predecessor; the block/object/template functions are layered on by the digital epoch in parallel.

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
    INPUT: "the set {1, 2, 3}"
    CONTEXT: a mathematical set in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: RIGHT_CURLY_BRACKET_FORM ≠ BLOCK_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: 'JSON {"name": "Ann"}'
    CONTEXT: a well-formed JSON object shown as text
    EXPECTED: INFO
    RISK: NONE
    GUARD: RIGHT_CURLY_BRACKET_FORM ≠ OBJECT_SAFETY_PROOF
  SAFE_CASE_003:
    INPUT: "if (x) { doThing() }"
    CONTEXT: a code block shown as literal text
    EXPECTED: INFO
    RISK: NONE
    GUARD: RIGHT_CURLY_BRACKET_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "CSS rule: body { margin: 0 }"
    CONTEXT: a CSS declaration block
    EXPECTED: INFO
    RISK: NONE
    GUARD: RIGHT_CURLY_BRACKET_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "the } key on a keyboard"
    CONTEXT: naming the brace key in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: RIGHT_CURLY_BRACKET_FORM ≠ BLOCK_ONLY_PROOF
  SAFE_CASE_006:
    INPUT: "quantifier a{2,3} in a regex"
    CONTEXT: describing a regex quantifier in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: RIGHT_CURLY_BRACKET_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: SSTI_EXPRESSION_CLOSE
    INPUT: "{{7*7}} completing an evaluated expression"
    CONTEXT: "}}" closing the expression so the engine evaluates it
    RISK: CRITICAL
    ATTACK: "}}" finalizes "{{...}}" so it is evaluated server-side (SSTI/RCE)
    GUARD: RIGHT_CURLY_BRACKET_FORM ≠ TEMPLATE_SAFETY_PROOF
  RISK_CASE_002:
    NAME: NOSQL_OBJECT_CLOSE
    INPUT: '{"$ne": null}'
    CONTEXT: "}" closing an injected NoSQL operator object
    RISK: HIGH
    ATTACK: "}" completes the "$ne" object so the always-true query runs (auth bypass)
    GUARD: RIGHT_CURLY_BRACKET_FORM ≠ OBJECT_SAFETY_PROOF
  RISK_CASE_003:
    NAME: FORMAT_FIELD_CLOSE
    INPUT: "{0.__class__} closing a format field"
    CONTEXT: "}" completing a format field that walks object internals
    RISK: HIGH
    ATTACK: "}" finalizes "{0...}" so str.format leaks internals/globals
    GUARD: RIGHT_CURLY_BRACKET_FORM ≠ EFFECT
  RISK_CASE_004:
    NAME: JSON_STRUCTURE_REBALANCE
    INPUT: 'x"}, "isAdmin": true, "y": {"a":"'
    CONTEXT: "}" rebalancing a JSON object to inject a forged key
    RISK: HIGH
    ATTACK: "}" closes early so "isAdmin": true is injected as a sibling key
    GUARD: RIGHT_CURLY_BRACKET_FORM ≠ BALANCED_PROOF
  RISK_CASE_005:
    NAME: ENCODED_BRACE_BYPASS
    INPUT: "%7B%7B7*7%7D%7D (with a later decode)"
    CONTEXT: an encoded "}}" decoded back before the template engine
    RISK: HIGH
    ATTACK: %7D decodes to "}" AFTER the check → completes a template expression
    GUARD: RIGHT_CURLY_BRACKET_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_BRACE_BYPASS
    INPUT: "｛｛7*7｝｝ (fullwidth ｝ U+FF5D)"
    CONTEXT: a look-alike to bypass a "}" filter
    RISK: MEDIUM
    ATTACK: a filter looks for ASCII "}", a normalizer may fold ｝ to "}"
    GUARD: RIGHT_CURLY_BRACKET_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ｝
    CODEPOINT: U+FF5D
    NAME: FULLWIDTH RIGHT CURLY BRACKET
    RISK: HIGH
    RULE: FULLWIDTH_RIGHT_CURLY_BRACKET ≠ RIGHT_CURLY_BRACKET (bypasses a filter looking for ASCII "}")
  CONFUSABLE_002:
    VISIBLE_FORM: ﹜
    CODEPOINT: U+FE5C
    NAME: SMALL RIGHT CURLY BRACKET
    RISK: MEDIUM
    RULE: SMALL_RIGHT_CURLY_BRACKET ≠ RIGHT_CURLY_BRACKET
  CONFUSABLE_003:
    VISIBLE_FORM: ❵
    CODEPOINT: U+2775
    NAME: MEDIUM RIGHT CURLY BRACKET ORNAMENT
    RISK: LOW
    RULE: MEDIUM_RIGHT_CURLY_BRACKET_ORNAMENT ≠ RIGHT_CURLY_BRACKET
  CONFUSABLE_004:
    VISIBLE_FORM: ⦄
    CODEPOINT: U+2984
    NAME: RIGHT WHITE CURLY BRACKET
    RISK: LOW
    RULE: RIGHT_WHITE_CURLY_BRACKET ≠ RIGHT_CURLY_BRACKET
  CONFUSABLE_005:
    VISIBLE_FORM: 𝄕
    CODEPOINT: U+1D115
    NAME: MUSICAL SYMBOL BRACKET
    RISK: LOW
    RULE: MUSICAL_SYMBOL_BRACKET ≠ RIGHT_CURLY_BRACKET

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "'}' is always a benign block close"
    RESPONSE: RIGHT_CURLY_BRACKET_FORM ≠ BLOCK_ONLY_PROOF
    RULE: "}}" completes a template expression an engine evaluates
  CG2:
    TRIGGER: "closing a template block is inert"
    RESPONSE: RIGHT_CURLY_BRACKET_FORM ≠ TEMPLATE_SAFETY_PROOF
    RULE: the completed expression is evaluated (SSTI/RCE)
  CG3:
    TRIGGER: "closing a JSON object cannot be dangerous"
    RESPONSE: RIGHT_CURLY_BRACKET_FORM ≠ OBJECT_SAFETY_PROOF
    RULE: "}" completes an injected operator ($ne) or a forged sibling key
  CG4:
    TRIGGER: "'%7D' is safe forever"
    RESPONSE: RIGHT_CURLY_BRACKET_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to "}" before the engine
  CG5:
    TRIGGER: "an ASCII '}' filter catches all braces"
    RESPONSE: RIGHT_CURLY_BRACKET_FORM ≠ EFFECT
    RULE: fullwidth ｝ (U+FF5D) and small ﹜ (U+FE5C) are different codepoints
  CG6:
    TRIGGER: "the presence of '}' means the input is sanitized"
    RESPONSE: RIGHT_CURLY_BRACKET_FORM ≠ SANITIZED_PROOF
    RULE: the presence of the sign says nothing about sanitization

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "}}"
      NAME: TEMPLATE_EXPR_CLOSE
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: completing an evaluated template expression (SSTI)
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: '"}'
      NAME: OBJECT_KEY_CLOSE
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: closing an object early to inject a sibling key
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "%}"
      NAME: TEMPLATE_TAG_CLOSE
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: closing a template control tag (if/for/include)
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — sequences with "}" are central to template/object injection.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "}" closes a block/object/template expression, but does not imitate the existence of a verified entity. Its risks are template/object injection, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: substitution of ASCII "}" with fullwidth ｝ (U+FF5D) to bypass a filter
  A2: substitution with small ﹜ (U+FE5C)
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: SSTI expression close {{7*7}}
  B2: NoSQL object close {"$ne": null}
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "}}" (SC1) — template expression close
  C2: '"}' (SC2) — object key close/rebalance
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "}" presented as a harmless JSON/code block close inside a template field
  D2: "%7D" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: template expression completion into a rendered page
  E2: N/A — vector: forged sibling-key injection via early object close
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: "}" is always a benign block close
  EXPECTED: FAIL_BLOCK_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: closing a template block is inert
  EXPECTED: FAIL_TEMPLATE_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: closing a JSON object cannot be dangerous
  EXPECTED: FAIL_OBJECT_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%7D" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: an ASCII "}" filter catches all brace look-alikes
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: the presence of "}" proves the input was sanitized
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to escape "}" per context (template/JSON/format) without false positives on code blocks/sets/CSS/regex quantifiers?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (sandboxed/logic-less templating + schema-validated JSON + safe format APIs is an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "the safety of '}' is decided by the parse/evaluation context".
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
