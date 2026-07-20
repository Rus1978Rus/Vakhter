# Notarius — collected working notes · Notarius — полный сборник наработок

AUTHOR / АВТОР: Руслан Малявский · COMMERCIAL USE PROHIBITED · DATE: 2026-07-20 · STATUS: `WORKING DOCUMENT`

🇬🇧 [English](#english) · 🇷🇺 [Русский](#русский)

---

<a name="english"></a>
## English

### 1. Definition
**Notarius** — a provenance tracker for data elements: where it came from, what it passed through, native or inserted.
```
ORIGIN + TRACE + CURRENT_STATE
```

### 2. Origin of the project
The idea grew out of the MSL/MIP Sign Alphabet.
Key clarification (Руслан): *"If this were a question of cryptography, it would have been solved decades ago."*
That split two layers:
```
Cryptography:  changed? is the signature valid?
Notarius:      where did the element come from? what did it pass through? native or inserted?

INTEGRITY_LAYER ≠ PROVENANCE_LAYER
```

### 3. The vertical of projects
```
MSL/MIP   → sign identity      → WHAT SIGN IS THIS?
Notarius  → element provenance → WHERE DID THE ELEMENT COME FROM?
SSP       → meaning provenance → WHAT HAPPENED TO THE MEANING?

SIGN ↓ ELEMENT ↓ MEANING

The shared question of all three:
not only "what is it?" but "where did it come from and what happened to it?"
```

### 4. Difference from cryptography

| Cryptography | Notarius |
|---|---|
| Is the signature valid? | Where is the element from? |
| Does the hash match? | What did it pass through? |
| Was the file changed? | Native or inserted? |
| Is the key known? | When did the break occur? |
| Container level | Element level |

```
SIGNED ≠ NATIVE
HASH_VALID ≠ CLEAN_ELEMENT
CONTAINER_INTACT ≠ ELEMENT_CLEAN
TRACE_EXISTS ≠ TRACE_CONTINUOUS
```

### 5. What Notarius does NOT do
```
Notarius ≠ cryptography
Notarius ≠ a replacement for a digital signature
Notarius ≠ a court
Notarius ≠ proof of truth
Notarius ≠ automatic seizure
Notarius ≠ asset recovery

VALIDATOR ≠ COURT
TRACE ≠ PROOF
```

### 6. Fixed properties

**6.1 SEMANTIC_MANIFEST_KEY** (`FIXED`, 2026-07-06)
The sender transmits a package (blocks in any order) + a trace key (semantic manifest). The receiver: key → assembly → verification of order + meaning. Without the key: the blocks are there, the meaning is opaque (semantic obfuscation). With the key: full structure.
Difference from blockchain: blockchain = a cryptographic chain with no block semantics; Notarius = `semantic_type + origin + state` per block.

**6.2 SEMANTIC_LAYERED_DEFENSE** (`FIXED`, 2026-07-06)
Four independent barriers for the attacker: (1) the key, (2) the block schema, (3) semantic typing, (4) assembly order.
`KEY_KNOWN ≠ STRUCTURE_KNOWN`; `STRUCTURE_KNOWN ≠ MEANING_RECOVERED`.
Difference from encryption: break the key and you get everything — here, break the key and you get shards with no assembly instructions. Even a weak password + an unknown semantic structure = the attacker gets meaningless mush.

**6.3 SEMANTIC_INVISIBLE_LENGTH_WITNESS** (`PROPERTY_CANDIDATE → needs conveyor`, 2026-07-07)
Each block carries a control length in Unicode codepoints in the manifest. Any insertion/deletion of a character — including invisibles (ZWSP U+200B, ZWJ U+200D, VS16 U+FE0F, BOM, bidi overrides) — shifts the count and breaks the check.
Catches: ZWSP/ZWJ/VS16/BOM inside a block (len +1); invisible at the start / end / middle of a block. Does NOT catch: an equal-length substitution ("1000" → "2000") — that needs a separate hash.
```
INVISIBLE_INSERTION → CODEPOINT_COUNT_SHIFT → MANIFEST_MISMATCH
LENGTH_INTACT ≠ CONTENT_INTACT   (both barriers needed)
KEY_KNOWN ≠ LENGTH_INTACT        (independent layer)
LENGTH_INTACT ∧ CONTENT_INTACT = the full pair
```
Minimal prototype (the first working Notarius code):
```python
def block_with_witness(data: str) -> dict:
    return {"data": data, "cp_len": len(data)}

def verify_witness(block: dict) -> bool:
    return len(block["data"]) == block["cp_len"]
```
Three lines. No dependencies. No cryptographic library.

### 7. FO candidate — MANIPULATION_LEAVES_SUBSTRATE_TRACE (`FO-CANDIDATE / NEEDS_CONVEYOR`, 2026-07-06)
`CORE_FORMULA: BEST_VERIFICATION_SYSTEM = SUBSTRATE_RECORDS_MANIPULATION_ITSELF`.
The best verification systems are those where the substrate itself records the intervention — with no external observer.
Verified cases: (1) a punched card (IBM, 1960s) — you can't reseal a punched hole unnoticed, the medium is the detector; (2) photographic film — a splice shows on the frame and the join; (3) a wax seal — opening it destroys the seal; (4) Notarius / semantic tracing — the substrate is `semantic manifest + blocks`, the manipulation breaks the `trace_chain`, the structure itself is the detector.
```
MANIPULATION_VISIBLE ≠ MANIPULATION_PREVENTED
SUBSTRATE_TRACE = BEST_AVAILABLE_DETERRENT
```

### 8. Product candidate — PROVENANCE_CARRIER (`CANDIDATE_REGISTERED — not conveyor-run, no prototype`, 2026-07-12)
The semantic trace is collected INSIDE the system. It must be verified OUTSIDE — where our code is not. The carrier = a compact, self-contained, detachable piece of evidence that survives leaving the system.
Layer 1 (REJECTED): QR as transport INSIDE the pipeline — blind to a missing finding, two extra points of silent failure, ~3 KB is too small for traces.
Layer 2 (CANDIDATE): a carrier AT THE BOUNDARY of the system. QR exists to carry data out to where our code isn't — onto paper, onto a screen, into other hands. It is not transport; it is the EXIT.
Open triangle (to solve together, not in sequence): (1) what MINIMALLY goes on the carrier? the full trace won't fit — a fingerprint? critical stamps? (2) is Kerckhoffs dropped or moved — who holds the key, where does the receiver get the public key? (3) QR or another carrier? — chosen AFTER answering (1).
Dependency: first the semantic tracing (collect the trace), then the carrier (carry it out). You can't print a routing sheet that doesn't exist yet.

### 9. Element state model
```
Each element has: ORIGIN, TRACE, TIME, CURRENT_STATE
Possible states: INTACT / MODIFIED / PARTIAL / SEGMENTED / MERGED /
                 MIXED / CONVERTED / UNKNOWN / ARCHIVED / DELETED / RECOVERED

Normal element:            Break:
  ELEMENT_ID: E-145          ELEMENT_ID: E-145
  ORIGIN: Sensor_A           CURRENT_STATE: MODIFIED
  CURRENT_STATE: INTACT      MODIFICATION_WINDOW: 14:35 - 14:42
  TRACE_STATUS: CONTINUOUS   TRACE_STATUS: BROKEN

PROVENANCE ≠ CURRENT_STATE
TRACE_BREAK_TIME ≠ EXACT_ATTACK_TIME
INTERVENTION_TIME ≠ INTERVENTION_CAUSE
```

### 10. Trace levels
```
TRACE_LEVEL_1 — CRITICAL_ONLY: amounts, statuses, dates, accesses, signatures, commands, coordinates
TRACE_LEVEL_2 — SEMANTIC_UNITS: intent, claim, value, role, permission, prohibition, provenance, authority_status, execution_status
TRACE_LEVEL_3 — FULL_ELEMENT_TRACE: characters, tokens, structural elements, transformation steps, byte representations

TRACE_DEPTH_FOLLOWS_RISK · TRACE_COST vs LOSS_SCALE · MORE_TRACE ≠ MORE_TRUTH · MORE_TRACE = MORE_OBSERVABILITY
```

### 11. Use in forensic examination
For a court, the difference between "I think it was forged" and "here is the provenance chain with a break at step 3". Notarius = a digital chain of custody for data elements.
Adoption model: banks historically introduced standards through pain (SWIFT, ISO 20022, PCI DSS). No need to lobby in advance — the product just has to exist and be ready for moment X.

### 12. Asset tracing
```
ASSET_A = 10 000 000  →  A1 = 2 000 000 → account_X
                         A2 = 3 000 000 → wallet_Y
                         A3 = 5 000 000 → securities_Z

Notarius sees: these are not independent pieces — they are fragments of one original origin.

SPLIT_ASSET ≠ LOST_PROVENANCE · MIXED_ASSET ≠ CLEAN_ASSET
UNREACHABLE_ASSET ≠ UNTRACEABLE_ASSET · TEMPORARY_SAFE_HAVEN ≠ PROVENANCE_RESET
```

### 13. Physical analogy (banknote)
A $100 note cut into three parts and taped together. The serial number MF 34567890 C is present on two fragments.
Observation: physical fragmentation does not destroy provenance if the identifier is embedded in the substrate, not the container.
```
SPLIT_OBJECT ≠ LOST_PROVENANCE
PROVENANCE_SURVIVES_FRAGMENTATION
```
Architecture takeaway: the provenance identifier must be embedded in the element, not only in the container.

### 14. Punched-card analogy
IBM EBCDIC punched card, 1960s. Each character is a unique combination of punches; forgery is impossible — a hole is either there or not.
```
Punched card:  character → unique physical mark
Notarius:      element   → unique semantic mark

Punched card = three-in-one: KEY (the punch combination = identifier),
CARRIER (the card itself holds the data), DETECTOR (manipulation is physically visible).

COMPLEXITY ≠ SECURITY · SIMPLICITY = VERIFIABILITY · VERIFIABILITY = TRUST
```

### 15. Niche check (web search, 2026-07-06)
What EXISTS: data lineage / data provenance (a real industry); academic element-level provenance (medicine, W3C); blockchain-based provenance (patent level).
What does NOT exist: a provider embedded on the transaction path; a real-time semantic mark at the element level; foreign-insertion detection as an infrastructure product.
**VERDICT: NICHE_CONFIRMED / SPACE_OPEN.**

### 16. First prototype (plan)
A plain-text provenance demo. Show: (1) an element with an origin tag; (2) an element with a normal trace chain; (3) an insertion with no tag; (4) break detection; (5) state: INTACT / INSERTED / UNKNOWN.
```
DOCUMENT_A:  amount=1000000  origin=invoice_458  trace=created→checked→archived  state=INTACT
after tamper: amount=9000000  origin=UNKNOWN  trace=missing  state=INSERTED_OR_MODIFIED
expected output: TRACE_BREAK_DETECTED · field: amount · expected_origin: invoice_458 · actual_origin: UNKNOWN · status: NEEDS_REVIEW
```

### 17. Current priority
```
ACTIVE_FRONT: MSL/MIP Sign Cards → Modules → Integrators
PARKED: Notarius · SSP · Video Trace · Element Provenance · Asset Recovery Trace · PROVENANCE_CARRIER
ORDER: 1. MSL/MIP core → 2. Notarius tracing (collect the trace) → 3. PROVENANCE_CARRIER (carry the trace out)
```

### 18. Canonical phrases
Cryptography checks the integrity of the container. Notarius checks the provenance of the element. SSP checks the state of the meaning.
Notarius does not recover the asset itself — it makes the asset's provenance hard to erase.
Not every byte. Not only the whole file. But `chunk + boundary`.
When internal memory is unreliable, you need an external trace.
The best verification systems are those where the substrate itself records the intervention.
**PRIMITIVE = RELIABLE = AUDITABLE.**

---

<a name="русский"></a>
## Русский

### 1. ОПРЕДЕЛЕНИЕ
**Notarius** — provenance-трекер для элементов данных: откуда пришёл, через что прошёл, свой или вставлен.
```
ORIGIN + TRACE + CURRENT_STATE
```

### 2. ПРОИСХОЖДЕНИЕ ПРОЕКТА
Идея возникла из MSL/MIP Sign Alphabet.
Ключевое уточнение (Руслан): *«Если бы вопрос был в криптографии, его бы решили много десятилетий назад.»*
Это разграничило два слоя:
```
Криптография:  изменили? подпись валидна?
Notarius:      откуда пришёл элемент? через что прошёл? свой или вставлен?

INTEGRITY_LAYER ≠ PROVENANCE_LAYER
```

### 3. ВЕРТИКАЛЬ ПРОЕКТОВ
```
MSL/MIP   → sign identity      → ЧТО ЭТО ЗА ЗНАК?
Notarius  → element provenance → ОТКУДА ПРИШЁЛ ЭЛЕМЕНТ?
SSP       → meaning provenance → ЧТО СЛУЧИЛОСЬ СО СМЫСЛОМ?

SIGN ↓ ELEMENT ↓ MEANING

Общий вопрос всех трёх: не только "что это?", а "откуда это пришло и что с ним происходило?"
```

### 4. ОТЛИЧИЕ ОТ КРИПТОГРАФИИ

| Криптография | Notarius |
|---|---|
| Подпись валидна? | Откуда элемент? |
| Хеш совпадает? | Через что прошёл? |
| Файл изменён? | Свой или вставленный? |
| Ключ известен? | Когда возник разрыв? |
| Уровень контейнера | Уровень элемента |

```
SIGNED ≠ NATIVE
HASH_VALID ≠ CLEAN_ELEMENT
CONTAINER_INTACT ≠ ELEMENT_CLEAN
TRACE_EXISTS ≠ TRACE_CONTINUOUS
```

### 5. ЧТО NOTARIUS НЕ ДЕЛАЕТ
```
Notarius ≠ криптография
Notarius ≠ замена цифровой подписи
Notarius ≠ суд
Notarius ≠ доказательство истины
Notarius ≠ автоматическая конфискация
Notarius ≠ возврат актива

VALIDATOR ≠ COURT
TRACE ≠ PROOF
```

### 6. ЗАФИКСИРОВАННЫЕ СВОЙСТВА

**6.1 SEMANTIC_MANIFEST_KEY** (`ЗАФИКСИРОВАНО`, 2026-07-06)
Отправитель передаёт пакет (блоки в любом порядке) + ключ трассировки (semantic manifest). Получатель: ключ → сборка → верификация порядка + смысла. Без ключа: блоки есть, смысл непонятен (семантическая обфускация). С ключом: полная структура.
Отличие от blockchain: blockchain = криптографическая цепочка без семантики блока; Notarius = `semantic_type + origin + state` для каждого блока.

**6.2 SEMANTIC_LAYERED_DEFENSE** (`ЗАФИКСИРОВАНО`, 2026-07-06)
Четыре независимых барьера для атакующего: (1) ключ, (2) схема блоков, (3) семантическая типизация, (4) порядок сборки.
`КЛЮЧ_ИЗВЕСТЕН ≠ СТРУКТУРА_ИЗВЕСТНА`; `СТРУКТУРА_ИЗВЕСТНА ≠ СМЫСЛ_ВОССТАНОВЛЕН`.
Отличие от шифрования: сломал ключ → получил всё; здесь сломал ключ → получил осколки без инструкции сборки. Даже слабый пароль + неизвестная семантическая структура = атакующий получает кашу без смысла.

**6.3 SEMANTIC_INVISIBLE_LENGTH_WITNESS** (`PROPERTY_CANDIDATE → требует конвейера`, 2026-07-07)
Каждый блок несёт в манифесте контрольную длину в кодпоинтах Unicode. Любая вставка/удаление символа, включая невидимые (ZWSP U+200B, ZWJ U+200D, VS16 U+FE0F, BOM, bidi-оверрайды), меняет счётчик и ломает сверку.
Ловит: ZWSP/ZWJ/VS16/BOM внутри блока (len +1); невидимый в начале / конце / середине блока. Не ловит: подмену равной длины («1000» → «2000») — для этого нужен отдельный хеш.
```
INVISIBLE_INSERTION → CODEPOINT_COUNT_SHIFT → MANIFEST_MISMATCH
LENGTH_INTACT ≠ CONTENT_INTACT   (нужны оба барьера)
KEY_KNOWN ≠ LENGTH_INTACT        (независимый слой)
LENGTH_INTACT ∧ CONTENT_INTACT = полная пара
```
Минимальный прототип (первый рабочий код Notarius):
```python
def block_with_witness(data: str) -> dict:
    return {"data": data, "cp_len": len(data)}

def verify_witness(block: dict) -> bool:
    return len(block["data"]) == block["cp_len"]
```
Три строки. Никаких зависимостей. Никакой криптографической библиотеки.

### 7. FO-КАНДИДАТ — MANIPULATION_LEAVES_SUBSTRATE_TRACE (`FO-CANDIDATE / NEEDS_CONVEYOR`, 2026-07-06)
`CORE_FORMULA: BEST_VERIFICATION_SYSTEM = SUBSTRATE_RECORDS_MANIPULATION_ITSELF`.
Лучшие системы верификации те, где субстрат сам фиксирует вмешательство — без внешнего наблюдателя.
Проверенные случаи: (1) перфокарта (IBM, 1960-е) — дырку нельзя заклеить незаметно, детектор — сам носитель; (2) фотоплёнка — склейка видна на кадре и стыке; (3) сургучная печать — вскрытие разрушает печать; (4) Notarius / семантическая трассировка — субстрат `semantic manifest + блоки`, манипуляция рвёт `trace_chain`, детектор — сама структура.
```
MANIPULATION_VISIBLE ≠ MANIPULATION_PREVENTED
SUBSTRATE_TRACE = BEST_AVAILABLE_DETERRENT
```

### 8. PRODUCT_CANDIDATE — PROVENANCE_CARRIER (`CANDIDATE_REGISTERED — конвейер не прогонялся, прототипа нет`, 2026-07-12)
Семантический след собирается ВНУТРИ системы. Проверять его нужно СНАРУЖИ — там, где нашего кода нет. Носитель = компактное, самодостаточное, отделимое свидетельство, которое переживает выход из системы.
Слой 1 (REJECTED): QR как транспорт ВНУТРИ тракта — слеп к неявке находки, два лишних места тихого сбоя, ёмкость ~3КБ мала для трейсов.
Слой 2 (CANDIDATE): носитель на ГРАНИЦЕ системы. QR существует, чтобы вынести данные туда, где нашего кода нет: на бумагу, на экран, в чужие руки. Это не транспорт — это ВЫХОД.
Открытый треугольник (решать вместе, не последовательно): (1) что МИНИМАЛЬНО в носитель? полный след не влезет — отпечаток? критические штампы? (2) Kerckhoffs снимается или переезжает — кто держит ключ, где получатель берёт публичный? (3) QR или другой носитель? — выбирается ПОСЛЕ ответа на п.1.
Зависимость: сначала семантическая трассировка (собрать след), потом носитель (вынести след). Нельзя печатать маршрутный лист, которого ещё нет.

### 9. МОДЕЛЬ СОСТОЯНИЙ ЭЛЕМЕНТА
```
Каждый элемент имеет: ORIGIN, TRACE, TIME, CURRENT_STATE
Возможные состояния: INTACT / MODIFIED / PARTIAL / SEGMENTED / MERGED /
                     MIXED / CONVERTED / UNKNOWN / ARCHIVED / DELETED / RECOVERED

Нормальный элемент:        Разрыв:
  ELEMENT_ID: E-145          ELEMENT_ID: E-145
  ORIGIN: Sensor_A           CURRENT_STATE: MODIFIED
  CURRENT_STATE: INTACT      MODIFICATION_WINDOW: 14:35 - 14:42
  TRACE_STATUS: CONTINUOUS   TRACE_STATUS: BROKEN

PROVENANCE ≠ CURRENT_STATE
TRACE_BREAK_TIME ≠ EXACT_ATTACK_TIME
INTERVENTION_TIME ≠ INTERVENTION_CAUSE
```

### 10. УРОВНИ ТРАССИРОВКИ
```
TRACE_LEVEL_1 — CRITICAL_ONLY: суммы, статусы, даты, доступы, подписи, команды, координаты
TRACE_LEVEL_2 — SEMANTIC_UNITS: intent, claim, value, role, permission, prohibition, provenance, authority_status, execution_status
TRACE_LEVEL_3 — FULL_ELEMENT_TRACE: символы, токены, структурные элементы, шаги преобразования, байтовые представления

TRACE_DEPTH_FOLLOWS_RISK · TRACE_COST vs LOSS_SCALE · MORE_TRACE ≠ MORE_TRUTH · MORE_TRACE = MORE_OBSERVABILITY
```

### 11. ПРИМЕНЕНИЕ В СУДЕБНОЙ ЭКСПЕРТИЗЕ
Для суда разница между «я думаю, что подделали» и «вот цепочка происхождения с разрывом на шаге 3». Notarius = цифровой chain of custody для элементов данных.
Модель внедрения: банки исторически вводили стандарты через боль (SWIFT, ISO 20022, PCI DSS). Не нужно лоббировать заранее — нужно, чтобы продукт существовал и был готов к моменту X.

### 12. ОТСЛЕЖИВАНИЕ АКТИВОВ
```
ASSET_A = 10 000 000  →  A1 = 2 000 000 → account_X
                         A2 = 3 000 000 → wallet_Y
                         A3 = 5 000 000 → securities_Z

Notarius видит: это не независимые куски — это фрагменты одного исходного происхождения.

SPLIT_ASSET ≠ LOST_PROVENANCE · MIXED_ASSET ≠ CLEAN_ASSET
UNREACHABLE_ASSET ≠ UNTRACEABLE_ASSET · TEMPORARY_SAFE_HAVEN ≠ PROVENANCE_RESET
```

### 13. ФИЗИЧЕСКАЯ АНАЛОГИЯ (банкнота)
Банкнота $100 разрезана на три части и склеена пластырем. Серийный номер MF 34567890 C присутствует на двух фрагментах.
Наблюдение: физическая фрагментация не уничтожает провенанс, если идентификатор встроен в субстрат, а не в контейнер.
```
SPLIT_OBJECT ≠ LOST_PROVENANCE
PROVENANCE_SURVIVES_FRAGMENTATION
```
Вывод для архитектуры: идентификатор происхождения должен быть встроен в элемент, а не только в контейнер.

### 14. АНАЛОГИЯ ПЕРФОКАРТЫ
IBM EBCDIC punched card, 1960-е. Каждый символ — уникальная комбинация пробивок; подделать невозможно: дырка либо есть, либо нет.
```
Перфокарта:  символ → уникальная физическая метка
Notarius:    элемент → уникальная семантическая метка

Перфокарта = три в одном: КЛЮЧ (комбинация пробивок = идентификатор),
НОСИТЕЛЬ (сама карта несёт данные), ДЕТЕКТОР (манипуляция физически видна).

COMPLEXITY ≠ SECURITY · SIMPLICITY = VERIFIABILITY · VERIFIABILITY = TRUST
```

### 15. ПРОВЕРКА НИШИ (веб-поиск, 2026-07-06)
Что существует: data lineage / data provenance (реальная индустрия); академические реализации element-level provenance (медицина, W3C); blockchain-based provenance (патентный уровень).
Чего не существует: встроенного на пути транзакций провайдера; реального времени семантической метки на уровне элемента; детекции чужеродных вставок как инфраструктурного продукта.
**ВЕРДИКТ: NICHE_CONFIRMED / SPACE_OPEN.**

### 16. ПЕРВЫЙ ПРОТОТИП (план)
Plain-text provenance demo. Показать: (1) элемент с origin tag; (2) элемент с нормальной trace chain; (3) вставку без метки; (4) детекцию разрыва; (5) состояние: INTACT / INSERTED / UNKNOWN.
```
DOCUMENT_A:  amount=1000000  origin=invoice_458  trace=created→checked→archived  state=INTACT
после подмены: amount=9000000  origin=UNKNOWN  trace=missing  state=INSERTED_OR_MODIFIED
ожидаемый вывод: TRACE_BREAK_DETECTED · field: amount · expected_origin: invoice_458 · actual_origin: UNKNOWN · status: NEEDS_REVIEW
```

### 17. ТЕКУЩИЙ ПРИОРИТЕТ
```
ACTIVE_FRONT: MSL/MIP Sign Cards → Modules → Integrators
PARKED: Notarius · SSP · Video Trace · Element Provenance · Asset Recovery Trace · PROVENANCE_CARRIER
ПОРЯДОК: 1. MSL/MIP ядро → 2. Notarius трассировка (собрать след) → 3. PROVENANCE_CARRIER (вынести след)
```

### 18. КАНОНИЧЕСКИЕ ФРАЗЫ
Криптография проверяет целостность контейнера. Notarius проверяет происхождение элемента. SSP проверяет состояние смысла.
Notarius не возвращает актив сам — он делает происхождение актива трудно стираемым.
Не каждый байт. Не только весь файл. А `chunk + boundary`.
Когда внутренняя память ненадёжна — нужен внешний след.
Лучшие системы верификации те, где субстрат сам фиксирует вмешательство.
**ПРИМИТИВНО = НАДЁЖНО = АУДИРУЕМО.**

---

*COMMERCIAL USE PROHIBITED / Руслан Малявский / 2026-07-20*
