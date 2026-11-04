# Lesson 14: The Charter (lecture notes for Lars, two sessions)

**Goal:** Jen builds the Charter Report for Queen Aldara end to end as a
small project: a module of functions (SQL via `read_sql` and pandas), check
scripts, a report script, a chart and a formatted workbook, and one sentence.
Nothing new in Python; the new skill is *structuring* the work and choosing
the measure that tells the truth.

Keep the briefings short. The sheet is long and she should be writing, not
listening. `demo.py` has one section per session.

---

## Session 1 briefing [15 min]

### [Opener, 2 min] The Queen's decree

Read the decree from `GUIDE.pdf`. The stakes: the Charter is renewed at
Midsummer or not, the Grimoire has told the Privy Council for years that the
guild wins 85% of its quests and should hunt wyrms, and if her numbers hold
up the Grimoire is closed for good.

### [2–7 min] The rules of the game

Walk through the table on page 1 of `EXERCISES.pdf` (the Queen's questions).
Three things to land, because each one is a bug hunt bug later:

1. **Fled is not a success.** It pays a quarter of the reward, and it is
   still running away. Demo section 1 shows 64.8% vs 85.2%.
2. **Paid, per day.** The notice board's reward is a promise; `paid` is what
   came home, and a quest that takes twelve days ties up a party for twelve
   days. `sum(paid) / sum(days)` per monster.
3. **Every region.** Thornwood has no warden, so it has no row in `regions`.
   A plain `JOIN` drops it (and its 90 quests); `LEFT JOIN` keeps it.

Ask: "Which monster would you send parties after?" Let her guess the Wyrm.
Exercise 3 will answer.

### [7–12 min] The shape of a project (demo section 1)

```
my_work/charter.py       functions only; never prints, never names a file
my_work/check1.py        import charter; open, load; print
my_work/report.py        session 2
```

- Lesson 07 again: a `.py` file next to the script is importable. Show
  `demo.py` section 1 importing from `demo_helpers.py`.
- Rule: *functions compute, scripts print.* It's what makes the report
  reusable next season, and checkable.
- Two crafts: the Vault (SQL, lessons 11–12) for counting and joining,
  pandas (lessons 09–10) for the rest. Both end up as DataFrames.
- Every function gets a docstring. One line is enough.

### [12–15 min] Start together

Create `my_work/charter.py` with the docstring and imports, write
`open_vault` and `outcome_counts` live, write `check1.py`, run it. Then leave
her to exercises 1–4. Stay nearby for exercise 4 (the LEFT JOIN with
`COALESCE` and `SUM(q.outcome = 'Success')`); it's on the cheat sheet, but
the first time is always odd.

---

## Session 2 briefing [10 min]

### [0–3 min] Recap

Run her `check2.py` through `check4.py`. Ask her to read the monster table
out loud as sentences ("Trolls earn 75.6 crowns a day…"). Then the Wyrm:
3,130 cr on the notice, 28.6 cr a day in the chest, seven quests, no wins.

### [3–7 min] From numbers to a report (demo section 2)

- Exercise 5 is the fairness view. Bards get the easiest quests (2.95 vs
  Warriors' 3.49) and leaders take 47.2% of the loot on shared quests.
  Don't judge it for her; ask her what she'd tell the Queen.
- Exercise 6: a script that calls the functions and prints. Point out that
  the report is short because all the thinking lives in `charter.py`.
- Exercise 7: lesson 13, condensed. A list comprehension for the colours,
  a dict for which columns get the crown format.

### [7–10 min] The ending

- The bug hunt is the Grimoire's last page: Dalvric's Python copy of its
  Charter figures. Bug 1 is rule 3 (INNER JOIN, Thornwood vanishes, KeyError),
  bug 2 is rule 2 (ranked by reward, the Wyrm wins), bug 3 is rule 1 (Fled
  counted as success). She has everything she needs to explain, in three
  commit messages, why the Privy Council was told 85% for years.
- Five optional riddles in `bughunt/riddles/` (GROUP BY, case, brackets,
  COUNT of a NULL column, integer division plus sort order). Solutions in
  `instructor/solutions/14-the-charter/riddles/`.
- The pull request is called "The Charter". Review it properly: ask one
  "why" question per function. Then award the Keeper's Seal.

---

## Reference answers (don't show)

| Figure | Value |
|---|---|
| Outcomes | 259 Success / 82 Fled / 59 Failed |
| Success rate | 64.8% (the Grimoire's, Fled counted in: 85.2%) |
| Success by difficulty 1→5 | 88.2 / 74.5 / 62.5 / 56.8 / 42.5 % |
| Injuries per quest 1→5 | 0.12 / 0.22 / 0.65 / 1.08 / 1.78 |
| Best / worst per quest-day | Trolls 75.6 cr / Giant Rats 17.6 cr (Wyrm 28.6, 7th of 8) |
| Thornwood | 90 quests, no warden, best success rate (71.1%) |
| Top hero by loot | Jasper Ironfoot, 4,428.68 cr |
| Avg difficulty by class | Bard 2.95 … Warrior 3.49 |
| Leaders' share on shared quests | 47.2% |

**Questions to check understanding:**
- Why is Fled not a success, even though it pays?
- Why measure crowns *paid* per *day*, not the reward on the notice?
- What would a plain `JOIN` do to Thornwood, and why doesn't `charter.py` print anything?
