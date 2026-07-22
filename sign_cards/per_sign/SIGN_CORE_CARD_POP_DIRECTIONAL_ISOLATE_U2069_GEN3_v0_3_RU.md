PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_POP_DIRECTIONAL_ISOLATE_U2069_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: Русский оригинал (authoritative). Английское зеркало — SIGN_CORE_CARD_POP_DIRECTIONAL_ISOLATE_U2069_GEN3_v0_3_EN. Кодпоинты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_POP_DIRECTIONAL_ISOLATE_U2069_GEN3_v0_3_RU
CODEPOINT: U+2069
VISIBLE_FORM: ⟨PDI⟩
UNICODE_NAME: POP DIRECTIONAL ISOLATE
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: pop directional isolate / bidi-терминатор изолята
CATEGORY_ROADMAP: LLM (bidi-терминатор изолята, обман баланса) · PHAGO: — (маскировка структуры)
GLYPH_NOTE: VISIBLE_FORM использует маркер ⟨PDI⟩; сам знак (U+2069) — невидимый Bidi_Control (Cf) и НИКОГДА не пишется литералом здесь. Примеры используют ⟨PDI⟩/⟨LRI⟩/%E2%81%A9, не байт.

============================================================
3. REQUIRED_GENERAL_GUARDS
============================================================
REQUIRED_GENERAL_GUARDS:
  - SIGN_FALSE_EFFECT_MIMICRY_GUARD_v0_2A_RU
    GUARD_COMPATIBILITY: применим без изменений — знак не создаёт effect-полей
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
VISIBLE_FORM: ⟨PDI⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: PDI_FORM ≠ EFFECT
SIGN_CATEGORY:
  - терминатор последнего изолята (LRI/RLI/FSI)
  - Unicode Bidi_Control, современный закрывающий изолята
  - легитимный закрывающий, завершающий ограниченный ряд изолята
  - (злоупотребление) неверно поставленный/лишний/пропущенный терминатор изолята, ломающий баланс вложенности

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — то, что он непечатаемый, не делает его инертным
  2. NOT_TERMINATOR_MEANS_BALANCED — наличие PDI не доказывает, что изоляты сбалансированы
  3. NOT_CLOSES_EMBEDDINGS — PDI закрывает ТОЛЬКО изоляты; embeddings/overrides используют PDF (U+202C) — не смешивать
  4. NOT_NEUTRAL_CLOSER — неверно поставленный или лишний PDI может преждевременно закрыть легитимный изолят
  5. NOT_ESCAPED_PROOF — наличие bidi-метки не значит, что она закавычена/экранирована
  6. NOT_ENCODED_SAFE — "%E2%81%A9" может быть раскодирован обратно в терминатор позже
  7. NOT_AUTHORITY — не подтверждает официальность
  8. NOT_EXECUTION_TRIGGER — сам по себе ничего не исполняет; он управляет вложенностью изолятов
  9. NOT_STANDALONE_SAFE — PDI без соответствующего открывающего изолята — это ошибка вложенности, а не no-op
  10. NOT_LEGACY_FILTER_COVERED — фильтр, моделирующий только PDF (202C), не отслеживает PDI (2069)
  11. NOT_ORDER_INDEPENDENT — место PDI определяет, какой изолят он закрывает

BASE_FORMULAS:
  PDI_FORM ≠ EFFECT
  PDI_FORM ≠ TERMINATOR_MEANS_BALANCED_PROOF
  PDI_FORM ≠ CLOSES_EMBEDDINGS_PROOF
  PDI_FORM ≠ NEUTRAL_CLOSER_PROOF
  PDI_FORM ≠ ESCAPED_PROOF
  PDI_FORM ≠ ENCODED_SAFETY_PROOF
  PDI_FORM ≠ AUTHORITY
  PDI_FORM ≠ EXECUTION_TRIGGER
  PDI_FORM ≠ INVISIBLE_HARMLESS_PROOF
  PDI_FORM ≠ STANDALONE_SAFETY_PROOF
  PDI_FORM ≠ LEGACY_FILTER_COVERAGE_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: PDI (ZONE_1) имеет параллельные функции (легитимный закрывающий изолята vs обман баланса через неверный счёт/размещение/неверный терминатор), сосуществующие без культурной прецессии. Полисемия стабильного Bidi_Control.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: управляющий знак-терминатор изолята без жестового предшественника; использование для обмана баланса надстроено цифровой эпохой параллельно легитимному закрытию изолята.

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
    INPUT: "PDI is U+2069 in Unicode"
    CONTEXT: название управляющего знака в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: PDI_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "a balanced isolate: LRI ... PDI"
    CONTEXT: описание легитимной пары открытие/закрытие изолята в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: PDI_FORM ≠ TERMINATOR_MEANS_BALANCED_PROOF
  SAFE_CASE_003:
    INPUT: "the marker is written as <PDI> here"
    CONTEXT: документационный маркер, не байт
    EXPECTED: INFO
    RISK: NONE
    GUARD: PDI_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "PDI closes isolates; PDF closes embeddings/overrides"
    CONTEXT: текст, различающий два терминатора
    EXPECTED: INFO
    RISK: NONE
    GUARD: PDI_FORM ≠ CLOSES_EMBEDDINGS_PROOF
  SAFE_CASE_005:
    INPUT: "the closer ends a scoped isolate run"
    CONTEXT: описание легитимного закрытия
    EXPECTED: INFO
    RISK: NONE
    GUARD: PDI_FORM ≠ NEUTRAL_CLOSER_PROOF
  SAFE_CASE_006:
    INPUT: "the Bidirectional Algorithm pops the isolate"
    CONTEXT: текст о UBA
    EXPECTED: INFO
    RISK: NONE
    GUARD: PDI_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: FALSE_BALANCE_CLAIM
    INPUT: "opener<LRI>...<PDI>...<RLI> (one PDI, two isolate openers)"
    CONTEXT: единственный PDI, заставляющий проверку «есть терминатор» считать изоляты сбалансированными
    RISK: HIGH
    ATTACK: несопоставленный второй открывающий изолят остаётся живым; наивная проверка «PDI есть → сбалансировано» пропускает реордер
    GUARD: PDI_FORM ≠ TERMINATOR_MEANS_BALANCED_PROOF
  RISK_CASE_002:
    NAME: WRONG_TERMINATOR_FOR_EMBEDDING
    INPUT: "embedding opened with RLE but closed with <PDI> not PDF"
    CONTEXT: парсер, трактующий PDI так, будто он закрыл embedding
    RISK: MEDIUM
    ATTACK: PDI не закрывает embedding; модель с неверным терминатором неверно отслеживает вложенность и оставляет спан открытым
    GUARD: PDI_FORM ≠ CLOSES_EMBEDDINGS_PROOF
  RISK_CASE_003:
    NAME: PREMATURE_ISOLATE_CLOSE
    INPUT: "legit<LRI>text<PDI-injected>more (лишний PDI, закрывающий рано)"
    CONTEXT: внедрённый лишний PDI, закрывающий легитимный изолят до его предполагаемого конца
    RISK: MEDIUM
    ATTACK: лишний терминатор снова обнажает внешнее направление, портя оставшееся отображение
    GUARD: PDI_FORM ≠ NEUTRAL_CLOSER_PROOF
  RISK_CASE_004:
    NAME: LEGACY_FILTER_GAP
    INPUT: "PDI passing a filter that only knows PDF (202C)"
    CONTEXT: legacy bidi-фильтр, моделирующий embeddings/overrides, но не изоляты
    RISK: HIGH
    ATTACK: терминатор изолята (и значит спан изолята) невидим для фильтра
    GUARD: PDI_FORM ≠ LEGACY_FILTER_COVERAGE_PROOF
  RISK_CASE_005:
    NAME: ENCODED_PDI_BYPASS
    INPUT: "value%E2%81%A9 (с поздним декодированием)"
    CONTEXT: percent-кодированный PDI, декодируемый обратно перед отображением
    RISK: MEDIUM
    ATTACK: "%E2%81%A9" декодируется в терминатор ПОСЛЕ проверки → манипуляция вложенностью изолятов
    GUARD: PDI_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: STANDALONE_PDI_NESTING_ERROR
    INPUT: "text<PDI>more (PDI без соответствующего открывающего изолята)"
    CONTEXT: одиночный PDI, трактуемый как безобидный no-op
    RISK: MEDIUM
    ATTACK: несопоставленный PDI — это ошибка вложенности, которую снисходительный рендерер разрешает непредсказуемо
    GUARD: PDI_FORM ≠ STANDALONE_SAFETY_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨PDF⟩
    CODEPOINT: U+202C
    NAME: POP DIRECTIONAL FORMATTING
    RISK: HIGH
    RULE: POP_DIRECTIONAL_FORMATTING ≠ POP_DIRECTIONAL_ISOLATE (PDF закрывает embeddings/overrides; PDI закрывает изоляты — не взаимозаменяемы)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨LRI⟩
    CODEPOINT: U+2066
    NAME: LEFT-TO-RIGHT ISOLATE
    RISK: MEDIUM
    RULE: LEFT_TO_RIGHT_ISOLATE ≠ POP_DIRECTIONAL_ISOLATE (открывающий vs терминатор; фильтр должен их спаривать, не смешивать)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨RLI⟩
    CODEPOINT: U+2067
    NAME: RIGHT-TO-LEFT ISOLATE
    RISK: MEDIUM
    RULE: RIGHT_TO_LEFT_ISOLATE ≠ POP_DIRECTIONAL_ISOLATE
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨FSI⟩
    CODEPOINT: U+2068
    NAME: FIRST STRONG ISOLATE
    RISK: LOW
    RULE: FIRST_STRONG_ISOLATE ≠ POP_DIRECTIONAL_ISOLATE (открывающий с авто-определением направления; PDI — его закрывающий)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨ALM⟩
    CODEPOINT: U+061C
    NAME: ARABIC LETTER MARK
    RISK: LOW
    RULE: ARABIC_LETTER_MARK ≠ POP_DIRECTIONAL_ISOLATE (bidi-метка, не терминатор; невидима для PDI-only фильтра)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "в ряду есть PDI, значит изоляты сбалансированы и безопасны"
    RESPONSE: PDI_FORM ≠ TERMINATOR_MEANS_BALANCED_PROOF
    RULE: один PDI не сопоставлен каждому открывающему изоляту; счёт и вложенность надо проверять
  CG2:
    TRIGGER: "PDI закрывает любой bidi-спан"
    RESPONSE: PDI_FORM ≠ CLOSES_EMBEDDINGS_PROOF
    RULE: PDI закрывает только изоляты; embeddings/overrides нужен PDF — модель с неверным терминатором сбивается
  CG3:
    TRIGGER: "закрывающий не может быть опасен"
    RESPONSE: PDI_FORM ≠ NEUTRAL_CLOSER_PROOF
    RULE: лишний/неверно поставленный PDI закрывает легитимный изолят рано, портя дальнейшее отображение
  CG4:
    TRIGGER: "'%E2%81%A9' безопасен навсегда"
    RESPONSE: PDI_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в терминатор перед отображением
  CG5:
    TRIGGER: "наш фильтр обрабатывает PDF, значит bidi-терминаторы прикрыты"
    RESPONSE: PDI_FORM ≠ LEGACY_FILTER_COVERAGE_PROOF
    RULE: PDI (2069) — отдельный, более новый терминатор, который PDF-only фильтр пропускает
  CG6:
    TRIGGER: "одиночный PDI — безобидный no-op"
    RESPONSE: PDI_FORM ≠ STANDALONE_SAFETY_PROOF
    RULE: несопоставленный PDI — ошибка вложенности, которую снисходительный рендерер разрешает непредсказуемо

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "isolate opener ... PDI (mismatched count)"
      NAME: FALSE_BALANCE
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: один терминатор, заставляющий поверхностную проверку считать несколько изолятов сбалансированными
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "PDI for an embedding"
      NAME: WRONG_TERMINATOR
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: PDI там, где нужен PDF, неверно отслеживая вложенность embedding
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "extra PDI"
      NAME: PREMATURE_CLOSE
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: внедрённый PDI, закрывающий легитимный изолят рано
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — риск PDI целиком в последовательности спаривания/вложенности изолятов.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: PDI закрывает направленный изолят (управление структурой/вложенностью), но не имитирует существование верифицированной сущности. Его риски — обман баланса/вложенности, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена PDI на PDF (U+202C), чтобы спаривание isolate/embedding было смоделировано неверно
  A2: percent-кодирование "%E2%81%A9" для проскальзывания мимо raw-byte скана
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: ложный баланс — один PDI, два открывающих изолята, проходит проверку «есть терминатор»
  B2: пробел legacy-фильтра — PDI невидим для PDF-only bidi-фильтра
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "isolate ... PDI (mismatched)" (SC1) — ложный баланс
  C2: "PDI for an embedding" (SC2) — неверный терминатор
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: PDI подан как безобидный закрывающий, «доказывающий» сбалансированность изолята
  D2: "%E2%81%A9" как «безопасный» кодированный текст с поздним декодированием
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: ложный баланс, пропускающий реордер изолята на ревью
  E2: N/A — вектор: преждевременное закрытие изолята, портящее дальнейшее отображение
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: ряд с PDI имеет сбалансированные изоляты и безопасен
  EXPECTED: FAIL_TERMINATOR_MEANS_BALANCED_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: PDI закрывает любой bidi-спан, включая embeddings
  EXPECTED: FAIL_CLOSES_EMBEDDINGS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: закрывающий не может быть опасен
  EXPECTED: FAIL_NEUTRAL_CLOSER_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E2%81%A9" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: PDF-only фильтр покрывает все bidi-терминаторы
  EXPECTED: FAIL_LEGACY_FILTER_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: одиночный PDI — безобидный no-op
  EXPECTED: FAIL_STANDALONE_SAFETY_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как верифицировать баланс изолятов (сопоставлять LRI/RLI/FSI с PDI по типу И счёту И вложенности, отдельно от PDF) без ложных срабатываний на легитимном ограниченном смешанном тексте?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (стек-проверка, спаривающая изоляты с PDI, а embeddings/overrides с PDF, отвергающая cross-type/over/under-pop — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «PDI закрывает только изоляты; и PDF-only модель, и проверка-наличия обе не срабатывают».
ALL_OPEN_QUESTIONS_CLOSED: NO (делегировано, не блокирует)

============================================================
11. PATCH_HISTORY
============================================================
PATCH_HISTORY:
  v0_1_PATCH_01: первичное создание (Ruslan Malyavsky, 2026-07-21) — черновик по шаблону GEN3_v0_3 (Vakhter); не прогнан по конвейеру.
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
  NOT_CONVEYOR_RUN (черновик для нашей работы; конвейер — отдельный проект)
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
