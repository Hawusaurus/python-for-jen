# Lesson 10: pandas II, the War Table (lecture notes for Lars)

**Goal:** Jen can build any PivotTable she'd build in Excel with `groupby`
or `pivot_table`, join a second table with `merge`, and handle the NaNs
that merges and empty cells produce. By the end of the sheet she has
rebuilt Captain Siv's War Table: regions, monsters and which notices are
worth the crowns.

Run `demo.py` section by section. `data/quests.csv`, `data/regions.csv`,
`data/heroes.csv` and `data/party.csv` are in the lesson folder.

---

## [Opener, 1 min] Eleven PivotTables pinned with daggers

Read Captain Siv's raven from `GUIDE.pdf`. Eleven printed PivotTables on the
War Table; one pointed at the wrong tab, and four Bards were sent after a
Troll. Today each of those tables is one line.

## [0–4 min] groupby is the PivotTable

```python
quests["region"].value_counts()                    # COUNTIF
quests.groupby("region")["reward"].mean()          # row field, values, summary
quests.groupby("region")["reward"].agg(["count", "mean", "median"])
quests.groupby(["monster", "outcome"])["quest_id"].count()
```

- Say it like the PivotTable dialog: *row field* `groupby(...)`, *values*
  `["reward"]`, *summarize by* `.mean()`.
- Two row fields = a list. Do `groupby("monster", "outcome")` on purpose,
  read the error ("level name outcome…"), fix it. That's the bug hunt crash.
- The result is a Series with a two-level index. `.unstack(fill_value=0)`
  moves the inner level to columns. Point at the Wyrm row: 4, 3, 0.

## [4–7 min] pivot_table: the dialog with names

```python
quests.pivot_table(index="region", columns="outcome",
                   values="quest_id", aggfunc="count", margins=True)
```

- `index` = Rows box, `columns` = Columns box, `values`+`aggfunc` = Values
  box, `margins=True` = Grand Total.
- Leave `aggfunc` out once and show that it quietly averages. Excel
  defaults to Sum, pandas to mean.

## [7–11 min] merge is XLOOKUP

```python
regions = pd.read_csv("data/regions.csv")
m = quests.merge(regions, on="region", how="left")
len(quests), len(m)
m["warden"].isna().sum()
m[m["warden"].isna()]["region"].unique()
```

- Thornwood isn't on the wardens' list (its warden post is vacant). With
  `how="left"`: 400 rows, 90 NaN. With `how="inner"`: 310 rows and no
  warning. Show both; say "count your rows after every merge" out loud.
- NaN is `#N/A`. `.isna().sum()` counts, `.fillna()` replaces (assign it
  back!), `.dropna()` removes. `.mean()` ignores NaN; `groupby` drops NaN keys.

## [11–13 min] Bands

```python
labels = ["Pittance", "Fair", "Handsome", "King's ransom"]
quests["band"] = pd.qcut(quests["reward"], 4, labels=labels)
pd.crosstab(quests["band"], quests["outcome"], normalize="index")
```

- `qcut` = equal *counts*, `cut` = equal *widths*. The bands are 108/95/100/97,
  not 100 each: ties on round rewards can't be split.
- The richer the notice, the less often the party wins: 73 % down to 54 %.

## [13–15 min] The War Table in a few lines, and handover

Run the last two sections of the demo: the success rate per region, and
crowns per day per monster. Trolls and Giant Spiders pay best per day; the
Wyrm has the biggest notices and is near the bottom, because nobody has
ever beaten one. That's the kind of answer Siv wants: not "mayhap", but
"stop pinning up Wyrm notices". Then open `EXERCISES.pdf`, do Exercise 1 (a)
together, and leave her to it with `CHEATSHEET.pdf`. Fast finishers: five extra riddles
in `bughunt/riddles/` (a method never called, `fillna` not kept, pivot_table's mean default, a reward
counted once per hero, reversed band labels; solutions in `instructor/solutions/10-pandas-2/riddles/`).

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
- What's wrong with `quests.groupby("region", "outcome")`?
- After `quests.merge(other, how="inner")`, can the result have fewer rows than `quests`? More?
- What's the difference between `qcut` and `cut`?
