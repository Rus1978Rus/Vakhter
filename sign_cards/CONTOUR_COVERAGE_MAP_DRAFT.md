PRIVATE AUTHORIAL PROJECT / ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ · COMMERCIAL USE PROHIBITED

# CONTOUR COVERAGE MAP — DEFAULT-IGNORABLE / INVISIBLE (DRAFT)

DOCUMENT_TYPE: COVERAGE_MAP · STATUS: WORKING_DRAFT / NOT_CONVEYOR_RUN · TEMPLATE_LINE: GEN3_v0_3
SCOPE: which draft class card owns which part of the Unicode Default_Ignorable_Code_Point contour ("class 138" = the 138 default-ignorable FORMAT chars, plus the assigned non-Cf tail, plus the reserved blanket).

🇬🇧 [English](#english) · 🇷🇺 [Русский](#русский)

---

<a name="english"></a>
## English

This map records that the invisible / default-ignorable contour is now **fully carded**. "Class 138" is exactly the **163 format (Cf) characters minus the 25 that are not default-ignorable = 138 default-ignorable format characters.** Those 138 were already covered by the first six axis cards; the three tail cards then close the assigned non-Cf families and the reserved blanket, so nothing in the whole Default_Ignorable space is left without a draft.

**A. The 138 (default-ignorable FORMAT chars, category Cf) — 138/138 covered**

| Card | Owns |
|---|---|
| INVISIBLE_CLASS | ZWSP, ZWNJ, ZWJ, WJ, BOM, SHY, CGJ, invisible math ops U+2061–2064 |
| BIDI_CLASS | LRE, RLE, PDF, LRO, RLO, LRI, RLI, FSI, PDI, LRM, RLM, ALM |
| TAG_CLASS | LANGUAGE TAG U+E0001, tag chars U+E0020–E007F |
| WHITESPACE_CLASS | LINE SEP U+2028, PARA SEP U+2029 (the Cf-relevant separators; the Zs spaces are visible-width) |
| MONITORED_FORMAT | MVS U+180E, deprecated U+206A–206F, shorthand U+1BCA0–1BCA3, musical U+1D173–1D17A |

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

**D. Adjacent tail NOT in the 138 (Cf but NOT default-ignorable) — not yet carded**
The prepended / enclosing format characters — Arabic number signs (U+0600–0605, U+06DD, U+0890, U+0891, U+08E2), Syriac abbreviation mark (U+070F), Kaithi number signs (U+110BD, U+110CD), interlinear annotation (U+FFF9–FFFB), Egyptian hieroglyph format (U+13430–1343F). These are format chars that DO affect visible layout, so they sit outside "class 138" and would be a separate PREPENDED_FORMAT card if wanted.

**Coverage summary (verified by `scratchpad/cov2.py` against the host Unicode DB):** the 138 = 138/138; assigned non-Cf tail = 10/10; reserved blanket = closed. WORKING_DRAFT / NOT_CONVEYOR_RUN — drafts exist and run, but conveyor closing is a separate project.

---

<a name="русский"></a>
## Русский

Эта карта фиксирует, что невидимый / default-ignorable контур теперь **полностью откарточен**. «Класс 138» это ровно **163 форматных (Cf) знака минус 25, не являющихся default-ignorable = 138 default-ignorable форматных знаков.** Эти 138 уже были покрыты первыми шестью осевыми карточками; три хвостовые карточки затем закрывают назначенные не-Cf семейства и зарезервированный бланкет, так что ничего во всём Default_Ignorable пространстве не остаётся без черновика.

**A. 138 (default-ignorable ФОРМАТНЫЕ знаки, категория Cf) — 138/138 покрыто**

| Карточка | Владеет |
|---|---|
| INVISIBLE_CLASS | ZWSP, ZWNJ, ZWJ, WJ, BOM, SHY, CGJ, невид. матоператоры U+2061–2064 |
| BIDI_CLASS | LRE, RLE, PDF, LRO, RLO, LRI, RLI, FSI, PDI, LRM, RLM, ALM |
| TAG_CLASS | LANGUAGE TAG U+E0001, tag-символы U+E0020–E007F |
| WHITESPACE_CLASS | LINE SEP U+2028, PARA SEP U+2029 (Cf-релевантные разделители; Zs-пробелы имеют видимую ширину) |
| MONITORED_FORMAT | MVS U+180E, устаревшие U+206A–206F, shorthand U+1BCA0–1BCA3, musical U+1D173–1D17A |

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

**D. Смежный хвост НЕ в 138 (Cf, но НЕ default-ignorable) — ещё не откарточен**
Prepended / enclosing форматные знаки — арабские числовые знаки (U+0600–0605, U+06DD, U+0890, U+0891, U+08E2), сирийская аббревиатурная марка (U+070F), кайтхи числовые знаки (U+110BD, U+110CD), interlinear annotation (U+FFF9–FFFB), египетский иероглифический формат (U+13430–1343F). Это форматные знаки, которые ВЛИЯЮТ на видимую раскладку, поэтому лежат вне «класса 138» и стали бы отдельной карточкой PREPENDED_FORMAT при желании.

**Сводка покрытия (проверено `scratchpad/cov2.py` против базы Unicode хоста):** 138 = 138/138; назначенный не-Cf хвост = 10/10; зарезервированный бланкет = закрыт. WORKING_DRAFT / NOT_CONVEYOR_RUN — черновики есть и бегут, но закрытие конвейером — отдельный проект.
