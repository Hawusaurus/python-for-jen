# Lesson 08: NumPy, whole columns at once (lecture notes for Lars)

**Goal:** Jen stops thinking "loop over rows" and starts thinking "operate on
the column". Arrays, vectorised maths, boolean masks, percentiles, axis.
NumPy is the bridge to pandas: next lesson's DataFrame columns *are* arrays.

Run `demo.py` section by section. Before that: `pip install -r requirements.txt`
together, so she sees that a lesson can bring its own packages.

---

## [Opener, 1 min] Mistress Pell's mug

Read Orrin's raven from `GUIDE.pdf`. The Grimoire's pay review walks the Roll
one subject at a time and takes forty seconds. Mistress Pell has a dedicated
tea mug for it. Today we retire the mug: a thousand coins at once, one line,
all 200 rows, no loop.

## [0–3 min] The loop she'd write, and the line instead

```python
# What she'd write after lesson 02:
monthly = []
for s in salaries:
    monthly.append(s / 12)

# NumPy:
salaries = np.array(salaries)
monthly = salaries / 12
```

- An array is a column. One type (`dtype`), one shape.
- Maths applies to every element: "vectorised". It's dragging `=B2/12` down,
  but the drag is free and never misses a row.
- Show `salaries.shape`, `salaries.dtype`, `salaries[:5]`.

## [3–6 min] Summaries

```python
salaries.min(), salaries.max(), salaries.mean(), salaries.sum()
np.median(salaries)
np.percentile(salaries, 75)          # NOT 0.75
np.percentile(salaries, [25, 50, 75])
```

- Make the `salaries.mean` (no brackets) mistake on purpose and read the
  output together: `<built-in method mean ...>`.
- Point out `np.median` is a function, not a method. No good reason; just is.

## [6–10 min] Masks: AutoFilter in one line

```python
high = salaries > 40000     # array of True/False
high[:5]
high.sum()                  # COUNTIF
salaries[high]              # filter
salaries[high].mean()       # AVERAGEIF
women = genders == "F"
salaries[women].mean()
(high & women).sum()        # &, not and
```

- Do `(salaries > 40000) and (genders == "F")` live and read the error:
  "truth value of an array is ambiguous". Then show `&` with brackets.
- A mask summed is a count; a mask averaged is a share. She'll use both.

## [10–13 min] Axis

Draw a 3×6 grid on paper (people × months).

```python
pay.sum()          # everything
pay.sum(axis=0)    # down the columns: one per month
pay.sum(axis=1)    # along the rows: one per person
pay[1, 3]          # row 1, column 3
pay[:, 2]          # whole column
```

"axis=0 is the SUM you'd put at the bottom; axis=1 is the SUM at the end."

## [13–15 min] The gap, in four lines, and handover

```python
hourly = salaries / 52 / hours
m = hourly[genders == "M"].mean()
f = hourly[genders == "F"].mean()
(m - f) / m * 100
```

That's the mean gender pay gap for all 200 employees. Exercise 4 does it
with median too; Exercise 5 does quartiles. Open `EXERCISES.pdf`, do the
loader from Exercise 1 together, then leave her to it with `CHEATSHEET.pdf`.

---

## Excel → NumPy table (show at the end)

| Excel | NumPy |
|---|---|
| drag `=B2/12` down | `salaries / 12` |
| `COUNTIF(B:B,">40000")` | `(salaries > 40000).sum()` |
| `AVERAGEIF` | `salaries[mask].mean()` |
| `IF(...)` dragged down | `np.where(mask, a, b)` |
| `PERCENTILE(B:B, 0.75)` | `np.percentile(salaries, 75)` |
| `MEDIAN` | `np.median(salaries)` |
| SUM under a column | `m.sum(axis=0)` |
| SUM at the end of a row | `m.sum(axis=1)` |

**Questions to check understanding:**
- What does `(salaries > 40000).sum()` give you? And `.mean()`?
- Why does `(a > 1) and (b > 2)` fail on arrays?
- In a people × months array, which axis gives one number per month?
