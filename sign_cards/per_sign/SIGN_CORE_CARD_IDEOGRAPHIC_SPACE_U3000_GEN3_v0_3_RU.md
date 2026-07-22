PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_IDEOGRAPHIC_SPACE_U3000_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный). Английское зеркало — SIGN_CORE_CARD_IDEOGRAPHIC_SPACE_U3000_GEN3_v0_3_EN. Кодпойнты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_IDEOGRAPHIC_SPACE_U3000_GEN3_v0_3_RU
CODEPOINT: U+3000
VISIBLE_FORM: ⟨IDSP⟩
UNICODE_NAME: IDEOGRAPHIC SPACE
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: идеографический пробел / полноширинный CJK-пробел, который не U+0020 (обход семейства пробелов)
CATEGORY_ROADMAP: LLM (space-homoglyph injection) · PHAGO: — (маскировка разделителя)
GLYPH_NOTE: VISIBLE_FORM использует маркер ⟨IDSP⟩; сам знак (U+3000) имеет широкое ВИДИМОЕ продвижение (полноширинный пробел) и НЕ пишется буквально — буквальный U+3000 маскировался бы под отступ в этом документе. Примеры используют ⟨IDSP⟩/%E3%80%80, но не байт.

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
VISIBLE_FORM: ⟨IDSP⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: IDSP_FORM ≠ EFFECT
SIGN_CATEGORY:
  - полноширинный (em-широкий) пробел, используемый в CJK-типографике
  - легитимное использование: отступы/выравнивание в CJK-тексте и формах
  - выглядит как щедрый отступ, но это U+3000, НЕ U+0020 (гомоглиф пробела, переносимый)
  - (при злоупотреблении) обходит проверку пробельности, реагирующую на 0x20, и проскакивает мимо фильтра, настроенного только на U+00A0 / U+202F

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_ORDINARY_SPACE — он отрисовывается как широкий отступ, но это другой кодпойнт (U+3000 ≠ U+0020)
  2. NOT_ASCII_TRIMMED — ASCII-only trim/strip, реагирующий на 0x20, оставляет U+3000 на месте
  3. NOT_WHITESPACE_TO_EVERY_CHECK — проверка, тестирующая только 0x20, не видит его как пробельный
  4. NOT_SEPARATOR_GUARANTEE — токенизатор, разбивающий по U+0020, не разобьёт по U+3000, так что два «слова» останутся одним токеном
  5. NOT_ENCODED_SAFE — «%E3%80%80» может быть декодирован обратно в U+3000 позже
  6. NOT_AUTHORITY — он не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе он ничего не исполняет; он обманывает логику пробельности
  8. NOT_SINGLE_SPACE_FAMILY_MEMBER — это один из более широкого семейства Unicode-пробелов (U+00A0/U+202F/U+2000-200A/U+205F); фильтрация только его упускает остальные
  9. NOT_ZERO_WIDTH — у него широкое видимое продвижение; он прячется, выглядя как обычный отступ, а не будучи невидимым
  10. NOT_SANITIZED_PROOF — присутствие символа не означает, что ввод санирован
  11. NOT_EQUAL_STRING_PROOF — две строки, выглядящие одинаково, могут различаться скрытым U+3000

BASE_FORMULAS:
  IDSP_FORM ≠ EFFECT
  IDSP_FORM ≠ ORDINARY_SPACE_PROOF
  IDSP_FORM ≠ ASCII_TRIMMED_PROOF
  IDSP_FORM ≠ WHITESPACE_TO_EVERY_CHECK_PROOF
  IDSP_FORM ≠ SEPARATOR_GUARANTEE_PROOF
  IDSP_FORM ≠ ENCODED_SAFETY_PROOF
  IDSP_FORM ≠ AUTHORITY
  IDSP_FORM ≠ EXECUTION_TRIGGER
  IDSP_FORM ≠ SINGLE_SPACE_FAMILY_MEMBER_PROOF
  IDSP_FORM ≠ ZERO_WIDTH_PROOF
  IDSP_FORM ≠ SANITIZED_PROOF
  IDSP_FORM ≠ EQUAL_STRING_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: IDSP (ZONE_1) имеет параллельные функции (легитимный CJK-отступ vs. обход через гомоглиф пробела), сосуществующие без культурной прецессии. Полисемия стабильного пробельного символа.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: полноширинный пробел с реальной типографской ролью, но без жестового предшественника; злоупотребление через обход пробельности надстроено цифровой эпохой параллельно с легитимным CJK-использованием.

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
    INPUT: "IDSP is U+3000 in Unicode"
    CONTEXT: именование символа в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: IDSP_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "an ideographic space is used for CJK spacing"
    CONTEXT: описание легитимной типографики в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: IDSP_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <IDSP> here"
    CONTEXT: документационный маркер, не байт
    EXPECTED: INFO
    RISK: NONE
    GUARD: IDSP_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "it looks like wide spacing but is a different codepoint"
    CONTEXT: описание свойства гомоглифа в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: IDSP_FORM ≠ ORDINARY_SPACE_PROOF
  SAFE_CASE_005:
    INPUT: "it is one of a wider Unicode space family"
    CONTEXT: описание семейства пробелов в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: IDSP_FORM ≠ SINGLE_SPACE_FAMILY_MEMBER_PROOF
  SAFE_CASE_006:
    INPUT: "a Unicode-aware normalizer can fold it"
    CONTEXT: описание аккуратной санитизации в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: IDSP_FORM ≠ ASCII_TRIMMED_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: ASCII_ONLY_FILTER_GAP
    INPUT: "input using U+3000 where a filter only handles U+0020 / U+00A0"
    CONTEXT: полноширинный пробел проскакивает мимо ASCII/NBSP-only нормализатора
    RISK: HIGH
    ATTACK: фильтр обрабатывает обычные пробелы, но не U+3000, так что гомоглиф пробела выживает
    GUARD: IDSP_FORM ≠ SINGLE_SPACE_FAMILY_MEMBER_PROOF
  RISK_CASE_002:
    NAME: TRIM_SURVIVAL
    INPUT: "admin<IDSP> submitted where admin is expected"
    CONTEXT: завершающий U+3000, переживающий ASCII-only trim, так что значение отличается
    RISK: HIGH
    ATTACK: «admin<IDSP>» хранится/сравнивается как отличное от «admin» для выдачи себя за другого или дубликата
    GUARD: IDSP_FORM ≠ EQUAL_STRING_PROOF
  RISK_CASE_003:
    NAME: TOKENIZER_SPLIT_EVASION
    INPUT: "drop<IDSP>table joined by a full-width space"
    CONTEXT: токенизатор split-on-U+0020, держащий два слова как один токен
    RISK: MEDIUM
    ATTACK: два ключевых слова выглядят разделёнными, но токенизируются как одно, побеждая правило границы слова
    GUARD: IDSP_FORM ≠ SEPARATOR_GUARANTEE_PROOF
  RISK_CASE_004:
    NAME: ENCODED_IDSP_BYPASS
    INPUT: "value%E3%80%80tail (with a later decode)"
    CONTEXT: percent-кодированный U+3000, декодируемый обратно перед использованием
    RISK: HIGH
    ATTACK: «%E3%80%80» декодируется в U+3000 ПОСЛЕ проверки → гомоглиф пробела возвращается
    GUARD: IDSP_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: WHITESPACE_CHECK_EVASION
    INPUT: "a required field filled with only U+3000"
    CONTEXT: проверка «пусто ли», реагирующая на 0x20, видит поле непустым
    RISK: MEDIUM
    ATTACK: поле проходит проверку непустоты, но отображается пустым, или наоборот
    GUARD: IDSP_FORM ≠ WHITESPACE_TO_EVERY_CHECK_PROOF
  RISK_CASE_006:
    NAME: SPACE_FAMILY_MIX
    INPUT: "input mixing U+3000 with U+00A0 / U+202F / U+2009"
    CONTEXT: несколько кодпойнтов семейства пробелов вместе для победы над фильтром одного кодпойнта
    RISK: MEDIUM
    ATTACK: обработка одного кодпойнта пробела за раз упускает более широкое семейство Unicode-пробелов
    GUARD: IDSP_FORM ≠ ORDINARY_SPACE_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨SP⟩
    CODEPOINT: U+0020
    NAME: SPACE
    RISK: HIGH
    RULE: SPACE ≠ IDEOGRAPHIC_SPACE (обычный ASCII-пробел; U+3000 отрисовывается шире и это другой кодпойнт, который ASCII-проверка упускает)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨NBSP⟩
    CODEPOINT: U+00A0
    NAME: NO-BREAK SPACE
    RISK: HIGH
    RULE: NO_BREAK_SPACE ≠ IDEOGRAPHIC_SPACE (неразрывный пробел; U+3000 переносимый и полноширинный — другой член семейства пробелов)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨NNBSP⟩
    CODEPOINT: U+202F
    NAME: NARROW NO-BREAK SPACE
    RISK: MEDIUM
    RULE: NARROW_NO_BREAK_SPACE ≠ IDEOGRAPHIC_SPACE (узкий неразрывный пробел; противоположная ширина, ещё один член семейства)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨ENSP⟩
    CODEPOINT: U+2002
    NAME: EN SPACE
    RISK: MEDIUM
    RULE: EN_SPACE ≠ IDEOGRAPHIC_SPACE (фиксированной ширины en-пробел; ещё один видимый кодпойнт пробела в семействе)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨MMSP⟩
    CODEPOINT: U+205F
    NAME: MEDIUM MATHEMATICAL SPACE
    RISK: LOW
    RULE: MEDIUM_MATHEMATICAL_SPACE ≠ IDEOGRAPHIC_SPACE (пробел математического контекста; ещё один член семейства, который фильтр одного кодпойнта упускает)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "it looks like spacing, so it is a space"
    RESPONSE: IDSP_FORM ≠ ORDINARY_SPACE_PROOF
    RULE: он отрисовывается как широкий отступ, но это U+3000; равенство и проверки видят другой байт
  CG2:
    TRIGGER: "trim removes trailing spaces, so it is gone"
    RESPONSE: IDSP_FORM ≠ ASCII_TRIMMED_PROOF
    RULE: ASCII-only trim оставляет U+3000 на месте
  CG3:
    TRIGGER: "our whitespace check covers it"
    RESPONSE: IDSP_FORM ≠ WHITESPACE_TO_EVERY_CHECK_PROOF
    RULE: проверка только-0x20 не трактует U+3000 как пробельный
  CG4:
    TRIGGER: "'%E3%80%80' is safe forever"
    RESPONSE: IDSP_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в U+3000 перед использованием
  CG5:
    TRIGGER: "the tokenizer will split it like a space"
    RESPONSE: IDSP_FORM ≠ SEPARATOR_GUARANTEE_PROOF
    RULE: токенизатор split-on-U+0020 не разбивает по U+3000; два слова остаются одним токеном
  CG6:
    TRIGGER: "we filter U+3000, so all lookalike spaces are handled"
    RESPONSE: IDSP_FORM ≠ SINGLE_SPACE_FAMILY_MEMBER_PROOF
    RULE: семейство Unicode-пробелов (U+00A0/U+202F/U+2000-200A/U+205F …) шире, чем один U+3000
  CG7:
    TRIGGER: "the two strings look the same, so they are equal"
    RESPONSE: IDSP_FORM ≠ EQUAL_STRING_PROOF
    RULE: визуальное сходство не есть равенство байтов; скрытый U+3000 ломает равенство

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "trailing U+3000 on a value"
      NAME: TRIM_SURVIVOR
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: завершающий полноширинный пробел, переживающий ASCII-trim и ломающий равенство
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "U+3000 between two keywords"
      NAME: NO_SPLIT_GLUE
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: два слова, оставленные одним токеном мимо правила split-on-space
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "mixed Unicode spaces (U+3000 + U+00A0 + U+202F)"
      NAME: SPACE_FAMILY_MIX
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: несколько кодпойнтов семейства пробелов вместе для обхода фильтра одного кодпойнта
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — риск IDSP о том, как он сидит внутри пробел-чувствительных последовательностей.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: IDSP маскируется под разделитель (маскировка разделителя), но не имитирует существование верифицированной сущности. Его риски — десинхрон пробельности/равенства, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена U+3000 на U+00A0 / U+202F / U+2002 для смены кодпойнта пробела / обхода фильтра одного кодпойнта
  A2: percent-кодирование "%E3%80%80" для проскока мимо сканера сырых байтов
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: пробел ASCII/NBSP-only фильтра (U+3000 переживает фолдинг, обрабатывающий только обычные пробелы)
  B2: переживание trim (admin<IDSP> не равно admin после ASCII-trim)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "U+3000 between two keywords" (SC2) — клей без разбиения
  C2: "mixed Unicode spaces" (SC3) — смесь семейства пробелов мимо фильтра одного кодпойнта
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: U+3000 подан как обычный широкий отступ, чтобы обозреватель счёл его безобидным
  D2: "%E3%80%80" как «безопасный» кодированный текст с последующим декодом
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: путаница разделителя (пробел, который не разбивает)
  E2: N/A — вектор: фильтр одного кодпойнта, упускающий более широкое семейство Unicode-пробелов
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: идеографический пробел есть обычный пробел
  EXPECTED: FAIL_ORDINARY_SPACE_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: ASCII-trim удаляет U+3000
  EXPECTED: FAIL_ASCII_TRIMMED_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: каждая проверка пробельности трактует U+3000 как пробельный
  EXPECTED: FAIL_WHITESPACE_TO_EVERY_CHECK_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E3%80%80" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: токенизатор split-on-space разбивает U+3000
  EXPECTED: FAIL_SEPARATOR_GUARANTEE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: фильтрация U+3000 обрабатывает все похожие пробелы
  EXPECTED: FAIL_SINGLE_SPACE_FAMILY_MEMBER_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как нормализовать всё семейство Unicode-пробелов (U+00A0, U+202F, U+2000-200A, U+205F, U+3000 …) к канонической форме до проверок пробельности, trim, токенизаторов и равенства — не ломая легитимный CJK/типографский отступ там, где он важен?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (Unicode-осведомлённый нормализатор пробелов, применяемый согласованно до проверки, trim, токенизации и сравнения — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «U+3000 выглядит как широкий отступ, но это не U+0020; ASCII-only или фильтр одного кодпойнта его упускает, и это один из более широкого семейства пробелов».
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
