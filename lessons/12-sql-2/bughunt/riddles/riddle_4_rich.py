# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 12 · RIDDLE 4: "No One Is Rich"
# ==================================================================
#
#  The first true answer wins the CASE; the rest are never read.
#  I asked "at least four hundred?" first, and gold just nodded its head.
#  A thousand crowns is also more than four hundred, you see,
#  so ask the biggest question first, or "Rich" will never be.
#
#  Quartermistress Pell sorts the notices into Small, Fair and Rich for the
#  notice board. Apparently nothing in three hundred years has been Rich.
#
#  Run:  python bughunt/riddles/riddle_4_rich.py
#  When it's fixed, it prints EXACTLY this:
#
#    NOTICES BY SIZE
#    Small  165 notices,    90 to   390 cr
#    Fair   191 notices,   400 to   990 cr
#    Rich    44 notices, 1,000 to 4,540 cr

import sqlite3

con = sqlite3.connect("data/guild.db")

rows = con.execute("""
    SELECT CASE WHEN reward >= 400 THEN 'Fair'
                WHEN reward >= 1000 THEN 'Rich'
                ELSE 'Small'
           END AS band,
           COUNT(*), MIN(reward), MAX(reward)
    FROM quests
    GROUP BY band
    ORDER BY MIN(reward)
""").fetchall()

print("NOTICES BY SIZE")
for band, n, low, high in rows:
    print(f"{band:<6}{n:>4} notices, {low:>5,} to {high:>5,} cr")
