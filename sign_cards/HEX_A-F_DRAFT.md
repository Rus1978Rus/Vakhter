ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ / COMMERCIAL USE PROHIBITED

HEX-LETTER BAND CARDS A–F (полные заготовки) — замыкание %00..%FF
INHERITS_FROM: SIGN_CORE_CARD_DIGIT_CLASS_0-9_GEN3_v0_1_RU
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION

СТРАТЕГИЯ (по решению автора, 2026-07-20): черновить ПО МАКСИМУМУ — то, что не
угроза сегодня, угроза завтра. Поэтому A–F подняты из «карты полос» в полные
заготовки. ДИСЦИПЛИНА калибровки, чтобы максимализм не давал ложных тревог:
  - каждая карточка есть на ВСЮ полосу;
  - TODAY_VERDICT откалиброван по сегодняшнему риску (NONE/LOW/HIGH);
  - FUTURE_WATCH держит риски «на вырост» (RISK_CASES, спящие до контекста);
  - CONVEYOR-приоритет = по TODAY_VERDICT (HIGH — первыми; LOW — в парке).
Это Preservation Planning из «Свода»: слот готовим ДО прихода угрозы.

NB: A–F — hex-БУКВЫ. SURFACE (двойник буквы) — территория БУКВЕННЫХ карточек.
Здесь их роль — CARRIER (старший полубайт полосы %Nx). Плюс важное: некоторые
байты этих полос ДЕКОДИРУЮТСЯ В НЕВИДИМЫЕ знаки -> уводятся в INVISIBLE_CLASS.

================================================================
CARD: HEX A   ID: SIGN_CORE_CARD_HEX_A_GEN3_v0_1_RU     TODAY_VERDICT: MEDIUM
================================================================
STATUS: WORKING_DRAFT / PREFLIGHT PENDING / CONVEYOR_REVIEW PENDING / NOT CLOSED
CARRIER_LEAD: %AX = 0xA0–0xAF (Latin-1: %A0 NBSP … %AD SOFT HYPHEN … ¡¢£»…)
INVISIBLE_ROUTING (важно):
  %A0 -> U+00A0 NBSP (неразрывный пробел — квазиневидимый) -> INVISIBLE_CLASS
  %AD -> U+00AD SOFT HYPHEN (условный перенос — НЕВИДИМ) -> INVISIBLE_CLASS
RISK (today):
  RA-1 NBSP_SPACE_HOMOGLYPH "admin%a0password" / NBSP вместо пробела  MED
     ATTACK: невидимый/двойник пробела -> обход токенизации, склейка полей.
     ROUTE: INVISIBLE_CLASS после декодирования.
  RA-2 SOFT_HYPHEN_HIDDEN "pay%adpal.com" (U+00AD не рисуется)  MED
     ATTACK: невидимый разрыв внутри слова/домена -> обход сравнения.
     ROUTE: INVISIBLE_CLASS.
FUTURE_WATCH (спит):
  «»¡¿©® как кавычки/скобки-двойники в новых контекстах  LOW-сегодня

================================================================
CARD: HEX B   ID: SIGN_CORE_CARD_HEX_B_GEN3_v0_1_RU     TODAY_VERDICT: LOW
================================================================
STATUS: WORKING_DRAFT / PREFLIGHT PENDING / CONVEYOR_REVIEW PENDING / NOT CLOSED
CARRIER_LEAD: %BX = 0xB0–0xBF (Latin-1 символы: °±²³´µ¶·¸¹º»¼½¾¿)
TODAY: почти нет отдельной угрозы — типографские символы (SAFE-доминантная).
SAFE: "20°C" | "площадь 5 м²" | "½ стакана" | "« цитата »"
FUTURE_WATCH (спит, RISK_CASES на вырост):
  FB-1 SUPERSCRIPT_DIGIT_HOMOGLYPH ²³¹ (U+00B2/B3/B9) как двойники 2/3/1
     -> обфускация чисел/версий, обход digit-нормализации.  LOW-сегодня
  FB-2 »«¿¡ как скобко/кавычко-двойники в парсерах, доверяющих ASCII.  LOW
NOTE: держим карточку-слот; при появлении контекста поднять FB-* в RISK.

================================================================
CARD: HEX C   ID: SIGN_CORE_CARD_HEX_C_GEN3_v0_1_RU     TODAY_VERDICT: HIGH
================================================================
STATUS: WORKING_DRAFT / PREFLIGHT PENDING / CONVEYOR_REVIEW PENDING / NOT CLOSED
CARRIER_LEAD: %CX = 0xC0–0xCF — UTF-8 2-байтовые ЛИД-байты
  %C0,%C1 = НЕЛЕГАЛЬНЫЕ лиды (только в overlong).  %C2–%CF = легитимные лиды.
RISK (today):
  RC-1 OVERLONG_2BYTE "%c0%ae"="." / "%c0%af"="/"  HIGH
     ATTACK: точка/слэш собраны overlong-байтами -> traversal мимо литеральных
       карточек.  ENFORCED: CANONICALIZATION_PRE_PASS v0.2 (overlong=True) —
       уже доказано на живом MSL.
SAFE: %c3%a0.. = «à», %d0.. и т.п. — легитимный многобайт (через %C2–%CF).
FUTURE_WATCH: новые «мягкие» декодеры, принимающие %C0/%C1 -> держать жёсткий отбой.

================================================================
CARD: HEX D   ID: SIGN_CORE_CARD_HEX_D_GEN3_v0_1_RU     TODAY_VERDICT: LOW
================================================================
STATUS: WORKING_DRAFT / PREFLIGHT PENDING / CONVEYOR_REVIEW PENDING / NOT CLOSED
CARRIER_LEAD: %DX = 0xD0–0xDF — UTF-8 2-байтовые лиды (КИРИЛЛИЦА, иврит и др.)
TODAY: нормальный многобайт. КРИТИЧНО не флагать (русский текст = %d0/%d1!).
  В overlong НЕ участвует (overlong-лиды — только %C0/%C1).
SAFE: "%d0%bf%d1%80%d0%b8%d0%b2%d0%b5%d1%82" = «привет»  -> INFO
FUTURE_WATCH (спит, но это РЕАЛЬНЫЙ растущий вектор — держим наготове):
  FD-1 CYRILLIC_HOMOGLYPH_IDN: а/о/е/р/с/х (кир.) ↔ a/o/e/p/c/x (лат.)
     -> "раypal.com" с кириллической «а» (IDN homograph).  MED-как-угроза,
     но это LETTER/CONFUSABLES-слой ПОСЛЕ декода, не «опасность байта %DX».
     ROUTE: механизм confusables (гомоглифы), не %DX-карточка.
NOTE: карточка-слот; сам байт LOW, но пометка на homoglyph-механизм важна.

================================================================
CARD: HEX E   ID: SIGN_CORE_CARD_HEX_E_GEN3_v0_1_RU     TODAY_VERDICT: HIGH
================================================================
STATUS: WORKING_DRAFT / PREFLIGHT PENDING / CONVEYOR_REVIEW PENDING / NOT CLOSED
CARRIER_LEAD: %EX = 0xE0–0xEF — UTF-8 3-байтовые ЛИД-байты
  ЭТО БАЙТОВЫЙ ДОМ НЕВИДИМЫХ И BIDI: здесь живут ZWSP/ZWJ/RLO/BOM как UTF-8.
INVISIBLE_ROUTING (ключевая стыковка с твоими картами невидимых):
  %e2%80%8b -> U+200B ZWSP   -> INVISIBLE_CLASS
  %e2%80%8d -> U+200D ZWJ    -> INVISIBLE_CLASS
  %e2%80%ae -> U+202E RLO    -> INVISIBLE_CLASS  (Trojan Source, bidi!)
  %ef%bb%bf -> U+FEFF BOM    -> INVISIBLE_CLASS
RISK (today):
  RE-1 OVERLONG_3BYTE "%e0%80%af"="/"  HIGH  ENFORCED pre-pass v0.2.
  RE-2 INVISIBLE_VIA_3BYTE "%e2%80%8b/8d/ae" -> невидимые/bidi собраны байтами
     HIGH  -> INVISIBLE_CLASS после декода (иначе обходят карточку ZWSP/BOM).
  RE-3 BOM_VIA_BYTES "%ef%bb%bf"  MED-HIGH -> INVISIBLE_CLASS.
SAFE: %e2%82%ac=«€», %e4..%e9.. = CJK и пр. — легитимный 3-байт.
FUTURE_WATCH: новые невидимые/форматные знаки в блоке U+2000..U+206F.

================================================================
CARD: HEX F   ID: SIGN_CORE_CARD_HEX_F_GEN3_v0_1_RU     TODAY_VERDICT: MED-HIGH
================================================================
STATUS: WORKING_DRAFT / PREFLIGHT PENDING / CONVEYOR_REVIEW PENDING / NOT CLOSED
CARRIER_LEAD: %FX = 0xF0–0xFF — UTF-8 4-байтовые лиды (%F0..%F4) + НЕВАЛИДНЫЕ (%F5..%FF)
RISK (today):
  RF-1 OVERLONG_4BYTE "%f0%80%80%af"="/"  HIGH  ENFORCED pre-pass v0.2.
  RF-2 INVALID_BYTES "%f5..%ff"  MED-HIGH
     ATTACK: невалидные байты -> расхождение парсеров (один дропает, другой
       оставляет) -> контрабанда/обход. Решить: отбивать сразу vs пометка.
  RF-3 UTF16_BOM_BYTES "%fe%ff" / "%ff%fe"  MED  маркеры BOM/порядка байт.
SAFE: %f0%9f%98%80 = «😀» и прочие эмодзи — легитимный 4-байт (НЕ флагать).
FUTURE_WATCH: новые плоскости Unicode, будущие форматные знаки.

================================================================
ИТОГ — ПРОСТРАНСТВО %00..%FF ПРОЧЕРНОВЛЕНО ПОЛНОСТЬЮ
================================================================
  %0X..%9X : карточки цифр 0–9        (готовы как заготовки)
  %AX..%FX : карточки hex A–F         (эти заготовки)
  КАЛИБРОВКА TODAY_VERDICT:
    HIGH сегодня:   C (overlong-2), E (overlong-3 + невидимые), F (overlong-4)
    MEDIUM сегодня: A (NBSP/soft-hyphen -> невидимые)
    LOW/парк:       B (типографика), D (кириллица; homoglyph — на confusables)
  INVISIBLE_ROUTING (байтовые дома невидимых, свести с картами невидимых):
    %A0 NBSP · %AD SOFT-HYPHEN · %E2%80%8B ZWSP · %E2%80%8D ZWJ ·
    %E2%80%AE RLO · %EF%BB%BF BOM
  CONVEYOR-приоритет: C,E,F,A -> первыми; B,D -> заготовки в парке до своего часа.
  ЭНФОРСМЕНТ carrier-рисков: CANONICALIZATION_PRE_PASS v0.2 (overlong уже бежит);
    невидимые после декода -> INVISIBLE_CLASS; homoglyph -> confusables-механизм.

STATUS: всё WORKING_DRAFT — заготовки на вход в конвейер, автором не закрыты.
