# ==================================================================
#  PAGES FROM THE GRIMOIRE, PAGE 14: "charter_figures.py" (the last page)
# ==================================================================
#
# Before he sailed west, Dalvric copied the Grimoire's Charter
# incantation into Python. For years it has told the Privy Council that
# the guild wins 85% of its quests and should hunt nothing but wyrms.
# Your report says otherwise. The Queen wants to know who's right.
#
# THREE bugs:
#   one crashes (a region has gone missing; ask yourself where),
#   one crowns the wrong monster with a perfectly straight face,
#   one counts running away as winning.
#
# Run it from inside the lesson folder:
#   python bughunt/grimoire_bug.py
#
# When it's fixed, it prints EXACTLY this:
#
#   THE GRIMOIRE'S CHARTER FIGURES, CHECKED
#   Success rate: 64.8%
#   Best monster per quest-day: Trolls (75.6 cr)
#   Thornwood: 90 quests, warden (none)
#   The Grimoire agrees with the Keeper. The Grimoire may now close.
#
# Fix ONE bug per commit and explain it in the message.

import sqlite3

import pandas as pd

con = sqlite3.connect("data/guild.db")
quests = pd.read_sql("SELECT * FROM quests", con)
print("THE GRIMOIRE'S CHARTER FIGURES, CHECKED")

# --- Part 1: how often do we win? ---
wins = quests["outcome"] != "Failed"
print(f"Success rate: {wins.mean() * 100:.1f}%")

# --- Part 2: which monster is worth the crowns? ---
table = quests.groupby("monster").agg(reward=("reward", "mean"),
                                      paid=("paid", "sum"),
                                      days=("days", "sum"))
table["per_day"] = table["paid"] / table["days"]
best = table["reward"].idxmax()
print(f"Best monster per quest-day: {best} ({table.loc[best, 'per_day']:.1f} cr)")

# --- Part 3: every region and its warden ---
sql = """
    SELECT q.region, COALESCE(r.warden, '(none)') AS warden, COUNT(*) AS quests
    FROM quests AS q
    JOIN regions AS r ON q.region = r.region
    GROUP BY q.region
"""
regions = pd.read_sql(sql, con).set_index("region")
row = regions.loc["Thornwood"]
print(f"Thornwood: {row['quests']} quests, warden {row['warden']}")
print("The Grimoire agrees with the Keeper. The Grimoire may now close.")
