PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_POP_DIRECTIONAL_FORMATTING_U202C_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: Русский оригинал (authoritative). Английское зеркало — SIGN_CORE_CARD_POP_DIRECTIONAL_FORMATTING_U202C_GEN3_v0_3_EN. Кодпоинты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_POP_DIRECTIONAL_FORMATTING_U202C_GEN3_v0_3_RU
CODEPOINT: U+202C
VISIBLE_FORM: ⟨PDF⟩
UNICODE_NAME: POP DIRECTIONAL FORMATTING
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: pop directional formatting / bidi-терминатор
CATEGORY_ROADMAP: LLM (bidi-терминатор, обман баланса) · PHAGO: — (маскировка структуры)
GLYPH_NOTE: VISIBLE_FORM использует маркер ⟨PDF⟩; сам знак (U+202C) — невидимый Bidi_Control (Cf) и НИКОГДА не пишется литералом здесь. Примеры используют ⟨PDF⟩/⟨RLO⟩/%E2%80%AC, не байт. (PDF здесь = Pop Directional Formatting, НЕ формат файла.)

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
VISIBLE_FORM: ⟨PDF⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: PDF_FORM ≠ EFFECT
SIGN_CATEGORY:
  - терминатор последнего встраивания/переопределения (LRE/RLE/LRO/RLO)
  - Unicode Bidi_Control (часть двунаправленного алгоритма)
  - легитимный закрывающий, восстанавливающий предыдущий уровень направления
  - (злоупотребление) неверно поставленный/лишний/пропущенный терминатор, ломающий баланс вложенности

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — то, что он непечатаемый, не делает его инертным
  2. NOT_TERMINATOR_MEANS_BALANCED — наличие PDF не доказывает, что спаны сбалансированы (счёт/вложенность могут не сходиться)
  3. NOT_NEUTRAL_CLOSER — неверно поставленный или лишний PDF может преждевременно закрыть легитимный спан, снова обнажив внешнее направление
  4. NOT_CLOSES_ISOLATES — PDF закрывает ТОЛЬКО embeddings/overrides; isolate закрывается PDI (U+2069) — не смешивать
  5. NOT_ESCAPED_PROOF — наличие bidi-метки не значит, что она закавычена/экранирована
  6. NOT_ENCODED_SAFE — "%E2%80%AC" может быть раскодирован обратно в терминатор позже
  7. NOT_AUTHORITY — не подтверждает официальность
  8. NOT_EXECUTION_TRIGGER — сам по себе ничего не исполняет; он управляет вложенностью
  9. NOT_STANDALONE_SAFE — PDF без соответствующего открывающего — это ошибка вложенности, а не no-op
  10. NOT_SANITIZED_PROOF — наличие PDF не значит, что ввод санитизирован
  11. NOT_ORDER_INDEPENDENT — место PDF определяет, какой спан он закрывает

BASE_FORMULAS:
  PDF_FORM ≠ EFFECT
  PDF_FORM ≠ TERMINATOR_MEANS_BALANCED_PROOF
  PDF_FORM ≠ NEUTRAL_CLOSER_PROOF
  PDF_FORM ≠ CLOSES_ISOLATES_PROOF
  PDF_FORM ≠ ESCAPED_PROOF
  PDF_FORM ≠ ENCODED_SAFETY_PROOF
  PDF_FORM ≠ AUTHORITY
  PDF_FORM ≠ EXECUTION_TRIGGER
  PDF_FORM ≠ INVISIBLE_HARMLESS_PROOF
  PDF_FORM ≠ STANDALONE_SAFETY_PROOF
  PDF_FORM ≠ ORDER_INDEPENDENCE_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: PDF (ZONE_1) имеет параллельные функции (легитимный закрывающий спана vs обман баланса через неверный счёт/размещение), сосуществующие без культурной прецессии. Полисемия стабильного Bidi_Control.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: управляющий знак-терминатор форматирования без жестового предшественника; использование для обмана баланса надстроено цифровой эпохой параллельно легитимному закрытию спана.

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
    INPUT: "PDF is U+202C in Unicode"
    CONTEXT: название управляющего знака в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: PDF_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "a balanced run: RLE ... PDF"
    CONTEXT: описание легитимной пары открывающий/закрывающий в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: PDF_FORM ≠ TERMINATOR_MEANS_BALANCED_PROOF
  SAFE_CASE_003:
    INPUT: "the marker is written as <PDF> here"
    CONTEXT: документационный маркер, не байт
    EXPECTED: INFO
    RISK: NONE
    GUARD: PDF_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "PDF closes embeddings/overrides; PDI closes isolates"
    CONTEXT: текст, различающий два терминатора
    EXPECTED: INFO
    RISK: NONE
    GUARD: PDF_FORM ≠ CLOSES_ISOLATES_PROOF
  SAFE_CASE_005:
    INPUT: "the closer restores the prior direction level"
    CONTEXT: описание легитимного восстановления
    EXPECTED: INFO
    RISK: NONE
    GUARD: PDF_FORM ≠ NEUTRAL_CLOSER_PROOF
  SAFE_CASE_006:
    INPUT: "the Bidirectional Algorithm pops the level"
    CONTEXT: текст о UBA
    EXPECTED: INFO
    RISK: NONE
    GUARD: PDF_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: FALSE_BALANCE_CLAIM
    INPUT: "opener<RLO>...<PDF>...<RLO> (one PDF, two openers)"
    CONTEXT: единственный PDF, заставляющий проверку «есть терминатор» считать ряд сбалансированным
    RISK: HIGH
    ATTACK: несопоставленный второй открывающий остаётся живым; наивная проверка «PDF есть → сбалансировано» пропускает реордер
    GUARD: PDF_FORM ≠ TERMINATOR_MEANS_BALANCED_PROOF
  RISK_CASE_002:
    NAME: PREMATURE_CLOSE
    INPUT: "legit<RLE>text<PDF-injected>more (лишний PDF, закрывающий рано)"
    CONTEXT: внедрённый лишний PDF, закрывающий легитимный спан до его предполагаемого конца
    RISK: MEDIUM
    ATTACK: лишний терминатор снова обнажает внешнее направление, портя оставшееся отображение
    GUARD: PDF_FORM ≠ NEUTRAL_CLOSER_PROOF
  RISK_CASE_003:
    NAME: ISOLATE_CONFUSION
    INPUT: "isolate opened with LRI but closed with <PDF> not PDI"
    CONTEXT: фильтр/парсер, трактующий PDF так, будто он закрыл isolate
    RISK: MEDIUM
    ATTACK: PDF не закрывает isolate; модель с неверным терминатором неверно отслеживает вложенность и оставляет спан открытым
    GUARD: PDF_FORM ≠ CLOSES_ISOLATES_PROOF
  RISK_CASE_004:
    NAME: STANDALONE_PDF_NESTING_ERROR
    INPUT: "text<PDF>more (PDF без соответствующего открывающего)"
    CONTEXT: одиночный PDF, трактуемый как безобидный no-op
    RISK: MEDIUM
    ATTACK: несопоставленный PDF — это ошибка вложенности, которую снисходительный рендерер разрешает непредсказуемо
    GUARD: PDF_FORM ≠ STANDALONE_SAFETY_PROOF
  RISK_CASE_005:
    NAME: ENCODED_PDF_BYPASS
    INPUT: "value%E2%80%AC (с поздним декодированием)"
    CONTEXT: percent-кодированный PDF, декодируемый обратно перед отображением
    RISK: MEDIUM
    ATTACK: "%E2%80%AC" декодируется в терминатор ПОСЛЕ проверки → манипуляция вложенностью
    GUARD: PDF_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: BALANCE_COUNT_MISMATCH
    INPUT: "two openers, three PDFs (over-popping the stack)"
    CONTEXT: PDF больше, чем открывающих, вытолкивание за базовый уровень
    RISK: MEDIUM
    ATTACK: over-pop влияет на текст вне предполагаемого спана — случай, который проверка «только по строке» пропускает
    GUARD: PDF_FORM ≠ TERMINATOR_MEANS_BALANCED_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨PDI⟩
    CODEPOINT: U+2069
    NAME: POP DIRECTIONAL ISOLATE
    RISK: HIGH
    RULE: POP_DIRECTIONAL_ISOLATE ≠ POP_DIRECTIONAL_FORMATTING (PDI закрывает isolate; PDF закрывает embeddings/overrides — не взаимозаменяемы)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨RLE⟩
    CODEPOINT: U+202B
    NAME: RIGHT-TO-LEFT EMBEDDING
    RISK: MEDIUM
    RULE: RIGHT_TO_LEFT_EMBEDDING ≠ POP_DIRECTIONAL_FORMATTING (открывающий vs терминатор; фильтр должен их спаривать, не смешивать)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨LRE⟩
    CODEPOINT: U+202A
    NAME: LEFT-TO-RIGHT EMBEDDING
    RISK: MEDIUM
    RULE: LEFT_TO_RIGHT_EMBEDDING ≠ POP_DIRECTIONAL_FORMATTING
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨RLO⟩
    CODEPOINT: U+202E
    NAME: RIGHT-TO-LEFT OVERRIDE
    RISK: LOW
    RULE: RIGHT_TO_LEFT_OVERRIDE ≠ POP_DIRECTIONAL_FORMATTING (override PDF терминирует, а не сам терминатор)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨ALM⟩
    CODEPOINT: U+061C
    NAME: ARABIC LETTER MARK
    RISK: LOW
    RULE: ARABIC_LETTER_MARK ≠ POP_DIRECTIONAL_FORMATTING (bidi-метка, не терминатор; невидима для PDF-only фильтра)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "в ряду есть PDF, значит он сбалансирован и безопасен"
    RESPONSE: PDF_FORM ≠ TERMINATOR_MEANS_BALANCED_PROOF
    RULE: один PDF не сопоставлен каждому открывающему; счёт и вложенность надо проверять
  CG2:
    TRIGGER: "закрывающий не может быть опасен"
    RESPONSE: PDF_FORM ≠ NEUTRAL_CLOSER_PROOF
    RULE: лишний/неверно поставленный PDF закрывает легитимный спан рано, портя дальнейшее отображение
  CG3:
    TRIGGER: "PDF закрывает любой bidi-спан"
    RESPONSE: PDF_FORM ≠ CLOSES_ISOLATES_PROOF
    RULE: PDF закрывает только embeddings/overrides; isolate нужен PDI — модель с неверным терминатором сбивается
  CG4:
    TRIGGER: "'%E2%80%AC' безопасен навсегда"
    RESPONSE: PDF_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в терминатор перед отображением
  CG5:
    TRIGGER: "одиночный PDF — безобидный no-op"
    RESPONSE: PDF_FORM ≠ STANDALONE_SAFETY_PROOF
    RULE: несопоставленный PDF — ошибка вложенности, которую снисходительный рендерер разрешает непредсказуемо
  CG6:
    TRIGGER: "наличие PDF значит, что ввод санитизирован"
    RESPONSE: PDF_FORM ≠ SANITIZED_PROOF (через INVISIBLE_HARMLESS_PROOF)
    RULE: наличие знака ничего не говорит о санитизации

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "opener ... PDF (mismatched count)"
      NAME: FALSE_BALANCE
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: один терминатор, заставляющий поверхностную проверку считать несколько открывающих сбалансированными
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "extra PDF"
      NAME: PREMATURE_CLOSE
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: внедрённый PDF, закрывающий легитимный спан рано
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "PDF for an isolate"
      NAME: WRONG_TERMINATOR
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: PDF там, где нужен PDI, неверно отслеживая вложенность isolate
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — риск PDF целиком в последовательности спаривания/вложенности.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: PDF закрывает направленный спан (управление структурой/вложенностью), но не имитирует существование верифицированной сущности. Его риски — обман баланса/вложенности, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена PDF на PDI (U+2069), чтобы спаривание isolate/embedding было смоделировано неверно
  A2: percent-кодирование "%E2%80%AC" для проскальзывания мимо raw-byte скана
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: ложный баланс — один PDF, два открывающих, проходит проверку «есть терминатор»
  B2: преждевременное закрытие — внедрённый лишний PDF, портящий дальнейшее отображение
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "opener ... PDF (mismatched)" (SC1) — ложный баланс
  C2: "PDF for an isolate" (SC3) — неверный терминатор
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: PDF подан как безобидный закрывающий, «доказывающий» сбалансированность ряда
  D2: "%E2%80%AC" как «безопасный» кодированный текст с поздним декодированием
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: ложный баланс, пропускающий реордер на ревью
  E2: N/A — вектор: over-pop стека за базовый уровень
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: ряд с PDF сбалансирован и безопасен
  EXPECTED: FAIL_TERMINATOR_MEANS_BALANCED_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: закрывающий не может быть опасен
  EXPECTED: FAIL_NEUTRAL_CLOSER_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: PDF закрывает любой bidi-спан, включая isolate
  EXPECTED: FAIL_CLOSES_ISOLATES_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E2%80%AC" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: одиночный PDF — безобидный no-op
  EXPECTED: FAIL_STANDALONE_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: невидимый управляющий символ не может быть опасен
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как верифицировать bidi-баланс (сопоставлять открывающие с PDF/PDI по типу И счёту И вложенности) без ложных срабатываний на легитимном сбалансированном смешанном тексте?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (стек-проверка баланса bidi, спаривающая каждый открывающий с правильным типом терминатора + отвергающая over/under-pop — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «наличие терминатора — не доказательство баланса; тип, счёт и вложенность должны совпадать».
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
