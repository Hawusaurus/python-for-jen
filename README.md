# Python for Jen

A hands-on Python course for someone who already knows Excel and VBA.
By the end you'll be able to replace a typical spreadsheet workflow with a
Python script, and we'll finish with a **gender pay gap report** built with
NumPy and pandas.

## How every lesson works

Each lesson lives on its own git branch (`lesson-01`, `lesson-02`, …) and has
the same parts:

| Part | Where | Time |
|---|---|---|
| Lecture | `LECTURE.md` + `demo.py` (Lars walks you through it) | ~15 min |
| Exercises | `exercises/` | ~1 h, on your own |
| Bug hunt | `bughunt/` | ~15 min |

Your routine for each lesson:

```bash
git checkout lesson-01              # switch to the lesson branch
git pull                            # get the newest version
pytest lessons/01-values-and-types  # see what's still red
# ... work on the exercises until everything is green ...
git add .
git commit -m "Lesson 01: exercises done"
git push
```

Then open a **pull request** on GitHub from `lesson-01` into `main`.
Lars reviews it, comments, and merges it.

## The tests are your answer key

Every exercise has tests. Run `pytest` on the lesson folder:

- **PASSED** (green): done, move on.
- **FAILED** (red): read the message. It tells you what your code returned
  and what was expected.

You are finished with a lesson when everything is green. Don't change the
test files. If you think a test is wrong, say so in the pull request.

## Lessons

| # | Topic | You know this from Excel/VBA as… |
|---|---|---|
| 00 | Setup: Python, VS Code, Git, GitHub | — |
| 01 | Values, types, variables, f-strings | `Dim`, number formats, `&` |
| 02 | Decisions and loops: `if`, `for`, `while` | `If`, `For Each` |
| 03 | Functions and testing | `Sub` / `Function` |
| 04 | Lists and dictionaries | arrays, `Scripting.Dictionary` |
| 05 | Strings and files: reading a CSV yourself | text functions, `Open … For Input` |
| 06 | Errors and debugging | `On Error`, the debugger |
| 07 | Modules, pip, virtual environments | add-ins |
| 08 | NumPy: whole columns at once | dragging a formula down |
| 09 | pandas I: DataFrames, filtering | AutoFilter |
| 10 | pandas II: groupby, pivot tables, merge | PivotTables, XLOOKUP |
| 11 | Charts and writing Excel files | charts |
| 12–13 | Project: gender pay gap report | the whole macro |
