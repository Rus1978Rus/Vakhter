PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_NO_BREAK_SPACE_U00A0_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный). Английское зеркало — SIGN_CORE_CARD_NO_BREAK_SPACE_U00A0_GEN3_v0_3_EN. Кодпойнты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_NO_BREAK_SPACE_U00A0_GEN3_v0_3_RU
CODEPOINT: U+00A0
VISIBLE_FORM: ⟨NBSP⟩
UNICODE_NAME: NO-BREAK SPACE
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: неразрывный пробел / пробел, который не U+0020 (обход проверки пробельности)
CATEGORY_ROADMAP: LLM (space-homoglyph injection) · PHAGO: — (маскировка разделителя)
GLYPH_NOTE: VISIBLE_FORM использует маркер ⟨NBSP⟩; сам знак (U+00A0) имеет ВИДИМОЕ продвижение (выглядит как обычный пробел) и НЕ пишется буквально — буквальный U+00A0 маскировался бы под обычный пробел в этом документе. Примеры используют ⟨NBSP⟩/%C2%A0, но не байт.

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
VISIBLE_FORM: ⟨NBSP⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: NBSP_FORM ≠ EFFECT
SIGN_CATEGORY:
  - пробел с видимым продвижением, ЗАПРЕЩАЮЩИЙ перенос строки (держит два слова вместе)
  - легитимная типографика (напр. «10 kg», имя и титул на одной строке)
  - выглядит как обычный пробел, но это U+00A0, НЕ U+0020 (гомоглиф пробела)
  - (при злоупотреблении) обходит проверку пробельности, реагирующую на 0x20, побеждает токенизаторы split-on-space, переживает наивный trim()

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_ORDINARY_SPACE — он отрисовывается как пробел, но это другой кодпойнт (U+00A0 ≠ U+0020)
  2. NOT_WHITESPACE_TO_EVERY_CHECK — проверка, тестирующая только 0x20 (или \t\n\r), не видит его как пробельный
  3. NOT_TRIMMED_BY_DEFAULT — многие trim/strip, реагирующие на ASCII-пробелы, оставляют U+00A0 на месте
  4. NOT_SEPARATOR_GUARANTEE — токенизатор, разбивающий по U+0020, не разобьёт по U+00A0, так что два «слова» останутся одним токеном
  5. NOT_ENCODED_SAFE — «%C2%A0» может быть декодирован обратно в U+00A0 позже
  6. NOT_AUTHORITY — он не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе он ничего не исполняет; он обманывает логику пробельности
  8. NOT_TRUST_SIGNAL — он не повышает доверие
  9. NOT_ZERO_WIDTH — в отличие от ZWSP/WJ у него видимое продвижение; он прячется, выглядя нормальным, а не будучи невидимым
  10. NOT_SANITIZED_PROOF — присутствие символа не означает, что ввод санирован
  11. NOT_EQUAL_STRING_PROOF — «admin » с завершающим U+00A0 не равно «admin» даже после ASCII-trim

BASE_FORMULAS:
  NBSP_FORM ≠ EFFECT
  NBSP_FORM ≠ ORDINARY_SPACE_PROOF
  NBSP_FORM ≠ WHITESPACE_TO_EVERY_CHECK_PROOF
  NBSP_FORM ≠ TRIMMED_BY_DEFAULT_PROOF
  NBSP_FORM ≠ SEPARATOR_GUARANTEE_PROOF
  NBSP_FORM ≠ ENCODED_SAFETY_PROOF
  NBSP_FORM ≠ AUTHORITY
  NBSP_FORM ≠ EXECUTION_TRIGGER
  NBSP_FORM ≠ ZERO_WIDTH_PROOF
  NBSP_FORM ≠ SANITIZED_PROOF
  NBSP_FORM ≠ EQUAL_STRING_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: NBSP (ZONE_1) имеет параллельные функции (легитимная неразрывная типографика vs. обход через гомоглиф пробела), сосуществующие без культурной прецессии. Полисемия стабильного пробельного символа.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: неразрывный пробел с реальной типографской ролью, но без жестового предшественника; злоупотребление через обход пробельности надстроено цифровой эпохой параллельно с легитимным использованием.

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
    INPUT: "NBSP is U+00A0 in Unicode"
    CONTEXT: именование символа в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: NBSP_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "a no-break space keeps two words on one line"
    CONTEXT: описание легитимной типографики в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: NBSP_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <NBSP> here"
    CONTEXT: документационный маркер, не байт
    EXPECTED: INFO
    RISK: NONE
    GUARD: NBSP_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "it looks like a space but is a different codepoint"
    CONTEXT: описание свойства гомоглифа в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: NBSP_FORM ≠ ORDINARY_SPACE_PROOF
  SAFE_CASE_005:
    INPUT: "a Unicode-aware trim can normalize it"
    CONTEXT: описание аккуратной санитизации в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: NBSP_FORM ≠ TRIMMED_BY_DEFAULT_PROOF
  SAFE_CASE_006:
    INPUT: "unlike a zero width space it has a visible advance"
    CONTEXT: отличие от ZWSP в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: NBSP_FORM ≠ ZERO_WIDTH_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: WHITESPACE_CHECK_EVASION
    INPUT: "a required field filled with only U+00A0"
    CONTEXT: проверка «пусто ли», реагирующая на 0x20, видит поле непустым
    RISK: HIGH
    ATTACK: поле проходит проверку непустоты, но отображается пустым, или наоборот
    GUARD: NBSP_FORM ≠ WHITESPACE_TO_EVERY_CHECK_PROOF
  RISK_CASE_002:
    NAME: TRIM_SURVIVAL
    INPUT: "admin<NBSP> submitted where admin is expected"
    CONTEXT: завершающий U+00A0, переживающий ASCII-only trim, так что значение отличается
    RISK: HIGH
    ATTACK: «admin<NBSP>» хранится/сравнивается как отличное от «admin» для выдачи себя за другого или дубликата
    GUARD: NBSP_FORM ≠ EQUAL_STRING_PROOF
  RISK_CASE_003:
    NAME: TOKENIZER_SPLIT_EVASION
    INPUT: "drop<NBSP>table joined by a no-break space"
    CONTEXT: токенизатор split-on-U+0020, держащий два слова как один токен
    RISK: MEDIUM
    ATTACK: два ключевых слова выглядят разделёнными, но токенизируются как одно, побеждая правило границы слова
    GUARD: NBSP_FORM ≠ SEPARATOR_GUARANTEE_PROOF
  RISK_CASE_004:
    NAME: ENCODED_NBSP_BYPASS
    INPUT: "value%C2%A0tail (with a later decode)"
    CONTEXT: percent-кодированный U+00A0, декодируемый обратно перед использованием
    RISK: HIGH
    ATTACK: «%C2%A0» декодируется в U+00A0 ПОСЛЕ проверки → гомоглиф пробела возвращается
    GUARD: NBSP_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: SPACE_HOMOGLYPH_STACK
    INPUT: "a display name using U+00A0 where a space is expected"
    CONTEXT: неразрывный пробел, проходящий за нормальный разделитель при визуальном обзоре
    RISK: MEDIUM
    ATTACK: похожий пробел заставляет подделанное значение читаться как нормальная безобидная строка
    GUARD: NBSP_FORM ≠ ORDINARY_SPACE_PROOF
  RISK_CASE_006:
    NAME: UNICODE_SPACE_FAMILY_GAP
    INPUT: "input using U+2007 / U+202F / U+3000 where only U+00A0 is filtered"
    CONTEXT: другие Unicode-пробелы проскакивают мимо фильтра только-NBSP
    RISK: MEDIUM
    ATTACK: фильтрация только U+00A0 упускает более широкое семейство Unicode-пробелов (figure/narrow/ideographic)
    GUARD: NBSP_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨SP⟩
    CODEPOINT: U+0020
    NAME: SPACE
    RISK: HIGH
    RULE: SPACE ≠ NO_BREAK_SPACE (обычный переносимый ASCII-пробел; U+00A0 отрисовывается так же, но это другой кодпойнт, запрещающий перенос)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨NNBSP⟩
    CODEPOINT: U+202F
    NAME: NARROW NO-BREAK SPACE
    RISK: HIGH
    RULE: NARROW_NO_BREAK_SPACE ≠ NO_BREAK_SPACE (более узкий неразрывный пробел; тот же обход, другой кодпойнт, который фильтр только-NBSP пропускает)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨FIGSP⟩
    CODEPOINT: U+2007
    NAME: FIGURE SPACE
    RISK: MEDIUM
    RULE: FIGURE_SPACE ≠ NO_BREAK_SPACE (неразрывный пробел ширины цифры; ещё один член семейства пробелов)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨IDSP⟩
    CODEPOINT: U+3000
    NAME: IDEOGRAPHIC SPACE
    RISK: MEDIUM
    RULE: IDEOGRAPHIC_SPACE ≠ NO_BREAK_SPACE (широкий CJK-пробел; выглядит просторно, но это ещё один кодпойнт-разделитель)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨ZWNBSP⟩
    CODEPOINT: U+FEFF
    NAME: ZERO WIDTH NO-BREAK SPACE
    RISK: LOW
    RULE: ZERO_WIDTH_NO_BREAK_SPACE ≠ NO_BREAK_SPACE (то же намерение неразрывности, но нулевой ширины и способен быть BOM; U+00A0 имеет видимое продвижение)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "it looks like a space, so it is a space"
    RESPONSE: NBSP_FORM ≠ ORDINARY_SPACE_PROOF
    RULE: он отрисовывается как U+0020, но это U+00A0; равенство и проверки видят другой байт
  CG2:
    TRIGGER: "our whitespace check covers it"
    RESPONSE: NBSP_FORM ≠ WHITESPACE_TO_EVERY_CHECK_PROOF
    RULE: проверка только-0x20 (или только-ASCII) не трактует U+00A0 как пробельный
  CG3:
    TRIGGER: "trim removes trailing spaces, so it is gone"
    RESPONSE: NBSP_FORM ≠ TRIMMED_BY_DEFAULT_PROOF
    RULE: многие trim — только ASCII и оставляют U+00A0 на месте
  CG4:
    TRIGGER: "'%C2%A0' is safe forever"
    RESPONSE: NBSP_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в U+00A0 перед использованием
  CG5:
    TRIGGER: "the tokenizer will split it like a space"
    RESPONSE: NBSP_FORM ≠ SEPARATOR_GUARANTEE_PROOF
    RULE: токенизатор split-on-U+0020 не разбивает по U+00A0; два слова остаются одним токеном
  CG6:
    TRIGGER: "we filter U+00A0, so all lookalike spaces are handled"
    RESPONSE: NBSP_FORM ≠ EFFECT
    RULE: семейство Unicode-пробелов (U+2007/U+202F/U+3000 …) шире, чем один U+00A0
  CG7:
    TRIGGER: "the two strings look the same, so they are equal"
    RESPONSE: NBSP_FORM ≠ EQUAL_STRING_PROOF
    RULE: визуальное сходство не есть равенство байтов; скрытый U+00A0 ломает равенство

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "trailing U+00A0 on a value"
      NAME: TRIM_SURVIVOR
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: завершающий неразрывный пробел, переживающий ASCII-trim и ломающий равенство
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "U+00A0 between two keywords"
      NAME: NO_SPLIT_GLUE
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: два слова, оставленные одним токеном мимо правила split-on-space
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "mixed Unicode spaces (U+00A0 + U+202F + U+2007)"
      NAME: SPACE_FAMILY_MIX
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: несколько кодпойнтов семейства пробелов вместе для обхода фильтра только-NBSP
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — риск NBSP о том, как он сидит внутри пробел-чувствительных последовательностей.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: NBSP маскируется под разделитель (маскировка разделителя), но не имитирует существование верифицированной сущности. Его риски — десинхрон пробельности/равенства, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена U+00A0 на U+202F / U+2007 / U+3000 для смены кодпойнта пробела / обхода фильтра только-NBSP
  A2: percent-кодирование "%C2%A0" для проскока мимо сканера сырых байтов
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: обход проверки пробельности (обязательное поле, заполненное только U+00A0)
  B2: переживание trim (admin<NBSP> не равно admin после ASCII-trim)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "U+00A0 between two keywords" (SC2) — клей без разбиения
  C2: "mixed Unicode spaces" (SC3) — смесь семейства пробелов мимо фильтра только-NBSP
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: U+00A0 подан как обычный пробел, чтобы обозреватель счёл его безобидным
  D2: "%C2%A0" как «безопасный» кодированный текст с последующим декодом
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: путаница разделителя (пробел, который не разбивает)
  E2: N/A — вектор: фильтр только-NBSP, упускающий более широкое семейство Unicode-пробелов
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: неразрывный пробел есть обычный пробел
  EXPECTED: FAIL_ORDINARY_SPACE_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: каждая проверка пробельности трактует U+00A0 как пробельный
  EXPECTED: FAIL_WHITESPACE_TO_EVERY_CHECK_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: trim удаляет U+00A0 по умолчанию
  EXPECTED: FAIL_TRIMMED_BY_DEFAULT_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%C2%A0" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: токенизатор split-on-space разбивает U+00A0
  EXPECTED: FAIL_SEPARATOR_GUARANTEE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: две строки, выглядящие одинаково, равны
  EXPECTED: FAIL_EQUAL_STRING_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как нормализовать всё семейство Unicode-пробелов (U+00A0, U+2007, U+202F, U+3000 …) к канонической форме до проверок пробельности, trim, токенизаторов и равенства — не ломая легитимную неразрывную типографику там, где она важна?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (Unicode-осведомлённый нормализатор пробелов, применяемый согласованно до проверки, trim, токенизации и сравнения — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «U+00A0 выглядит как пробел, но не есть U+0020; ASCII-only логика пробельности/trim/split его упускает, и это лишь один из более широкого семейства пробелов».
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
