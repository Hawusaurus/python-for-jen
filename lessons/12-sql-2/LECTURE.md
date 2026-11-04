# Lesson 12: SQL II, the Deep Archive (lecture notes for Lars)

**Goal:** Jen can JOIN two and three tables, use LEFT JOIN to keep the rows
that don't match (and find them with IS NULL), write CASE WHEN and
subqueries, pass values with `?`, and pull a query into pandas. After this
she can answer any question the Charter Report needs from the Vault.

Run `demo.py` section by section. `data/guild.db` is the same Vault as last
week. `pip install -r requirements.txt` (pandas) for the last section and
Exercise 7.

---

## [Opener, 1 min] Between the shelves

Read the Queen's decree from `GUIDE.pdf`. Last week every question used one
table. The party table says "H072 went on Q0001": true, and useless until
you look H072 up. That lookup, for every row at once, is a JOIN.

## [0–4 min] JOIN is XLOOKUP for every row

```sql
SELECT p.quest_id, h.name, h.class, p.loot_share
FROM party AS p
JOIN heroes AS h ON p.hero_id = h.hero_id
WHERE p.quest_id = 'Q0002'
```

- `ON` says which column matches which. Aliases (`p`, `h`) keep it short and
  say where each column comes from.
- Show a JOIN without ON: 143,280 rows (1,194 × 120). Every row met every
  row. That's riddle 1.
- `quest_id` exists in party *and* quests: without a prefix SQLite says
  "ambiguous column name". That's the bug hunt crash.
- Add a second JOIN to quests: per class, average difficulty. Bards 2.95,
  Warriors 3.49 (same answer as lesson 10, Exercise 7).

## [4–8 min] LEFT JOIN and the hole in the map

```sql
SELECT COUNT(*) FROM quests AS q JOIN regions AS r ON q.region = r.region       -- 310
SELECT COUNT(*) FROM quests AS q LEFT JOIN regions AS r ON q.region = r.region  -- 400
... WHERE r.region IS NULL                                                       -- Thornwood
COALESCE(r.warden, '(no warden)')
```

- Inner JOIN silently drops Thornwood's 90 quests: `how="inner"` all over
  again. LEFT keeps every quest and fills the right side with NULL.
- `IS NULL`, never `= NULL`. `COALESCE` is IFERROR.
- Mention: a condition on the right table belongs in `ON`, not `WHERE`, or
  the LEFT JOIN quietly becomes inner (riddle 3).

## [8–11 min] CASE WHEN

```sql
SUM(CASE WHEN outcome = 'Success' THEN 1 ELSE 0 END) * 100.0 / COUNT(*)
CASE WHEN reward >= 1000 THEN 'Rich' WHEN reward >= 400 THEN 'Fair' ELSE 'Small' END
```

- CASE is a nested IF; inside SUM it's a COUNTIF. 88 % at difficulty 1,
  42 % at difficulty 5: the Queen's sentence.
- First true WHEN wins: biggest threshold first.

## [11–13 min] Subqueries, WITH, and ?

```sql
WHERE level > (SELECT AVG(level) FROM heroes)
WITH loot AS (SELECT hero_id, SUM(loot_share) AS total FROM party GROUP BY hero_id) ...
```
```python
con.execute("SELECT COUNT(*) FROM quests WHERE region = ?", (region,))
```

- A subquery is a helper cell; WITH is a helper cell with a name.
- Values from Python go in with `?` and a tuple (the comma!). Uncomment the
  f-string line in the demo with `"Biscuit's Lair"`: the apostrophe ends the
  string early and the query breaks. With a nastier value it would do worse.
  Rule: never f-string a value into SQL.

## [13–15 min] Into pandas, and handover

`pd.read_sql_query(sql, con)` gives a DataFrame; from there it's lesson 10.
SQL fetches, pandas arranges. Then open `EXERCISES.pdf`, do Exercise 1 (a)
together, and leave her to it with `CHEATSHEET.pdf`. Fast finishers: five
extra riddles in `bughunt/riddles/` (JOIN without ON, `= NULL`, a LEFT JOIN
filtered in WHERE, CASE in the wrong order, a missing tuple comma plus an
uncorrelated subquery; solutions in `instructor/solutions/12-sql-2/riddles/`).

---

## Excel → pandas → SQL (show at the end)

| Excel | pandas | SQL |
|---|---|---|
| XLOOKUP (found only) | `a.merge(b, on="k", how="inner")` | `JOIN b ON a.k = b.k` |
| XLOOKUP with #N/A | `a.merge(b, on="k", how="left")` | `LEFT JOIN b ON a.k = b.k` |
| `ISNA` | `.isna()` | `IS NULL` |
| `IFERROR(x, "none")` | `.fillna("none")` | `COALESCE(x, 'none')` |
| `IF` / `IFS` | `pd.cut` / `np.where` | `CASE WHEN … END` |
| `COUNTIF` | `(df["c"] == "x").sum()` | `SUM(CASE WHEN c = 'x' THEN 1 ELSE 0 END)` |
| helper cell | a variable | subquery / `WITH` |

**Questions to check understanding:**
- Why did the inner JOIN of quests and regions give 310 rows, not 400?
- What happens to the payout column when you join quests to party?
- Why `(region,)` and not `(region)`? Why not an f-string?
