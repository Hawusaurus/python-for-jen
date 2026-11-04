# Lesson 11: SQL I, the Vault Beneath (lecture notes for Lars)

**Goal:** Jen can open a SQLite database from Python, write single-table
queries (SELECT, WHERE, ORDER BY, LIMIT, DISTINCT, aggregates, GROUP BY,
HAVING) and print the rows. She should leave knowing that SQL is the same
AutoFilter/PivotTable thinking she already has, in a different language.

Run `demo.py` section by section (or paste the queries into the REPL).
`data/guild.db` is the Vault: tables heroes, quests, party, regions. Nothing
to pip install; `sqlite3` is part of Python. Optional: open `guild.db` in
DB Browser for SQLite (free) so she can *see* the tables.

---

## [Opener, 1 min] The Vault

Read Orrin's raven from `GUIDE.pdf`. Same guild data as the CSVs, but in a
database: one file, four tables, and you talk to it in SQL. Say why it
matters: every analytics job asks for SQL. It's the most employable thing
in this course.

## [0–3 min] Python asks, SQL answers

```python
import sqlite3
con = sqlite3.connect("data/guild.db")
rows = con.execute("SELECT * FROM heroes LIMIT 3").fetchall()
```

- `execute` runs the SQL string; `fetchall()` gives a list of tuples;
  `fetchone()` the first tuple. Python does the printing.
- SQL keywords in capitals is a habit, not a rule. Triple quotes let a query
  span lines; long queries should.

## [3–7 min] SELECT and WHERE are the AutoFilter

```sql
SELECT name, level FROM heroes WHERE class = 'Ranger' AND level >= 14
SELECT COUNT(*) FROM heroes WHERE class = 'ranger'     -- 0!
WHERE kin IN ('Dwarf', 'Gnome')
WHERE level BETWEEN 12 AND 20
WHERE title LIKE '%chapel%'
WHERE region IS NULL
```

- Text in single quotes, exact case: show the `'ranger'` query returning 0.
  No error, just nothing. That's the bug hunt's silent bug.
- `AND` before `OR`: brackets. `IS NULL`, never `= NULL` (it matters next week).

## [7–9 min] ORDER BY, LIMIT, DISTINCT

```sql
SELECT quest_id, monster, reward FROM quests ORDER BY reward DESC LIMIT 3
SELECT DISTINCT region FROM quests ORDER BY region
```

- ASC is the default. "Top 5" = `ORDER BY … DESC LIMIT 5`.

## [9–13 min] Aggregates, GROUP BY, HAVING

```sql
SELECT COUNT(*), SUM(paid), ROUND(AVG(reward), 2) FROM quests
SELECT SUM(paid) / COUNT(*), SUM(paid) * 1.0 / COUNT(*) FROM quests
SELECT monster, COUNT(*) AS quests, ROUND(SUM(paid) * 1.0 / SUM(days), 1) AS per_day
FROM quests GROUP BY monster HAVING quests >= 30 ORDER BY per_day DESC
```

- Whole number ÷ whole number drops the decimals: 365 vs 365.375. Show it.
- GROUP BY is the PivotTable's row field. WHERE filters rows before grouping,
  HAVING filters groups after. Write the clause order on the whiteboard:
  SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY, LIMIT.
- Uncomment the last line of the demo (WHERE after GROUP BY) and read the
  syntax error together. That's the bug hunt crash.

## [13–15 min] Same answer, three languages, and handover

Trolls and Giant Spiders pay best per day, same as last week in pandas.
Point at the cheat sheet's Excel → pandas → SQL table. Then open
`EXERCISES.pdf`, do Exercise 1 (a) together, and leave her to it with
`CHEATSHEET.pdf`. Fast finishers: five extra riddles in
`bughunt/riddles/` (a missing comma, unquoted text, ASC instead of DESC,
AND/OR without brackets, an aggregate in WHERE plus COUNT without DISTINCT;
solutions in `instructor/solutions/11-sql-1/riddles/`).

---

## Excel → pandas → SQL (show at the end)

| Excel | pandas | SQL |
|---|---|---|
| AutoFilter | `df[df["level"] >= 12]` | `WHERE level >= 12` |
| Hide columns | `df[["name", "level"]]` | `SELECT name, level` |
| Sort Z–A | `df.sort_values("reward", ascending=False)` | `ORDER BY reward DESC` |
| Top 5 | `.head(5)` | `LIMIT 5` |
| Remove duplicates | `df["monster"].unique()` | `SELECT DISTINCT monster` |
| COUNTA | `len(df)` | `COUNT(*)` |
| PivotTable | `df.groupby("monster")["reward"].mean()` | `GROUP BY monster` with `AVG(reward)` |
| Filter the pivot | `t[t["n"] >= 30]` | `HAVING COUNT(*) >= 30` |

**Questions to check understanding:**
- Why does `WHERE class = 'ranger'` find nothing, without an error?
- What's the difference between WHERE and HAVING?
- Why is `SUM(paid) / COUNT(*)` not quite the average in SQLite?
