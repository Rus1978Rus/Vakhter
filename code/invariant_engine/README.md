# Invariant Engine — v0.2

🇬🇧 [English](#english) · 🇷🇺 [Русский](#русский)

---

<a name="english"></a>
## English

An extension of the morning ERG prototype **into the general concept**: not a "detector of something", but one engine of context-invariance onto which different inputs are plugged. Pure Python, no dependencies.

> **What is real / meaningful = the structure that is invariant under a transform, not the local surface sign.**

### Two axes (both pluggable)
- **MSL (nature)** — reads the structure of ONE input: what it is and how blatantly it is "out of place". Invariance across the **substrate**. → `invariant_engine/msl.py`
- **ERG (reality)** — does that structure survive a transform: coarse-graining across **scale** (signal) or recurrence across **time/stream** (text/code). → `invariant_engine/erg.py`

The core (`core.py`) neither knows nor cares what the input is. A signal, a text, a prompt, code — these are **adapters**, not different products. One engine, many doors.

### Proven by running (11/11 tests, `python demo.py`)

| Input | What was sent | Verdict | Which axis fired |
|---|---|---|---|
| signal | strong single spike (0.9) | `NOISE` | scale: did not survive coarse-graining |
| signal | weak persistent (0.4) | `WATCH` | scale: survived, but weak |
| signal | strong persistent (0.9) | `ALARM` | scale: survived and strong |
| text | 1 phishing URL, **no stream** | `WATCH` | suspicious but unconfirmed |
| text | same URL, **in a stream** | `ALARM` | time: recurs → real |
| text | a harmless message | `OK` | — |
| **code** | a hidden invisible char U+200B | `ALARM` | structure: Trojan-Source, conclusive |
| code | an ordinary function | `OK` | — |

`intensity ≠ objectivity` (the spike is stronger than the persistent one, yet is cut off) **and** `substrate-independent` (one core across signal, text, and code) — both on facts.

### Run
```bash
python demo.py                 # show all scenarios + self-check
python tests/test_engine.py    # 11 tests, no pytest
pytest                         # if installed
```

### Structure
```
invariant_engine/
  core.py   InvariantEngine, Finding, Verdict, judge() — the shared 2×2 (nature × reality)
  msl.py    structural readers: signal_reader, text_reader
            (invisible/bidi chars, URL brand mimicry, bracket integrity)
  erg.py    survival: scale_survival (coarse-graining), recurrence_survival (stream)
demo.py     4 substrates on one core
tests/      signal (scale) + text (time) + code (structure) + API masking
```

### The real MSL is wired in (not a stub) — `msl_real.py`
The core now calls the **real `msl_mip_runtime.py`** (with its core/single_sign/sequence and sign cards), not a stub. `msl_real.real_text_reader` calls the real `analyze()` and maps its verdict (`pass < log_only < queue_for_review < hold_pending_review < escalate_to_human`) into a `Finding`.

The real MSL is a whole project, not one file, so the adapter **locates** the installed repo rather than copying it:
```bash
MSL_MIP_HOME=/path/to/msl_mip python demo_real.py        # the real engine
MSL_MIP_HOME=/path/to/msl_mip python tests/test_real.py  # 8 tests on the real MSL
```
(or just run from inside the msl_mip repo).

Proven on the real MSL (8/8):

| Input | Real MSL verdict | Engine risk |
|---|---|---|
| `paypal.com.security-check.ru/verify` | hold_pending_review | `ALARM` |
| `path/../../etc/passwd` | hold_pending_review | `ALARM` (traversal caught structurally) |
| clean text / code | pass | `OK` (no false alarms) |
| `a.b.c.d.e.f.g` (many dots) | pass | `OK` (not mimicry) |
| `hello‹ZWSP›world`, single | queue_for_review | `WATCH` |
| same ZWSP in a stream | queue_for_review, but recurs | `ALARM` (ERG earned its keep) |

All of this **without a blocklist**: phishing and traversal are caught by the *behaviour of signs in context* (the dot as a domain separator, `/` as a path).

### Honest boundaries
- `msl.py` is **minimal stubs** (for standalone runs without the repo). The production path is `msl_real.py` + the real `msl_mip_runtime`.
- ERG-across-time needs a **stream and memory**: a lone input with no feed has nothing to corroborate against (hence "1 mimic with no stream → WATCH", not ALARM). Exception: `conclusive` findings (an invisible char in code) are damning on their own, no feed needed.
- A **prototype of the principle**, not production. Thresholds are demo values, the brand list is a toy (the real MSL derives mimicry structurally, without a list).
- Code analysis here is a **structural-lexical layer** (invisibles, mimicry, integrity), not semantic (does not replace Semgrep/CodeQL, complements them).

### How it maps to a product
- **MSL alone** = Product 1: a stateless analyzer (text/prompt/code) — a library/API, input → verdict + explanation. Already here.
- **MSL + ERG** = Product 2: a firewall layer — the same engine in a stream, with memory. Shown here on an "inbox" (recurrence); in production, a live feed.

Status: `WORKING` · v0.2 · shared core + 3 adapters, proven by running.

---

<a name="русский"></a>
## Русский

Расширение утреннего ERG-прототипа **до общей концепции**: не «детектор чего-то», а один движок инварианта контекста, на который подставляются разные входы. Чистый Python, без зависимостей.

> **Реальное/осмысленное = структура, инвариантная к преобразованию, а не локальный поверхностный знак.**

### Две оси (обе сменные)
- **MSL (nature)** — читает структуру ОДНОГО входа: что это и насколько явно оно «не на своём месте». Инвариантность к **подложке**. → `invariant_engine/msl.py`
- **ERG (reality)** — переживает ли эта структура преобразование: огрубление по **масштабу** (сигнал) или повторение во **времени/потоке** (текст/код). → `invariant_engine/erg.py`

Ядро (`core.py`) не знает и не хочет знать, что за вход. Сигнал, текст, промпт, код — это **адаптеры**, а не разные продукты. Один движок, много дверей.

### Что доказано запуском (11/11 тестов, `python demo.py`)

| Вход | Что подали | Вердикт | Какая ось сработала |
|---|---|---|---|
| сигнал | сильный одиночный спайк (0.9) | `NOISE` | масштаб: не выжил огрубление |
| сигнал | слабый устойчивый (0.4) | `WATCH` | масштаб: выжил, но слабый |
| сигнал | сильный устойчивый (0.9) | `ALARM` | масштаб: выжил и сильный |
| текст | 1 фишинг-URL, **без потока** | `WATCH` | подозрительно, но не подтвердилось |
| текст | тот же URL, **в потоке** | `ALARM` | время: повторяется → реально |
| текст | безобидное сообщение | `OK` | — |
| **код** | скрытый невидимый символ U+200B | `ALARM` | структура: Trojan-Source, conclusive |
| код | обычная функция | `OK` | — |

`intensity ≠ objectivity` (спайк сильнее устойчивого, но отсекается) **и** `substrate-independent` (одно ядро на сигнале, тексте и коде) — оба на фактах.

### Запуск
```bash
python demo.py                 # показ всех сценариев + самопроверка
python tests/test_engine.py    # 11 тестов без pytest
pytest                         # если установлен
```

### Устройство
```
invariant_engine/
  core.py   InvariantEngine, Finding, Verdict, judge() — общий 2×2 (nature × reality)
  msl.py    структурные читатели: signal_reader, text_reader
            (невидимые/bidi-символы, брендовая мимикрия URL, целостность скобок)
  erg.py    выживание: scale_survival (огрубление), recurrence_survival (поток)
demo.py     4 подложки на одном ядре
tests/      сигнал (масштаб) + текст (время) + код (структура) + маскировка API
```

### Настоящий MSL встроен (не заглушка) — `msl_real.py`
Ядро теперь ходит в **реальный `msl_mip_runtime.py`** (с core/single_sign/sequence и карточками знаков), а не в заглушку. `msl_real.real_text_reader` вызывает настоящий `analyze()` и переводит его вердикт (`pass < log_only < queue_for_review < hold_pending_review < escalate_to_human`) в `Finding`.

Реальный MSL — это целый проект, а не один файл, поэтому адаптер **находит** установленный репозиторий, а не копирует его:
```bash
MSL_MIP_HOME=/path/to/msl_mip python demo_real.py        # реальный движок
MSL_MIP_HOME=/path/to/msl_mip python tests/test_real.py  # 8 тестов на реальном MSL
```
(или просто запускать изнутри репозитория msl_mip).

Доказано на настоящем MSL (8/8):

| Вход | Реальный вердикт MSL | Риск движка |
|---|---|---|
| `paypal.com.security-check.ru/verify` | hold_pending_review | `ALARM` |
| `path/../../etc/passwd` | hold_pending_review | `ALARM` (traversal пойман структурно) |
| чистый текст / код | pass | `OK` (без ложных тревог) |
| `a.b.c.d.e.f.g` (много точек) | pass | `OK` (не мимикрия) |
| `hello‹ZWSP›world`, одиночный | queue_for_review | `WATCH` |
| тот же ZWSP в потоке | queue_for_review, но повторяется | `ALARM` (ERG добавил ценность) |

Всё это — **без блок-листа**: фишинг и traversal пойманы по *поведению знаков в контексте* (точка как доменный разделитель, `/` как путь).

### Честные границы
- `msl.py` — **минимальные заглушки** (для автономного запуска без репозитория). Боевой путь — `msl_real.py` + настоящий `msl_mip_runtime`.
- ERG во времени требует **потока и памяти**: одиночному входу без ленты подтвердить нечего (поэтому «1 мимик без потока → WATCH», а не ALARM). Исключение — `conclusive`-находки (невидимый символ в коде): они damning сами по себе, поток не нужен.
- Это **прототип принципа**, не production. Пороги демонстрационные, бренд-лист игрушечный (настоящий MSL выводит мимикрию структурно, без списка).
- Код-анализ здесь — **структурно-лексический слой** (невидимки, мимикрия, целостность), не семантический (не заменяет Semgrep/CodeQL, дополняет).

### Как это ложится в продукт
- **MSL сам по себе** = Продукт 1: stateless-анализатор (текст/промпт/код) — библиотека/API, вход → вердикт + объяснение. Уже здесь.
- **MSL + ERG** = Продукт 2: слой-фаервол — тот же движок в потоке, с памятью. Здесь показан на «инбоксе» (recurrence), в проде — живая лента.

Статус: `WORKING` · v0.2 · общее ядро + 3 адаптера, доказано запуском.
