# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 12 · RIDDLE 2: "Equal to Nothing"
# ==================================================================
#
#  I asked the Vault, "Is this one equal to nothing at all?"
#  It shrugged: "How can I tell? Nothing's not a thing I can call."
#  Not equal, not unequal, so no row was ever found;
#  ask whether it IS nothing, and the missing come around.
#
#  Orrin wants to know how many quests ended up in regions the map has no
#  entry for, and how many crowns went there.
#
#  Run:  python bughunt/riddles/riddle_2_nothing.py
#  When it's fixed, it prints EXACTLY this:
#
#    Quests off the map: 90
#    Crowns paid there:  32,780 cr

import sqlite3

con = sqlite3.connect("data/guild.db")

n, paid = con.execute("""
    SELECT COUNT(*), COALESCE(SUM(q.paid), 0)
    FROM quests AS q
    LEFT JOIN regions AS r ON q.region = r.region
    WHERE r.region = NULL
""").fetchone()

print(f"Quests off the map: {n}")
print(f"Crowns paid there:  {paid:,} cr")
