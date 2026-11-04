# Lesson 09: The Living Ledger — pandas I (lecture notes for Lars)

**Goal:** Jen opens the quest ledger as a DataFrame and does the
Quartermistress's monthly routine (filter, sort, helper columns, save) in a
handful of lines. She should leave knowing DataFrame = sheet, Series = column,
index = row label, and that masks work exactly as in NumPy.

`pip install -r requirements.txt` together first (pandas + openpyxl).
Run `demo.py` section by section; typing it live is better. Data:
`data/quests.csv` (400 quests), `data/heroes.csv` (120 heroes) and
`data/guild_ledger.xlsx` (sheets "Quests" and "Notes").

---

## [Opener, 1 min] The 14 tabs

Read Pell's raven from `GUIDE.pdf`. The old ledger workbook has 14 tabs,
including "Dalvric working" (locked, password lost at sea). Today the
Quartermistress's monthly routine becomes a script, and the workbook stays
untouched.

## [0–3 min] Open it and look

```python
import pandas as pd
df = pd.read_csv("data/quests.csv")
df.shape          # (400, 12)
df.head()
df.columns
df.info()         # types and missing values
df.describe()     # the Excel "Data Analysis" summary, free
```

- "This is the sheet. `df` holds all of it."
- `head()` prints with `...` when it's too wide; show `pd.set_option("display.width", 120)`.
- Point at the index on the left: row *labels*, start at 0, not Excel rows.

## [3–6 min] Columns

```python
df["reward"]                     # a Series: a column with a name and index
df["reward"].mean()
df[["quest_id", "reward"]]       # two columns: list inside brackets
df["per_day"] = df["paid"] / df["days"]
```

- Make the `df["a", "b"]` mistake live, read the error, fix with `[[...]]`.
- A new column is "drag the formula down" from last lesson, but it lives
  in the table and has a name.

## [6–10 min] AutoFilter

```python
df[df["reward"] > 1000]
df[(df["region"] == "Northern Wilds") & (df["outcome"] == "Failed")]
df[df["region"].isin(["Greyfen", "Saltmarsh"])]
df[df["title"].str.contains("old mill")]
len(df[mask])                    # COUNTIFS
```

- Same masks as NumPy, same `&`/`|` rule.
- Show that the index "sticks": filtered rows keep their original labels.

## [10–13 min] Sort, save, Excel

```python
df.sort_values("per_day", ascending=False).head()
df.sort_values(["region", "reward"], ascending=[True, False])
df.nlargest(5, "per_day")
df[mask].to_csv("my_work/out.csv", index=False)
pd.read_excel("data/guild_ledger.xlsx", sheet_name="Quests")
```

- `sort_values` returns a *copy*; `df` is unchanged. Show it.
- `index=False`: forget it once and show the "Unnamed: 0" column.
- Open `data/guild_ledger.xlsx` in Excel next to the DataFrame: same thing.

## [13–15 min] The Quartermistress's month in five lines, and handover

```python
df = pd.read_csv("data/quests.csv")
df["per_day"] = (df["paid"] / df["days"]).round(2)
fled = df[df["outcome"] == "Fled"]
fled = fled.sort_values("region")
fled.to_csv("my_work/fled.csv", index=False)
```

"That's a tab she makes by hand every month." Open `EXERCISES.pdf`, type the
opener together, then leave her to it with `CHEATSHEET.pdf`. The bug hunt is
`bughunt/ironhills_bug.py` (Grimoire, page 9). Fast finishers: five optional
riddles in `bughunt/riddles/`, one bug each (the last has two); answers in
`instructor/solutions/09-pandas-1/riddles/`.

---

## Excel → pandas table (show at the end)

| Excel | pandas |
|---|---|
| a sheet | `df` |
| a column | `df["col"]` |
| several columns | `df[["a", "b"]]` |
| AutoFilter | `df[mask]` |
| Sort | `df.sort_values("col")` |
| helper column | `df["new"] = ...` |
| `COUNTIFS` | `len(df[mask])` |
| `AVERAGEIF` | `df[mask]["col"].mean()` |
| Save As CSV | `df.to_csv(path, index=False)` |
| Open workbook | `pd.read_excel(path, sheet_name=...)` |

**Questions to check understanding:**
- What's the difference between `df["a"]` and `df[["a"]]`?
- After `df.sort_values("x")`, is `df` sorted?
- What does the number down the left of a printed DataFrame mean?
