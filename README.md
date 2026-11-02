# Python for Jen 👑

> **The Royal Treasury of Thornmere**: counting the realm's coin since the year 1019.
> Wages reckoned, for the last three hundred years, by the **Grimoire of Dalvric**.

You are the new **Keeper of the Ledger**. The Grimoire is 4,000 lines of
incantations left by a court wizard who sailed west and never came back. It
fails every full moon, nobody dares touch it, and Queen Aldara has signed the
**Accord of Equal Coin**: by Midsummer, the Treasury must report the pay gap
between the women and men of the realm. Properly. In a sentence a queen can
say out loud.

Your quest: learn Python, one lesson at a time, and **close the Grimoire** by
building that report yourself, with NumPy and pandas.

## The court

| | |
|---|---|
| **Queen Aldara** | Sends decrees at dusk on the last day of the week. "No pressure. (Some pressure.)" |
| **Mistress Pell** | Paymaster of the Guilds. Sharp, busy, sends most of the ravens. |
| **Orrin of the Clockworks** | Keeps the realm's machines running. Has seen things. |
| **Lady Siv of the Rewards** | Wants yes or no, never "mayhap". |
| **Dalvric the Vanished** | Court wizard, left in 1019. His torn pages turn up in every lesson, always broken. |
| **Biscuit** | A small kitchen dragon. Not allowed near the abacus. Often near the abacus. |

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
| `bughunt/` | Pages from the Grimoire: Dalvric's broken code, for you to fix (~15 min) |
| `LECTURE.md`, `demo.py` | What Lars shows you at the start (~15 min) |

Run your files with `python my_work/<file>.py` and compare with the expected
output on the sheet. When you're done: commit, push, and open a pull request.
Lars reviews it, and you earn the lesson's rune.

## The quest

| # | Lesson | Python topics | Rune |
|---|---|---|---|
| 00 | The Keeper's Oath | setup, VS Code, Git, GitHub | Rune of the Gate |
| 01 | Mistress Pell's Ravens | numbers, text, types, f-strings | Rune of Coin |
| 02 | The Midwinter Bonus | `if`, `for`, `while` | Rune of Choice |
| 03 | Dalvric's Tangle | functions | Rune of Craft |
| 04 | The Roll of the Realm | lists and dictionaries | Rune of the Roll |
| 05 | The Scriptorium Scroll | strings, files, reading a CSV | Rune of the Scroll |
| 06 | The Full Moon | errors, tracebacks, `try`/`except`, debugging | Rune of the Moon |
| 07 | The Armoury | modules, the standard library, venv, pip | Rune of the Forge |
| 08 | A Thousand Coins at Once | NumPy | Rune of the Legion |
| 09 | The Living Ledger | pandas I: DataFrames, filtering, Excel in and out | Rune of the Ledger |
| 10 | The Council of Guilds | pandas II: groupby, pivot tables, merge | Rune of Council |
| 11 | Before the Throne | charts, formatted Excel workbooks | Rune of the Throne |
| 12 | The Grimoire Closes | the Accord of Equal Coin report (two sessions) | The Keeper's Seal |
