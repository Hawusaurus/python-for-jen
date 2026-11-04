# ==================================================================
#  PAGES FROM THE GRIMOIRE, PAGE 11: "vault_report.py"
# ==================================================================
#
# Orrin found this in the Vault itself, folded inside the lid of the
# oldest chest. Dalvric's report of the hard quests (difficulty 3 and
# up) by region: how many, how many were won, and the average payout.
# Orrin says the Vault "makes a noise like a disappointed aunt" when
# it runs.
#
# THREE bugs:
#   one crashes (sqlite3 complains about a syntax error near "WHERE";
#                SQL clauses have a fixed order),
#   one quietly finds no wins at all (the Vault is fussy about spelling),
#   one gets every average subtly wrong (look at the pennies).
#
# Run it from inside the lesson folder:
#   python bughunt/vault_report.py
#
# When it's fixed, it prints EXACTLY this:
#
#   HARD QUESTS (DIFFICULTY 3+), BY REGION
#   REGION           QUESTS   WON    AVG PAID
#   Ironhills            54    33   507.41 cr
#   Thornwood            54    32   431.30 cr
#   Northern Wilds       51    28   490.78 cr
#   Greyfen              49    23   301.63 cr
#   Saltmarsh            48    31   406.88 cr
#
# Fix ONE bug per commit and explain it in the message, like a detective:
#   git commit -m "Bug hunt: <what was wrong and why>"

import sqlite3

con = sqlite3.connect("data/guild.db")

won = {}
for region, n in con.execute("""
        SELECT region, COUNT(*) FROM quests
        WHERE difficulty >= 3 AND outcome = 'success'
        GROUP BY region""").fetchall():
    won[region] = n

rows = con.execute("""
    SELECT region, COUNT(*), SUM(paid) / COUNT(*)
    FROM quests
    GROUP BY region
    WHERE difficulty >= 3
    ORDER BY COUNT(*) DESC, region""").fetchall()

print("HARD QUESTS (DIFFICULTY 3+), BY REGION")
print(f"{'REGION':<16}{'QUESTS':>7}{'WON':>6}{'AVG PAID':>12}")
for region, n, avg in rows:
    print(f"{region:<16}{n:>7}{won.get(region, 0):>6}{avg:>9.2f} cr")
