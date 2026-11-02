# Python for Jen ⚔️

> **The Adventurers' Guild of Thornmere**: quests posted, monsters met, loot shared since the year 1019.
> Its records kept, for three hundred years, by the **Grimoire of Dalvric**.

You are the new **Keeper of the Guild Ledger**. The Grimoire is four hundred
lines of incantations left by a court wizard who sailed west and never came
back. It fails every full moon and nobody dares touch it. And Queen Aldara will
renew the guild's **Royal Charter** at Midsummer only if the guild can show,
properly, which quests are worth the crowns, which are too dangerous, and
whether the loot is shared fairly. In a sentence a queen can say out loud.

Your quest: learn Python (and then SQL), one lesson at a time, and **close the
Grimoire** by building the **Charter Report** yourself.

## The guild

| | |
|---|---|
| **Queen Aldara** | Grants the Charter. Sends decrees at dusk on the last day of the week. "No pressure. (Some pressure.)" |
| **Quartermistress Pell** | Keeps the guild's stores and accounts. Sharp, busy, sends most of the ravens. |
| **Orrin of the Clockworks** | Keeps the guild's machines running, and later the Vault beneath the hall. Has seen things. |
| **Captain Siv** | Quest master. Wants yes or no, never "mayhap". |
| **Wren Hawkridge** | Elf ranger, level 19. The guild's legend. |
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
| `bughunt/riddles/` | The Grimoire's Riddles: five extra broken scripts, each with a rhyming hint |
| `data/` | The guild's records for this lesson (from lesson 05 on) |
| `LECTURE.md`, `demo.py` | What Lars shows you at the start (~15 min) |

Run your files with `python my_work/<file>.py` and compare with the expected
output on the sheet. When you're done: commit, push, and open a pull request.
Lars reviews it, and you earn the lesson's rune.

## The quest

| # | Lesson | Topics | Rune |
|---|---|---|---|
| 00 | The Guild Hall Door | setup, VS Code, Git, GitHub | Rune of the Gate |
| 01 | The Notice Board | numbers, text, types, f-strings | Rune of Coin |
| 02 | The Loot Split | `if`, `for`, `while` | Rune of Choice |
| 03 | Dalvric's Tangle | functions | Rune of Craft |
| 04 | The Roster | lists and dictionaries | Rune of the Roll |
| 05 | The Scriptorium Scroll | strings, files, reading a CSV | Rune of the Scroll |
| 06 | The Full Moon | errors, tracebacks, `try`/`except`, debugging | Rune of the Moon |
| 07 | The Armoury | modules, the standard library, venv, pip | Rune of the Forge |
| 08 | A Thousand Arrows at Once | NumPy | Rune of the Legion |
| 09 | The Living Ledger | pandas I: DataFrames, filtering, Excel in and out | Rune of the Ledger |
| 10 | The War Table | pandas II: groupby, pivot tables, merge | Rune of Council |
| 11 | The Vault Beneath | SQL I: SELECT, WHERE, ORDER BY, GROUP BY, HAVING | Rune of the Vault |
| 12 | The Deep Archive | SQL II: JOINs, subqueries, CASE, SQL into pandas | Rune of the Archive |
| 13 | Before the Throne | charts, formatted Excel workbooks | Rune of the Throne |
| 14 | The Charter | the Charter Report (two sessions) | The Keeper's Seal |
