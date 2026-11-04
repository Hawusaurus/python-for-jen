# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 11 · RIDDLE 3: "The Shortest Long Walk"
# ==================================================================
#
#  I lined the quests up, short to long, the way the Vault prefers,
#  then took the first five off the top: the shortest, quickest stirs.
#  You wanted those who walked the most, the blistered and the worn;
#  turn round the line before you cut, or the wrong five will be borne.
#
#  The cobbler wants to know which five parties spent longest in the field,
#  so he can send them a leaflet about boots.
#
#  Run:  python bughunt/riddles/riddle_3_longest.py
#  When it's fixed, it prints EXACTLY this:
#
#    THE FIVE LONGEST QUESTS
#    Q0373  Northern Wilds  14 days
#    Q0064  Northern Wilds  13 days
#    Q0174  Northern Wilds  13 days
#    Q0227  Northern Wilds  13 days
#    Q0303  Northern Wilds  13 days

import sqlite3

con = sqlite3.connect("data/guild.db")

rows = con.execute("""
    SELECT quest_id, region, days
    FROM quests
    ORDER BY days, quest_id
    LIMIT 5
""").fetchall()

print("THE FIVE LONGEST QUESTS")
for quest_id, region, days in rows:
    print(f"{quest_id}  {region:<15}{days:>3} days")
