# Lesson 12: The Grimoire Closes (lecture notes for Lars, two sessions)

**Goal:** Jen builds the Accord of Equal Coin report (the UK gender pay gap
report, with the same six figures) end to end as a small project: a module of functions, check scripts, a report script, a chart and
a workbook. Nothing new in Python; the new skill is *structuring* the work.

Keep the briefings short. The sheet is long and she should be writing, not
listening. `demo.py` is one section per session.

---

## Session 1 briefing [15 min]

### [Opener, 2 min] The Queen's decree

Read the decree from `GUIDE.pdf`. The stakes: the Privy Council sits, the
Grimoire has told it 24.6% every year since anyone can remember, and if her
numbers hold up the Grimoire is closed for good.

### [2–7 min] The rules of the game

Walk through the table on page 1 of `EXERCISES.pdf` (the six figures).
Three things to land, because each one is a bug hunt bug later:

1. Everything is a share of **men's** pay: `(men - women) / men`.
2. Hourly, never annual. Show in the REPL: someone on 18.75 h with 10,300 cr
   a year has an hourly rate of 10.56 cr. Annual pay would call her underpaid.
3. Bonus gap = only people who got a bonus. "Proportion receiving" = everyone.

Ask: "Why both mean and median?" If she doesn't know: mean is pulled by the
few at the top (mostly men); median is the typical person. Mean gap > median
gap means the problem is at the top. In Thornmere it's 19.7 vs 18.7, so
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
Then the headcount: 41.5% of the realm's Treasury roll is women. Let that sit.

### [3–7 min] From numbers to a report (demo section 2)

- Exercise 5 is the "where does it come from" view. The Kitchens will have the
  biggest gap *and* be 67% women. Don't explain in advance; ask her to explain
  it to you when she gets there. (Answer: of the four men in the Kitchens, two
  are Guildmasters and one a Master. Demo section 2 shows it.)
- Exercise 6: a script that calls the five functions and prints. Point out
  that the report is now ~25 lines because all the thinking lives in
  `paygap.py`.
- Exercise 7: lesson 11, condensed. Stacked bars: `bottom=`.

### [7–10 min] The ending

- The bug hunt is the Grimoire's last page: Dalvric's Python copy of its pay
  gap incantation. Bug 2 is rule 1 from session 1 (divide by men's pay), bug 3
  is the mean-vs-median question, bug 1 is a plain KeyError. She has everything she needs to explain,
  in three commit messages, why the Privy Council was told 24.6% for years.
- The pull request is called "The Grimoire Closes". Review it properly: ask
  one "why" question per function. Then award the Keeper's Seal.

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
| The Grimoire's wrong mean (divided by women's pay) | 24.6% |

**Questions to check understanding:**
- Why divide by men's pay and not the average of both?
- Why would the median gap be smaller than the mean gap, and what does it tell you?
- Why doesn't `paygap.py` print anything?
