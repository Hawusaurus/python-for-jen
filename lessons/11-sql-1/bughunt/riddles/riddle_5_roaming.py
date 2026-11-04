# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 11 · RIDDLE 5: "The Roaming Monsters"
# ==================================================================
#
#  I filtered groups before I'd made them: WHERE can't count a crowd;
#  it reads the rows one at a time, and sums aren't yet allowed.
#  And counting grades, I counted quests: each "3" I counted thrice.
#  Count every different grade just once. The Vault can do it. Nice.
#
#  Orrin wants the common monsters (40 quests or more) and at how many
#  different difficulty grades each one has been posted. Two bugs on this page.
#
#  Run:  python bughunt/riddles/riddle_5_roaming.py
#  When it's fixed, it prints EXACTLY this:
#
#    MONSTER         QUESTS  GRADES
#    Goblins             81       4
#    Bandits             72       3
#    Wolves              64       2
#    Ghouls              61       3
#    Giant Rats          42       3
#    Giant Spiders       42       3

import sqlite3

con = sqlite3.connect("data/guild.db")

rows = con.execute("""
    SELECT monster, COUNT(*), COUNT(difficulty)
    FROM quests
    WHERE COUNT(*) >= 40
    GROUP BY monster
    ORDER BY COUNT(*) DESC, monster
""").fetchall()

print(f"{'MONSTER':<15}{'QUESTS':>7}{'GRADES':>8}")
for monster, n, grades in rows:
    print(f"{monster:<15}{n:>7}{grades:>8}")
