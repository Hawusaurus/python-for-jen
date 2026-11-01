# Python for Jen ☂️

> **Brightwell Umbrellas Ltd**: keeping Britain dry since 1952.
> Payroll since 2009: one VBA macro called **MACRO-9000**.

You've just joined Brightwell as People Analytics Lead. The pay gap report
is due, the payroll macro crashes every other Monday, and the person who
wrote it (Dave) left in 2019 to live on a narrowboat.

Your mission: learn Python, one lesson at a time, and **retire MACRO-9000**
by building the gender pay gap report yourself, with NumPy and pandas.

## The cast

| | |
|---|---|
| **Gerald** | Managing Director. Grandson of the founder. Sends requests at 16:55 on Fridays. |
| **Priya** | Payroll. Sharp, busy, sends tickets. |
| **Mo** | IT. Has seen things. |
| **Siobhan** | Reward & Benefits. Needs yes/no answers. |
| **Dave** | Left in 2019. Left behind MACRO-9000 and lots of broken code. |
| **Biscuit** | Office beagle. Not allowed near the keyboard. Often near the keyboard. |

## How a lesson works

**Every lesson is its own folder on its own branch.** Lessons don't depend
on each other.

```bash
git checkout lesson-01            # switch to the lesson
cd lessons/01-values-and-types    # always work inside the lesson folder
```

Each lesson folder contains:

| | |
|---|---|
| `GUIDE.pdf` | **Start here.** The story, what you'll learn, and what "done" looks like |
| `EXERCISES.pdf` | The exercise sheet (~1 hour). What to write, and the output to expect |
| `CHEATSHEET.pdf` | Everything from the lesson on one page. Keep it open while working |
| `my_work/` | Your files. You write every one of them yourself |
| `bughunt/` | Dave's Leftovers: broken code to fix (~15 min) |
| `LECTURE.md`, `demo.py` | What Lars shows you at the start (~15 min) |

Run your files with `python my_work/<file>.py` and compare with the expected
output on the sheet. When you're done: commit, push, and open a pull request.
Lars reviews it, and you get the badge. 🏅

## Lessons

| # | Mission | Python topics | Badge |
|---|---|---|---|
| 00 | Day One at Brightwell | setup, VS Code, Git, GitHub | Keycard Issued |
| 01 | Priya's Inbox | numbers, text, types, f-strings | Number Wrangler |
| 02 | The Bonus Run | `if`, `for`, `while` | Decision Maker |
| 03 | Dave's Spaghetti | functions | Function Forger |
| 04 | The Staff List | lists and dictionaries | List Keeper |
| 05 | The Export | strings, files, reading a CSV | File Reader |
| 06 | Monday Morning | errors, tracebacks, `try`/`except`, debugging | Bug Whisperer |
| 07 | The Toolbox | modules, the standard library, venv, pip | Toolsmith |
| 08 | Whole Columns at Once | NumPy | Vectoriser |
| 09 | The Spreadsheet That Isn't | pandas I: DataFrames, filtering, Excel in and out | Frame Builder |
| 10 | Pivot Season | pandas II: groupby, pivot tables, merge | Pivot Master |
| 11 | Show Gerald | charts, formatted Excel workbooks | Chart Topper |
| 12 | Retire MACRO-9000 | the gender pay gap report (two sessions) | MACRO-9000 Retired |
