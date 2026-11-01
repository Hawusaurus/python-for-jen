# Lesson 00: Setup and the big picture (lecture notes for Lars)

**Goal:** Jen understands *where* Python lives, how to run it, and the git
workflow for the whole course. Do this lecture **after** she has finished
`SETUP.md`, or do the setup together right after the lecture.

---

## [Opener, 1 min] Welcome to Brightwell

Open `GUIDE.pdf` and read the mission briefing out loud. Jen is the new People
Analytics Lead at **Brightwell Umbrellas Ltd** ("Keeping Britain dry since 1952").
Introduce the cast: Gerald (MD, sends requests at 4:55 pm on Fridays),
Priya (Payroll, sends tickets), Dave (left in 2019, left behind MACRO-9000
and a lot of broken code), and Biscuit (office beagle).
The course goal is to retire MACRO-9000 before pay gap reporting day.

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

---

**Questions to check understanding:**
- Where does Python code "live", compared with VBA?
- What's the difference between a commit and a push?
- Why does she work on a branch instead of directly on `main`?
