# Applications · Приложения

🇬🇧 [English](#english) · 🇷🇺 [Русский](#русский)

---

<a name="english"></a>
## English — the same mechanisms, other fields

The guard (`code/`) was one product. Its parts are general primitives, so the
same machinery spins out into other fields. These are runnable MVP sketches
(one file each, zero dependencies) built from the project's own components —
same honest style: measured, reproducible, primitive = reliable = auditable.

All of them sit on the one idea the whole project turns on:
> **real / meaningful = the structure that is INVARIANT under a transform —
> native vs inserted, signal vs noise — not the surface value.**

| product | guards | the transform it is invariant to | reused from |
|---|---|---|---|
| **ai_gateway** (Vakhter) | a message/prompt reaching an LLM | substrate / encoding | MSL + cards + ERG |
| **notarius_data** | a data record / ledger row | tampering / insertion / foreign origin | provenance + transparency |
| **erg_fraud** | a stream of numbers | scale (coarse-graining) | ERG (intensity ≠ objectivity) |

### ai_gateway — Vakhter in front of an LLM (`ai_gateway/ai_gateway.py`)
The guard as a drop-in shield for an AI app. One call — `guarded_llm_call(user_msg, context_docs, llm)` — scans the user message **and** every retrieved/tool document before the model reads them: a hidden command, a `data:` URI, an invisible-smuggled instruction, a look-alike domain are blocked at the gate; only clean text reaches the model. Honest scope: this is the **structural** half; pure natural-language injection is the job of a semantic guardrail beside it.
Fields: chatbots, RAG assistants, agents — anything that reads untrusted text.

### notarius_data — provenance ledger (`notarius_data/notarius_ledger.py`)
A lightweight, no-heavy-DB provenance layer for DATA RECORDS (invoices, transactions, document fields). Four independent barriers, each catching a different attack: **hash** (content), **codepoint-length witness** (insertion, incl. invisibles — crypto-free), **signed lineage** (native origin: SIGNED ≠ NATIVE), **append-only log** (tamper-evident history). Demo catches: equal-length edit, length-changing edit + invisible-char injection, attacker re-sign (forged lineage), a FOREIGN row with a valid hash, and a rewritten log entry (chain break).
Fields: finance/audit ledgers, ETL data lineage (element-level), document notarisation / chain of custody.

### erg_fraud — anomaly detection by survival across scale (`erg_fraud/erg_fraud.py`)
A real anomaly SURVIVES zoom-out. Coarse-grain the stream at several scales; a one-off spike (a legit big purchase) is intense at the finest scale but DISSOLVES when averaged → NOISE; a distributed pattern (structuring / card-testing / slow drain — many small events clustered in time) SURVIVES → REAL, even though no single event trips a per-transaction threshold. Verified across 5 seeds: a naive threshold false-alarms on the spike AND misses the distributed fraud; ERG does the opposite. No model, no training, no database.
Fields: fraud / AML, IoT & sensor validation, trading anomalies (its origin, ERG-CAD), any signal-vs-noise stream.

### Honest status
MVP sketches, not products: learning HMAC (→ real asymmetric signatures in prod), hand-tuned thresholds, small demo batteries. Mature incumbents exist in data lineage (DataHub) and anomaly detection — the edge here is the same as the guard's: lightweight, reasons instead of looks-up, fully auditable, fails safe.
Run: `python applications/ai_gateway/ai_gateway.py` · `python applications/notarius_data/notarius_ledger.py` · `python applications/erg_fraud/erg_fraud.py`.

---

<a name="русский"></a>
## Русский — те же механизмы, другие сферы

Вахтёр (`code/`) был одним продуктом. Его части — общие примитивы, поэтому та же механика даёт ответвления в другие сферы. Это запускаемые MVP-наброски (по одному файлу, без зависимостей), собранные из компонентов самого проекта — в том же честном стиле: измеримо, воспроизводимо, примитивно = надёжно = аудируемо.

Все они стоят на одной мысли, вокруг которой построен проект:
> **реальное / осмысленное = структура, ИНВАРИАНТНАЯ к преобразованию —
> родное или вставленное, сигнал или шум — а не поверхностное значение.**

| продукт | что охраняет | к какому преобразованию инвариантен | взято из |
|---|---|---|---|
| **ai_gateway** (Vakhter) | сообщение/промпт, идущее в LLM | подложка / кодировка | MSL + карточки + ERG |
| **notarius_data** | запись данных / строку реестра | подмене / вставке / чужому origin | провенанс + transparency |
| **erg_fraud** | поток чисел | масштабу (огрублению) | ERG (интенсивность ≠ объективность) |

### ai_gateway — Vakhter перед LLM (`ai_gateway/ai_gateway.py`)
Вахтёр как drop-in щит для ИИ-приложения. Один вызов — `guarded_llm_call(user_msg, context_docs, llm)` — проверяет сообщение пользователя **и** каждый найденный/инструментальный документ до того, как их прочитает модель: спрятанная команда, `data:`-URI, невидимо-протащенная инструкция, домен-двойник блокируются на входе; до модели доходит только чистое. Честная граница: это **структурная** половина; чисто языковая инъекция — работа смыслового барьера рядом.
Сферы: чат-боты, RAG-ассистенты, агенты — всё, что читает недоверенный текст.

### notarius_data — provenance-реестр (`notarius_data/notarius_ledger.py`)
Лёгкий, без тяжёлой БД, слой происхождения для ЗАПИСЕЙ ДАННЫХ (счета, транзакции, поля документов). Четыре независимых барьера, каждый ловит свою атаку: **хеш** (содержимое), **улика длины в кодпоинтах** (вставка, включая невидимки — без криптографии), **подписанная родословная** (родной origin: SIGNED ≠ NATIVE), **append-only лог** (история с уликой на подмену). Демо ловит: правку равной длины, правку со сменой длины + вставку невидимого символа, пере-подпись атакующим (поддельная родословная), ЧУЖУЮ строку с валидным хешем и переписанную запись лога (разрыв цепочки).
Сферы: финансовые/аудиторские реестры, data-lineage в ETL (на уровне элемента), нотаризация документов / chain of custody.

### erg_fraud — детекция аномалий по выживанию через масштаб (`erg_fraud/erg_fraud.py`)
Реальная аномалия ВЫЖИВАЕТ при отдалении. Огрубляем поток на нескольких масштабах; разовый всплеск (честная крупная покупка) интенсивен на самом мелком масштабе, но РАСТВОРЯЕТСЯ при усреднении → ШУМ; распределённый паттерн (structuring / card-testing / медленный слив — много мелких событий, скученных во времени) ВЫЖИВАЕТ → РЕАЛЬНО, хотя ни одно событие не перебивает по-транзакционный порог. Проверено на 5 сидах: наивный порог даёт ложную тревогу на всплеске И пропускает распределённое мошенничество; ERG — наоборот. Без модели, без обучения, без базы.
Сферы: фрод / AML, валидация IoT-сенсоров, торговые аномалии (его родина, ERG-CAD), любой поток «сигнал против шума».

### Честный статус
MVP-наброски, не продукты: учебный HMAC (→ настоящие асимметричные подписи в проде), пороги вручную, небольшие демо-батареи. В data-lineage (DataHub) и детекции аномалий есть зрелые игроки — наш край тот же, что у вахтёра: лёгкий, рассуждает вместо справочника, полностью аудируем, падает безопасно.
Запуск: `python applications/ai_gateway/ai_gateway.py` · `python applications/notarius_data/notarius_ledger.py` · `python applications/erg_fraud/erg_fraud.py`.
