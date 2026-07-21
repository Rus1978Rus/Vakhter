PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_RIGHT_TO_LEFT_EMBEDDING_U202B_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: Русский оригинал (authoritative). Английское зеркало — SIGN_CORE_CARD_RIGHT_TO_LEFT_EMBEDDING_U202B_GEN3_v0_3_EN. Кодпоинты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_RIGHT_TO_LEFT_EMBEDDING_U202B_GEN3_v0_3_RU
CODEPOINT: U+202B
VISIBLE_FORM: ⟨RLE⟩
UNICODE_NAME: RIGHT-TO-LEFT EMBEDDING
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: RTL-встраивание / bidi реордер (слабее override)
CATEGORY_ROADMAP: LLM (bidi визуальный реордер, Trojan Source) · PHAGO: — (маскировка структуры)
GLYPH_NOTE: VISIBLE_FORM использует маркер ⟨RLE⟩; сам знак (U+202B) — невидимый Bidi_Control (Cf) и НИКОГДА не пишется литералом здесь — литеральный RLE переупорядочил бы этот документ. Примеры используют ⟨RLE⟩/⟨PDF⟩/%E2%80%AB, не байт.

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
VISIBLE_FORM: ⟨RLE⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: RLE_FORM ≠ EFFECT
SIGN_CATEGORY:
  - двунаправленное встраивание (открывает RTL-уровень, УВАЖАЯ направление сильных символов)
  - Unicode Bidi_Control (часть двунаправленного алгоритма)
  - легитимный вложенный RTL-текст внутри большего абзаца
  - (злоупотребление) более тонкий-чем-override реордер в вариантах Trojan Source

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — то, что он непечатаемый, не делает его инертным
  2. NOT_DISPLAY_ONLY — он переупорядочивает ВИЗУАЛЬНЫЙ ряд, а логические байты неизменны (рассинхрон)
  3. NOT_WEAKER_MEANS_SAFE — embedding тоньше override, но всё равно переупорядочивает и всё равно обманывает
  4. NOT_RENDERING_COSMETIC — реордер меняет то, что человек одобряет, vs что исполняется/хранится
  5. NOT_ENCODED_SAFE — "%E2%80%AB" может быть раскодирован обратно во встраивание позже
  6. NOT_AUTHORITY — не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе ничего не исполняет; он обманывает читателя
  8. NOT_TRUST_SIGNAL — не повышает доверие
  9. NOT_BALANCED_PROOF — незавершённое встраивание (без PDF/PDI) растекает уровень на остаток
  10. NOT_SANITIZED_PROOF — наличие встраивания не значит, что ввод санитизирован
  11. NOT_OVERRIDE_ONLY_FILTER_SAFE — стрип, целящий только RLO/LRO, оставляет RLE/LRE живыми

BASE_FORMULAS:
  RLE_FORM ≠ EFFECT
  RLE_FORM ≠ DISPLAY_ONLY_PROOF
  RLE_FORM ≠ WEAKER_MEANS_SAFE_PROOF
  RLE_FORM ≠ RENDERING_COSMETIC_PROOF
  RLE_FORM ≠ LOGICAL_ORDER_PROOF
  RLE_FORM ≠ ENCODED_SAFETY_PROOF
  RLE_FORM ≠ AUTHORITY
  RLE_FORM ≠ EXECUTION_TRIGGER
  RLE_FORM ≠ INVISIBLE_HARMLESS_PROOF
  RLE_FORM ≠ SANITIZED_PROOF
  RLE_FORM ≠ BALANCED_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: RLE (ZONE_1) имеет параллельные функции (легитимная вложенная RTL-вёрстка vs обман визуального порядка), сосуществующие без культурной прецессии. Полисемия стабильного Bidi_Control.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: управляющий знак форматирования без жестового предшественника; использование для обмана-реордера надстроено цифровой эпохой параллельно легитимной вложенной RTL-вёрстке.

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
    INPUT: "RLE is U+202B in Unicode"
    CONTEXT: название управляющего знака в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLE_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "RLE opens a nested RTL run in a mixed paragraph"
    CONTEXT: описание легитимной вложенной RTL-вёрстки в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLE_FORM ≠ RENDERING_COSMETIC_PROOF
  SAFE_CASE_003:
    INPUT: "the marker is written as <RLE> here"
    CONTEXT: документационный маркер, не байт
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLE_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "embedding respects strong chars; override forces"
    CONTEXT: текст, различающий embedding и override
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLE_FORM ≠ WEAKER_MEANS_SAFE_PROOF
  SAFE_CASE_005:
    INPUT: "a properly terminated embedding (RLE...PDF)"
    CONTEXT: описание сбалансированного легитимного использования
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLE_FORM ≠ BALANCED_PROOF
  SAFE_CASE_006:
    INPUT: "the Bidirectional Algorithm handles direction"
    CONTEXT: текст о UBA
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLE_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: EMBEDDING_CODE_REORDER
    INPUT: 'value = safe <RLE> // danger? <PDF>'
    CONTEXT: встраивание, переупорядочивающее код-ряд для введения ревьюера в заблуждение
    RISK: HIGH
    ATTACK: встраивание переупорядочивает визуальный ряд (тоньше override), так что логика ≠ отображение
    GUARD: RLE_FORM ≠ RENDERING_COSMETIC_PROOF
  RISK_CASE_002:
    NAME: OVERRIDE_FILTER_GAP
    INPUT: "input passing a strip that removes only RLO/LRO overrides"
    CONTEXT: фильтр, нейтрализующий overrides, но оставляющий RLE/LRE embeddings
    RISK: HIGH
    ATTACK: override-only стрип оставляет реордер встраивания живым (слабее ≠ безопасно)
    GUARD: RLE_FORM ≠ OVERRIDE_ONLY_FILTER_SAFE
  RISK_CASE_003:
    NAME: UNTERMINATED_EMBEDDING_BLEED
    INPUT: "label<RLE>rest of the line with no PDF"
    CONTEXT: встраивание без PDF/PDI, растекающее RTL-уровень на последующий контент
    RISK: HIGH
    ATTACK: незавершённое встраивание портит направление всего после своего предполагаемого спана
    GUARD: RLE_FORM ≠ BALANCED_PROOF
  RISK_CASE_004:
    NAME: NESTED_EMBEDDING_CRAFT
    INPUT: "outer<RLE>inner<RLE>...<PDF><PDF> (глубокая вложенность)"
    CONTEXT: вложенные встраивания, создающие многоуровневый реордер, переживающий поверхностные проверки
    RISK: MEDIUM
    ATTACK: глубокая вложенность переупорядочивает сегменты, которые одноуровневая проверка не моделирует
    GUARD: RLE_FORM ≠ EFFECT
  RISK_CASE_005:
    NAME: ENCODED_BIDI_BYPASS
    INPUT: "value%E2%80%ABtail (с поздним декодированием)"
    CONTEXT: percent-кодированный RLE, декодируемый обратно перед отображением
    RISK: HIGH
    ATTACK: "%E2%80%AB" декодируется во встраивание ПОСЛЕ проверки → обман-реордер
    GUARD: RLE_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: BIDI_HOMOGLYPH_STACK
    INPUT: "раyраl<RLE> ... (bidi + confusable-буквы вместе)"
    CONTEXT: встраивание, сложенное с confusable-буквами для углубления спуфа
    RISK: MEDIUM
    ATTACK: встраивание плюс буквы-двойники проводят враждебную строку через поверхностное визуальное ревью
    GUARD: RLE_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨LRE⟩
    CODEPOINT: U+202A
    NAME: LEFT-TO-RIGHT EMBEDDING
    RISK: HIGH
    RULE: LEFT_TO_RIGHT_EMBEDDING ≠ RIGHT_TO_LEFT_EMBEDDING (зеркальное встраивание, противоположный уровень; наивный фильтр их смешивает)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨RLO⟩
    CODEPOINT: U+202E
    NAME: RIGHT-TO-LEFT OVERRIDE
    RISK: HIGH
    RULE: RIGHT_TO_LEFT_OVERRIDE ≠ RIGHT_TO_LEFT_EMBEDDING (override форсирует направление; embedding уважает сильные символы)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨LRO⟩
    CODEPOINT: U+202D
    NAME: LEFT-TO-RIGHT OVERRIDE
    RISK: MEDIUM
    RULE: LEFT_TO_RIGHT_OVERRIDE ≠ RIGHT_TO_LEFT_EMBEDDING
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨RLI⟩
    CODEPOINT: U+2067
    NAME: RIGHT-TO-LEFT ISOLATE
    RISK: MEDIUM
    RULE: RIGHT_TO_LEFT_ISOLATE ≠ RIGHT_TO_LEFT_EMBEDDING (isolate ограничивает и не влияет на окружение; embedding влияет)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨PDF⟩
    CODEPOINT: U+202C
    NAME: POP DIRECTIONAL FORMATTING
    RISK: LOW
    RULE: POP_DIRECTIONAL_FORMATTING ≠ RIGHT_TO_LEFT_EMBEDDING (терминатор, не открывающий; наличие PDF ≠ сбалансировано)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "bidi-встраивание меняет только отображение, значит косметика"
    RESPONSE: RLE_FORM ≠ RENDERING_COSMETIC_PROOF
    RULE: реордер меняет то, что человек одобряет, vs что исполняется/хранится (логика ≠ отображение)
  CG2:
    TRIGGER: "невидимый управляющий символ не может быть опасен"
    RESPONSE: RLE_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: невидимость ортогональна эффекту; RLE управляет рассинхроном визуал/логика
  CG3:
    TRIGGER: "embedding слабее override, значит безопасен"
    RESPONSE: RLE_FORM ≠ WEAKER_MEANS_SAFE_PROOF
    RULE: слабее всё равно переупорядочивает и всё равно обманывает; override-only фильтр его пропускает
  CG4:
    TRIGGER: "'%E2%80%AB' безопасен навсегда"
    RESPONSE: RLE_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно во встраивание перед отображением
  CG5:
    TRIGGER: "стирание RLE останавливает bidi-атаки"
    RESPONSE: RLE_FORM ≠ EFFECT
    RULE: LRE/RLO/LRO/RLI/PDF тоже участвуют; стирание одного символа пропускает семейство
  CG6:
    TRIGGER: "наличие bidi-метки значит, что ввод санитизирован"
    RESPONSE: RLE_FORM ≠ SANITIZED_PROOF
    RULE: наличие знака ничего не говорит о санитизации

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "RLE ... PDF"
      NAME: BALANCED_EMBEDDING_SPAN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: ограниченный вложенный RTL-спан для переупорядочивания конкретного токена
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "RLE (no PDF)"
      NAME: UNTERMINATED_BLEED
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: встраивание без терминатора, растекающее уровень на последующий контент
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "RLE + RLE nesting"
      NAME: DEEP_NESTING
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: вложенные встраивания, создающие многоуровневый реордер
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — последовательности с RLE центральны для обмана визуального порядка.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: RLE переупорядочивает вложенный ряд (маскировка структуры), но не имитирует существование верифицированной сущности. Его риски — рассинхрон визуал/логика, а не мимикрия сущности. (Спуф имени файла естественнее через override; см. RLO/LRO.)
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена RLE на LRE (U+202A) / RLO (U+202E) для обхода RLE-only фильтра
  A2: percent-кодирование "%E2%80%AB" для проскальзывания мимо raw-byte скана
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: реордер кода встраиванием value=safe <RLE> // danger? <PDF>
  B2: пробел override-only фильтра (RLE переживает RLO/LRO стрип)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "RLE ... PDF" (SC1) — ограниченный спан встраивания
  C2: "RLE (no PDF)" (SC2) — незавершённое растекание
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: RLE подан как безобидная вложенная RTL-вёрстка внутри поля кода
  D2: "%E2%80%AB" как «безопасный» кодированный текст с поздним декодированием
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: реордер кода, обманывающий ревьюера
  E2: N/A — вектор: реордер вложенного встраивания, переживающий поверхностную одноуровневую проверку
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: bidi-встраивание — косметика только отображения
  EXPECTED: FAIL_RENDERING_COSMETIC_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: невидимый управляющий символ не может быть опасен
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: embedding слабее override, значит безопасен
  EXPECTED: FAIL_WEAKER_MEANS_SAFE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E2%80%AB" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: стирание только overrides останавливает все bidi-атаки
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: наличие bidi-метки доказывает санитизацию ввода
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как нейтрализовать embeddings И overrides И isolates вместе (всё семейство Bidi_Control) без поломки легитимного вложенного смешанного текста?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (отвергать незавершённые/нарушающие вложенность bidi + рендерить логический порядок для ревью + стирать полное семейство, не только overrides — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «слабее (embedding) не безопаснее; override-only фильтр недостаточен».
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
