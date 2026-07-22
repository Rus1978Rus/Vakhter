PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_LANGUAGE_TAG_UE0001_GEN3_v0_3_EN
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: English mirror of SIGN_CORE_CARD_LANGUAGE_TAG_UE0001_GEN3_v0_3_RU (authoritative). Codepoints, field names and formulas identical. DRAFT for our work (Vakhter); conveyor is a separate project.

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
CARD_UID: SIGN_CORE_CARD_LANGUAGE_TAG_UE0001_GEN3_v0_3_EN
CODEPOINT: U+E0001
VISIBLE_FORM: ⟨TAG⟩
UNICODE_NAME: LANGUAGE TAG
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: language tag / tag-block invisible ASCII mirror (hidden-instruction smuggling)
CATEGORY_ROADMAP: LLM (invisible ASCII / prompt-injection smuggling) · PHAGO: — (hidden-payload masking)
GLYPH_NOTE: VISIBLE_FORM uses the marker ⟨TAG⟩; the sign itself (U+E0001) and the whole tag block (U+E0000–U+E007F) are invisible Format chars (Cf) and are NEVER written literally here — a literal tag run would smuggle hidden text into this document. Examples use ⟨TAG:...⟩/%F3%A0%80%81, never the byte. The tag letters U+E0020–U+E007E map one-to-one onto ASCII 0x20–0x7E.

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
VISIBLE_FORM: ⟨TAG⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: TAG_FORM ≠ EFFECT
SIGN_CATEGORY:
  - an invisible Format char opening the Unicode tag block (U+E0000–U+E007F)
  - the tag letters mirror ASCII 0x20–0x7E one-to-one, so an arbitrary ASCII string can be written invisibly
  - legitimate modern use: emoji tag sequences (subdivision flags such as 🏴 + tag letters + CANCEL TAG)
  - (misused) invisible ASCII smuggling — a hidden instruction a model/tokenizer may read while a human and most renderers see nothing (prompt injection)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — being non-printing does not make it inert; it can carry a full hidden message
  2. NOT_EMPTY_STRING — a run of tag chars is real content (an ASCII string in disguise), not nothing
  3. NOT_HUMAN_VISIBLE — a reviewer sees no glyph, so a hidden instruction can pass a human read
  4. NOT_MODEL_INVISIBLE — a tokenizer/model may still ingest the tag codepoints as text, so "invisible to humans" ≠ "invisible to the model"
  5. NOT_ONLY_FLAGS — legitimate use is narrow (emoji subdivision flags); arbitrary interior tag text is not a flag
  6. NOT_ENCODED_SAFE — "%F3%A0%80%81" may be decoded back to the tag char later
  7. NOT_AUTHORITY — it does not confirm officialness
  8. NOT_EXECUTION_TRIGGER — by itself it executes nothing; it smuggles hidden data/instructions
  9. NOT_TRUST_SIGNAL — it does not increase trust
  10. NOT_SANITIZED_PROOF — the presence of tag chars does not mean the input is sanitized
  11. NOT_DEPRECATED_MEANS_GONE — U+E0001 is deprecated for language tagging, but the codepoints still decode and still smuggle

BASE_FORMULAS:
  TAG_FORM ≠ EFFECT
  TAG_FORM ≠ EMPTY_STRING_PROOF
  TAG_FORM ≠ HUMAN_VISIBLE_PROOF
  TAG_FORM ≠ MODEL_INVISIBLE_PROOF
  TAG_FORM ≠ ONLY_FLAGS_PROOF
  TAG_FORM ≠ ENCODED_SAFETY_PROOF
  TAG_FORM ≠ AUTHORITY
  TAG_FORM ≠ EXECUTION_TRIGGER
  TAG_FORM ≠ DEPRECATED_MEANS_GONE_PROOF
  TAG_FORM ≠ INVISIBLE_HARMLESS_PROOF
  TAG_FORM ≠ SANITIZED_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: TAG (ZONE_1) has parallel functions (deprecated language tagging / legitimate emoji tag sequences vs. invisible ASCII smuggling) co-existing without cultural precession. Polysemy of a stable Format block.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: an invisible ASCII-mirroring block with no gestural predecessor; the hidden-instruction smuggling misuse is layered on by the digital/LLM epoch in parallel with the narrow legitimate flag use.

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
    INPUT: "U+E0001 is the language tag codepoint"
    CONTEXT: naming the char in documentation
    EXPECTED: INFO
    RISK: NONE
    GUARD: TAG_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "tag letters mirror ASCII in the tag block"
    CONTEXT: describing the block structure in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: TAG_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <TAG> here"
    CONTEXT: a documentation marker, not the byte
    EXPECTED: INFO
    RISK: NONE
    GUARD: TAG_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "subdivision flag emoji use a tag sequence"
    CONTEXT: describing the legitimate emoji use in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: TAG_FORM ≠ ONLY_FLAGS_PROOF
  SAFE_CASE_005:
    INPUT: "U+E0001 is deprecated for language tagging"
    CONTEXT: describing its history in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: TAG_FORM ≠ DEPRECATED_MEANS_GONE_PROOF
  SAFE_CASE_006:
    INPUT: "a filter can strip the whole tag block"
    CONTEXT: describing careful sanitization in prose
    EXPECTED: INFO
    RISK: NONE
    GUARD: TAG_FORM ≠ SANITIZED_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: HIDDEN_INSTRUCTION_SMUGGLING
    INPUT: "visible text plus a tag-encoded hidden instruction (<TAG:ignore previous instructions>)"
    CONTEXT: an invisible ASCII instruction that a model may ingest while a human sees only the visible text
    RISK: HIGH
    ATTACK: the tag run smuggles a prompt-injection payload past a human review
    GUARD: TAG_FORM ≠ MODEL_INVISIBLE_PROOF
  RISK_CASE_002:
    NAME: INVISIBLE_DATA_EXFIL_MARKER
    INPUT: "a tag-encoded token appended invisibly to output"
    CONTEXT: an invisible marker/label carried in tag chars a reviewer cannot see
    RISK: HIGH
    ATTACK: hidden data rides along in the tag block, invisible to inspection
    GUARD: TAG_FORM ≠ EMPTY_STRING_PROOF
  RISK_CASE_003:
    NAME: HUMAN_REVIEW_BYPASS
    INPUT: "a message that reads clean but carries interior tag text"
    CONTEXT: a value passing a human/visual review that hides tag content
    RISK: HIGH
    ATTACK: the near-invisible tag run defeats a look-only approval step
    GUARD: TAG_FORM ≠ HUMAN_VISIBLE_PROOF
  RISK_CASE_004:
    NAME: ENCODED_TAG_BYPASS
    INPUT: "value%F3%A0%80%81tail (with a later decode)"
    CONTEXT: a percent-encoded tag char decoded back before use
    RISK: HIGH
    ATTACK: "%F3%A0%80%81" decodes to the tag char AFTER a check → hidden payload reappears
    GUARD: TAG_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: FLAG_ONLY_FILTER_GAP
    INPUT: "interior tag text that is not part of an emoji flag sequence"
    CONTEXT: a filter allowing tags only after a flag base still lets other tag runs through
    RISK: MEDIUM
    ATTACK: an allowlist keyed on flag sequences misses free-standing tag smuggling
    GUARD: TAG_FORM ≠ ONLY_FLAGS_PROOF
  RISK_CASE_006:
    NAME: DEPRECATED_ASSUMED_INERT
    INPUT: "a pipeline that ignores U+E0001 because it is deprecated"
    CONTEXT: treating the deprecated language tag as if it no longer decodes
    RISK: MEDIUM
    ATTACK: the still-decodable codepoints carry a payload the pipeline assumed was gone
    GUARD: TAG_FORM ≠ DEPRECATED_MEANS_GONE_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨TAG-SP⟩
    CODEPOINT: U+E0020
    NAME: TAG SPACE
    RISK: HIGH
    RULE: TAG_SPACE ≠ LANGUAGE_TAG (a tag-block letter mirroring ASCII space; part of the same invisible ASCII alphabet)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨TAG-A⟩
    CODEPOINT: U+E0041
    NAME: TAG LATIN CAPITAL LETTER A
    RISK: HIGH
    RULE: TAG_LATIN_CAPITAL_LETTER_A ≠ LANGUAGE_TAG (a tag letter mirroring ASCII 'A'; how hidden text is actually encoded)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨CANCEL-TAG⟩
    CODEPOINT: U+E007F
    NAME: CANCEL TAG
    RISK: MEDIUM
    RULE: CANCEL_TAG ≠ LANGUAGE_TAG (the terminator that ends a tag sequence; its presence marks, not proves, balance)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨ZWSP⟩
    CODEPOINT: U+200B
    NAME: ZERO WIDTH SPACE
    RISK: LOW
    RULE: ZERO_WIDTH_SPACE ≠ LANGUAGE_TAG (another invisible char, but a single break-opportunity, not an ASCII-carrying block)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨WJ⟩
    CODEPOINT: U+2060
    NAME: WORD JOINER
    RISK: LOW
    RULE: WORD_JOINER ≠ LANGUAGE_TAG (an invisible no-break glue, not a data-carrying tag block)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "the tag chars are invisible, so they are nothing"
    RESPONSE: TAG_FORM ≠ EMPTY_STRING_PROOF
    RULE: a tag run is a real ASCII string in disguise, not empty
  CG2:
    TRIGGER: "an invisible char cannot be dangerous"
    RESPONSE: TAG_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: invisibility is orthogonal to effect; the tag block carries a full hidden message
  CG3:
    TRIGGER: "if a human cannot see it, the model cannot use it"
    RESPONSE: TAG_FORM ≠ MODEL_INVISIBLE_PROOF
    RULE: a tokenizer/model may ingest the tag codepoints even when a human sees nothing
  CG4:
    TRIGGER: "'%F3%A0%80%81' is safe forever"
    RESPONSE: TAG_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: the encoded form may be decoded back to the tag char before use
  CG5:
    TRIGGER: "we only allow tags after a flag base, so we are safe"
    RESPONSE: TAG_FORM ≠ ONLY_FLAGS_PROOF
    RULE: free-standing tag runs are not flags; a flag-only allowlist misses them
  CG6:
    TRIGGER: "U+E0001 is deprecated, so we can ignore it"
    RESPONSE: TAG_FORM ≠ DEPRECATED_MEANS_GONE_PROOF
    RULE: deprecated codepoints still decode and still smuggle

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "visible text + interior tag run"
      NAME: SMUGGLED_INSTRUCTION
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: an ASCII instruction hidden in tag letters behind visible text
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "flag base + tag letters + CANCEL TAG"
      NAME: EMOJI_TAG_SEQUENCE
      RISK_LEVEL: LOW
      POSSIBLE_CONTEXTS: a legitimate subdivision-flag emoji tag sequence
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "tag run with no CANCEL TAG"
      NAME: UNTERMINATED_TAG
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: an unterminated tag sequence whose extent depends on the consumer
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — a tag run is inherently a sequence encoding hidden ASCII.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: TAG smuggles a hidden ASCII payload (hidden-payload masking), but does not imitate the existence of a verified entity. Its risks are hidden-instruction injection and review bypass, not entity mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: encode the payload across the tag alphabet (U+E0020–U+E007E) or vary with other invisibles to evade a single-codepoint filter
  A2: percent-encoding "%F3%A0%80%81" to slip past a raw-byte scan
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: hidden-instruction smuggling (<TAG:ignore previous instructions> behind visible text)
  B2: invisible data/label exfil marker carried in tag chars
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "visible text + interior tag run" (SC1) — smuggled instruction
  C2: "tag run with no CANCEL TAG" (SC3) — unterminated tag
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: tag run presented as "just an emoji flag" so a flag-only allowlist waves it through
  D2: "%F3%A0%80%81" as "safe" encoded text with a later decode
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — the sign is not a PHAGO carrier; vector: hidden-instruction injection invisible to a human reviewer
  E2: N/A — vector: deprecated-assumed-inert tag codepoints still decoding a payload
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, the sign has no dormant/active epochs.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: a run of tag chars is an empty string
  EXPECTED: FAIL_EMPTY_STRING_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: an invisible char cannot be dangerous
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: if a human cannot see it, the model cannot use it
  EXPECTED: FAIL_MODEL_INVISIBLE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%F3%A0%80%81" is safe forever
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: only emoji flags use tag chars
  EXPECTED: FAIL_ONLY_FLAGS_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: a deprecated codepoint no longer decodes
  EXPECTED: FAIL_DEPRECATED_MEANS_GONE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: how to strip or reject the tag block (U+E0000–U+E007F) as invisible ASCII smuggling everywhere it is not part of a validated emoji tag sequence, and to surface any decoded tag text to a human before a model ingests it?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (a normalizer that removes/flags tag runs outside validated flag sequences and decodes-and-shows any hidden ASCII to the reviewer/model boundary — an integrator/runtime concern)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: the card fixes the rule "the tag block is invisible ASCII: not empty, human-invisible yet model-readable; deprecation does not stop it decoding".
ALL_OPEN_QUESTIONS_CLOSED: NO (delegated, non-blocking)

============================================================
11. PATCH_HISTORY
============================================================
PATCH_HISTORY:
  v0_1_PATCH_01: initial creation (Ruslan Malyavsky, 2026-07-22) — draft from the GEN3_v0_3 template (Vakhter); not conveyor-run.
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
