# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 11 · RIDDLE 4: "North, Or Else"
# ==================================================================
#
#  "The Wilds or else the Ironhills, and deadly": so I said.
#  But AND binds tighter than an OR, the way a knot binds thread.
#  The Ironhills got "deadly" and the Wilds got all their lot;
#  a pair of brackets round the OR would tie the proper knot.
#
#  Captain Siv: how many difficulty-5 quests did we post in the north
#  (Northern Wilds or Ironhills), and what did they offer in total?
#
#  Run:  python bughunt/riddles/riddle_4_north.py
#  When it's fixed, it prints EXACTLY this:
#
#    Difficulty-5 quests in the north: 16
#    Crowns offered:                   27,020 cr

import sqlite3

con = sqlite3.connect("data/guild.db")

n, total = con.execute("""
    SELECT COUNT(*), SUM(reward)
    FROM quests
    WHERE region = 'Northern Wilds' OR region = 'Ironhills' AND difficulty = 5
""").fetchone()

print(f"Difficulty-5 quests in the north: {n}")
print(f"Crowns offered:                   {total:,} cr")
