# Lesson 03: Functions (lecture notes for Lars)

**Goal:** Jen can define functions with parameters and defaults, return
values (and knows why `print` isn't `return`), compose small functions, and
has a working picture of scope.

The whole lecture is one live refactor: last week's bonus loop → functions.
Start from `demo.py`, section "Before", and type the rest.

---

## [Opener, 1 min] Forty-one copies

Read Orrin's raven from `GUIDE.pdf`. The bonus rule is in the Grimoire
forty-one times, and thirty-eight copies agree. Dalvric's margin note:
`'TODO: make this a function (what is a function)`. Today we answer Dalvric.

## [0–4 min] `def` and `return`

```python
def monthly_salary(annual_salary):
    """One twelfth of the salary, to the penny."""
    return round(annual_salary / 12, 2)

print(monthly_salary(32500))
```

- `def`, name, parameters in brackets, colon, indented body. `return` hands
  the result back. VBA: `Function … End Function`, `MonthlySalary = …`.
- Defining does nothing. Calling runs it. Type `monthly_salary` without
  brackets and show what she gets (`<function …>`).
- Docstring: the first string in the body. `help(monthly_salary)` shows it.
- Define above, call below. Swap them and show the NameError.

## [4–7 min] `return` is not `print`

```python
def money_print(x):
    print(f"{x:,.2f} cr")

def money(x):
    return f"{x:,.2f} cr"

result = money_print(5)
print(result)          # None
print(money(5) + " net")
print(money_print(5) + " net")   # TypeError
```

- The first "works" until you try to use the result. `None` is what a
  function gives back when it doesn't `return`. That's the bug hunt.
- Rule of thumb: functions return, the script prints.

## [7–10 min] Refactor the napkin, live

Take the `if/elif` from last week, wrap it in `def bonus_rate(months, rating)`.
Replace each `rate = …` with `return …`. Point out that once you return, the
function is done, so the `elif`s can become plain `if`s.

Then `def bonus(salary, months, rating): return salary * bonus_rate(months, rating)`.
Functions call functions. Change the 8 % to 10 % in one place and show every
call follow. Forty-one copies, gone.

## [10–13 min] Defaults, keywords, scope

```python
def percent(x, decimals=1):
    return f"{x * 100:.{decimals}f}%"

percent(0.125); percent(0.125, 0); percent(0.125, decimals=2)
```

- Defaults after required parameters. Keywords make long calls readable:
  `print_pay_scroll("Orrin", 36500, pension_rate=0.08)`.
- Scope in 60 seconds:

```python
rate = 0.05
def pension(basic):
    deduction = basic * rate
    return deduction
pension(2000)
print(deduction)       # NameError
```

  Inside can read outside. Outside can't see inside. Want it out? Return it.
  Want it in? Pass it. (Don't mention `global`. She doesn't need it.)

## [13–15 min] Handover

Open `EXERCISES.pdf`. Point out that on this sheet the Given lines are the
*calls* and she writes the functions above them. Do exercise 1 together up
to the `def` line. Mention `python -i my_work/ex5_holiday.py` for trying
functions one at a time.
After the bug hunt: five optional riddles in `bughunt/riddles/` (one bug each, the last has two). Answers in `instructor/solutions/03-functions/riddles/`.

---

## VBA → Python cheat table (show at the end)

| VBA | Python |
|---|---|
| `Function F(x As Long) As Double` | `def f(x):` |
| `F = result` (then `End Function`) | `return result` |
| `Sub S(x)` (no return value) | `def s(x):` with no `return` (returns `None`) |
| `Optional rate As Double = 0.05` | `rate=0.05` in the parameter list |
| `Call S(name:="Orrin")` | `s(name="Orrin")` |
| `Dim x` inside a procedure | any assignment inside the function (local by default) |
| comment above the procedure | docstring `"""…"""` as the first line |

**Questions to check understanding:**
- What does a function return if it has no `return`?
- `money` vs `money(50)`: what's the difference?
- `rate` is set to 0.05 outside; a function has a parameter also called `rate`. Which one does the function use?
