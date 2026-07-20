PRIVATE AUTHORIAL PROJECT / ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ · COMMERCIAL USE PROHIBITED

# HEX-LETTER BANDS A–F — closing the %XX space (DRAFT / MAP)

INHERITS_FROM: SIGN_CORE_CARD_DIGIT_CLASS_0-9_GEN3_v0_1_RU
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME

🇬🇧 [English](#english) · 🇷🇺 [Русский](#русский)

---

<a name="english"></a>
## English

PURPOSE: digits 0–9 closed the bands %0X..%9X. This map closes %AX..%FX and thereby the WHOLE percent-encoding space %00..%FF.

IMPORTANT (honest): A–F are hex LETTERS, not "digit-signs". Their SURFACE (letter look-alike) is the territory of the LETTER cards, not these. Here they have ONLY the CARRIER role: the high nibble of their byte band in %XX. So this is a MAP of bands, not 6 full sign cards. Enforcement is the pre-pass (see below), not the map.

### Bands A–F (what each high nibble leads)

- **A → %AX  0xA0–0xAF.** %A0 = NBSP (a non-breaking space — quasi-INVISIBLE whitespace!), Latin-1 punctuation (¡¢£¤¥…). Also a UTF-8 continuation byte. RISK: %A0 as a hidden space → tokenization bypass / space look-alike. MED
- **B → %BX  0xB0–0xBF.** Latin-1 symbols (°±²³µ¶·…). Mostly harmless signs. UTF-8 continuation byte. Little standalone weight. LOW
- **C → %CX  0xC0–0xCF ← KEY.** UTF-8 2-byte LEAD bytes. %C0 and %C1 are ILLEGAL lead bytes, appearing ONLY in overlong: %c0%ae="." %c0%af="/". %C2–%CF are legit leads (Latin-1 extended, start of Cyrillic). RISK: %C0/%C1 = overlong bypass of dot/slash. HIGH
- **D → %DX  0xD0–0xDF.** UTF-8 2-byte lead bytes (Cyrillic, Hebrew, etc. — legit). Not involved in overlong (overlong leads are only %C0/%C1). LOW
- **E → %EX  0xE0–0xEF ← KEY.** UTF-8 3-byte LEAD bytes. %E0 — overlong 3-byte (%e0%80%af="/"). %EF leads %EF%BB%BF = UTF-8 BOM (an INVISIBLE marker, the ZWSP/BOM family!). RISK: overlong-3 + BOM smuggling. HIGH
- **F → %FX  0xF0–0xFF ← KEY.** UTF-8 4-byte LEAD bytes. %F0 — overlong 4-byte. %F5–%FF — INVALID UTF-8 bytes; %FE %FF = UTF-16 BOM bytes. RISK: overlong-4 + invalid bytes for parser divergence/breakage. MED-HIGH

### Risk concentration (not all bands are equal)
- DANGEROUS: %C0 %C1 (overlong-2), %E0 (overlong-3), %F0 (overlong-4), %A0 (NBSP), %EF%BB%BF (BOM), %F5–%FF (invalid bytes)
- MOSTLY LEGIT: %BX, %DX, %C2–%CF, most of %E/%F — this is NORMAL multibyte UTF-8 (Cyrillic, emoji, etc.)
- CONCLUSION: bands B and D carry almost no standalone threat; the whole weight is on the overlong leads (C0/C1/E0/F0) and on BOM/NBSP.

### Enforcement (this is what actually closes it, not the map)
CANONICALIZATION_PRE_PASS v0.2 (`canonicalize.py`) already: percent-decodes %XX into RAW BYTES; leniently decodes UTF-8, REVEALING overlong forms; flags `overlong_utf8=True` on any overlong sequence; passes legit multibyte UTF-8 through unchanged (`overlong=False`). Proven on the live MSL (`demo_overlong.py`):
```
..%c0%af..%c0%afetc%c0%afpasswd -> "../../etc/passwd" [overlong] -> ALARM
%e0%80%af..                     -> "/.." [overlong]              -> ALARM
%d0%bf%d1%80%d0%b8%d0%b2%d0%b5%d1%82 -> "привет" [not overlong]  -> OK
```
That is: the existing dot/solidus cards catch the revealed sign, and the overlong flag is itself a strong signal ("why encode '/' in 2 bytes if not to bypass?").

OPEN (honest): %A0 NBSP and %EF%BB%BF BOM, after revelation, should route into the INVISIBLE_CLASS cards (they are invisible) — wire the pre-pass to them; %F5–%FF invalid: decide reject-immediately vs. flag-as-suspicion; position gating (do not decode explanatory text) — as before.

### Coverage summary %00..%FF
- %0X..%9X : per-digit cards 0–9 (SURFACE directly + CARRIER via pre-pass)
- %AX..%FX : this map; CARRIER enforcement via pre-pass v0.2 (overlong/BOM/NBSP)
- THE SPACE IS CLOSED: every byte %00..%FF has either a sign card (0–9 + existing DOT/SOLIDUS/AT/INVISIBLE) or is decoded by the pre-pass to a sign that has a card. No open bands.

---

<a name="русский"></a>
## Русский

НАЗНАЧЕНИЕ: цифры 0–9 закрыли полосы %0X..%9X. Эта карта закрывает %AX..%FX и тем самым ВСЁ пространство percent-кодирования %00..%FF.

ВАЖНО (честно): A–F — это hex-БУКВЫ, а не «цифры-знаки». Их SURFACE (двойник буквы) — территория БУКВЕННЫХ карточек, не этих. Здесь у них ТОЛЬКО CARRIER-роль: старший полубайт своей байтовой полосы в %XX. Поэтому это КАРТА полос, а не 6 полноценных знаковых карточек. Энфорсмент — pre-pass (см. низ), не карта.

### Полосы A–F (что ведёт каждый старший полубайт)

- **A → %AX  0xA0–0xAF.** %A0 = NBSP (неразрывный пробел — квазиНЕВИДИМЫЙ whitespace!), Latin-1 пунктуация (¡¢£¤¥…). Также байт-продолжение UTF-8. РИСК: %A0 как скрытый пробел → обход токенизации/двойник пробела. MED
- **B → %BX  0xB0–0xBF.** Latin-1 символы (°±²³µ¶·…). В основном безобидные знаки. Байт-продолжение UTF-8. Отдельного веса мало. LOW
- **C → %CX  0xC0–0xCF ← КЛЮЧЕВАЯ.** UTF-8 2-байтовые ЛИД-байты. %C0 и %C1 — НЕЛЕГАЛЬНЫЕ лид-байты, встречаются ТОЛЬКО в overlong: %c0%ae="." %c0%af="/". %C2–%CF — легитимные лиды (Latin-1 доп., начало кириллицы). РИСК: %C0/%C1 = overlong-обход точки/слэша. HIGH
- **D → %DX  0xD0–0xDF.** UTF-8 2-байтовые лид-байты (кириллица, иврит и т.д. — легитимно). В overlong не участвует (overlong-лиды — только %C0/%C1). LOW
- **E → %EX  0xE0–0xEF ← КЛЮЧЕВАЯ.** UTF-8 3-байтовые ЛИД-байты. %E0 — overlong 3-байт (%e0%80%af="/"). %EF ведёт %EF%BB%BF = UTF-8 BOM (НЕВИДИМЫЙ маркер, семья ZWSP/BOM!). РИСК: overlong-3 + BOM-контрабанда. HIGH
- **F → %FX  0xF0–0xFF ← КЛЮЧЕВАЯ.** UTF-8 4-байтовые ЛИД-байты. %F0 — overlong 4-байт. %F5–%FF — НЕВАЛИДНЫЕ байты UTF-8; %FE %FF = байты UTF-16 BOM. РИСК: overlong-4 + невалидные байты для сбоя/расхождения парсеров. MED-HIGH

### Концентрация риска (не все полосы равны)
- ОПАСНЫЕ: %C0 %C1 (overlong-2), %E0 (overlong-3), %F0 (overlong-4), %A0 (NBSP), %EF%BB%BF (BOM), %F5–%FF (невалидные байты)
- В ОСНОВНОМ ЛЕГИТИМНЫЕ: %BX, %DX, %C2–%CF, большая часть %E/%F — это НОРМАЛЬНЫЙ многобайтовый UTF-8 (кириллица, эмодзи и пр.)
- ВЫВОД: полосы B и D почти не несут отдельной угрозы; вся тяжесть — на overlong-лидах (C0/C1/E0/F0) и на BOM/NBSP.

### Энфорсмент (вот чем реально закрыто, а не картой)
CANONICALIZATION_PRE_PASS v0.2 (`canonicalize.py`) уже: percent-декодирует %XX в СЫРЫЕ БАЙТЫ; щадяще декодирует UTF-8, ВСКРЫВАЯ overlong-формы; ставит флаг `overlong_utf8=True` на любой overlong-последовательности; легитимный многобайтовый UTF-8 отдаёт как есть (`overlong=False`). Доказано на живом MSL (`demo_overlong.py`):
```
..%c0%af..%c0%afetc%c0%afpasswd -> "../../etc/passwd" [overlong] -> ALARM
%e0%80%af..                     -> "/.." [overlong]              -> ALARM
%d0%bf%d1%80%d0%b8%d0%b2%d0%b5%d1%82 -> "привет" [не overlong]   -> OK
```
То есть existing карточки точки/солидуса ловят раскрытый знак, а overlong-флаг сам по себе — сильный сигнал («зачем кодировать '/' в 2 байта, если не для обхода»).

ОСТАЁТСЯ (открытые вопросы, честно): %A0 NBSP и %EF%BB%BF BOM после раскрытия должны попадать в INVISIBLE_CLASS-карточки (они невидимые) — связать pre-pass с ними; %F5–%FF невалидные: решить, отбивать сразу или помечать как подозрение; гейт по позиции (не декодировать пояснительный текст) — как и раньше.

### Итог покрытия %00..%FF
- %0X..%9X : per-digit карточки 0–9 (SURFACE напрямую + CARRIER через pre-pass)
- %AX..%FX : эта карта; CARRIER-энфорсмент через pre-pass v0.2 (overlong/BOM/NBSP)
- ПРОСТРАНСТВО ЗАМКНУТО: каждый байт %00..%FF имеет либо знаковую карточку (0–9 + существующие DOT/SOLIDUS/AT/INVISIBLE), либо декодируется pre-pass'ом до знака, у которого карточка есть. Незакрытых полос нет.
