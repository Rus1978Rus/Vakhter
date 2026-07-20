ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_DIGIT_CLASS_0-9_GEN3_v0_1_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU

DRAFT_NOTE (внешняя заготовка, 2026-07-20): черновик КЛАССОВОЙ карточки
  цифр 0–9 для входа в конвейер. НЕ прогонялся через конвейер, НЕ
  author-decided. Содержит ДВА слоя (см. раздел 4): SURFACE (цифра как
  число/хост/двойник) и CARRIER — "двойное дно": цифра как атом
  кодировки, способный воссоздать ЛЮБОЙ другой знак, включая охраняемые
  (точка, солидус, @) и невидимые (ZWSP через &#8203;). Класс-карточка —
  общий каркас; специфика отдельных цифр (0,1,5) вынесена в приложение A
  под будущие per-digit карточки.

============================================================
0. UNIVERSALITY
============================================================

BOUND_TO_SPECIFIC_SIGN: CLASS (0 1 2 3 4 5 6 7 8 9)
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
  WORKINGLY_CLOSED: NO

============================================================
2. META
============================================================

ZONE: ZONE_1 (стабильный письменный знак, полисемичный)
WHY_THIS_SIGN_MATTERS: цифра — не только число. Она базовый атом
  систем кодирования (percent, HTML-entity, unicode-escape, radix),
  а значит потенциальный переносчик любого другого знака мимо его
  собственной карточки. Плюс она формирует числовые хосты (IP), где
  точка ведёт себя иначе, чем между доменными метками.
INTERACTS_WITH: DOT (U+002E), SOLIDUS (U+002F), AT (U+0040),
  INVISIBLE_CLASS (ZWSP/ZWJ/BOM) — все они воссоздаваемы цифрами.

============================================================
3. REQUIRED_GENERAL_GUARDS
============================================================

RAW_SIGN_INPUT_STATUS: DATA_ONLY
NO_EXECUTION_FROM_SIGN: YES
NO_TRUST_FROM_SIGN: YES
DECODE_BEFORE_TRUST: YES  (см. раздел 10 — CANONICALIZATION_PRE_PASS)

============================================================
4. SIGN IDENTITY — LAYER_A: STABLE CORE
LAYER_A_LOCK: PERMANENT
============================================================

VISIBLE_FORM: 0 1 2 3 4 5 6 7 8 9
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY

BASE_MODE: DATA_ONLY_GLYPH
BASE_MODE_FORMULA: DIGIT_FORM ≠ EFFECT

DUAL_LAYER: YES   # "двойное дно" — семья невидимых по типу опасности
  SURFACE_LAYER: цифра как числовое значение (версия, счёт, дата, хост)
  CARRIER_LAYER: цифра как АТОМ КОДИРОВКИ — может воссоздать другой знак
    (percent %2e, HTML-entity &#46;, unicode-escape ., radix-IP).
  PARALLEL: как невидимый знак "есть, но не виден", цифра "видна, но не
    то, чем кажется" — оба про КАНОНИЗАЦИЮ до сравнения.

SIGN_CATEGORY:
  - numeral (числовое значение)
  - radix_digit (основание записи: dec/hex/oct/bin)
  - encoding_atom (percent / numeric-entity / escape)
  - network_host_component (октет IP)
  - potential_letter_lookalike (0/O, 1/l/I, 5/S, 6/b, 8/B)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_LITERAL_VALUE_ONLY — цифра может быть частью кодировки,
     воссоздающей другой знак (%2e -> ".", &#8203; -> ZWSP)
  2. NOT_FINAL_SURFACE — то, что дошло цифрами, может декодироваться
     в иной знак; проверять до декодирования нельзя
  3. NOT_HOST_VALIDITY_PROOF — цифры+точки, сложившиеся в IP, не
     доказывают безопасность хоста (внутренние сети, метаданные)
  4. NOT_LETTER — цифра, похожая на букву (0/O, 1/l), не есть эта буква
  5. NOT_ASCII_GUARANTEE — глиф, похожий на цифру, может быть не-ASCII
     цифрой (полноширинная, арабо-индийская) с другим кодом
  6. NOT_VERSION_TRUST — число версии/индекса не доказывает надёжность
  7. NOT_EXECUTION_TRIGGER — цифра сама по себе ничего не запускает

BASE_FORMULAS:
  DIGIT_FORM ≠ NUMERIC_VALUE_ONLY
  DIGIT_FORM ≠ FINAL_SURFACE
  DIGIT_FORM ≠ HOST_VALIDITY_PROOF
  DIGIT_FORM ≠ LETTER
  DIGIT_FORM ≠ ASCII_GUARANTEE
  DIGIT_FORM ≠ VERSION_TRUST
  DIGIT_FORM ≠ EXECUTION_TRIGGER

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================

EPOCH_TRACKER: NOT_APPLICABLE
NOTE: цифры имеют несколько ОДНОВРЕМЕННЫХ функций (счёт, разряд системы
  счисления, октет хоста, атом кодировки) без культурной прецессии одной
  над другой — полисемия стабильного класса, не смена эпох.

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
7. SAFE / RISK / CONFUSABLES / GUARDS — LAYER_B: SEMI-STABLE LAYER
LAYER_B_LOCK: REVIEWABLE
============================================================

SAFE_CASES:
  SAFE_CASE_001:
    INPUT: "version 1.0"
    CONTEXT: номер версии в свободном тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: DIGIT_FORM ≠ VERSION_TRUST
  SAFE_CASE_002:
    INPUT: "3.14"
    CONTEXT: десятичная дробь
    EXPECTED: INFO
    RISK: NONE
    GUARD: DIGIT_FORM ≠ NUMERIC_VALUE_ONLY (десятичный контекст)
  SAFE_CASE_003:
    INPUT: "год 2026, дом 12, +7 900 000 00 00"
    CONTEXT: год / номер / телефон — обычные числа
    EXPECTED: INFO
    RISK: NONE
    GUARD: none required
  SAFE_CASE_004:
    INPUT: "1. Первый пункт  2. Второй пункт"
    CONTEXT: нумерация списка
    EXPECTED: INFO
    RISK: NONE
    GUARD: none required
  SAFE_CASE_005:
    INPUT: "символ %2f в URL означает слэш"
    CONTEXT: текст ОБ кодировке (мета-упоминание), не сама атака
    EXPECTED: INFO
    RISK: NONE
    GUARD: DECODE_ONLY_IN_EXECUTABLE_POSITION (не декодировать
      пояснительный текст) — см. LIMITATION

RISK_CASES:
  # ---- SURFACE LAYER (цифра как хост / двойник) ----
  RISK_CASE_001:
    NAME: IP_HOST_INTERNAL_SSRF
    INPUT: "http://192.168.0.1/admin"
    CONTEXT: числовой хост в приватном диапазоне в позиции URL
    RISK: HIGH
    ATTACK: цифры+точки образуют внутренний IP -> стук во внутреннюю
      сеть (SSRF), минуя доменную репутацию
    GUARD: DIGIT_FORM ≠ HOST_VALIDITY_PROOF
  RISK_CASE_002:
    NAME: IP_HOST_CLOUD_METADATA
    INPUT: "http://169.254.169.254/latest/meta-data/"
    CONTEXT: link-local адрес облачных метаданных
    RISK: HIGH
    ATTACK: доступ к облачным метаданным/кредам через SSRF — один из
      самых опасных числовых хостов
    GUARD: DIGIT_FORM ≠ HOST_VALIDITY_PROOF
  RISK_CASE_003:
    NAME: ALT_IP_ENCODING_OBFUSCATION
    INPUT: "http://2130706433/  |  http://0x7f000001/  |  http://0177.0.0.1/"
    CONTEXT: 127.0.0.1 записан десятично / hex / octal
    RISK: HIGH
    ATTACK: чистыми цифрами (иное основание) переписан IP, чтобы обойти
      фильтр, ищущий "127.0.0.1"
    GUARD: DIGIT_FORM ≠ FINAL_SURFACE (нормализовать основание до
      сравнения)
  RISK_CASE_004:
    NAME: DIGIT_AS_LETTER_BRAND_MIMICRY
    INPUT: "paypa1.com  |  g00gle.com  |  micr0soft.com"
    CONTEXT: цифра подменяет похожую букву в бренде
    RISK: HIGH
    ATTACK: 1->l, 0->o, 5->s создают визуальный двойник домена
    GUARD: DIGIT_FORM ≠ LETTER (взаимодействие с CONFUSABLES)
  RISK_CASE_005:
    NAME: NON_ASCII_DIGIT_HOST
    INPUT: "http://１２７.０.０.１"  (полноширинные цифры)
    CONTEXT: хост из не-ASCII цифр
    RISK: MEDIUM
    ATTACK: глиф-цифра с иным кодом обходит проверку по ASCII-цифрам
    GUARD: DIGIT_FORM ≠ ASCII_GUARANTEE

  # ---- CARRIER LAYER (двойное дно: цифра воссоздаёт другой знак) ----
  RISK_CASE_006:
    NAME: PERCENT_ENCODED_GUARDED_SIGN
    INPUT: "%2e%2e%2f%2e%2e%2fetc/passwd"
    CONTEXT: "../../" собран percent-кодировкой цифрами/hex
    RISK: HIGH
    ATTACK: точка и солидус воссозданы как %2e/%2f -> traversal
      проезжает мимо КАРТОЧЕК ТОЧКИ и СОЛИДУСА, которые ищут литерал
    GUARD: DIGIT_FORM ≠ FINAL_SURFACE; требует CANONICALIZATION_PRE_PASS
  RISK_CASE_007:
    NAME: NUMERIC_ENTITY_REBUILDS_INVISIBLE
    INPUT: "admin&#8203;istrator"
    CONTEXT: ZWSP (U+200B) воссоздан десятичной HTML-entity &#8203;
    RISK: HIGH
    ATTACK: цифрами собран НЕВИДИМЫЙ знак -> обходит карточку ZWSP,
      которая сработала бы на литеральный невидимый символ
    GUARD: DIGIT_FORM ≠ FINAL_SURFACE (декодировать entity до
      применения INVISIBLE_CLASS)
  RISK_CASE_008:
    NAME: DOUBLE_ENCODING_DEPTH
    INPUT: "%252e%252e%252f"
    CONTEXT: "%2e.." закодирован повторно ("%25"="%")
    RISK: HIGH
    ATTACK: один проход декодирования даёт "%2e..", не ".." — глубина
      кодирования обманывает однократную нормализацию
    GUARD: DECODE_DEPTH_AWARE (см. LIMITATION — предел глубины)
  RISK_CASE_009:
    NAME: DECIMAL_CHAR_STRING_SMUGGLING
    INPUT: "&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;"
    CONTEXT: слово собрано из десятичных numeric character references
    RISK: MEDIUM
    ATTACK: любой текст (в т.ч. ключевые слова) переписан цифрами,
      чтобы обойти проверку по литеральным словам
    GUARD: DIGIT_FORM ≠ FINAL_SURFACE

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ０
    CODEPOINT: U+FF10
    NAME: FULLWIDTH DIGIT ZERO
    RISK: MEDIUM
    RULE: FULLWIDTH_ZERO ≠ ASCII_ZERO
  CONFUSABLE_002:
    VISIBLE_FORM: ٠
    CODEPOINT: U+0660
    NAME: ARABIC-INDIC DIGIT ZERO
    RISK: MEDIUM
    RULE: ARABIC_INDIC_ZERO ≠ ASCII_ZERO
  CONFUSABLE_003:
    VISIBLE_FORM: O
    CODEPOINT: U+004F
    NAME: LATIN CAPITAL LETTER O
    RISK: HIGH
    RULE: LETTER_O ≠ DIGIT_ZERO   (обратный двойник: буква как цифра)
  CONFUSABLE_004:
    VISIBLE_FORM: l
    CODEPOINT: U+006C
    NAME: LATIN SMALL LETTER L
    RISK: HIGH
    RULE: LETTER_L ≠ DIGIT_ONE
  CONFUSABLE_005:
    VISIBLE_FORM: Ⅰ
    CODEPOINT: U+2160
    NAME: ROMAN NUMERAL ONE
    RISK: LOW
    RULE: ROMAN_ONE ≠ DIGIT_ONE

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================

SEED_ATTACKS_REQUIRED_IN_RUN:
  - IP_HOST (internal / loopback / metadata)
  - ALT_IP_ENCODING (dec / hex / oct / mixed)
  - DIGIT_LETTER_LOOKALIKE (brand mimicry)
  - PERCENT_ENCODED traversal (single и double)
  - NUMERIC_ENTITY воссоздание невидимого и охраняемого знака
  - NON_ASCII_DIGIT host
MODEL_FAMILY_DIVERSITY_REQUIRED: YES (минимум 2 разных семейства)

============================================================
9. MUTATION_CHECK
============================================================

MUTATIONS_TO_SURVIVE:
  - смена основания (127.0.0.1 <-> 2130706433 <-> 0x7f000001)
  - смена кодировки (%2e <-> &#46; <-> .)
  - смена глубины (%2e <-> %252e)
  - смена ширины/скрипта (0 <-> ０ <-> ٠)
INVARIANT: после канонизации все варианты должны давать ОДИН вердикт.

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================

Q1_CANONICALIZATION_PRE_PASS (двойное дно, ключевое):
  CARRIER_LAYER означает, что цифровая карточка НЕ листик, а СЕМЯ
  этапа НОРМАЛИЗАЦИИ, который должен декодировать вход (percent /
  numeric-entity / unicode-escape / radix-IP) ДО применения остальных
  карточек. Иначе любой охраняемый знак обходится фразой "напиши это
  числами". Это КРОСС-КАРТОЧНЫЙ / ДВИЖКОВЫЙ вопрос, шире одной карточки.
  ОТКРЫТО: где живёт pre-pass (движок vs карточка), какова граница.
Q2_DECODE_DEPTH: докуда декодировать (double/triple encoding) и как не
  зациклиться (decode-loop) — предел глубины.
Q3_DECODE_CONTEXT: где декодировать НЕЛЬЗЯ (пояснительный текст про
  "%2f", SAFE_CASE_005) — иначе ложные тревоги.
Q4_PER_DIGIT_SPLIT: выносить ли 0 и 1 (главные двойники/кодировка) в
  отдельные усиленные per-digit карточки (приложение A).

============================================================
11. PATCH_HISTORY
============================================================

v0_1 (2026-07-20): первичный черновик КЛАССОВОЙ карточки цифр с двумя
  слоями (SURFACE + CARRIER). Не прогонялся через конвейер.

============================================================
12. LIMITATION_STATEMENT
============================================================

  1. Это WORKING_DRAFT: не прошёл конвейер, не author-decided, не
     runtime, не валидатор.
  2. CARRIER_LAYER (двойное дно) НЕ реализуется этой карточкой — она
     лишь НАЗЫВАЕТ опасность и СЕЯТ CANONICALIZATION_PRE_PASS. Само
     декодирование — отдельная движковая работа (раздел 10).
  3. Канонизация зависима от ГЛУБИНЫ: однократное декодирование
     пропускает double-encoding (%252e). Слишком жадное — ломает
     легитимный текст ОБ кодировке (SAFE_CASE_005). Граница —
     открытый вопрос.
  4. Класс-карточка обобщает 0–9; специфика отдельных цифр (0: octal/
     hex/leading-zero/O-двойник; 1: l/I-двойник; 5: S-двойник) — в
     приложении A, под будущие per-digit карточки.
  5. Не покрывает языковой слой (числа-как-слова смысла) — это не
     задача знаковой карточки.

============================================================
13. INTEGRATION_INTERFACE_STATUS
============================================================

INTEGRATION_STATUS: PENDING
REQUIRES:
  - CANONICALIZATION_PRE_PASS хук в рантайме (до scan_signs)
  - взаимодействие с карточками: DOT (IP-граница), SOLIDUS (path),
    AT (email-хост), INVISIBLE_CLASS (entity-воссоздание)
NOTE: до появления pre-pass карточка работает только на SURFACE_LAYER
  (литеральные IP/двойники); CARRIER_LAYER остаётся заявленным, но не
  перехваченным — это надо честно показывать в отчёте, а не выдавать
  за покрытое.

============================================================
ПРИЛОЖЕНИЕ A. PER-DIGIT SPECIALIZATION (seed под отдельные карточки)
============================================================

  0: octal/hex-префиксы, leading-zero, двойник буквы O, "null"-семантика
  1: двойник l/I, ведущая цифра версий/индексов
  2: hex-компонент, редкий двойник Z (стилизованный)
  5: двойник S (p5ypal), leetspeak
  6: двойник b, 8: двойник B, 9: двойник g/q — leetspeak-мимикрия
  3 4 7: преимущественно SURFACE (хост/число), слабые двойники
