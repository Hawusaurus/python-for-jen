# Lesson 10: pandas II, the Council of Guilds (lecture notes for Lars)

**Goal:** Jen can build any PivotTable she'd build in Excel with `groupby`
or `pivot_table`, join a second table with `merge`, and handle the NaNs
that merges and empty cells produce. By the end of the sheet she has every
number the statutory pay gap report needs.

Run `demo.py` section by section. The payroll CSV and
`data/guilds.csv` are in the lesson folder.

---

## [Opener, 1 min] Eleven PivotTables

Read the Queen's decree from `GUIDE.pdf`. Last year Lady Siv built eleven
PivotTables by hand and one pointed at the wrong tab; they found out in
front of the Council of Guilds. Today each of those is one line.

## [0–4 min] groupby is the PivotTable

```python
df["department"].value_counts()                     # COUNTIF
df.groupby("department")["annual_salary"].mean()    # row field, values, summary
df.groupby("department")["annual_salary"].agg(["count", "mean", "median"])
df.groupby(["department", "gender"])["hourly"].mean()
```

- Say it like the PivotTable dialog: *row field* `groupby(...)`, *values*
  `["annual_salary"]`, *summarize by* `.mean()`.
- Two row fields = a list. Do `groupby("department", "gender")` on purpose,
  read the error, fix it. That's the bug hunt crash.
- The result of a single-column groupby is a Series with a (multi-)index.
  `.unstack()` moves the inner level to columns.

## [4–7 min] pivot_table: the dialog with names

```python
df.pivot_table(index="department", columns="gender",
               values="hourly", aggfunc="mean", margins=True)
```

- `index` = Rows box, `columns` = Columns box, `values`+`aggfunc` = Values
  box, `margins=True` = Grand Total.
- Show the same table built two ways (groupby+unstack vs pivot_table).
  Same numbers. groupby is more flexible, pivot_table reads like Excel.

## [7–11 min] merge is XLOOKUP

```python
guilds = pd.read_csv("data/guilds.csv")
m = df.merge(guilds, on="department", how="left")
len(df), len(m)
m["vault"].isna().sum()
m[m["vault"].isna()]["department"].unique()
```

- The Apothecary isn't on the Council's list. With `how="left"`: 200 rows, 15 NaN.
  With `how="inner"`: 185 rows and no warning. Show both; say "count your
  rows after every merge" out loud.
- NaN is `#N/A`. `.isna().sum()` counts, `.fillna()` replaces, `.dropna()`
  removes. `.mean()` ignores NaN; `+` with NaN gives NaN.

## [11–13 min] Quartiles

```python
df["quartile"] = pd.qcut(df["hourly"], 4, labels=["Lower", "Lower middle", "Upper middle", "Upper"])
pd.crosstab(df["quartile"], df["gender"], normalize="index")
```

- `qcut` = equal *counts* (50 each), `cut` = equal *widths*. The Accord
  wants `qcut`.
- Compare with lesson 08: 72 % women in the lower quartile, 18 % in the
  upper. Same answer, now as a grid.

## [13–15 min] The Council's table in one line, and handover

```python
df.groupby(["department", "gender"])["hourly"].mean().unstack()
```

Add `gap_pct = (M - F) / M * 100`, sort it, and the Kitchens are at the
top at 45 %. Pause on that: a guild that is mostly women, with the gap
driven by the few men at the top. It's the kind of thing the report exists
to surface, and it's not what anyone guesses first. Then open `EXERCISES.pdf`, do Exercise 1 (a)
together, and leave her to it with `CHEATSHEET.pdf`.

---

## Excel → pandas table (show at the end)

| Excel | pandas |
|---|---|
| `COUNTIF` by category | `df["col"].value_counts()` |
| PivotTable, one row field | `df.groupby("a")["v"].mean()` |
| PivotTable, two row fields | `df.groupby(["a", "b"])["v"].mean()` |
| PivotTable, rows + columns | `df.pivot_table(index=, columns=, values=, aggfunc=)` |
| Grand Total | `margins=True` |
| `XLOOKUP` | `df.merge(other, on="key", how="left")` |
| `#N/A` | `NaN` |
| `IFERROR(x, 0)` | `.fillna(0)` |
| `QUARTILE` groups | `pd.qcut(col, 4)` |

**Questions to check understanding:**
- What's wrong with `df.groupby("department", "gender")`?
- After `df.merge(other, how="inner")`, can the result have fewer rows than `df`? More?
- What's the difference between `qcut` and `cut`?
