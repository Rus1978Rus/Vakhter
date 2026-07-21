PRIVATE AUTHORIAL PROJECT / ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ · COMMERCIAL USE PROHIBITED

# CONTOUR COVERAGE MAP — DEFAULT-IGNORABLE / INVISIBLE (DRAFT)

DOCUMENT_TYPE: COVERAGE_MAP · STATUS: WORKING_DRAFT / NOT_CONVEYOR_RUN · TEMPLATE_LINE: GEN3_v0_3
SCOPE: which draft class card owns which part of the Unicode Default_Ignorable_Code_Point contour ("class 138" = the 138 default-ignorable FORMAT chars, plus the assigned non-Cf tail, plus the reserved blanket).

🇬🇧 [English](#english) · 🇷🇺 [Русский](#русский)

---

<a name="english"></a>
## English

This map records that the invisible / default-ignorable contour is now **fully carded**. "Class 138" is exactly the **163 format (Cf) characters minus the 25 that are not default-ignorable = 138 default-ignorable format characters.** Those 138 were already covered by the first six axis cards; the three tail cards then close the assigned non-Cf families and the reserved blanket, so nothing in the whole Default_Ignorable space is left without a draft.

**A. The 138 (Default_Ignorable ∧ category Cf) — 138/138 covered**

Authoritative predicate (MSL/MIP `oracle_class_138`, DI source UCD 17.0 — cross-checked **set-identical** by `code/range/range_class138_coverage.py`): `General_Category==Cf AND Default_Ignorable_Code_Point==True`. Oracle buckets: PURE 23 · DIRECTIONAL 12 · TAG 97 · DEPRECATED 6 = 138.

| Card | Owns | Bucket(s) | # of 138 |
|---|---|---|---|
| INVISIBLE_CLASS | ZWSP, ZWNJ, ZWJ, WJ, BOM, SHY, invisible math ops U+2061–2064 | PURE | 10 |
| BIDI_CLASS | LRE, RLE, PDF, LRO, RLO, LRI, RLI, FSI, PDI, LRM, RLM, ALM | DIRECTIONAL | 12 |
| TAG_CLASS | LANGUAGE TAG U+E0001, tag chars U+E0020–E007F | TAG | 97 |
| MONITORED_FORMAT | MVS U+180E, deprecated U+206A–206F, shorthand U+1BCA0–1BCA3, musical U+1D173–1D17A | PURE + DEPRECATED | 19 |

**NOT in the 138** (settled by the oracle predicate; category is decisive): **CGJ U+034F** is category **Mn** → covered by INVISIBLE_CLASS but belongs to tail B, not the Cf-138; **LINE SEP U+2028 / PARA SEP U+2029** are **Zl/Zp** → covered by WHITESPACE_CLASS as a line/paragraph-separator concern, not part of class 138.

**B. Assigned non-Cf default-ignorable tail (10 signs) — now covered**

| Card | Owns | Category |
|---|---|---|
| VARIATION_SELECTOR_CLASS | VS U+FE00–FE0F, VS-supplement U+E0100–E01EF | Mn |
| HANGUL_FILLER_CLASS | U+115F, U+1160, U+3164, U+FFA0 | Lo |
| SCRIPT_IGNORABLE_CLASS | Mongolian FVS U+180B–180D/180F, Khmer inherent U+17B4–17B5 | Mn |

**C. Reserved (unassigned, category Cn) default-ignorable — blanket covered**

| Card | Owns |
|---|---|
| RESERVED_IGNORABLE_CLASS | U+2065; U+FFF0–FFF8; U+E0000; U+E0002–E001F; U+E0080–E00FF; U+E01F0–E0FFF (~3.7k reserved code points) |

**D. Adjacent tail NOT in the 138 (Cf but NOT default-ignorable) — now covered**

| Card | Owns | Branch |
|---|---|---|
| PREPENDED_FORMAT_CLASS | U+0600–0605, U+06DD, U+0890, U+0891, U+08E2, U+070F, U+110BD, U+110CD | prepended concatenation marks (scope = following digits/letters) |
| PREPENDED_FORMAT_CLASS | U+FFF9–FFFB, U+13430–1343F | bracketing / annotation controls (balanced runs) |

These are format chars that DO affect visible layout — format that ACTS, not hides — so they sit outside "class 138". This closes the whole Cf set (163 = 138 default-ignorable + 25 prepended/enclosing).

**Coverage summary (verified by `code/range/range_class138_coverage.py` against the host Unicode DB):** the 138 = 138/138 (each owned by exactly one card, 0 over-reach, buckets match the oracle); assigned non-Cf DI tail = 10/10; reserved blanket = closed; Cf-not-DI tail (25) = covered. Whole format (Cf) set + full Default_Ignorable contour carded. WORKING_DRAFT / NOT_CONVEYOR_RUN — drafts exist and run, but conveyor closing is a separate project.

**Cross-project findings (simulated before adoption; MSL/MIP mirror).**
1. **138 predicate confirmed.** Vakhter's independent derivation is **set-identical** to the MSL/MIP `oracle_class_138` (138/138, same predicate, UCD 17.0). This map's buckets/counts are aligned to that oracle.
2. **Parser-desync (their "B5") — prototyped as `canonical_view`.** A raw-vs-canonical two-view divergence detector (`code/range/canonical_view.py`, harness `range_canonical_view.py`). Simulation: it escalates invisible-against-domain-punctuation (`pay‹ZWSP›.pal.com`, `user‹ZWSP›@host`) from WATCH → ALARM (**+3**, desync ALARMs 2/5 → 5/5) with **0 own false alarms** on emoji glue / trailing invisibles. It answers the parser-desync OPEN_QUESTION carried by INVISIBLE_CLASS and WHITESPACE_CLASS.

---

<a name="русский"></a>
## Русский

Эта карта фиксирует, что невидимый / default-ignorable контур теперь **полностью откарточен**. «Класс 138» это ровно **163 форматных (Cf) знака минус 25, не являющихся default-ignorable = 138 default-ignorable форматных знаков.** Эти 138 уже были покрыты первыми шестью осевыми карточками; три хвостовые карточки затем закрывают назначенные не-Cf семейства и зарезервированный бланкет, так что ничего во всём Default_Ignorable пространстве не остаётся без черновика.

**A. 138 (Default_Ignorable ∧ категория Cf) — 138/138 покрыто**

Авторитетный предикат (MSL/MIP `oracle_class_138`, источник DI — UCD 17.0 — кросс-проверено **до знака** через `code/range/range_class138_coverage.py`): `General_Category==Cf AND Default_Ignorable_Code_Point==True`. Бакеты оракула: PURE 23 · DIRECTIONAL 12 · TAG 97 · DEPRECATED 6 = 138.

| Карточка | Владеет | Бакет(ы) | Из 138 |
|---|---|---|---|
| INVISIBLE_CLASS | ZWSP, ZWNJ, ZWJ, WJ, BOM, SHY, невид. матоператоры U+2061–2064 | PURE | 10 |
| BIDI_CLASS | LRE, RLE, PDF, LRO, RLO, LRI, RLI, FSI, PDI, LRM, RLM, ALM | DIRECTIONAL | 12 |
| TAG_CLASS | LANGUAGE TAG U+E0001, tag-символы U+E0020–E007F | TAG | 97 |
| MONITORED_FORMAT | MVS U+180E, устаревшие U+206A–206F, shorthand U+1BCA0–1BCA3, musical U+1D173–1D17A | PURE + DEPRECATED | 19 |

**НЕ в 138** (решается предикатом оракула; категория решающая): **CGJ U+034F** это категория **Mn** → покрыт INVISIBLE_CLASS, но принадлежит хвосту B, не Cf-138; **LINE SEP U+2028 / PARA SEP U+2029** это **Zl/Zp** → покрыты WHITESPACE_CLASS как забота о разделителях строк/абзацев, не часть класса 138.

**B. Назначенный не-Cf default-ignorable хвост (10 знаков) — теперь покрыт**

| Карточка | Владеет | Категория |
|---|---|---|
| VARIATION_SELECTOR_CLASS | VS U+FE00–FE0F, VS-supplement U+E0100–E01EF | Mn |
| HANGUL_FILLER_CLASS | U+115F, U+1160, U+3164, U+FFA0 | Lo |
| SCRIPT_IGNORABLE_CLASS | монгольские FVS U+180B–180D/180F, кхмерские присущие U+17B4–17B5 | Mn |

**C. Зарезервированный (не назначен, категория Cn) default-ignorable — бланкет покрыт**

| Карточка | Владеет |
|---|---|
| RESERVED_IGNORABLE_CLASS | U+2065; U+FFF0–FFF8; U+E0000; U+E0002–E001F; U+E0080–E00FF; U+E01F0–E0FFF (~3.7k зарезервированных кодпоинтов) |

**D. Смежный хвост НЕ в 138 (Cf, но НЕ default-ignorable) — теперь покрыт**

| Карточка | Владеет | Ветка |
|---|---|---|
| PREPENDED_FORMAT_CLASS | U+0600–0605, U+06DD, U+0890, U+0891, U+08E2, U+070F, U+110BD, U+110CD | prepended concatenation marks (область = следующие цифры/буквы) |
| PREPENDED_FORMAT_CLASS | U+FFF9–FFFB, U+13430–1343F | скобящие / аннотационные контроли (сбалансированные прогоны) |

Это форматные знаки, которые ВЛИЯЮТ на видимую раскладку — формат, что ДЕЙСТВУЕТ, а не прячет — поэтому лежат вне «класса 138». Это закрывает весь Cf-набор (163 = 138 default-ignorable + 25 prepended/enclosing).

**Сводка покрытия (проверено `code/range/range_class138_coverage.py` против базы Unicode хоста):** 138 = 138/138 (каждый принадлежит ровно одной карточке, 0 over-reach, бакеты совпадают с оракулом); назначенный не-Cf DI хвост = 10/10; зарезервированный бланкет = закрыт; Cf-не-DI хвост (25) = покрыт. Весь форматный (Cf) набор + полный Default_Ignorable контур откарточены. WORKING_DRAFT / NOT_CONVEYOR_RUN — черновики есть и бегут, но закрытие конвейером — отдельный проект.

**Кросс-проектные находки (прогнаны в симуляциях до внесения; зеркало MSL/MIP).**
1. **Предикат 138 подтверждён.** Независимый вывод Vakhter **до знака совпадает** с MSL/MIP `oracle_class_138` (138/138, тот же предикат, UCD 17.0). Бакеты/счётчики этой карты выровнены по оракулу.
2. **Parser-desync (их «B5») — прототип `canonical_view`.** Детектор расхождения двух прочтений raw-vs-canonical (`code/range/canonical_view.py`, harness `range_canonical_view.py`). Симуляция: он повышает невидимый-рядом-с-доменной-пунктуацией (`pay‹ZWSP›.pal.com`, `user‹ZWSP›@host`) с WATCH → ALARM (**+3**, desync-ALARM 2/5 → 5/5) при **0 собственных ложных тревог** на emoji-клее / хвостовых невидимках. Он отвечает на OPEN_QUESTION о parser-desync, который несут INVISIBLE_CLASS и WHITESPACE_CLASS.
