# Lesson 00: Setup and the big picture (lecture notes for Lars)

**Goal:** Jen understands *where* Python lives, how to run it, and the git
workflow for the whole course. Do this lecture **after** she has finished
`SETUP.md`, or do the setup together right after the lecture.

---

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
- **The tests are the answer key.** Run `pytest lessons/00-setup` and show
  red vs green. Show how to read a failure: "expected X, got Y".
- Show `GIT_CHEATSHEET.md`.
- Hand over to `exercises/README.md`.

---

**Questions to check understanding:**
- Where does Python code "live", compared with VBA?
- What's the difference between a commit and a push?
- Why does she work on a branch instead of directly on `main`?
