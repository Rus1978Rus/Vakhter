PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_COMBINING_GRAPHEME_JOINER_U034F_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный). Английское зеркало — SIGN_CORE_CARD_COMBINING_GRAPHEME_JOINER_U034F_GEN3_v0_3_EN. Кодпойнты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_COMBINING_GRAPHEME_JOINER_U034F_GEN3_v0_3_RU
CODEPOINT: U+034F
VISIBLE_FORM: ⟨CGJ⟩
UNICODE_NAME: COMBINING GRAPHEME JOINER
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: объединяющий соединитель графем / невидимая КОМБИНИРУЮЩАЯ метка (Mn), меняющая сортировку/сопоставление
CATEGORY_ROADMAP: LLM (invisible combining-mark injection) · PHAGO: — (маскировка сортировки / равенства)
GLYPH_NOTE: VISIBLE_FORM использует маркер ⟨CGJ⟩; сам знак (U+034F) — невидимая КОМБИНИРУЮЩАЯ метка (категория Mn, НЕ Cf) и НИКОГДА не пишется буквально — буквальный CGJ прикрепился бы к предыдущему символу в этом документе. Примеры используют ⟨CGJ⟩/%CD%8F, но не байт.

============================================================
3. REQUIRED_GENERAL_GUARDS
============================================================
REQUIRED_GENERAL_GUARDS:
  - SIGN_FALSE_EFFECT_MIMICRY_GUARD_v0_2A_RU
    GUARD_COMPATIBILITY: применим без изменений — знак не создаёт полей-эффектов
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
VISIBLE_FORM: ⟨CGJ⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: CGJ_FORM ≠ EFFECT
SIGN_CATEGORY:
  - невидимая КОМБИНИРУЮЩАЯ метка (категория Mn) без собственного глифа
  - легитимное использование: блокировать контракцию сортировки или держать последовательность база+комбинирующая как один графем
  - она влияет на ключи сортировки/collation и может влиять на группировку нормализации без всякого видимого изменения
  - (при злоупотреблении) невидимый внутренний символ, меняющий сопоставление/сортировку/равенство при одинаковом виде, и который сканер только-Cf невидимок упускает (это Mn, не Cf)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — непечатаемость не делает знак инертным
  2. NOT_A_FORMAT_CHAR — это КОМБИНИРУЮЩАЯ метка (Mn); сканер, перечисляющий только Format-символы (Cf), её не видит
  3. NOT_NO_EFFECT_ON_SORTING — она может блокировать контракцию сортировки и менять порядок сортировки / ключи collation
  4. NOT_DISPLAY_ONLY — у неё нет глифа, но байт проходит сквозь сравнение, сортировку и нормализацию
  5. NOT_ENCODED_SAFE — «%CD%8F» может быть декодирован обратно в CGJ позже
  6. NOT_AUTHORITY — она не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сама по себе она ничего не исполняет; она обманывает логику сравнения/сортировки
  8. NOT_TRUST_SIGNAL — она не повышает доверие
  9. NOT_NORMALIZED_AWAY_PROOF — NFC/NFD её не удаляют (это не совместимостный символ); присутствие не означает, что она будет свёрнута
  10. NOT_SANITIZED_PROOF — присутствие символа не означает, что ввод санирован
  11. NOT_EQUAL_STRING_PROOF — «admin» и «admin⟨CGJ⟩» выглядят одинаково, но сравниваются неравно

BASE_FORMULAS:
  CGJ_FORM ≠ EFFECT
  CGJ_FORM ≠ FORMAT_CHAR_PROOF
  CGJ_FORM ≠ NO_EFFECT_ON_SORTING_PROOF
  CGJ_FORM ≠ DISPLAY_ONLY_PROOF
  CGJ_FORM ≠ ENCODED_SAFETY_PROOF
  CGJ_FORM ≠ AUTHORITY
  CGJ_FORM ≠ EXECUTION_TRIGGER
  CGJ_FORM ≠ NORMALIZED_AWAY_PROOF
  CGJ_FORM ≠ INVISIBLE_HARMLESS_PROOF
  CGJ_FORM ≠ SANITIZED_PROOF
  CGJ_FORM ≠ EQUAL_STRING_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: CGJ (ZONE_1) имеет параллельные функции (легитимный контроль сортировки/графемов vs. невидимая инъекция равенства/сортировки), сосуществующие без культурной прецессии. Полисемия стабильной комбинирующей метки.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: безглифовый комбинирующий control без жестового предшественника; злоупотребление через инъекцию равенства/сортировки надстроено цифровой эпохой параллельно с легитимным использованием сортировки.

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
    INPUT: "CGJ is U+034F in Unicode"
    CONTEXT: именование символа в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: CGJ_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "a combining grapheme joiner can block a collation contraction"
    CONTEXT: описание легитимной функции в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: CGJ_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <CGJ> here"
    CONTEXT: документационный маркер, не байт
    EXPECTED: INFO
    RISK: NONE
    GUARD: CGJ_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "it is a combining mark, not a format character"
    CONTEXT: описание его Unicode-категории в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: CGJ_FORM ≠ FORMAT_CHAR_PROOF
  SAFE_CASE_005:
    INPUT: "normalization does not remove it"
    CONTEXT: описание поведения NFC/NFD в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: CGJ_FORM ≠ NORMALIZED_AWAY_PROOF
  SAFE_CASE_006:
    INPUT: "it has no glyph of its own"
    CONTEXT: описание его отрисовки в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: CGJ_FORM ≠ DISPLAY_ONLY_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: EQUALITY_BYPASS
    INPUT: "admin<CGJ> registered where admin is expected"
    CONTEXT: невидимая комбинирующая метка делает два идентификатора неравными при одинаковом виде
    RISK: HIGH
    ATTACK: «admin<CGJ>» проходит проверку уникальности как отличное от «admin» для выдачи себя за другого или дубликата
    GUARD: CGJ_FORM ≠ EQUAL_STRING_PROOF
  RISK_CASE_002:
    NAME: CF_ONLY_SCANNER_GAP
    INPUT: "input passing a scanner that enumerates only Format (Cf) invisibles"
    CONTEXT: CGJ проскакивает фильтр, смотрящий только на Cf-format-символы
    RISK: HIGH
    ATTACK: CGJ категории Mn, вне сканирования только-Cf невидимок, так что она выживает
    GUARD: CGJ_FORM ≠ FORMAT_CHAR_PROOF
  RISK_CASE_003:
    NAME: COLLATION_ORDER_SHIFT
    INPUT: "a CGJ inserted to block a collation contraction"
    CONTEXT: CGJ меняет ключ сортировки, так что запись упорядочивается иначе, чем ожидалось
    RISK: MEDIUM
    ATTACK: невидимая метка сдвигает collation, пряча запись от диапазонного запроса или упорядочивая её вне видимости
    GUARD: CGJ_FORM ≠ NO_EFFECT_ON_SORTING_PROOF
  RISK_CASE_004:
    NAME: ENCODED_CGJ_BYPASS
    INPUT: "value%CD%8Ftail (with a later decode)"
    CONTEXT: percent-кодированный CGJ, декодируемый обратно перед использованием
    RISK: HIGH
    ATTACK: «%CD%8F» декодируется в CGJ ПОСЛЕ проверки → скрытая метка возвращается
    GUARD: CGJ_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: NORMALIZATION_ASSUMED_FOLD
    INPUT: "a pipeline assuming NFC removes the CGJ"
    CONTEXT: трактовка нормализации как если бы она срезала комбинирующий соединитель
    RISK: MEDIUM
    ATTACK: NFC/NFD сохраняют CGJ, так что предполагаемая свёртка не происходит и метка сохраняется
    GUARD: CGJ_FORM ≠ NORMALIZED_AWAY_PROOF
  RISK_CASE_006:
    NAME: INVISIBLE_HOMOGLYPH_STACK
    INPUT: "раy<CGJ>раl (combining mark + confusable letters combined)"
    CONTEXT: CGJ в связке с похожими буквами для усиления подделки
    RISK: MEDIUM
    ATTACK: невидимая метка плюс буквы-двойники проводят враждебную строку через поверхностный обзор
    GUARD: CGJ_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨ZWJ⟩
    CODEPOINT: U+200D
    NAME: ZERO WIDTH JOINER
    RISK: HIGH
    RULE: ZERO_WIDTH_JOINER ≠ COMBINING_GRAPHEME_JOINER («joiner» только в названии: ZWJ — Cf-format-символ, соединяющий глифы; CGJ — Mn-комбинирующая метка, влияющая на collation)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨ZWNJ⟩
    CODEPOINT: U+200C
    NAME: ZERO WIDTH NON-JOINER
    RISK: MEDIUM
    RULE: ZERO_WIDTH_NON_JOINER ≠ COMBINING_GRAPHEME_JOINER (Cf-control соединения, не Mn-метка collation)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨ZWSP⟩
    CODEPOINT: U+200B
    NAME: ZERO WIDTH SPACE
    RISK: MEDIUM
    RULE: ZERO_WIDTH_SPACE ≠ COMBINING_GRAPHEME_JOINER (Cf-точка переноса, не комбинирующая метка)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨COMBINING-ACUTE⟩
    CODEPOINT: U+0301
    NAME: COMBINING ACUTE ACCENT
    RISK: MEDIUM
    RULE: COMBINING_ACUTE_ACCENT ≠ COMBINING_GRAPHEME_JOINER (ВИДИМЫЙ комбинирующий акцент в том же блоке; CGJ безглифов)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨VS16⟩
    CODEPOINT: U+FE0F
    NAME: VARIATION SELECTOR-16
    RISK: LOW
    RULE: VARIATION_SELECTOR_16 ≠ COMBINING_GRAPHEME_JOINER (селектор вариации, запрашивающий эмодзи-представление; другой невидимый механизм)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "our scanner covers the invisible format chars, so we are covered"
    RESPONSE: CGJ_FORM ≠ FORMAT_CHAR_PROOF
    RULE: CGJ — комбинирующая метка (Mn), не Format-символ (Cf); сканирование только-Cf её упускает
  CG2:
    TRIGGER: "an invisible char cannot be dangerous"
    RESPONSE: CGJ_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: невидимость ортогональна эффекту; CGJ меняет collation и равенство
  CG3:
    TRIGGER: "it has no glyph, so it cannot change sorting"
    RESPONSE: CGJ_FORM ≠ NO_EFFECT_ON_SORTING_PROOF
    RULE: она блокирует контракции сортировки и сдвигает ключи сортировки
  CG4:
    TRIGGER: "'%CD%8F' is safe forever"
    RESPONSE: CGJ_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в CGJ перед использованием
  CG5:
    TRIGGER: "normalization strips it"
    RESPONSE: CGJ_FORM ≠ NORMALIZED_AWAY_PROOF
    RULE: NFC/NFD сохраняют CGJ; присутствие не подразумевает свёртку
  CG6:
    TRIGGER: "the two strings look the same, so they are equal"
    RESPONSE: CGJ_FORM ≠ EQUAL_STRING_PROOF
    RULE: визуальное сходство не есть равенство байтов; скрытый CGJ ломает равенство

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "identifier with an interior CGJ"
      NAME: EQUALITY_SPLIT
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: CGJ внутри ASCII-идентификатора, побеждающий проверку уникальности/равенства
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "CGJ blocking a collation contraction"
      NAME: COLLATION_SHIFT
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: CGJ, сдвигающий порядок сортировки, чтобы спрятать или сместить запись
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "CGJ + confusable letters"
      NAME: INVISIBLE_HOMOGLYPH_STACK
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: комбинирующая метка в связке с похожими буквами для подделки
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — эффект CGJ на сравнение/collation окружающей последовательности.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: CGJ маскирует равенство/collation (маскировка сортировки/равенства), но не имитирует существование верифицированной сущности. Его риски — десинхрон сравнения/сортировки, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена CGJ на ZWJ (U+200D) / ZWSP (U+200B) для смены невидимого символа / обхода фильтра, моделирующего одну категорию
  A2: percent-кодирование "%CD%8F" для проскока мимо сканера сырых байтов
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: обход равенства (admin<CGJ> не равно admin)
  B2: пробел сканера только-Cf (Mn-комбинирующая метка переживает сканирование Format-символов)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "CGJ blocking a collation contraction" (SC2) — сдвиг collation
  C2: "CGJ + confusable letters" (SC3) — невидимый гомоглиф-стек
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: CGJ подан как безобидный «контроль графемов», пока он меняет равенство/collation
  D2: "%CD%8F" как «безопасный» кодированный текст с последующим декодом
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: невидимая путаница идентификаторов (admin<CGJ> vs admin)
  E2: N/A — вектор: предполагаемая-свёртка нормализации, оставляющая метку на месте
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: CGJ это Format-символ, ловимый сканированием Cf
  EXPECTED: FAIL_FORMAT_CHAR_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: невидимый символ не может быть опасен
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: безглифовая метка не может менять сортировку
  EXPECTED: FAIL_NO_EFFECT_ON_SORTING_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%CD%8F" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: нормализация удаляет CGJ
  EXPECTED: FAIL_NORMALIZED_AWAY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: две строки, выглядящие одинаково, равны
  EXPECTED: FAIL_EQUAL_STRING_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как перечислить невидимые символы по их фактическому эффекту (Default_Ignorable / комбинирующий / формат), а не по одной Unicode-категории, чтобы Mn-метка вроде CGJ ловилась наряду с Cf-невидимками до равенства/collation, не ломая легитимные комбинирующие последовательности?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (нормализатор, реагирующий на свойства Default_Ignorable_Code_Point и комбинирования, применяемый до сравнения/сортировки/уникальности — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «CGJ — невидимая комбинирующая метка (Mn), не Format-символ; она меняет collation/равенство, и нормализация её не удаляет».
ALL_OPEN_QUESTIONS_CLOSED: NO (delegated, non-blocking)

============================================================
11. PATCH_HISTORY
============================================================
PATCH_HISTORY:
  v0_1_PATCH_01: первичное создание (Ruslan Malyavsky, 2026-07-22) — черновик из шаблона GEN3_v0_3 (Vakhter); не конвейер-ран.
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
