# Cherokee homoglyphs — the hard-mix method · Гомоглифы чероки — метод hard-mix

AUTHOR / АВТОР: Руслан Малявский · STATUS / СТАТУС: `WORKING NOTE` · 2026-07-23

🇬🇧 [English](#english) · 🇷🇺 [Русский](#русский)

---

<a name="english"></a>
## English

### Why Cherokee has no per-sign cards

Cyrillic, Greek, Roman-numeral and Armenian homoglyphs each get a per-sign
`SIGN_CORE_CARD` that names the Latin letter they impersonate (`а` → `a`, `օ` →
`o`, …). Cherokee does **not** — on purpose.

The Cherokee syllabary (U+13A0–13FF, plus the Supplement U+AB70–ABBF) contains
many glyphs that resemble Latin capitals (it is a documented IDN-spoofing
script). But the *exact* letter-to-letter equivalences are not something this
project is willing to assert without a verified source: **a security table must
not claim a look-alike it has not checked** (see AUTHOR_DECISIONS AD-25). Guessing
`Ꭰ → D` or `Ᏼ → B` from font memory would put an unverified claim into the record.

### How Cherokee is detected instead

We do not need the per-letter map. The confusable detector's core law is that a
**script MIX within one token** is the tell (AD-2). Cherokee has a property that
makes the mix *alone* conclusive:

> No natural language interleaves Latin letters with Cherokee letters inside a
> single token.

This is the crucial difference from CJK. Japanese and Chinese **do** mix Latin
mid-token — `IDカード`, `iPhone12`, `日本語ID`, `USB端子` are all ordinary tokens —
so a blanket "Latin + non-Latin = spoof" rule would flood them with false
positives. Cherokee (like Cyrillic/Greek/Armenian alphabets) never mixes with
Latin mid-token, so:

```
LATIN + CHEROKEE in one token  →  anomalous script mix  →  ALARM
pure single-script Cherokee (ᏣᎳᎩ)  →  OK
LATIN + CJK in one token (IDカード)  →  OK   (legitimate, not a hard-mix script)
```

The detector flags the anomaly **without naming an impersonated Latin skeleton** —
an honest reflection of exactly what has been verified: that the mix is anomalous,
not which specific letter stands in for which.

### If per-sign Cherokee cards are ever wanted

Populate a `CHER_TO_LAT` table from the Unicode `confusables.txt` data (not from
memory), add `CHEROKEE_` to `coverage_lock.HOMOGLYPH_FAMILIES` and the table to
`detector_codepoints()`, and generate cards the same way as Armenian. Until that
verified source is in hand, the hard-mix rule is the correct, honest coverage.

---

<a name="русский"></a>
## Русский

### Почему у чероки нет per-sign карточек

Гомоглифы кириллицы, греческого, римских цифр и армянского получают per-sign
`SIGN_CORE_CARD`, называющую латинскую букву, под которую они мимикрируют (`а` →
`a`, `օ` → `o`, …). У чероки её **нет** — намеренно.

Силлабарий чероки (U+13A0–13FF плюс дополнение U+AB70–ABBF) содержит много
глифов, похожих на латинские заглавные (это задокументированный IDN-спуф-скрипт).
Но *точные* побуквенные соответствия проект не готов утверждать без выверенного
источника: **security-таблица не должна заявлять двойника, которого не
проверила** (см. AUTHOR_DECISIONS AD-25). Угадать `Ꭰ → D` или `Ᏼ → B` по памяти
шрифта — значит внести невыверенное утверждение в запись.

### Как чероки детектится вместо этого

Побуквенная карта не нужна. Базовый закон детектора конфузаблов: признак — это
**смесь письменностей внутри одного токена** (AD-2). У чероки есть свойство,
делающее *саму* смесь окончательной:

> Ни один естественный язык не переплетает латинские буквы с буквами чероки
> внутри одного токена.

Это ключевое отличие от CJK. Японский и китайский **смешивают** латиницу внутри
токена — `IDカード`, `iPhone12`, `日本語ID`, `USB端子` — обычные токены, поэтому
огульное правило «латиница + не-латиница = спуф» завалило бы их ложными
срабатываниями. Чероки (как алфавиты кириллицы/греческого/армянского) не
смешивается с латиницей внутри токена, поэтому:

```
ЛАТИНИЦА + ЧЕРОКИ в одном токене  →  аномальная смесь письменностей  →  ТРЕВОГА
чистый односкриптовый чероки (ᏣᎳᎩ)  →  OK
ЛАТИНИЦА + CJK в одном токене (IDカード)  →  OK   (законно, не hard-mix скрипт)
```

Детектор флагует аномалию **не называя имитируемый латинский скелет** — честное
отражение ровно того, что выверено: что смесь аномальна, а не какая конкретно
буква кого подменяет.

### Если per-sign карточки чероки всё же понадобятся

Заполнить таблицу `CHER_TO_LAT` из данных Unicode `confusables.txt` (не по
памяти), добавить `CHEROKEE_` в `coverage_lock.HOMOGLYPH_FAMILIES` и таблицу в
`detector_codepoints()`, и сгенерировать карточки так же, как армянские. Пока
выверенного источника нет, правило hard-mix — корректное и честное покрытие.
