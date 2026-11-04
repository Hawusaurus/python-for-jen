# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 14 · RIDDLE 1: "The Lonely Group"
# ==================================================================
#
#  I asked the Vault to sort its beasts in heaps, and named the pile,
#  but left a little word behind, and Vault just stared a while.
#  It "groups" by nothing, so it says, and grumbles at the name:
#  two words make up the order; one alone is not the same.
#
#  Orrin found this on the Vault door, the first line of the Charter
#  incantation. It should count the quests per monster, biggest first.
#
#  Run:  python bughunt/riddles/riddle_1_grouping.py
#  When it's fixed, it prints EXACTLY this:
#
#    Goblins          81
#    Bandits          72
#    Wolves           64
#    Ghouls           61
#    Giant Rats       42
#    Giant Spiders    42
#    Trolls           31
#    Wyrm              7

import sqlite3

import pandas as pd

con = sqlite3.connect("data/guild.db")
sql = """
    SELECT monster, COUNT(*) AS quests
    FROM quests
    GROUP monster
    ORDER BY quests DESC, monster
"""
table = pd.read_sql(sql, con)
for monster, n in zip(table["monster"], table["quests"]):
    print(f"{monster:<15}{n:>4}")
