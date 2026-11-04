# Lesson 08: A Thousand Arrows at Once — NumPy (lecture notes for Lars)

**Goal:** Jen stops thinking "loop over rows" and starts thinking "operate on
the column". Arrays, vectorised maths, boolean masks, percentiles, axis.
NumPy is the bridge to pandas: next lesson's DataFrame columns *are* arrays.

Run `demo.py` section by section. Before that: `pip install -r requirements.txt`
together, so she sees that a lesson can bring its own packages. The data is
`data/quests.csv`: 400 quests from the guild ledger.

---

## [Opener, 1 min] The Quartermistress's mug

Read Orrin's raven from `GUIDE.pdf`. The Grimoire's quest tally walks the ledger
one quest at a time and takes forty seconds. Pell has a dedicated tea mug for
it. Today we retire the mug: a thousand arrows at once, one line, all 400 rows,
no loop.

## [0–3 min] The loop she'd write, and the line instead

```python
# What she'd write after lesson 02:
per_day = []
for i in range(len(paid)):
    per_day.append(paid[i] / days[i])

# NumPy:
paid = np.array(paid)
days = np.array(days)
per_day = paid / days
```

- An array is a column. One type (`dtype`), one shape.
- Maths applies to every element: "vectorised". It's dragging `=L2/G2` down,
  but the drag is free and never misses a row.
- Show `paid.shape`, `paid.dtype`, `paid[:5]`.

## [3–6 min] Summaries

```python
rewards.min(), rewards.max(), rewards.mean(), rewards.sum()
np.median(rewards)
np.percentile(rewards, 75)          # NOT 0.75
np.percentile(rewards, [25, 50, 75])
```

- Make the `rewards.mean` (no brackets) mistake on purpose and read the
  output together: `<built-in method mean ...>`.
- Point out `np.median` is a function, not a method. No good reason; just is.
- Mean 587.72 vs median 470: the Wyrm rewards drag the mean up.

## [6–10 min] Masks: AutoFilter in one line

```python
big = rewards > 1000         # array of True/False
big[:5]
big.sum()                    # COUNTIF
rewards[big]                 # filter
rewards[big].mean()          # AVERAGEIF
success = outcomes == "Success"
(big & success).sum()        # &, not and
success[difficulty == 5].mean()   # share of hard quests that worked
```

- Do `(rewards > 1000) and (outcomes == "Success")` live and read the error:
  "truth value of an array is ambiguous". Then show `&` with brackets.
- A mask summed is a count; a mask averaged is a share. She'll use both.

## [10–13 min] Axis

Draw a 3×6 grid on paper (parties × months of loot).

```python
loot.sum()          # everything
loot.sum(axis=0)    # down the columns: one per month
loot.sum(axis=1)    # along the rows: one per party
loot[1, 3]          # row 1, column 3
loot[:, 2]          # whole column
```

"axis=0 is the SUM you'd put at the bottom; axis=1 is the SUM at the end."

## [13–15 min] The Charter question, in four lines, and handover

```python
per_day = paid / days
for d in range(1, 6):
    level = difficulty == d
    print(d, success[level].mean(), per_day[level].mean())
```

Success falls from 88 % at difficulty 1 to 42 % at 5, yet crowns per day go
*up*. That's the start of the sentence for the Queen. Exercise 4 does it
properly; Exercise 5 does quartiles. Open `EXERCISES.pdf`, do the loader from
Exercise 1 together, then leave her to it with `CHEATSHEET.pdf`. The bug hunt is
`bughunt/danger_bug.py` (Grimoire, page 8). Fast finishers: five optional
riddles in `bughunt/riddles/`, one bug each (the last has two); answers in
`instructor/solutions/08-numpy/riddles/`.

---

## Excel → NumPy table (show at the end)

| Excel | NumPy |
|---|---|
| drag `=L2/G2` down | `paid / days` |
| `COUNTIF(H:H,">1000")` | `(rewards > 1000).sum()` |
| `AVERAGEIF` | `rewards[mask].mean()` |
| `IF(...)` dragged down | `np.where(mask, a, b)` |
| `PERCENTILE(H:H, 0.75)` | `np.percentile(rewards, 75)` |
| `MEDIAN` | `np.median(rewards)` |
| SUM under a column | `m.sum(axis=0)` |
| SUM at the end of a row | `m.sum(axis=1)` |

**Questions to check understanding:**
- What does `(rewards > 1000).sum()` give you? And `.mean()`?
- Why does `(a > 1) and (b > 2)` fail on arrays?
- In a parties × months array, which axis gives one number per month?
