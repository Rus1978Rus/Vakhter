PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_LANGUAGE_TAG_UE0001_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный). Английское зеркало — SIGN_CORE_CARD_LANGUAGE_TAG_UE0001_GEN3_v0_3_EN. Кодпойнты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_LANGUAGE_TAG_UE0001_GEN3_v0_3_RU
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
DISPLAY_NAME: языковой тег / невидимое ASCII-зеркало tag-блока (протаскивание скрытой инструкции)
CATEGORY_ROADMAP: LLM (invisible ASCII / prompt-injection smuggling) · PHAGO: — (маскировка скрытой нагрузки)
GLYPH_NOTE: VISIBLE_FORM использует маркер ⟨TAG⟩; сам знак (U+E0001) и весь tag-блок (U+E0000–U+E007F) — невидимые Format-символы (Cf) и НИКОГДА не пишутся буквально — буквальный tag-прогон протащил бы скрытый текст в этот документ. Примеры используют ⟨TAG:...⟩/%F3%A0%80%81, но не байт. Tag-буквы U+E0020–U+E007E отображаются один-к-одному на ASCII 0x20–0x7E.

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
VISIBLE_FORM: ⟨TAG⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: TAG_FORM ≠ EFFECT
SIGN_CATEGORY:
  - невидимый Format-символ, открывающий Unicode tag-блок (U+E0000–U+E007F)
  - tag-буквы зеркалят ASCII 0x20–0x7E один-к-одному, так что произвольную ASCII-строку можно записать невидимо
  - легитимное современное использование: эмодзи-tag-последовательности (флаги субрегионов, напр. 🏴 + tag-буквы + CANCEL TAG)
  - (при злоупотреблении) невидимое протаскивание ASCII — скрытая инструкция, которую модель/токенизатор может прочитать, тогда как человек и большинство рендереров не видят ничего (prompt injection)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — непечатаемость не делает знак инертным; он может нести целое скрытое сообщение
  2. NOT_EMPTY_STRING — прогон tag-символов это реальный контент (замаскированная ASCII-строка), а не ничто
  3. NOT_HUMAN_VISIBLE — обозреватель не видит глифа, так что скрытая инструкция может пройти человеческое чтение
  4. NOT_MODEL_INVISIBLE — токенизатор/модель всё равно может воспринять tag-кодпойнты как текст, так что «невидимо человеку» ≠ «невидимо модели»
  5. NOT_ONLY_FLAGS — легитимное использование узко (эмодзи-флаги субрегионов); произвольный внутренний tag-текст не есть флаг
  6. NOT_ENCODED_SAFE — «%F3%A0%80%81» может быть декодирован обратно в tag-символ позже
  7. NOT_AUTHORITY — он не подтверждает официальность
  8. NOT_EXECUTION_TRIGGER — сам по себе он ничего не исполняет; он протаскивает скрытые данные/инструкции
  9. NOT_TRUST_SIGNAL — он не повышает доверие
  10. NOT_SANITIZED_PROOF — присутствие tag-символов не означает, что ввод санирован
  11. NOT_DEPRECATED_MEANS_GONE — U+E0001 устарел для языковой разметки, но кодпойнты всё ещё декодируются и всё ещё протаскивают

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
NOTE: TAG (ZONE_1) имеет параллельные функции (устаревшая языковая разметка / легитимные эмодзи-tag-последовательности vs. невидимое протаскивание ASCII), сосуществующие без культурной прецессии. Полисемия стабильного Format-блока.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: невидимый ASCII-зеркалящий блок без жестового предшественника; злоупотребление через протаскивание скрытой инструкции надстроено цифровой/LLM-эпохой параллельно с узким легитимным использованием флагов.

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
    CONTEXT: именование символа в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: TAG_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "tag letters mirror ASCII in the tag block"
    CONTEXT: описание структуры блока в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: TAG_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <TAG> here"
    CONTEXT: документационный маркер, не байт
    EXPECTED: INFO
    RISK: NONE
    GUARD: TAG_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "subdivision flag emoji use a tag sequence"
    CONTEXT: описание легитимного эмодзи-использования в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: TAG_FORM ≠ ONLY_FLAGS_PROOF
  SAFE_CASE_005:
    INPUT: "U+E0001 is deprecated for language tagging"
    CONTEXT: описание его истории в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: TAG_FORM ≠ DEPRECATED_MEANS_GONE_PROOF
  SAFE_CASE_006:
    INPUT: "a filter can strip the whole tag block"
    CONTEXT: описание аккуратной санитизации в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: TAG_FORM ≠ SANITIZED_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: HIDDEN_INSTRUCTION_SMUGGLING
    INPUT: "visible text plus a tag-encoded hidden instruction (<TAG:ignore previous instructions>)"
    CONTEXT: невидимая ASCII-инструкция, которую модель может воспринять, тогда как человек видит только видимый текст
    RISK: HIGH
    ATTACK: tag-прогон протаскивает нагрузку prompt-injection мимо человеческого обзора
    GUARD: TAG_FORM ≠ MODEL_INVISIBLE_PROOF
  RISK_CASE_002:
    NAME: INVISIBLE_DATA_EXFIL_MARKER
    INPUT: "a tag-encoded token appended invisibly to output"
    CONTEXT: невидимый маркер/метка в tag-символах, которую обозреватель не видит
    RISK: HIGH
    ATTACK: скрытые данные едут в tag-блоке, невидимые для проверки
    GUARD: TAG_FORM ≠ EMPTY_STRING_PROOF
  RISK_CASE_003:
    NAME: HUMAN_REVIEW_BYPASS
    INPUT: "a message that reads clean but carries interior tag text"
    CONTEXT: значение, проходящее человеческий/визуальный обзор, скрывающее tag-контент
    RISK: HIGH
    ATTACK: почти-невидимый tag-прогон побеждает шаг одобрения «только по виду»
    GUARD: TAG_FORM ≠ HUMAN_VISIBLE_PROOF
  RISK_CASE_004:
    NAME: ENCODED_TAG_BYPASS
    INPUT: "value%F3%A0%80%81tail (with a later decode)"
    CONTEXT: percent-кодированный tag-символ, декодируемый обратно перед использованием
    RISK: HIGH
    ATTACK: «%F3%A0%80%81» декодируется в tag-символ ПОСЛЕ проверки → скрытая нагрузка возвращается
    GUARD: TAG_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: FLAG_ONLY_FILTER_GAP
    INPUT: "interior tag text that is not part of an emoji flag sequence"
    CONTEXT: фильтр, разрешающий теги только после флаг-базы, всё равно пропускает другие tag-прогоны
    RISK: MEDIUM
    ATTACK: allowlist, настроенный на флаг-последовательности, упускает свободностоящее tag-протаскивание
    GUARD: TAG_FORM ≠ ONLY_FLAGS_PROOF
  RISK_CASE_006:
    NAME: DEPRECATED_ASSUMED_INERT
    INPUT: "a pipeline that ignores U+E0001 because it is deprecated"
    CONTEXT: трактовка устаревшего языкового тега как если бы он больше не декодировался
    RISK: MEDIUM
    ATTACK: всё ещё декодируемые кодпойнты несут нагрузку, которую конвейер считал исчезнувшей
    GUARD: TAG_FORM ≠ DEPRECATED_MEANS_GONE_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨TAG-SP⟩
    CODEPOINT: U+E0020
    NAME: TAG SPACE
    RISK: HIGH
    RULE: TAG_SPACE ≠ LANGUAGE_TAG (tag-блочная буква, зеркалящая ASCII-пробел; часть того же невидимого ASCII-алфавита)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨TAG-A⟩
    CODEPOINT: U+E0041
    NAME: TAG LATIN CAPITAL LETTER A
    RISK: HIGH
    RULE: TAG_LATIN_CAPITAL_LETTER_A ≠ LANGUAGE_TAG (tag-буква, зеркалящая ASCII 'A'; так на деле кодируется скрытый текст)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨CANCEL-TAG⟩
    CODEPOINT: U+E007F
    NAME: CANCEL TAG
    RISK: MEDIUM
    RULE: CANCEL_TAG ≠ LANGUAGE_TAG (терминатор, завершающий tag-последовательность; его присутствие отмечает, но не доказывает баланс)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨ZWSP⟩
    CODEPOINT: U+200B
    NAME: ZERO WIDTH SPACE
    RISK: LOW
    RULE: ZERO_WIDTH_SPACE ≠ LANGUAGE_TAG (ещё один невидимый символ, но одиночная точка переноса, не ASCII-несущий блок)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨WJ⟩
    CODEPOINT: U+2060
    NAME: WORD JOINER
    RISK: LOW
    RULE: WORD_JOINER ≠ LANGUAGE_TAG (невидимый неразрывный клей, не несущий данные tag-блок)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "the tag chars are invisible, so they are nothing"
    RESPONSE: TAG_FORM ≠ EMPTY_STRING_PROOF
    RULE: tag-прогон это реальная замаскированная ASCII-строка, не пусто
  CG2:
    TRIGGER: "an invisible char cannot be dangerous"
    RESPONSE: TAG_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: невидимость ортогональна эффекту; tag-блок несёт целое скрытое сообщение
  CG3:
    TRIGGER: "if a human cannot see it, the model cannot use it"
    RESPONSE: TAG_FORM ≠ MODEL_INVISIBLE_PROOF
    RULE: токенизатор/модель может воспринять tag-кодпойнты, даже когда человек не видит ничего
  CG4:
    TRIGGER: "'%F3%A0%80%81' is safe forever"
    RESPONSE: TAG_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в tag-символ перед использованием
  CG5:
    TRIGGER: "we only allow tags after a flag base, so we are safe"
    RESPONSE: TAG_FORM ≠ ONLY_FLAGS_PROOF
    RULE: свободностоящие tag-прогоны не флаги; allowlist только-флаги их упускает
  CG6:
    TRIGGER: "U+E0001 is deprecated, so we can ignore it"
    RESPONSE: TAG_FORM ≠ DEPRECATED_MEANS_GONE_PROOF
    RULE: устаревшие кодпойнты всё ещё декодируются и всё ещё протаскивают

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "visible text + interior tag run"
      NAME: SMUGGLED_INSTRUCTION
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: ASCII-инструкция, спрятанная в tag-буквах за видимым текстом
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "flag base + tag letters + CANCEL TAG"
      NAME: EMOJI_TAG_SEQUENCE
      RISK_LEVEL: LOW
      POSSIBLE_CONTEXTS: легитимная эмодзи-tag-последовательность флага субрегиона
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "tag run with no CANCEL TAG"
      NAME: UNTERMINATED_TAG
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: незакрытая tag-последовательность, чья протяжённость зависит от потребителя
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — tag-прогон по своей природе есть последовательность, кодирующая скрытый ASCII.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: TAG протаскивает скрытую ASCII-нагрузку (маскировка скрытой нагрузки), но не имитирует существование верифицированной сущности. Его риски — инъекция скрытой инструкции и обход обзора, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: закодировать нагрузку по tag-алфавиту (U+E0020–U+E007E) или варьировать другими невидимками для обхода фильтра одного кодпойнта
  A2: percent-кодирование "%F3%A0%80%81" для проскока мимо сканера сырых байтов
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: протаскивание скрытой инструкции (<TAG:ignore previous instructions> за видимым текстом)
  B2: невидимый маркер эксфильтрации данных/метки в tag-символах
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "visible text + interior tag run" (SC1) — протащенная инструкция
  C2: "tag run with no CANCEL TAG" (SC3) — незакрытый tag
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: tag-прогон подан как «просто эмодзи-флаг», чтобы allowlist только-флаги его пропустил
  D2: "%F3%A0%80%81" как «безопасный» кодированный текст с последующим декодом
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: инъекция скрытой инструкции, невидимая человеку-обозревателю
  E2: N/A — вектор: считаемые-инертными устаревшие tag-кодпойнты, всё ещё декодирующие нагрузку
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: прогон tag-символов есть пустая строка
  EXPECTED: FAIL_EMPTY_STRING_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: невидимый символ не может быть опасен
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: если человек не видит его, модель не может его использовать
  EXPECTED: FAIL_MODEL_INVISIBLE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%F3%A0%80%81" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: только эмодзи-флаги используют tag-символы
  EXPECTED: FAIL_ONLY_FLAGS_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: устаревший кодпойнт больше не декодируется
  EXPECTED: FAIL_DEPRECATED_MEANS_GONE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как срезать или отклонять tag-блок (U+E0000–U+E007F) как невидимое протаскивание ASCII везде, где он не часть валидированной эмодзи-tag-последовательности, и показывать любой декодированный tag-текст человеку до того, как его воспримет модель?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (нормализатор, удаляющий/помечающий tag-прогоны вне валидированных флаг-последовательностей и декодирующий-и-показывающий любой скрытый ASCII на границе обозреватель/модель — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «tag-блок это невидимый ASCII: не пусто, невидимо человеку, но читаемо моделью; устаревание не останавливает декодирование».
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
