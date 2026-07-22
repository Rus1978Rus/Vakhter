PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_MONGOLIAN_VOWEL_SEPARATOR_U180E_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный). Английское зеркало — SIGN_CORE_CARD_MONGOLIAN_VOWEL_SEPARATOR_U180E_GEN3_v0_3_EN. Кодпойнты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_MONGOLIAN_VOWEL_SEPARATOR_U180E_GEN3_v0_3_RU
CODEPOINT: U+180E
VISIBLE_FORM: ⟨MVS⟩
UNICODE_NAME: MONGOLIAN VOWEL SEPARATOR
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: монгольский разделитель гласных / невидимка, чья Unicode-категория ИЗМЕНИЛАСЬ между версиями
CATEGORY_ROADMAP: LLM (invisible version-dependent injection) · PHAGO: — (маскировка токена / пробельности)
GLYPH_NOTE: VISIBLE_FORM использует маркер ⟨MVS⟩; сам знак (U+180E) — невидимый символ (ныне категория Cf) и НИКОГДА не пишется буквально. Примеры используют ⟨MVS⟩/%E1%A0%8E, но не байт. Его свойство менялось между версиями Unicode (когда-то пробел-подобный Zs, теперь Cf-format нулевой ширины), так что разные компоненты расходятся по нему.

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
VISIBLE_FORM: ⟨MVS⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: MVS_FORM ≠ EFFECT
SIGN_CATEGORY:
  - невидимый control монгольской письменности (ныне категория Cf, нулевой ширины)
  - легитимное использование: разделитель гласных в шейпинге монгольского текста
  - его Unicode-свойство ИЗМЕНИЛОСЬ между версиями (исторически трактовался как пробел, Zs; позже переклассифицирован в Cf)
  - (при злоупотреблении) невидимый внутренний символ, чей смысл зависит от версии Unicode, с которой поставляется компонент — пробел версионного расхождения между чекером и исполнителем

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — непечатаемость не делает знак инертным
  2. NOT_STABLE_PROPERTY — его категория/ширина менялись между версиями Unicode; две библиотеки могут классифицировать его по-разному
  3. NOT_ALWAYS_A_SPACE — старые таблицы трактовали его как пробел; новые нет, так что правило пробельности расходится по версии
  4. NOT_DISPLAY_ONLY — у него (ныне) нулевая ширина, но байт проходит сквозь сопоставление и сравнение
  5. NOT_ENCODED_SAFE — «%E1%A0%8E» может быть декодирован обратно в MVS позже
  6. NOT_AUTHORITY — он не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе он ничего не исполняет; он обманывает версионно-чувствительную логику
  8. NOT_TRUST_SIGNAL — он не повышает доверие
  9. NOT_MONGOLIAN_TEXT_ONLY — его риск инъекции не ограничен монгольским контентом
  10. NOT_SANITIZED_PROOF — присутствие символа не означает, что ввод санирован
  11. NOT_SAME_ACROSS_STACK — чекер на одной версии Unicode и исполнитель на другой могут трактовать его по-разному → десинхрон

BASE_FORMULAS:
  MVS_FORM ≠ EFFECT
  MVS_FORM ≠ STABLE_PROPERTY_PROOF
  MVS_FORM ≠ ALWAYS_A_SPACE_PROOF
  MVS_FORM ≠ DISPLAY_ONLY_PROOF
  MVS_FORM ≠ ENCODED_SAFETY_PROOF
  MVS_FORM ≠ AUTHORITY
  MVS_FORM ≠ EXECUTION_TRIGGER
  MVS_FORM ≠ MONGOLIAN_TEXT_ONLY_PROOF
  MVS_FORM ≠ INVISIBLE_HARMLESS_PROOF
  MVS_FORM ≠ SANITIZED_PROOF
  MVS_FORM ≠ SAME_ACROSS_STACK_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: MVS (ZONE_1) имеет параллельные функции (легитимное монгольское разделение гласных vs. невидимая инъекция версионного расхождения), сосуществующие без культурной прецессии. Изменение его Unicode-свойства — артефакт версионирования, не семантическая эпоха знака.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: невидимый control шейпинга без жестового предшественника; злоупотребление через версионное расхождение надстроено цифровой эпохой параллельно с легитимным монгольским использованием.

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
    INPUT: "MVS is U+180E in Unicode"
    CONTEXT: именование символа в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: MVS_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "the Mongolian vowel separator shapes Mongolian text"
    CONTEXT: описание легитимной функции в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: MVS_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <MVS> here"
    CONTEXT: документационный маркер, не байт
    EXPECTED: INFO
    RISK: NONE
    GUARD: MVS_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "its Unicode category changed between versions"
    CONTEXT: описание истории версионирования в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: MVS_FORM ≠ STABLE_PROPERTY_PROOF
  SAFE_CASE_005:
    INPUT: "older tables treated it as whitespace"
    CONTEXT: описание прежней классификации в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: MVS_FORM ≠ ALWAYS_A_SPACE_PROOF
  SAFE_CASE_006:
    INPUT: "a normalizer can strip it consistently across the stack"
    CONTEXT: описание аккуратной санитизации в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: MVS_FORM ≠ SAME_ACROSS_STACK_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: VERSION_SKEW_DESYNC
    INPUT: "a checker on an old Unicode version and an executor on a new one disagreeing on U+180E"
    CONTEXT: один компонент трактует его как пробел, другой как Cf-format нулевой ширины
    RISK: HIGH
    ATTACK: проверка нормализует/разбивает иначе, чем исполнитель → обход в этом пробеле
    GUARD: MVS_FORM ≠ SAME_ACROSS_STACK_PROOF
  RISK_CASE_002:
    NAME: WHITESPACE_ASSUMPTION_GAP
    INPUT: "a trim/blank check assuming U+180E is whitespace"
    CONTEXT: правило, построенное на старой классификации Zs, неверно обрабатывает ныне-Cf символ
    RISK: HIGH
    ATTACK: поле трактуется как пустое/пробел одним слоем, но как контент другим
    GUARD: MVS_FORM ≠ ALWAYS_A_SPACE_PROOF
  RISK_CASE_003:
    NAME: INVISIBLE_IN_IDENTIFIER
    INPUT: "ad<MVS>min vs admin (look-alike username)"
    CONTEXT: невидимый символ внутри ASCII-идентификатора делает его неравным при одинаковом виде
    RISK: MEDIUM
    ATTACK: «ad<MVS>min» регистрируется как двойник «admin» для выдачи себя за другого
    GUARD: MVS_FORM ≠ EFFECT
  RISK_CASE_004:
    NAME: ENCODED_MVS_BYPASS
    INPUT: "value%E1%A0%8Etail (with a later decode)"
    CONTEXT: percent-кодированный MVS, декодируемый обратно перед использованием
    RISK: HIGH
    ATTACK: «%E1%A0%8E» декодируется в MVS ПОСЛЕ проверки → скрытый символ возвращается
    GUARD: MVS_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: NON_MONGOLIAN_CONTEXT_INJECTION
    INPUT: "an MVS dropped into an otherwise Latin/ASCII string"
    CONTEXT: MVS, использованный как обобщённая невидимка, где у него нет легитимной роли
    RISK: MEDIUM
    ATTACK: предполагая, что MVS важен только в монгольском тексте, фильтр игнорирует его в латинском вводе
    GUARD: MVS_FORM ≠ MONGOLIAN_TEXT_ONLY_PROOF
  RISK_CASE_006:
    NAME: INVISIBLE_HOMOGLYPH_STACK
    INPUT: "раy<MVS>раl (invisible char + confusable letters combined)"
    CONTEXT: MVS в связке с похожими буквами для усиления подделки
    RISK: MEDIUM
    ATTACK: невидимый символ плюс буквы-двойники проводят враждебную строку через поверхностный обзор
    GUARD: MVS_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨ZWSP⟩
    CODEPOINT: U+200B
    NAME: ZERO WIDTH SPACE
    RISK: HIGH
    RULE: ZERO_WIDTH_SPACE ≠ MONGOLIAN_VOWEL_SEPARATOR (оба невидимые нулевой ширины, но MVS несёт версионно-изменённое свойство и роль письменности)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨NBSP⟩
    CODEPOINT: U+00A0
    NAME: NO-BREAK SPACE
    RISK: MEDIUM
    RULE: NO_BREAK_SPACE ≠ MONGOLIAN_VOWEL_SEPARATOR (пробел с видимым продвижением; MVS ныне нулевой ширины и раньше был пробел-классифицирован)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨WJ⟩
    CODEPOINT: U+2060
    NAME: WORD JOINER
    RISK: MEDIUM
    RULE: WORD_JOINER ≠ MONGOLIAN_VOWEL_SEPARATOR (невидимый неразрывный клей, не монгольский control шейпинга)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨FVS1⟩
    CODEPOINT: U+180B
    NAME: MONGOLIAN FREE VARIATION SELECTOR ONE
    RISK: MEDIUM
    RULE: MONGOLIAN_FREE_VARIATION_SELECTOR_ONE ≠ MONGOLIAN_VOWEL_SEPARATOR (соседний невидимый монгольский селектор; другая роль шейпинга)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨ZWNBSP⟩
    CODEPOINT: U+FEFF
    NAME: ZERO WIDTH NO-BREAK SPACE
    RISK: LOW
    RULE: ZERO_WIDTH_NO_BREAK_SPACE ≠ MONGOLIAN_VOWEL_SEPARATOR (неразрывный пробел нулевой ширины / BOM; другая невидимка со своей двойной ролью)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "its Unicode property is fixed, so all libs agree"
    RESPONSE: MVS_FORM ≠ STABLE_PROPERTY_PROOF
    RULE: его категория/ширина менялись между версиями; библиотеки на разных версиях расходятся
  CG2:
    TRIGGER: "an invisible char cannot be dangerous"
    RESPONSE: MVS_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: невидимость ортогональна эффекту; MVS создаёт десинхрон версионного расхождения
  CG3:
    TRIGGER: "it is whitespace, trim will drop it"
    RESPONSE: MVS_FORM ≠ ALWAYS_A_SPACE_PROOF
    RULE: только старые таблицы классифицировали его как пробел; новые делают его Cf-format нулевой ширины
  CG4:
    TRIGGER: "'%E1%A0%8E' is safe forever"
    RESPONSE: MVS_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в MVS перед использованием
  CG5:
    TRIGGER: "it only matters inside Mongolian text"
    RESPONSE: MVS_FORM ≠ MONGOLIAN_TEXT_ONLY_PROOF
    RULE: его можно вбросить в любую строку как обобщённую невидимку
  CG6:
    TRIGGER: "checker and executor treat it the same"
    RESPONSE: MVS_FORM ≠ SAME_ACROSS_STACK_PROOF
    RULE: компоненты на разных версиях Unicode могут классифицировать его по-разному → десинхрон

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "U+180E across a version-skewed checker/executor"
      NAME: VERSION_SKEW_GAP
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: MVS, классифицируемый по-разному двумя компонентами в конвейере
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "identifier with an interior MVS"
      NAME: SPLIT_IDENTIFIER
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: MVS внутри ASCII-имени для выдачи себя за другого или победы над сопоставлением
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "MVS + confusable letters"
      NAME: INVISIBLE_HOMOGLYPH_STACK
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: невидимый символ в связке с похожими буквами для подделки
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — ключевой риск MVS именно в межкомпонентном версионном расхождении.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: MVS маскирует токены/пробельность через версионное расхождение (маскировка токена/пробельности), но не имитирует существование верифицированной сущности. Его риски — десинхрон версионного расхождения, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена MVS на ZWSP (U+200B) / WJ (U+2060) для смены невидимого символа / обхода фильтра только-MVS
  A2: percent-кодирование "%E1%A0%8E" для проскока мимо сканера сырых байтов
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: десинхрон версионного расхождения (чекер vs исполнитель классифицируют U+180E по-разному)
  B2: пробел предположения о пробельности (trim, построенный на старой классификации Zs)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "identifier with an interior MVS" (SC2) — разбитый идентификатор
  C2: "MVS + confusable letters" (SC3) — невидимый гомоглиф-стек
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: MVS подан как «безобидный монгольский шейпинг», пока используется как обобщённая невидимка в латинском вводе
  D2: "%E1%A0%8E" как «безопасный» кодированный текст с последующим декодом
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: невидимая путаница идентификаторов (ad<MVS>min vs admin)
  E2: N/A — вектор: пробел версионного расхождения между компонентами на разных версиях Unicode
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: его Unicode-свойство стабильно между версиями
  EXPECTED: FAIL_STABLE_PROPERTY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: невидимый символ не может быть опасен
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: он всегда пробельный
  EXPECTED: FAIL_ALWAYS_A_SPACE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E1%A0%8E" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: он важен только внутри монгольского текста
  EXPECTED: FAIL_MONGOLIAN_TEXT_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: каждый компонент стека трактует его одинаково
  EXPECTED: FAIL_SAME_ACROSS_STACK_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как зафиксировать одну версию Unicode (или одну явную политику невидимых символов) во всех компонентах конвейера, чтобы версионно-изменённый символ вроде U+180E классифицировался идентично чекером и исполнителем, не завися от таблиц, поставляемых каждой библиотекой?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (единая политика нормализации с явным набором невидимок, применяемая до каждой стадии, независимо от Unicode-версий отдельных библиотек — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «Unicode-свойство U+180E менялось между версиями; трактовка его как стабильного или всегда-пробельного приглашает десинхрон чекера/исполнителя».
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
