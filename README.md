# Vakhter

**A structural guardian for AI.** · **Структурный страж для ИИ.**

🇬🇧 [English](#english) · 🇷🇺 [Русский](#русский)

> *Vakhter* — from German **Wächter**, "the one who keeps watch". The name says what it does.
> *Вахтёр* — от немецкого **Wächter**, «тот, кто на страже». Имя говорит, что он делает.

**PRIVATE AUTHORIAL PROJECT · COMMERCIAL USE PROHIBITED**
Author / Автор: Руслан Малявский · Status / Статус: `WORKING_DRAFT`

---

<a name="english"></a>
## English

Vakhter is a **security gate for AI applications** and the engine behind it. It sits in front of a model and reads every incoming piece of text *before* the model does — so a hidden command smuggled inside a document, a look-alike domain, an invisible character, or an encoding trick never reaches the model as an instruction.

Everything here rests on one idea the whole project turns on:

> **What is real is what survives a transform.** Native vs. inserted, signal vs. noise — judged by the *structure* that does not break under a change of substrate, encoding, scale, or tampering, not by the surface it happens to wear.

One engine, two axes, many substrates: **MSL** reads what a *sign does in context* (invariance across substrate); **ERG** asks whether that structure *survives coarse-graining* (invariance across scale/time). A signal, a text, a prompt, or code are just adapters onto the same core, with a canonicalization pass that peels encoding tricks before the reading.

### What runs (executable code)

| Module | What it does | Status |
|---|---|---|
| `code/invariant_engine/` | the core + adapters, with the **real MSL** wired in | ✅ 11/11 + 8/8 tests |
| `code/range/` | the assembled guard (`product.py`), detector cards, self-defense, and supply-chain gates | ✅ runs on real MSL |
| `code/canonicalization/` | encoding pre-pass: percent / HTML-entity / escapes / **overlong UTF-8** | ✅ proven on MSL |
| `code/erg_cad_mvp/` | the ERG detector ("intensity ≠ objectivity") | ✅ 6/6 tests |
| `code/eval/` | a prompt-injection eval (MSL vs keyword baseline) | ✅ indicative |

The real MSL runtime lives in a separate repository; the adapter *locates* it via `MSL_MIP_HOME` rather than copying it. Coverage, measured before/after per category, is in [`COVERAGE_MAP.md`](COVERAGE_MAP.md).

### The three applications

The guard's parts are general primitives, so they spin out into other fields ([`applications/`](applications/)):

- **ai_gateway** — Vakhter itself, embedded in front of an LLM app. One call (`guarded_llm_call`) scans the user message and every retrieved document; only clean text reaches the model.
- **notarius_data** — a lightweight provenance ledger for data records: native vs. inserted, tamper-evident, crypto-free length witness.
- **erg_fraud** — anomaly detection by survival across scale: a one-off spike dissolves (noise), distributed fraud survives (real).

### Honest boundaries

- Vakhter catches **structural** attacks (smuggled / encoded / invisible / look-alike). It is **blind by design** to purely natural-language injection ("ignore all previous instructions") — that is the job of a semantic layer standing *beside* it.
- The drafted sign cards ([`sign_cards/`](sign_cards/)) are `WORKING_DRAFT`, not conveyor-closed detectors.
- This is a **prototype of the principle**, not a certified product. `NOT A FINAL STANDARD · NOT A SECURITY CERTIFICATE · NOT A PRODUCTION VALIDATOR.`

### Layout

```
README.md              — this file
COVERAGE_MAP.md        — measured coverage by category (before/after)
code/
  invariant_engine/    — core + adapters + real MSL
  range/               — the assembled guard, cards, harnesses, supply-chain gates
  canonicalization/    — encoding pre-pass
  erg_cad_mvp/         — the ERG detector
  eval/                — prompt-injection eval harness
applications/          — ai_gateway (Vakhter shield), notarius_data, erg_fraud
docs/                  — architecture, notarius, Foundation-Layer alignment
sign_cards/            — drafted sign cards (0–9 + A–F)
```

---

<a name="русский"></a>
## Русский

Vakhter — это **турникет безопасности для приложений на ИИ** и движок под ним. Он стоит перед моделью и читает каждый входящий текст *раньше* неё: спрятанная в документе команда, домен-двойник, невидимый символ или трюк с кодировкой не доходят до модели как инструкция.

Всё держится на одной мысли, вокруг которой построен проект:

> **Реальное — это то, что выживает при преобразовании.** Родное или вставленное, сигнал или шум — по *структуре*, которая не рушится при смене подложки, кодировки, масштаба или подмены, а не по поверхности, в которую оно на миг одето.

Один движок, две оси, много подложек: **MSL** читает, *что знак делает в контексте* (инвариантность к подложке); **ERG** спрашивает, *переживёт ли структура огрубление* (инвариантность к масштабу/времени). Сигнал, текст, промпт или код — просто адаптеры на одно ядро, плюс слой канонизации, снимающий кодировочные обёртки до чтения.

### Что работает (запускаемый код)

| Модуль | Что делает | Статус |
|---|---|---|
| `code/invariant_engine/` | ядро + адаптеры, встроен **настоящий MSL** | ✅ 11/11 + 8/8 тестов |
| `code/range/` | собранный вахтёр (`product.py`), карточки-детекторы, самозащита, воротца цепочки поставки | ✅ бежит на настоящем MSL |
| `code/canonicalization/` | pre-pass кодировок: percent / HTML-entity / escapes / **overlong-UTF-8** | ✅ доказано на MSL |
| `code/erg_cad_mvp/` | ERG-детектор («интенсивность ≠ объективность») | ✅ 6/6 тестов |
| `code/eval/` | eval prompt-injection (MSL против keyword) | ✅ индикативно |

Настоящий MSL живёт в отдельном репозитории; адаптер **находит** его через `MSL_MIP_HOME`, а не копирует. Измеренный охват по категориям (до/после) — в [`COVERAGE_MAP.md`](COVERAGE_MAP.md).

### Три приложения

Части вахтёра — общие примитивы, поэтому дают ответвления в другие сферы ([`applications/`](applications/)):

- **ai_gateway** — сам Vakhter, встроенный перед LLM-приложением. Один вызов (`guarded_llm_call`) проверяет сообщение и каждый найденный документ; до модели доходит только чистое.
- **notarius_data** — лёгкий provenance-реестр для записей данных: родное или вставленное, с уликой на подмену и счётчиком-длины без криптографии.
- **erg_fraud** — детекция аномалий по выживанию через масштаб: разовый всплеск растворяется (шум), распределённое мошенничество выживает (реально).

### Честные границы

- Vakhter ловит **структурные** атаки (контрабанда / кодировка / невидимки / двойники). К чисто языковой инъекции («забудь все инструкции») он **слеп by design** — это работа смыслового слоя, стоящего *рядом*.
- Черновые карточки знаков ([`sign_cards/`](sign_cards/)) — `WORKING_DRAFT`, а не закрытые конвейером детекторы.
- Это **прототип принципа**, не сертифицированный продукт. `НЕ ФИНАЛЬНЫЙ СТАНДАРТ · НЕ СЕРТИФИКАТ БЕЗОПАСНОСТИ · НЕ PRODUCTION-ВАЛИДАТОР.`

### Структура

```
README.md              — этот файл
COVERAGE_MAP.md        — измеренный охват по категориям (до/после)
code/
  invariant_engine/    — ядро + адаптеры + настоящий MSL
  range/               — собранный вахтёр, карточки, харнессы, воротца цепочки поставки
  canonicalization/    — pre-pass кодировок
  erg_cad_mvp/         — ERG-детектор
  eval/                — харнесс eval prompt-injection
applications/          — ai_gateway (щит Vakhter), notarius_data, erg_fraud
docs/                  — архитектура, нотариус, привязка к Foundation Layer
sign_cards/            — черновые карточки знаков (0–9 + A–F)
```

---

## License / Лицензия

Private authorial project. Commercial use prohibited.
Частный авторский проект. Коммерческое использование запрещено.
