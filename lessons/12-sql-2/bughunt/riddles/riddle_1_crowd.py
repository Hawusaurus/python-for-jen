# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 12 · RIDDLE 1: "The Endless Crowd"
# ==================================================================
#
#  I joined the party to the roll but never said on what;
#  so every hero met each row, and joined the lot, the lot.
#  Four heroes went, but in they marched, a hundred times and more:
#  say how the two tables meet, and the crowd goes back to four.
#
#  Captain Siv wants the names of the party she sent on Q0002. Dalvric's
#  page returns rather more heroes than the guild has.
#
#  Run:  python bughunt/riddles/riddle_1_crowd.py
#  When it's fixed, it prints EXACTLY this:
#
#    Heroes on Q0002: 4
#      Idony Nightingale
#      Jasper Ironfoot
#      Ninian Underhill
#      Wren Hawkridge

import sqlite3

con = sqlite3.connect("data/guild.db")

rows = con.execute("""
    SELECT h.name
    FROM party AS p
    JOIN heroes AS h
    WHERE p.quest_id = 'Q0002'
    ORDER BY h.name
""").fetchall()

print(f"Heroes on Q0002: {len(rows)}")
for (name,) in rows:
    print(" ", name)
