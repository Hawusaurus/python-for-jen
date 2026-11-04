# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 14 · RIDDLE 5: "The Best Three Beasts"
# ==================================================================
#
#  The Vault divides in whole crowns only, sheared of every penny,
#  unless you hand it one point oh and tell it there are many.
#  And when you've asked it for the best, then turn the order round:
#  it starts at the bottom of the heap unless you say "go down".
#
#  Queen Aldara wants the three monsters that earn the guild the most
#  per quest-day, to the penny. Dalvric's page names three very poor ones,
#  in suspiciously round numbers.
#
#  Run:  python bughunt/riddles/riddle_5_per_day.py
#  When it's fixed, it prints EXACTLY this:
#
#    Trolls          75.6 cr a day
#    Giant Spiders   71.8 cr a day
#    Bandits         53.9 cr a day

import sqlite3

import pandas as pd

con = sqlite3.connect("data/guild.db")
sql = """
    SELECT monster, ROUND(SUM(paid) / SUM(days), 1) AS per_day
    FROM quests
    GROUP BY monster
    ORDER BY per_day
    LIMIT 3
"""
best = pd.read_sql(sql, con)
for monster, per_day in zip(best["monster"], best["per_day"]):
    print(f"{monster:<15}{per_day:>5} cr a day")
