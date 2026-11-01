# Lesson 12: Retire MACRO-9000 (lecture notes for Lars, two sessions)

**Goal:** Jen builds the UK gender pay gap report end to end as a small
project: a module of functions, check scripts, a report script, a chart and
a workbook. Nothing new in Python; the new skill is *structuring* the work.

Keep the briefings short. The sheet is long and she should be writing, not
listening. `demo.py` is one section per session.

---

## Session 1 briefing [15 min]

### [Opener, 2 min] Gerald's memo

Read the memo from `GUIDE.pdf`. The stakes: board meeting, MACRO-9000 has
said 24.6% since 2019, if her numbers hold up the macro gets switched off.

### [2–7 min] The rules of the game

Walk through the table on page 1 of `EXERCISES.pdf` (the six figures).
Three things to land, because each one is a bug hunt bug later:

1. Everything is a share of **men's** pay: `(men - women) / men`.
2. Hourly, never annual. Show in the REPL: someone on 18.75 h with £10,300
   a year has an hourly rate of £10.56. Annual pay would call her underpaid.
3. Bonus gap = only people who got a bonus. "Proportion receiving" = everyone.

Ask: "Why both mean and median?" If she doesn't know: mean is pulled by the
few at the top (mostly men); median is the typical person. Mean gap > median
gap means the problem is at the top. At Brightwell it's 19.7 vs 18.7, so
it's everywhere.

### [7–12 min] The shape of a project (demo section 1)

```
my_work/paygap.py        functions only; never prints, never reads a file on its own
my_work/check1.py        import paygap; load; print
my_work/report.py        session 2
```

- Lesson 07 again: a `.py` file next to the script is importable. Show
  `demo.py` section 1 importing from `demo_helpers.py`.
- Rule: *functions compute, scripts print.* It's what makes the report
  reusable next April, and testable.
- Every function gets a docstring. One line is enough.

### [12–15 min] Start together

Create `my_work/paygap.py` with the docstring and the import, write
`load_payroll` live, write `check1.py`, run it. Then leave her to
exercises 1–4. Stay nearby for exercise 4 (`qcut` + `crosstab`); it's on
the cheat sheet, but the first time is always odd.

---

## Session 2 briefing [10 min]

### [0–3 min] Recap

Run her `check2.py` through `check4.py`. Ask her to read the quartile table
out loud as sentences ("72% of the lowest-paid quarter are women…").
Then the headcount: 41.5% of the company is women. Let that sit.

### [3–7 min] From numbers to a report (demo section 2)

- Exercise 5 is the "where does it come from" view. HR will have the biggest
  gap *and* be 67% women. Don't explain in advance; ask her to explain it
  to you when she gets there. (Answer: the four men in HR are senior.)
- Exercise 6: a script that calls the five functions and prints. Point out
  that the report is now ~25 lines because all the thinking lives in
  `paygap.py`.
- Exercise 7: lesson 11, condensed. Stacked bars: `bottom=`.

### [7–10 min] The ending

- Bug hunt #12 is Dave's port of MACRO-9000. The three bugs are exactly the
  three rules from session 1. She has everything she needs to explain, in
  three commit messages, why the board was told 24.6% for three years.
- The pull request is called "Retire MACRO-9000". Review it properly: ask
  one "why" question per function.

---

## Reference answers (don't show)

| Figure | Value |
|---|---|
| Mean hourly gap | 19.7% |
| Median hourly gap | 18.7% |
| Mean bonus gap | 22.8% |
| Median bonus gap | 30.8% |
| Receiving a bonus | women 45.8%, men 66.7% |
| Quartiles, % women | 72.0 / 46.0 / 30.0 / 18.0 |
| Dave's wrong mean (divided by women's pay) | 24.6% |

**Questions to check understanding:**
- Why divide by men's pay and not the average of both?
- Why would the median gap be smaller than the mean gap, and what does it tell you?
- Why doesn't `paygap.py` print anything?
