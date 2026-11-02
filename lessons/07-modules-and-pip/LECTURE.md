# Lesson 07: The Armoury — modules, venv and pip (lecture notes for Lars)

**Goal:** Jen can set up a virtual environment, install packages from
`requirements.txt`, import from the standard library, and put her own functions
into a module. This is the gate to NumPy and pandas, so the venv part has to
actually work on her machine before she leaves today.

Do the venv live in the terminal *inside the lesson folder*, slowly. Then
`demo.py` for the rest.

---

## [Opener, 1 min] The Armoury

Read Orrin's raven from `GUIDE.pdf`: `loot_share()` exists in eleven files, three
of them different. Today: forge it once, import it everywhere, and borrow the
rest from smiths with more patience.

## [0–5 min] venv and pip, live

```powershell
cd lessons\07-modules-and-pip
python -m venv .venv            # a private armoury for this project
.venv\Scripts\activate          # prompt now starts with (.venv)
pip install -r requirements.txt
pip list
python -c "import rich; print('ok')"
deactivate                      # and activate again, so she sees both
```

- Why a venv: packages go into `.venv/`, not into Windows. Different projects,
  different versions, nothing breaks. Delete the folder and it's gone.
- `requirements.txt` is the shopping list. Show the file: one line, `rich`.
- Mention `.gitignore` already hides `.venv/`. `git status` to prove it.
- If "running scripts is disabled": `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.
- VS Code will offer to pick `.venv` as the interpreter. Say yes; then the ▶
  button uses it too.

## [5–8 min] import, three ways

```python
import math;                math.ceil(8 / 3)          # 3 parties of three for 8 heroes
from datetime import date;  date(2026, 4, 5)          # no prefix
import statistics as st;    st.mean([260, 550, 2710]) # nickname
```

The standard library ships with Python: `math`, `statistics`, `datetime`,
`random`, `csv` (she knows), `pathlib` (she knows). `help(statistics)` in the
REPL is the manual. Nobody memorises it; everybody looks it up.

Excel anchor: `=AVERAGE`, `=MEDIAN`, `=STDEV.S`, `=ROUNDUP`, `=DATEDIF`,
`=RAND()`. Same functions, different drawer.

Point at mean vs median with the Wyrm in the list: one 2,710 cr reward drags the
mean far above the "typical" quest. The Queen will ask which average; she
should be able to answer.

## [8–11 min] datetime in two minutes

```python
from datetime import date, timedelta
start = date.fromisoformat("2014-06-21")   # Wren joined the guild
today = date(2026, 4, 5)                   # fixed, so the sheet's answers are stable
(today - start).days                       # 4306, an int
today + timedelta(days=90)
f"{start:%d %b %Y} ({start:%A})"           # 21 Jun 2014 (Saturday)
```

Subtracting dates gives a `timedelta`; print it and you get
`4306 days, 0:00:00`. Ask for `.days`. (Bug 3 in today's bug hunt.)

## [11–14 min] Your own module

Create `my_work/questkit.py` live with one function and a docstring, then
run a file next to it:

```python
import questkit
questkit.share(550, 4)     # 110.0: four heroes, leader takes two shares -> 5 shares
help(questkit)
```

- A module is a file. `import questkit` runs it once, top to bottom. So:
  no `print` at module level, or it prints on every import.
- `if __name__ == "__main__":` — she saw it in lesson 00. Now it makes sense:
  quiet when imported, chatty when run. Show both.
- Python finds modules next to the file being run. Both files in `my_work/`.
- Warn: a file called `random.py` in `my_work/` hides the real `random`.

## [14–15 min] Handover

Open `EXERCISES.pdf`. Exercise 1 is the venv, in the terminal, no file. Make
sure the `(.venv)` prompt shows before she moves on. Exercise 6 is a package
she's never seen (`rich`): the exercise is reading documentation, so don't
explain it. The bug hunt is `bughunt/party_bug.py` (Grimoire, page 7). Fast
finishers: five optional riddles in `bughunt/riddles/`, one bug each (the last
has two); answers in `instructor/solutions/07-modules-and-pip/riddles/`.

---

## VBA → Python cheat table (show at the end)

| VBA / Excel | Python |
|---|---|
| Tools → References, add-ins | `pip install`, `import` |
| a `.bas` module you import into a workbook | `questkit.py`, `import questkit` |
| `WorksheetFunction.Average` | `statistics.mean` |
| `Application.RoundUp` | `math.ceil` |
| `DateDiff("d", a, b)` | `(b - a).days` |
| `DateAdd("d", 90, d)` | `d + timedelta(days=90)` |
| `Format(d, "dd/mm/yyyy")` | `d.strftime("%d/%m/%Y")` |
| `Rnd`, `Randomize` | `random.random()`, `random.seed()` |
| `Sub Main()` | `if __name__ == "__main__":` |

**Questions to check understanding:**
- What's the difference between `import math` and `from math import ceil`?
- Why does `pip install` go into `.venv/` and not into Windows?
- What happens on `import questkit` if `questkit.py` has a `print` at the top?
