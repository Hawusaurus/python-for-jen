# Lesson 01: Values, types and variables (lecture notes for Lars)

**Goal:** Jen can store values in variables, knows the four basic types
(`int`, `float`, `str`, `bool`), converts between them, and formats output
with f-strings. Plus the handful of places where Python behaves differently
from Excel/VBA in ways that would trip her up.

Run `demo.py` section by section, or type into the REPL live. Live typing is
better: make mistakes on purpose and read the errors together.

---

## [Opener, 1 min] Priya's inbox

Read the mission briefing from `GUIDE.pdf`. It's Monday. Priya in Payroll
has seven tickets waiting, MACRO-9000 crashed over the weekend
("Run-time error '13': Type mismatch"), and Gerald wants the pay gap
"in a sentence, for the board". Today's tools are numbers, text, and
formatting. Hand Jen the cheat sheet now; she'll use it during the
exercises.

## [0–2 min] Variables: no `Dim`

```python
salary = 32500
name = "Jane Smith"
```

- No `Dim`, no `As Long`. Python figures out the type itself.
- `=` means "store". It's never a comparison (that's `==`, see below).
- Names are **case-sensitive**: `Salary` and `salary` are two different
  variables. VBA doesn't care about case; Python does.
- Convention: `snake_case` (`annual_salary`), not `AnnualSalary`.

## [2–5 min] Numbers: `int` and `float`

```python
32500 / 12        # 2708.333...   / always gives a float
32500 // 12       # 2708          whole-number division
32500 % 12        # 4             remainder, like MOD
2 ** 10           # 1024          power
2 ^ 10            # 8 (!!)        NOT power: it's XOR. Classic VBA trap.
0.1 + 0.2         # 0.30000000000000004
round(2.5)        # 2   (rounds half to even, like VBA's Round, unlike Excel's ROUND)
```

Spend 30 seconds on `0.1 + 0.2`. Excel hides this by displaying only
15 digits. It's not a Python bug, it's how all computers store decimals.
For money: round at the end, and display with 2 decimals.

## [5–8 min] Strings

```python
first = "Jane"
last = 'Smith'                 # ' and " both work
first + " " + last             # + joins strings (VBA: &)
"  jane  ".strip().title()     # TRIM, then PROPER
len("Brightwell")              # LEN
"FIN-0042"[0]                  # "F": counting starts at 0!
"FIN-0042"[:3]                 # "FIN"   LEFT(…, 3)
"FIN-0042"[-4:]                # "0042"  RIGHT(…, 4)
```

Index-from-0 is the biggest mental switch from Excel. Draw the positions
under the string once:

```
F I N - 0 0 4 2
0 1 2 3 4 5 6 7
```

## [8–10 min] Types and conversion

```python
type(42), type(4.2), type("42"), type(True)
"5" + 3          # TypeError: Python never converts silently
int("5") + 3     # 8
float("37.5")
str(42) + " employees"
```

Key message: **everything from a file or a form arrives as text.** You
convert it before calculating. Read the TypeError together:
it says *which* types clashed.

## [10–13 min] f-strings: number formats

```python
monthly = 32500 / 12
f"Monthly pay: £{monthly:,.2f}"     # 'Monthly pay: £2,708.33'
f"{0.131:.1%}"                      # '13.1%'
f"{'Basic pay':<15}|"               # left-aligned in 15 characters
f"{42:04d}"                         # '0042'
```

The bit after `:` is like Excel's custom number format codes. She'll
recognise the idea immediately.

## [13–15 min] Booleans, `None`, and handover

```python
salary = 28000
salary == 28000        # True
25000 <= salary <= 32000   # True: chained comparison, very handy
True and False, True or False, not True
```

- `True`/`False` are capitalised.
- `None` means "no value", like VBA's `Nothing`/`Empty`.

**Handover:** open `EXERCISES.pdf` together and do the first line of
Exercise 1 live: create `my_work/ex1_pay_maths.py`, type the Given lines,
add one `print`, run it. Then leave her to it, with `CHEATSHEET.pdf` open.

---

## VBA → Python cheat table (show at the end)

| VBA / Excel | Python |
|---|---|
| `Dim x As Long` | `x = 5` |
| `'` comment | `#` comment |
| `&` | `+` (strings) or f-strings |
| `^` | `**` |
| `Mod`, `MOD()` | `%` |
| `Int(a / b)` | `a // b` |
| `=` (compare) | `==` |
| `<>` | `!=` |
| `And`, `Or`, `Not` | `and`, `or`, `not` |
| `Nothing` / `Empty` | `None` |
| `CInt`, `CDbl`, `CStr` | `int()`, `float()`, `str()` |
| `LEFT/RIGHT/MID` | `s[:n]`, `s[-n:]`, `s[a:b]` |
| `UCase`, `LCase`, `Trim` | `.upper()`, `.lower()`, `.strip()` |
| `Format(x, "#,##0.00")` | `f"{x:,.2f}"` |
| `Debug.Print` | `print()` |
| case-insensitive names | **case-sensitive** names |

**Questions to check understanding:**
- What's `7 / 2`, `7 // 2`, `7 % 2`?
- Why does `"5" + 3` fail, and how do you fix it?
- What's `"Brightwell"[1]`?
