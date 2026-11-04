# Lesson 11 demo: run from the lesson folder with  python demo.py
# or copy sections into the REPL one by one.
import sqlite3

con = sqlite3.connect("data/guild.db")


def show(sql):
    """Run a query and print every row (a helper for the demo only)."""
    print(sql.strip())
    for row in con.execute(sql).fetchall():
        print("   ", row)
    print()


print("--- What's in the Vault ---")
show("SELECT name FROM sqlite_master WHERE type = 'table'")
show("SELECT * FROM heroes LIMIT 3")

print("--- SELECT + WHERE = the AutoFilter ---")
show("SELECT name, level FROM heroes WHERE class = 'Ranger' AND level >= 14")
show("SELECT COUNT(*) FROM heroes WHERE class = 'ranger'")      # 0: exact match!
show("SELECT name, kin FROM heroes WHERE kin IN ('Gnome') AND level BETWEEN 10 AND 20")
show("SELECT COUNT(*) FROM quests WHERE title LIKE '%chapel%'")

print("--- ORDER BY, LIMIT, DISTINCT ---")
show("SELECT quest_id, monster, reward FROM quests ORDER BY reward DESC LIMIT 3")
show("SELECT DISTINCT region FROM quests ORDER BY region")

print("--- Aggregates ---")
show("SELECT COUNT(*), SUM(paid), ROUND(AVG(reward), 2) FROM quests")
show("SELECT SUM(paid) / COUNT(*), SUM(paid) * 1.0 / COUNT(*) FROM quests")   # whole-number trap

print("--- GROUP BY + HAVING = the PivotTable ---")
show("""
SELECT monster, COUNT(*) AS quests, ROUND(SUM(paid) * 1.0 / SUM(days), 1) AS per_day
FROM quests
GROUP BY monster
HAVING quests >= 30
ORDER BY per_day DESC
""")

# show("SELECT region, COUNT(*) FROM quests GROUP BY region WHERE difficulty >= 3")   # <- uncomment: clause order
