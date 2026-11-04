# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 14 · RIDDLE 4: "The Wood Nobody Counted"
# ==================================================================
#
#  The wood without a warden kept its quests through every join,
#  but when the tally came to it, it didn't get a coin.
#  You counted what the wardens wrote, and where there's no one there,
#  the count skips every empty space: so count the rows, not air.
#
#  Captain Siv asked how many quests each region posted, wardens or no.
#  Dalvric's answer adds up to rather less than the four hundred she posted.
#
#  Run:  python bughunt/riddles/riddle_4_wardens.py
#  When it's fixed, it prints EXACTLY this:
#
#    Greyfen          68
#    Ironhills        85
#    Northern Wilds   75
#    Saltmarsh        82
#    Thornwood        90
#    Total: 400

import sqlite3

import pandas as pd

con = sqlite3.connect("data/guild.db")
sql = """
    SELECT q.region, COUNT(r.warden) AS quests
    FROM quests AS q
    LEFT JOIN regions AS r ON q.region = r.region
    GROUP BY q.region
    ORDER BY q.region
"""
table = pd.read_sql(sql, con)
for region, n in zip(table["region"], table["quests"]):
    print(f"{region:<15}{n:>4}")
print("Total:", table["quests"].sum())
