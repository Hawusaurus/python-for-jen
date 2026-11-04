# ==================================================================
#  PAGES FROM THE GRIMOIRE, PAGE 12: "deep_archive.py"
# ==================================================================
#
# Orrin found this in the Deep Archive, the oldest shelf of the Vault,
# wrapped round a candle stub. Dalvric's region report for the Queen:
# each region's warden, how many quests, how many heroes were sent, and
# the crowns the guild paid out there. The Queen has asked for it every
# Midsummer for three hundred years. She has never received it.
#
# THREE bugs:
#   one crashes (sqlite3 says a column name is "ambiguous": two tables have it),
#   one quietly loses a whole region (count the rows: there should be five),
#   one gets the crowns subtly wrong (compare Thornwood with your Exercise 3).
#
# Run it from inside the lesson folder:
#   python bughunt/deep_archive.py
#
# When it's fixed, it prints EXACTLY this:
#
#   THE DEEP ARCHIVE: REGIONS
#   REGION         WARDEN                   QUESTS  HEROES    CROWNS PAID
#   Ironhills      Warden Hild Stonebridge      85     245      34,730 cr
#   Northern Wilds Warden Corwin Northwind      75     241      33,600 cr
#   Thornwood      (no warden)                  90     258      32,780 cr
#   Saltmarsh      Warden Nerys Saltmarsh       82     235      26,890 cr
#   Greyfen        Warden Alder Pike            68     215      18,150 cr
#
# Fix ONE bug per commit and explain it in the message, like a detective:
#   git commit -m "Bug hunt: <what was wrong and why>"

import sqlite3

con = sqlite3.connect("data/guild.db")

rows = con.execute("""
    SELECT q.region,
           COALESCE(r.warden, '(no warden)') AS warden,
           COUNT(DISTINCT quest_id) AS quests,
           COUNT(*) AS heroes_sent,
           SUM(q.paid) AS crowns
    FROM party AS p
    JOIN quests AS q ON p.quest_id = q.quest_id
    JOIN regions AS r ON q.region = r.region
    GROUP BY q.region
    ORDER BY crowns DESC
""").fetchall()

print("THE DEEP ARCHIVE: REGIONS")
print(f"{'REGION':<15}{'WARDEN':<25}{'QUESTS':>6}{'HEROES':>8}{'CROWNS PAID':>15}")
for region, warden, quests, heroes, crowns in rows:
    print(f"{region:<15}{warden:<25}{quests:>6}{heroes:>8}{crowns:>12,.0f} cr")
