# CANONICALIZATION_PRE_PASS — the digit card's double bottom, in code · двойное дно цифровой карточки в коде

🇬🇧 [English](#english) · 🇷🇺 [Русский](#русский)

---

<a name="english"></a>
## English

This is the "bottom" of the digit card: a digit is an atom of encoding, and an encoded attack sails past your cards until the input is brought to an honest form. This pre-pass decodes digit-encodings so that the **existing** cards see the real sign. Pure stdlib.

### Proven on the REAL MSL (`python demo_prepass.py`)

| Attack (raw input) | MSL on raw | MSL after pre-pass |
|---|---|---|
| `%252e%252e%252fboot.ini` (double-encoded `../`) | **OK — slips through!** | 🚨 **ALARM** (traversal) |
| `admin&#8203;istrator` (invisible ZWSP built from digits) | **OK — slips through!** | **WATCH** (ZWSP card woke up) |
| `%2e%2e%2f…/etc/hosts` | WATCH | 🚨 ALARM |
| `http://2130706433/` (127.0.0.1 in decimal) | OK | OK — *normalised, but needs the IP card* |
| `note: %2f is how a slash…` (text ABOUT encoding) | OK | WATCH — **false alarm (over-decode)** |

Three honest conclusions:
1. **The double bottom is real.** Double-encoded traversal and entity-ZWSP **completely** bypass MSL on raw input.
2. **The pre-pass fixes it.** Decoding wakes the **already existing** cards (dot / solidus / ZWSP) — no new ones needed. Depth matters: double-encoding takes 2 passes.
3. **Pre-pass and card complement each other.** The decimal IP is normalised by the pre-pass, but MSL can only flag it with a **digit/IP card** (the SURFACE layer). Neither closes it alone.

### Honest boundary (visible right in the demo)
The last row is **over-decode**: the benign text "`%2f` means a slash" became `/…` after decoding and got a WATCH. This is exactly `Q3_DECODE_CONTEXT` from the card: **explanatory text must not be decoded.** A naive pre-pass decodes everywhere; a real one must gate by position (executable vs. descriptive). Depth is also capped (`max_depth=3`) against a decode-loop.

### Structure
```
canonicalize.py
  decode_layers(text, max_depth)  # percent + HTML-entity + \u/\x escapes, with depth
  normalize_ip_hosts(text)        # decimal/hex host -> dotted-quad
  canonicalize(text)              # full pass -> (canon, info)
demo_prepass.py                    # raw vs canonicalized on the real MSL
```

### How to wire it in
At runtime the pre-pass sits **before** `scan_signs` (card section 13: the `CANONICALIZATION_PRE_PASS` hook). In our engine it is one wrapper: `reader = lambda t: real_text_reader(canonicalize(t)[0])` — and all cards start seeing through digit-encodings.

Status: a demonstration of the principle. Position gating (Q3) and the depth limit (Q2) are the next work, marked in the card.

---

<a name="русский"></a>
## Русский

То самое «низ» карточки цифр: цифра — атом кодировки, и закодированная атака проезжает мимо твоих карточек, пока вход не привести к честному виду. Этот pre-pass декодирует digit-кодировки, чтобы **существующие** карточки увидели настоящий знак. Чистый stdlib.

### Доказано на НАСТОЯЩЕМ MSL (`python demo_prepass.py`)

| Атака (сырой вход) | MSL на сыром | MSL после pre-pass |
|---|---|---|
| `%252e%252e%252fboot.ini` (double-encoded `../`) | **OK — мимо!** | 🚨 **ALARM** (traversal) |
| `admin&#8203;istrator` (цифрами собран невидимый ZWSP) | **OK — мимо!** | **WATCH** (карточка ZWSP проснулась) |
| `%2e%2e%2f…/etc/hosts` | WATCH | 🚨 ALARM |
| `http://2130706433/` (127.0.0.1 десятичным) | OK | OK — *нормализовал, но нужен IP-card* |
| `note: %2f is how a slash…` (текст ОБ кодировке) | OK | WATCH — **ложная тревога (over-decode)** |

Три вывода, все честные:
1. **Двойное дно реально.** Double-encoded traversal и entity-ZWSP **полностью** обходят MSL на сыром входе.
2. **Pre-pass чинит.** Декодирование будит **уже существующие** карточки (точка/солидус/ZWSP) — новых не нужно. Глубина важна: double-encoding взят за 2 прохода.
3. **Pre-pass и карточка дополняют друг друга.** Десятичный IP pre-pass нормализует, но флагнуть его MSL сможет только с **цифровой/IP-карточкой** (SURFACE-слой). Одно без другого не закрывает.

### Честная граница (видно прямо в демо)
Последняя строка — **over-decode**: безобидный текст «`%2f` значит слэш» после декодирования стал `/…` и получил WATCH. Это ровно `Q3_DECODE_CONTEXT` из карточки: **декодировать нельзя пояснительный текст**. Наивный pre-pass декодирует везде; настоящий должен гейтить по позиции (исполняемая vs описательная). Плюс глубина капнута (`max_depth=3`) от decode-loop.

### Устройство
```
canonicalize.py
  decode_layers(text, max_depth)  # percent + HTML-entity + \u/\x escapes, с глубиной
  normalize_ip_hosts(text)        # десятичный/hex хост -> dotted-quad
  canonicalize(text)              # полный проход -> (canon, info)
demo_prepass.py                    # сырой vs канонизированный на настоящем MSL
```

### Как встроить
В рантайме pre-pass встаёт **до** `scan_signs` (раздел 13 карточки: хук `CANONICALIZATION_PRE_PASS`). В нашем движке это одна обёртка: `reader = lambda t: real_text_reader(canonicalize(t)[0])` — и все карточки начинают видеть сквозь digit-кодировки.

Статус: демонстрация принципа. Гейт по позиции (Q3) и предел глубины (Q2) — следующая работа, помечены в карточке.
