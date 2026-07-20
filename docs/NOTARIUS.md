# NOTARIUS — Полный сборник наработок
AUTHOR: Руслан Малявский
COMMERCIAL USE PROHIBITED
DATE: 2026-07-20
STATUS: WORKING DOCUMENT

---

## 1. ОПРЕДЕЛЕНИЕ

**Notarius** — provenance-трекер для элементов данных:
откуда пришёл, через что прошёл, свой или вставлен.

КОРОТКАЯ ФОРМУЛА:
```
ORIGIN + TRACE + CURRENT_STATE
```

---

## 2. ПРОИСХОЖДЕНИЕ ПРОЕКТА

Идея возникла из MSL/MIP Sign Alphabet.

Ключевое уточнение (Руслан):
> «Если бы вопрос был в криптографии, его бы решили много десятилетий назад.»

Это разграничило два слоя:
```
Криптография:  изменили? подпись валидна?
Notarius:      откуда пришёл элемент? через что прошёл? свой или вставлен?

INTEGRITY_LAYER ≠ PROVENANCE_LAYER
```

---

## 3. ВЕРТИКАЛЬ ПРОЕКТОВ

```
MSL/MIP   → sign identity     → ЧТО ЭТО ЗА ЗНАК?
Notarius  → element provenance → ОТКУДА ПРИШЁЛ ЭЛЕМЕНТ?
SSP       → meaning provenance → ЧТО СЛУЧИЛОСЬ СО СМЫСЛОМ?

SIGN
↓
ELEMENT
↓
MEANING

Общий вопрос всех трёх:
Не только "что это?" —
а "откуда это пришло и что с ним происходило?"
```

---

## 4. ОТЛИЧИЕ ОТ КРИПТОГРАФИИ

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

---

## 5. ЧТО NOTARIUS НЕ ДЕЛАЕТ

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

---

## 6. ЗАФИКСИРОВАННЫЕ СВОЙСТВА

### 6.1 SEMANTIC_MANIFEST_KEY
```
STATUS: ЗАФИКСИРОВАНО
DATE: 2026-07-06

Отправитель передаёт:
  пакет (блоки в любом порядке)
  + ключ трассировки (semantic manifest)

Получатель:
  ключ → сборка → верификация порядка + смысла

БЕЗ КЛЮЧА:  блоки есть, смысл непонятен (семантическая обфускация)
С КЛЮЧОМ:   полная структура

ОТЛИЧИЕ ОТ BLOCKCHAIN:
  blockchain = криптографическая цепочка без семантики блока
  Notarius   = semantic_type + origin + state для каждого блока
```

### 6.2 SEMANTIC_LAYERED_DEFENSE
```
STATUS: ЗАФИКСИРОВАНО
DATE: 2026-07-06

ЧЕТЫРЕ НЕЗАВИСИМЫХ БАРЬЕРА для атакующего:
  1. ключ
  2. схема блоков
  3. семантическая типизация
  4. порядок сборки

КЛЮЧ_ИЗВЕСТЕН ≠ СТРУКТУРА_ИЗВЕСТНА
СТРУКТУРА_ИЗВЕСТНА ≠ СМЫСЛ_ВОССТАНОВЛЕН

ОТЛИЧИЕ ОТ ШИФРОВАНИЯ:
  Шифрование: сломал ключ → получил всё
  Notarius:   сломал ключ → получил осколки без инструкции сборки

Даже слабый пароль + неизвестная семантическая структура =
атакующий получает каша без смысла.
```

### 6.3 SEMANTIC_INVISIBLE_LENGTH_WITNESS
```
STATUS: PROPERTY_CANDIDATE → требует конвейера
DATE: 2026-07-07

Каждый блок несёт в манифесте контрольную длину в кодпоинтах Unicode.
Любая вставка/удаление символа включая невидимые (ZWSP U+200B,
ZWJ U+200D, VS16 U+FE0F, BOM, bidi-оверрайды) меняет счётчик
и ломает сверку.

ЛОВИТ:
  ZWSP/ZWJ/VS16/BOM внутри блока     → len +1
  невидимый в начале блока            → ЛОВИТ
  невидимый в конце блока             → ЛОВИТ
  невидимый в середине                → ЛОВИТ

НЕ ЛОВИТ:
  подмену равной длины: "1000" → "2000" (та же длина)
  → для этого нужен отдельный хеш

ФОРМУЛА:
  INVISIBLE_INSERTION → CODEPOINT_COUNT_SHIFT → MANIFEST_MISMATCH
  LENGTH_INTACT ≠ CONTENT_INTACT  (нужны оба барьера)
  KEY_KNOWN ≠ LENGTH_INTACT       (независимый слой)

LENGTH_INTACT ∧ CONTENT_INTACT = полная пара

МИНИМАЛЬНЫЙ ПРОТОТИП (первый рабочий код Notarius):

  def block_with_witness(data: str) -> dict:
      return {"data": data, "cp_len": len(data)}

  def verify_witness(block: dict) -> bool:
      return len(block["data"]) == block["cp_len"]

Три строки. Никаких зависимостей. Никакой криптографической библиотеки.
```

---

## 7. FO-КАНДИДАТ

### MANIPULATION_LEAVES_SUBSTRATE_TRACE
```
STATUS: FO-CANDIDATE / NEEDS_CONVEYOR
DATE: 2026-07-06

CORE_FORMULA:
BEST_VERIFICATION_SYSTEM = SUBSTRATE_RECORDS_MANIPULATION_ITSELF

OBSERVATION:
Лучшие системы верификации те,
где субстрат сам фиксирует вмешательство —
без внешнего наблюдателя.

VERIFIED_CASES:

CASE_1: Перфокарта (IBM, 1960-е)
  Субстрат: физическая карта
  Манипуляция: дырку нельзя заклеить незаметно
  Детектор: сам носитель

CASE_2: Фотографическая плёнка
  Субстрат: химический слой
  Манипуляция: склейка видна на кадре и стыке
  Детектор: сам носитель

CASE_3: Сургучная печать
  Субстрат: воск
  Манипуляция: вскрытие разрушает печать
  Детектор: сам носитель

CASE_4: Notarius / семантическая трассировка
  Субстрат: semantic manifest + блоки
  Манипуляция: разрыв trace_chain
  Детектор: сама структура

ФОРМУЛЫ:
  MANIPULATION_VISIBLE ≠ MANIPULATION_PREVENTED
  SUBSTRATE_TRACE = BEST_AVAILABLE_DETERRENT
```

---

## 8. PRODUCT_CANDIDATE

### PROVENANCE_CARRIER
```
STATUS: CANDIDATE_REGISTERED — конвейер не прогонялся, прототипа нет
DATE: 2026-07-12

СУТЬ:
Семантический след собирается ВНУТРИ системы.
Проверять его нужно СНАРУЖИ — там где нашего кода нет.
Носитель = компактное, самодостаточное, отделимое свидетельство
которое переживает выход из системы.

СЛОЙ 1 (REJECTED):
  QR как транспорт ВНУТРИ тракта.
  Слеп к неявке находки. Два лишних места тихого сбоя.
  Ёмкость ~3КБ мала для трейсов.

СЛОЙ 2 (CANDIDATE):
  Носитель на ГРАНИЦЕ системы.
  QR существует затем чтобы вынести данные туда
  где нашего кода нет: на бумагу, на экран, в чужие руки.
  Это не транспорт — это ВЫХОД.

ОТКРЫТЫЙ ТРЕУГОЛЬНИК (решать вместе, не последовательно):
  1. Что МИНИМАЛЬНО в носитель?
     Полный след не влезет. Отпечаток? Критические штампы?
  2. Kerckhoffs снимается или переезжает?
     Кто держит ключ? Где получатель берёт публичный ключ?
  3. QR или другой носитель?
     Носитель выбирается ПОСЛЕ ответа на п.1.

ЗАВИСИМОСТЬ:
  Сначала семантическая трассировка (собрать след).
  Потом носитель (вынести след).
  Нельзя печатать маршрутный лист которого ещё нет.
```

---

## 9. МОДЕЛЬ СОСТОЯНИЙ ЭЛЕМЕНТА

```
Каждый элемент имеет:
  ORIGIN
  TRACE
  TIME
  CURRENT_STATE

Возможные состояния:
  INTACT / MODIFIED / PARTIAL / SEGMENTED / MERGED /
  MIXED / CONVERTED / UNKNOWN / ARCHIVED / DELETED / RECOVERED

Пример нормального элемента:
  ELEMENT_ID: E-145
  ORIGIN: Sensor_A
  CURRENT_STATE: INTACT
  LAST_CONFIRMED: 2026-06-07 14:35
  TRACE_STATUS: CONTINUOUS

Пример разрыва:
  ELEMENT_ID: E-145
  CURRENT_STATE: MODIFIED
  MODIFICATION_WINDOW: 14:35 - 14:42
  TRACE_STATUS: BROKEN

ФОРМУЛЫ:
  PROVENANCE ≠ CURRENT_STATE
  TRACE_BREAK_TIME ≠ EXACT_ATTACK_TIME
  INTERVENTION_TIME ≠ INTERVENTION_CAUSE
```

---

## 10. УРОВНИ ТРАССИРОВКИ

```
TRACE_LEVEL_1 — CRITICAL_ONLY
  суммы, статусы, даты, доступы, подписи, команды, координаты

TRACE_LEVEL_2 — SEMANTIC_UNITS
  intent, claim, value, role, permission, prohibition,
  provenance, authority_status, execution_status

TRACE_LEVEL_3 — FULL_ELEMENT_TRACE
  символы, токены, структурные элементы,
  шаги преобразования, байтовые представления

ПРИНЦИПЫ:
  TRACE_DEPTH_FOLLOWS_RISK
  TRACE_COST must be compared with LOSS_SCALE
  MORE_TRACE ≠ MORE_TRUTH
  MORE_TRACE = MORE_OBSERVABILITY
```

---

## 11. ПРИМЕНЕНИЕ В СУДЕБНОЙ ЭКСПЕРТИЗЕ

Для суда разница между:
- «я думаю что подделали»
- «вот цепочка происхождения с разрывом на шаге 3»

Notarius = цифровой chain of custody для элементов данных.

```
Модель внедрения:
Банки исторически вводили стандарты через боль
(SWIFT, ISO 20022, PCI DSS).
Не нужно лоббировать заранее.
Нужно чтобы продукт существовал и был готов к моменту X.
```

---

## 12. ОТСЛЕЖИВАНИЕ АКТИВОВ

```
ASSET_A = 10 000 000
split →
  A1 = 2 000 000 → account_X
  A2 = 3 000 000 → wallet_Y
  A3 = 5 000 000 → securities_Z

Notarius видит:
  это не независимые куски —
  это фрагменты одного исходного происхождения.

ФОРМУЛЫ:
  SPLIT_ASSET ≠ LOST_PROVENANCE
  MIXED_ASSET ≠ CLEAN_ASSET
  UNREACHABLE_ASSET ≠ UNTRACEABLE_ASSET
  TEMPORARY_SAFE_HAVEN ≠ PROVENANCE_RESET
```

---

## 13. ФИЗИЧЕСКАЯ АНАЛОГИЯ (банкнота)

Банкнота $100 разрезана на три части и склеена пластырем.
Серийный номер MF 34567890 C присутствует на двух фрагментах.

```
НАБЛЮДЕНИЕ:
Физическая фрагментация не уничтожает провенанс
если идентификатор встроен в субстрат, а не в контейнер.

ФОРМУЛА:
SPLIT_OBJECT ≠ LOST_PROVENANCE
PROVENANCE_SURVIVES_FRAGMENTATION

ВЫВОД ДЛЯ АРХИТЕКТУРЫ:
Идентификатор происхождения должен быть встроен в элемент,
а не только в контейнер.
```

---

## 14. АНАЛОГИЯ ПЕРФОКАРТЫ

IBM EBCDIC punched card, 1960-е.
Каждый символ — уникальная комбинация пробивок.
Подделать невозможно: дырка либо есть либо нет.

```
Перфокарта:  символ → уникальная физическая метка
Notarius:    элемент → уникальная семантическая метка

Перфокарта:  три в одном:
  КЛЮЧ:      комбинация пробивок = идентификатор
  НОСИТЕЛЬ:  сама карта несёт данные
  ДЕТЕКТОР:  манипуляция физически видна

ПРИНЦИП:
  COMPLEXITY ≠ SECURITY
  SIMPLICITY = VERIFIABILITY
  VERIFIABILITY = TRUST
```

---

## 15. ПРОВЕРКА НИШИ

```
Веб-поиск, 2026-07-06:

ЧТО СУЩЕСТВУЕТ:
  Data lineage / data provenance — реальная индустрия
  Академические реализации element-level provenance (медицина, W3C)
  Blockchain-based provenance (патентный уровень)

ЧТО НЕ СУЩЕСТВУЕТ:
  Встроенный на пути транзакций провайдер
  Реального времени семантическая метка на уровне элемента
  Детекция чужеродных вставок как инфраструктурный продукт

ВЕРДИКТ: NICHE_CONFIRMED / SPACE_OPEN
```

---

## 16. ПЕРВЫЙ ПРОТОТИП (план)

```
Plain text provenance demo.

Показать:
  1. Элемент с origin tag
  2. Элемент с нормальной trace chain
  3. Вставка без метки
  4. Детекция разрыва
  5. Состояние: INTACT / INSERTED / UNKNOWN

Пример:
  DOCUMENT_A:
  amount = 1000000
  origin = invoice_458
  trace = created → checked → archived
  state = INTACT

  После подмены:
  amount = 9000000
  origin = UNKNOWN
  trace = missing
  state = INSERTED_OR_MODIFIED

  Ожидаемый вывод:
  TRACE_BREAK_DETECTED
  field: amount
  expected_origin: invoice_458
  actual_origin: UNKNOWN
  status: NEEDS_REVIEW
```

---

## 17. ТЕКУЩИЙ ПРИОРИТЕТ

```
ACTIVE_FRONT:
  MSL/MIP Sign Cards → Modules → Integrators

PARKED:
  Notarius
  SSP
  Video Trace
  Element Provenance
  Asset Recovery Trace
  PROVENANCE_CARRIER

ПОРЯДОК:
  1. MSL/MIP ядро
  2. Notarius трассировка (собрать след)
  3. PROVENANCE_CARRIER (вынести след)
```

---

## 18. КАНОНИЧЕСКИЕ ФРАЗЫ

```
Криптография проверяет целостность контейнера.
Notarius проверяет происхождение элемента.
SSP проверяет состояние смысла.

Notarius не возвращает актив сам.
Notarius делает происхождение актива трудно стираемым.

Не каждый байт. Не только весь файл.
А chunk + boundary.

Когда внутренняя память ненадёжна — нужен внешний след.

Лучшие системы верификации те,
где субстрат сам фиксирует вмешательство.

ПРИМИТИВНО = НАДЁЖНО = АУДИРУЕМО
```

---

*COMMERCIAL USE PROHIBITED / Руслан Малявский / 2026-07-20*
