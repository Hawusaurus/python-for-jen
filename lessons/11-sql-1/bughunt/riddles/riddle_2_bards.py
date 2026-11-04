# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 11 · RIDDLE 2: "The Bard Without Quotes"
# ==================================================================
#
#  I asked the Vault for Bards, and wrote the word out plain and bare;
#  it searched its chests for a column called "Bard", and found none there.
#  A word that's only meant as words must wear its little coat:
#  a single mark on either side, the way the Vault takes note.
#
#  Pell is ordering lutes. She needs to know how many Bards the guild has
#  and how experienced they are (it affects the lute).
#
#  Run:  python bughunt/riddles/riddle_2_bards.py
#  When it's fixed, it prints EXACTLY this:
#
#    Bards in the guild: 13
#    Average level:      9.7
#    Highest level:      17

import sqlite3

con = sqlite3.connect("data/guild.db")

n, level, best = con.execute("""
    SELECT COUNT(*), ROUND(AVG(level), 1), MAX(level)
    FROM heroes
    WHERE class = Bard
""").fetchone()

print(f"Bards in the guild: {n}")
print(f"Average level:      {level}")
print(f"Highest level:      {best}")
