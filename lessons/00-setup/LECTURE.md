# Lesson 00: Setup and the big picture (lecture notes for Lars)

**Goal:** Jen understands *where* Python lives, how to run it, and the git
workflow for the whole course. Do this lecture **after** she has finished
`SETUP.md`, or do the setup together right after the lecture.

---

## [Opener, 1 min] Welcome to Thornmere

Open `GUIDE.pdf` and read the Queen's decree out loud. Jen is the new Keeper
of the Ledger at the **Royal Treasury of Thornmere** ("counting the realm's
coin since the year 1019"). Introduce the court: Queen Aldara (decrees at dusk
on the last day of the week), Mistress Pell (Paymaster, sends ravens), Orrin of
the Clockworks, Lady Siv of the Rewards, Dalvric the Vanished (court wizard,
sailed west, left behind the Grimoire and a lot of broken code), and Biscuit
(a small kitchen dragon). The course goal is to close the Grimoire before the
Accord of Equal Coin report is due at Midsummer.

## [0–3 min] Python vs VBA: where does the code live?

- VBA lives *inside* the workbook. It can't exist without Excel.
- Python lives *outside*, in plain `.py` text files. It reads Excel files,
  CSVs, and databases, and writes results back.
- Consequence: a Python script can process 300 workbooks overnight without
  opening Excel once.
- Python is free, runs everywhere, and has huge libraries. pandas is
  effectively "Excel for programmers", and it's where we're heading.

## [3–7 min] Three ways to run Python (demo)

1. **The REPL.** Type `python` in the terminal. It's a calculator that
   answers back, like the VBA Immediate window (Ctrl+G).
   ```python
   >>> 2 + 3
   >>> 35000 / 12
   >>> "Jen" * 3
   >>> exit()
   ```
2. **A script.** Create `hello.py` containing `print("Hello, Jen")` and run
   `python hello.py`. This is like running a macro.
3. **VS Code.** Same file, press the ▶ button at the top right.

Point out: there is no `Sub ... End Sub`. The file runs top to bottom.

## [7–12 min] Git in one picture

Draw this:

```
main      ●────────────●─────────────●
           \          /  (merge)    ...
lesson-01   ●──●──●──●
              (Jen's commits)
```

- Repo = folder with memory. Commit = save point with a note.
- Branch = parallel copy. `main` is the approved version.
- Pull request = Track Changes in Word: "here's what I changed, please
  review." I comment, she fixes, I merge.
- Show `git status`, `git add .`, `git commit -m "..."`, `git push` once,
  live.
- Show the GitHub PR page: the diff, comments, the merge button.

## [12–15 min] How every lesson will work

- Lecture (like this), then about an hour of exercises alone, then a bug hunt.
- Every lesson has three PDFs: `GUIDE.pdf` (story and goals), `EXERCISES.pdf`
  (the sheet) and `CHEATSHEET.pdf`. Show all three.
- She writes **every** file herself in `my_work/` and checks it against the
  expected output on the sheet. No templates, no autograder.
- Show how to read an error: last line first (what), then the line number (where).
- Every lesson lives in its own folder on its own branch, and lessons don't depend
  on each other.
- Hand over to `EXERCISES.pdf`.
- After the bug hunt: five optional riddles in `bughunt/riddles/` (one bug each, the last has two). Answers in `instructor/solutions/00-setup/riddles/`.

---

**Questions to check understanding:**
- Where does Python code "live", compared with VBA?
- What's the difference between a commit and a push?
- Why does she work on a branch instead of directly on `main`?
