# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 11 · RIDDLE 1: "The Missing Comma"
# ==================================================================
#
#  Two columns asked for, side by side, but nothing stood between;
#  so one became the other's name, and one was never seen.
#  A little hook of ink, that's all; a comma, small and plain,
#  and name and level each come home as columns once again.
#
#  Captain Siv wants the five highest-level heroes in the guild, for a
#  quest she won't describe. The Vault hands back something odd.
#
#  Run:  python bughunt/riddles/riddle_1_comma.py
#  When it's fixed, it prints EXACTLY this:
#
#    THE FIVE MIGHTIEST
#    Wren Hawkridge       level 19
#    Ysolde Goldenhand    level 18
#    Ada Fallowfield      level 17
#    Jasper Ironfoot      level 17
#    Jasper Nightingale   level 17

import sqlite3

con = sqlite3.connect("data/guild.db")

rows = con.execute("""
    SELECT name level
    FROM heroes
    ORDER BY level DESC, name
    LIMIT 5
""").fetchall()

print("THE FIVE MIGHTIEST")
for name, level in rows:
    print(f"{name:<20} level {level}")
