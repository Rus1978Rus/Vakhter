PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_RIGHT_TO_LEFT_OVERRIDE_U202E_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: Русский оригинал (authoritative). Английское зеркало — SIGN_CORE_CARD_RIGHT_TO_LEFT_OVERRIDE_U202E_GEN3_v0_3_EN. Кодпоинты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_RIGHT_TO_LEFT_OVERRIDE_U202E_GEN3_v0_3_RU
CODEPOINT: U+202E
VISIBLE_FORM: ⟨RLO⟩
UNICODE_NAME: RIGHT-TO-LEFT OVERRIDE
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: RTL-переопределение / Trojan Source
CATEGORY_ROADMAP: LLM (bidi визуальный реордер, Trojan Source) · PHAGO: ○ (частично — спуф имени/типа файла)
GLYPH_NOTE: VISIBLE_FORM использует маркер ⟨RLO⟩; сам знак (U+202E) — невидимый Bidi_Control (Cf) и НИКОГДА не пишется литералом здесь — литеральный RLO переупорядочил бы этот документ. Все примеры используют ⟨RLO⟩/⟨PDF⟩/%E2%80%AE, не байт.

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
VISIBLE_FORM: ⟨RLO⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: RLO_FORM ≠ EFFECT
SIGN_CATEGORY:
  - двунаправленное переопределение (форсирует RTL-порядок отображения следующих символов)
  - Unicode Bidi_Control (часть двунаправленного алгоритма)
  - легитимная вёрстка смешанного LTR/RTL-текста
  - (злоупотребление) реордер токенов Trojan Source / спуф расширения файла

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — то, что он непечатаемый, не делает его инертным
  2. NOT_DISPLAY_ONLY — он переупорядочивает ВИЗУАЛЬНЫЙ ряд, а логические байты неизменны (рассинхрон)
  3. NOT_RENDERING_COSMETIC — реордер меняет то, что человек одобряет, vs что исполняется/хранится
  4. NOT_ESCAPED_PROOF — наличие bidi-метки не значит, что она закавычена/экранирована
  5. NOT_ENCODED_SAFE — "%E2%80%AE" может быть раскодирован обратно в переопределение позже
  6. NOT_AUTHORITY — не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе ничего не исполняет; он обманывает читателя
  8. NOT_TRUST_SIGNAL — не повышает доверие
  9. NOT_BALANCED_PROOF — незавершённое переопределение (без PDF/PDI) растекается RTL на остаток
  10. NOT_SANITIZED_PROOF — наличие переопределения не значит, что ввод санитизирован
  11. NOT_LTR_CONTEXT_SAFE — даже внутри LTR-документа он форсирует RTL-ряд

BASE_FORMULAS:
  RLO_FORM ≠ EFFECT
  RLO_FORM ≠ DISPLAY_ONLY_PROOF
  RLO_FORM ≠ RENDERING_COSMETIC_PROOF
  RLO_FORM ≠ LOGICAL_ORDER_PROOF
  RLO_FORM ≠ ESCAPED_PROOF
  RLO_FORM ≠ ENCODED_SAFETY_PROOF
  RLO_FORM ≠ AUTHORITY
  RLO_FORM ≠ EXECUTION_TRIGGER
  RLO_FORM ≠ INVISIBLE_HARMLESS_PROOF
  RLO_FORM ≠ SANITIZED_PROOF
  RLO_FORM ≠ BALANCED_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: RLO (ZONE_1) имеет параллельные функции (легитимная RTL-вёрстка vs обман визуального порядка), сосуществующие без культурной прецессии. Полисемия стабильного Bidi_Control.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: управляющий знак форматирования без жестового предшественника; использование для обмана-реордера надстроено цифровой эпохой параллельно легитимной RTL-вёрстке.

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
    INPUT: "RLO is U+202E in Unicode"
    CONTEXT: название управляющего знака в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLO_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "bidi controls lay out mixed Hebrew/English"
    CONTEXT: описание легитимной RTL-вёрстки в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLO_FORM ≠ RENDERING_COSMETIC_PROOF
  SAFE_CASE_003:
    INPUT: "the marker is written as <RLO> here"
    CONTEXT: документационный маркер, не байт
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLO_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "Arabic and Hebrew are right-to-left scripts"
    CONTEXT: текст об RTL-письменностях (без управляющего байта)
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLO_FORM ≠ DISPLAY_ONLY_PROOF
  SAFE_CASE_005:
    INPUT: "a properly terminated RTL run (RLO...PDF) in an editor"
    CONTEXT: описание сбалансированного легитимного использования
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLO_FORM ≠ BALANCED_PROOF
  SAFE_CASE_006:
    INPUT: "the Bidirectional Algorithm handles direction"
    CONTEXT: текст о UBA
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLO_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: TROJAN_SOURCE_COMMENT_REORDER
    INPUT: 'isAdmin = true <RLO> // safe? <PDF>'
    CONTEXT: переопределение, из-за которого исполняемый код отображается как внутри комментария
    RISK: CRITICAL
    ATTACK: переопределение переупорядочивает визуальный ряд, ревьюер одобряет код, который неверно прочитал (логика ≠ отображение)
    GUARD: RLO_FORM ≠ RENDERING_COSMETIC_PROOF
  RISK_CASE_002:
    NAME: FILENAME_EXTENSION_SPOOF
    INPUT: "resume<RLO>cod.exe"
    CONTEXT: переопределение, разворачивающее хвост, так что ".exe" отображается как ".doc"
    RISK: HIGH
    ATTACK: "cod.exe" отображается развёрнуто как "exe.doc" — опасный файл выглядит как документ
    GUARD: RLO_FORM ≠ DISPLAY_ONLY_PROOF
  RISK_CASE_003:
    NAME: UNTERMINATED_OVERRIDE_BLEED
    INPUT: "label<RLO>rest of the line with no PDF"
    CONTEXT: переопределение без PDF/PDI, форсирующее RTL на всё последующее
    RISK: HIGH
    ATTACK: незавершённое переопределение растекается RTL за свой предполагаемый спан, портя поздние поля
    GUARD: RLO_FORM ≠ BALANCED_PROOF
  RISK_CASE_004:
    NAME: IDENTIFIER_LOGIC_SPOOF
    INPUT: "if (user<RLO>nimda<PDF>) grant()"
    CONTEXT: переопределение, из-за которого идентификатор читается иначе, чем хранится
    RISK: HIGH
    ATTACK: видимый идентификатор отличается от логического, скрывая привилегированную ветку
    GUARD: RLO_FORM ≠ LOGICAL_ORDER_PROOF
  RISK_CASE_005:
    NAME: ENCODED_BIDI_BYPASS
    INPUT: "value%E2%80%AEtail (с поздним декодированием)"
    CONTEXT: percent-кодированный RLO, декодируемый обратно перед отображением
    RISK: HIGH
    ATTACK: "%E2%80%AE" декодируется в переопределение ПОСЛЕ проверки → обман-реордер
    GUARD: RLO_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: BIDI_HOMOGLYPH_STACK
    INPUT: "раyраl<RLO> ... (bidi + confusable-буквы вместе)"
    CONTEXT: переопределение, сложенное с confusable-буквами для углубления спуфа
    RISK: MEDIUM
    ATTACK: переопределение плюс буквы-двойники проводят враждебную строку через поверхностное визуальное ревью
    GUARD: RLO_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨LRO⟩
    CODEPOINT: U+202D
    NAME: LEFT-TO-RIGHT OVERRIDE
    RISK: HIGH
    RULE: LEFT_TO_RIGHT_OVERRIDE ≠ RIGHT_TO_LEFT_OVERRIDE (зеркальное переопределение, реордер в другую сторону; наивный фильтр их смешивает)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨RLE⟩
    CODEPOINT: U+202B
    NAME: RIGHT-TO-LEFT EMBEDDING
    RISK: HIGH
    RULE: RIGHT_TO_LEFT_EMBEDDING ≠ RIGHT_TO_LEFT_OVERRIDE (встраивание vs переопределение; иная сила, похожий реордер)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨LRE⟩
    CODEPOINT: U+202A
    NAME: LEFT-TO-RIGHT EMBEDDING
    RISK: MEDIUM
    RULE: LEFT_TO_RIGHT_EMBEDDING ≠ RIGHT_TO_LEFT_OVERRIDE
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨RLI⟩
    CODEPOINT: U+2067
    NAME: RIGHT-TO-LEFT ISOLATE
    RISK: MEDIUM
    RULE: RIGHT_TO_LEFT_ISOLATE ≠ RIGHT_TO_LEFT_OVERRIDE (isolate ограничивает направление; фильтр, стирающий только RLO, его пропускает)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨ALM⟩
    CODEPOINT: U+061C
    NAME: ARABIC LETTER MARK
    RISK: LOW
    RULE: ARABIC_LETTER_MARK ≠ RIGHT_TO_LEFT_OVERRIDE (bidi-метка, тоже влияющая на порядок, невидима для RLO-only фильтра)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "bidi-переопределение меняет только отображение, значит косметика"
    RESPONSE: RLO_FORM ≠ RENDERING_COSMETIC_PROOF
    RULE: реордер меняет то, что человек одобряет, vs что исполняется/хранится (логика ≠ отображение)
  CG2:
    TRIGGER: "невидимый управляющий символ не может быть опасен"
    RESPONSE: RLO_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: невидимость ортогональна эффекту; RLO управляет рассинхроном визуал/логика
  CG3:
    TRIGGER: "важен логический порядок байтов, значит отображение безопасно"
    RESPONSE: RLO_FORM ≠ LOGICAL_ORDER_PROOF
    RULE: ревьюеры одобряют ОТОБРАЖЕНИЕ; атака живёт в зазоре отображение↔логика
  CG4:
    TRIGGER: "'%E2%80%AE' безопасен навсегда"
    RESPONSE: RLO_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в переопределение перед отображением
  CG5:
    TRIGGER: "стирание RLO останавливает bidi-атаки"
    RESPONSE: RLO_FORM ≠ EFFECT
    RULE: LRO/RLE/LRE/RLI/ALM тоже переупорядочивают; стирание одного символа пропускает семейство
  CG6:
    TRIGGER: "наличие bidi-метки значит, что ввод санитизирован"
    RESPONSE: RLO_FORM ≠ SANITIZED_PROOF
    RULE: наличие знака ничего не говорит о санитизации

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "RLO ... PDF"
      NAME: BALANCED_OVERRIDE_SPAN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: ограниченный спан реордера для переупорядочивания конкретного токена (Trojan Source)
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "RLO (no PDF)"
      NAME: UNTERMINATED_BLEED
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: переопределение без терминатора, растекающее RTL на последующий контент
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "RLO + confusable letters"
      NAME: STACKED_SPOOF
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: переопределение в сочетании с гомоглифами для более глубокого визуального спуфа
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — последовательности с RLO центральны для обмана визуального порядка.

PHAGO_ENTITY_MIMICRY:
  PARTIAL:
    LEVEL: ○
    REASON: базовый механизм RLO — РАССИНХРОН визуал/логика (маскировка структуры), но спуф имени/
      расширения файла (".exe", отображаемый как ".doc") частично имитирует ИДЕНТИЧНОСТЬ безобидного
      типа файла — враждебная сущность в видимом имени безопасной. Частичная мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена RLO на LRO (U+202D) / RLE (U+202B) для обхода RLO-only фильтра
  A2: percent-кодирование "%E2%80%AE" для проскальзывания мимо raw-byte скана
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: реордер комментария Trojan Source isAdmin=true <RLO> // safe? <PDF>
  B2: спуф расширения файла resume<RLO>cod.exe
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "RLO ... PDF" (SC1) — ограниченный спан Trojan Source
  C2: "RLO (no PDF)" (SC2) — незавершённое растекание
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: RLO подан как безобидная RTL-вёрстка внутри поля кода/идентификатора
  D2: "%E2%80%AE" как «безопасный» кодированный текст с поздним декодированием
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: спуф имени/типа — ".exe" в видимой идентичности ".doc" (частичная мимикрия сущности)
  E2: спуф идентификатора — привилегированная ветка в безобидно выглядящем имени
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: bidi-переопределение — косметика только отображения
  EXPECTED: FAIL_RENDERING_COSMETIC_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: невидимый управляющий символ не может быть опасен
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: важен только логический порядок байтов, отображение безопасно
  EXPECTED: FAIL_LOGICAL_ORDER_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E2%80%AE" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: стирание RLO останавливает все bidi-атаки
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
  QUESTION: как детектировать/нейтрализовать bidi-реордер (отвергать несбалансированные спаны, нормализовать) без ложных срабатываний на легитимном смешанном RTL/LTR-тексте?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (отвергать незавершённые/нарушающие вложенность bidi в коде/идентификаторах/именах файлов + рендерить логический порядок для ревью + стирать всё семейство Bidi_Control, не только RLO — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «RLO обманывает через зазор отображение↔логика; безопасность решается контекстом рендера/разбора».
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
