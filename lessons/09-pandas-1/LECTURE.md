# Lesson 09: pandas I, the living ledger (lecture notes for Lars)

**Goal:** Jen opens the Roll as a DataFrame and does Mistress Pell's monthly
routine (filter, sort, helper columns, save) in a handful of lines. She
should leave knowing DataFrame = sheet, Series = column, index = row label,
and that masks work exactly as in NumPy.

`pip install -r requirements.txt` together first (pandas + openpyxl).
Run `demo.py` section by section; typing it live is better.

---

## [Opener, 1 min] The 14 tabs

Read Mistress Pell's raven from `GUIDE.pdf`. The Treasury workbook has 14 tabs,
including "Dalvric working" (locked, password lost at sea). Today Mistress
Pell's monthly routine becomes a script, and the workbook stays untouched.

## [0–3 min] Open it and look

```python
import pandas as pd
df = pd.read_csv("data/thornmere_payroll.csv")
df.shape          # (200, 12)
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
df["annual_salary"]              # a Series: a column with a name and index
df["annual_salary"].mean()
df[["first_name", "annual_salary"]]   # two columns: list inside brackets
df["hourly"] = df["annual_salary"] / 52 / df["weekly_hours"]
```

- Make the `df["a", "b"]` mistake live, read the error, fix with `[[...]]`.
- A new column is "drag the formula down" from last lesson, but it lives
  in the table and has a name.

## [6–10 min] AutoFilter

```python
df[df["annual_salary"] > 40000]
df[(df["department"] == "Guard") & (df["weekly_hours"] < 37.5)]
df[df["location"].isin(["Westmarch", "Harbourtown"])]
df[df["job_title"].str.contains("Warden")]
len(df[mask])                    # COUNTIFS
```

- Same masks as NumPy, same `&`/`|` rule.
- Show that the index "sticks": filtered rows keep their original labels.

## [10–13 min] Sort, save, Excel

```python
df.sort_values("hourly", ascending=False).head()
df.sort_values(["department", "hourly"], ascending=[True, False])
df.nlargest(5, "hourly")
df[mask].to_csv("my_work/out.csv", index=False)
pd.read_excel("data/payroll.xlsx", sheet_name="Payroll")
```

- `sort_values` returns a *copy*; `df` is unchanged. Show it.
- `index=False`: forget it once and show the "Unnamed: 0" column.
- Open `data/payroll.xlsx` in Excel next to the DataFrame: same thing.

## [13–15 min] Mistress Pell's month in five lines, and handover

```python
df = pd.read_csv("data/thornmere_payroll.csv")
df["hourly"] = (df["annual_salary"] / 52 / df["weekly_hours"]).round(2)
part = df[df["weekly_hours"] < 37.5]
part = part.sort_values("department")
part.to_csv("my_work/part_timers.csv", index=False)
```

"That's a tab she makes by hand every month." Open `EXERCISES.pdf`, type the
opener together, then leave her to it with `CHEATSHEET.pdf`.

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
