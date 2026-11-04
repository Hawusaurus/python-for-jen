# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 12 · RIDDLE 5: "Above Whose Average?"
# ==================================================================
#
#  I passed the name in brackets, thinking brackets made a pair;
#  a comma makes a tuple, and without one, letters everywhere.
#  And then the inner question roamed the whole realm for its mean,
#  when it should stay at home, inside the region it has been.
#
#  Captain Siv: in each region, how many notices offered more than that
#  region's own average? Two bugs on this page.
#
#  Run:  python bughunt/riddles/riddle_5_above.py
#  When it's fixed, it prints EXACTLY this:
#
#    RICHER THAN THE LOCAL AVERAGE
#    Greyfen          29 notices
#    Ironhills        37 notices
#    Northern Wilds   30 notices
#    Saltmarsh        37 notices
#    Thornwood        31 notices

import sqlite3

con = sqlite3.connect("data/guild.db")


def above_average(region):
    return con.execute("""
        SELECT COUNT(*)
        FROM quests
        WHERE region = ?
          AND reward > (SELECT AVG(reward) FROM quests)
    """, (region)).fetchone()[0]


print("RICHER THAN THE LOCAL AVERAGE")
for region in ["Greyfen", "Ironhills", "Northern Wilds", "Saltmarsh", "Thornwood"]:
    print(f"{region:<15}{above_average(region):>4} notices")
