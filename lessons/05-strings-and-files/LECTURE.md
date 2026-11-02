# Lesson 05: Strings and files (lecture notes for Lars)

**Goal:** Jen can read and write text files and CSVs, and knows that a file is
just lines of text until she converts it. By the end of the sheet she has turned
the Scriptorium's messy copy of the notice board into a clean CSV with a script.

Run `demo.py` section by section from the lesson folder, or type it live.
Open `data/notice_board_messy.csv` in VS Code (not Excel) at the start so she
sees the raw text with the quotes and the mess.

---

## [Opener, 1 min] The Scriptorium Scroll

Read Quartermistress Pell's letter from `GUIDE.pdf`. The Scriptorium copies the
notice board by hand every new moon, it's a mess every moon, and Excel "helps" by
turning the dates foreign. Today the fix becomes a script that does the same thing every moon.

## [0–3 min] Split and join

```python
"Hawkridge, Wren".split(", ")      # ['Hawkridge', 'Wren']
"Copying the   notice board".split()  # whitespace, any amount
"-".join(["a", "b", "c"])          # 'a-b-c'   (VBA: Join / Split)
last, first = "Hawkridge, Wren".split(", ")
"4 heroes".split()[0]              # '4'
"3/5".split("/")[0]                # '3'
```

Point out: `split` gives a list (lesson 04), `join` is called on the
*separator*, not on the list. That trips everyone once.

## [3–7 min] Files are lines of text

```python
with open("my_work/note.txt", "w", encoding="utf-8") as f:
    f.write("Notices copied: 1019\n")      # you add the \n

with open("my_work/note.txt", encoding="utf-8") as f:
    for line in f:
        print(repr(line))                  # 'Notices copied: 1019\n'
```

- `with` closes the file even if the code inside crashes. VBA: `Open ... For
  Output` / `Close`, but you can't forget the Close.
- `"w"` replaces the file. Say it twice. Never open anything in `data/` with `"w"`.
- `repr()` shows the `\n`. Use it whenever a string looks "right" but compares wrong.
- `encoding="utf-8"`: Windows defaults to a legacy encoding. Accented names come
  out garbled (`Ã©` instead of `é`) without it.

## [7–11 min] CSV the right way

Show the raw file in VS Code: `"4,540 cr"` has a comma inside quotes.
Then:

```python
import csv
with open("data/notice_board_messy.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row["Quest"], row["Reward"])
```

- `DictReader`: header becomes the keys. Each row is a dict (lesson 04).
- Everything is text: `row["Reward"]` is `'260 cr'`, `row["Danger"]` might be `'****'`. Lesson 01's cleaning
  tools come back here: `strip`, `replace`, `float`.
- Why not `line.split(",")`? Do it live on the Wyrm line (Q0015, `"4,540 cr"`) and
  watch the reward break into two pieces.
- Writing: `csv.DictWriter(f, fieldnames=[...])`, `writeheader()`, `writerows()`.
  `newline=""` on both reading and writing, or Windows double-spaces the output.

## [11–14 min] pathlib

```python
from pathlib import Path
p = Path("data") / "quests.csv"
p.exists(), p.name, p.stat().st_size
for p in Path("data").glob("*.csv"): print(p.name)
```

A `Path` can be passed to `open()`. The `/` joins parts and works on every OS.
Mention: printing a Path on Windows shows backslashes, so print `p.name`.

## [14–15 min] Handover

Open `EXERCISES.pdf`. Stress the house rule: run from the lesson folder, or
`data/...` isn't found. Do the first line of Exercise 3 together (open the
file, print `reader.fieldnames`), then leave her to it.

The bug hunt is `bughunt/tally_bug.py`. Mention `bughunt/riddles/`: five optional
one-bug riddles (the last has two) for fast finishers or homework; your answers are
in `instructor/solutions/05-strings-and-files/riddles/`.

---

## VBA → Python cheat table (show at the end)

| VBA / Excel | Python |
|---|---|
| `Split(s, ",")` | `s.split(",")` |
| `Join(arr, ",")` | `",".join(arr)` |
| `Open f For Input As #1` … `Close #1` | `with open(f) as fh:` |
| `Line Input #1, s` | `for line in fh:` |
| `Print #1, s` | `fh.write(s + "\n")` |
| `Workbooks.OpenText` / Text Import Wizard | `csv.DictReader` |
| `Dir("*.csv")` | `Path("data").glob("*.csv")` |
| `FileLen(f)` | `Path(f).stat().st_size` |

**Questions to check understanding:**
- What does `with` do for you that `open()` alone doesn't?
- Why is `row["reward"] + 100` an error?
- Why not split a CSV line at the commas yourself?
