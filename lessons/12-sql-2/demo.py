# Lesson 12 demo: run from the lesson folder with  python demo.py
# or copy sections into the REPL one by one.
import sqlite3

import pandas as pd

pd.set_option("display.width", 120)
con = sqlite3.connect("data/guild.db")


def show(sql, params=()):
    """Run a query and print every row (a helper for the demo only)."""
    print(sql.strip())
    for row in con.execute(sql, params).fetchall():
        print("   ", row)
    print()


print("--- JOIN: XLOOKUP for every row ---")
show("SELECT * FROM party LIMIT 3")              # hero_ids nobody can read
show("""
SELECT p.quest_id, h.name, h.class, p.loot_share
FROM party AS p
JOIN heroes AS h ON p.hero_id = h.hero_id
WHERE p.quest_id = 'Q0002'
""")
show("SELECT COUNT(*) FROM party AS p JOIN heroes AS h")   # no ON: 1194 x 120!

print("--- Three tables ---")
show("""
SELECT h.class, COUNT(*), ROUND(AVG(q.difficulty), 2)
FROM party AS p
JOIN heroes AS h ON p.hero_id = h.hero_id
JOIN quests AS q ON p.quest_id = q.quest_id
GROUP BY h.class
ORDER BY AVG(q.difficulty)
""")

print("--- LEFT JOIN: the hole in the map ---")
show("SELECT COUNT(*) FROM quests AS q JOIN regions AS r ON q.region = r.region")
show("SELECT COUNT(*) FROM quests AS q LEFT JOIN regions AS r ON q.region = r.region")
show("""
SELECT q.region, COALESCE(r.warden, '(no warden)'), COUNT(*)
FROM quests AS q
LEFT JOIN regions AS r ON q.region = r.region
WHERE r.region IS NULL
GROUP BY q.region
""")

print("--- CASE WHEN ---")
show("""
SELECT difficulty,
       ROUND(SUM(CASE WHEN outcome = 'Success' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1)
FROM quests GROUP BY difficulty
""")

print("--- Subqueries and WITH ---")
show("SELECT COUNT(*) FROM heroes WHERE level > (SELECT AVG(level) FROM heroes)")
show("""
WITH loot AS (SELECT hero_id, SUM(loot_share) AS total FROM party GROUP BY hero_id)
SELECT h.name, ROUND(l.total, 2) FROM loot AS l JOIN heroes AS h ON l.hero_id = h.hero_id
ORDER BY l.total DESC LIMIT 3
""")

print("--- ? parameters (never f-strings) ---")
show("SELECT COUNT(*) FROM quests WHERE region = ?", ("Thornwood",))
show("SELECT COUNT(*) FROM quests WHERE region = ?", ("Biscuit's Lair",))
# region = "Biscuit's Lair"
# show(f"SELECT COUNT(*) FROM quests WHERE region = '{region}'")   # <- uncomment: the apostrophe breaks it

print("--- Into pandas ---")
df = pd.read_sql_query("""
    SELECT h.class, q.outcome
    FROM party AS p
    JOIN heroes AS h ON p.hero_id = h.hero_id
    JOIN quests AS q ON p.quest_id = q.quest_id
""", con)
print(df.shape)
print((pd.crosstab(df["class"], df["outcome"], normalize="index") * 100).round(1))
