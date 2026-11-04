# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 12 · RIDDLE 3: "Send It By Road"
# ==================================================================
#
#  I kept the left, as LEFT JOIN should, and all the regions stayed,
#  then wrote my "near enough" in WHERE, and three of them were weighed
#  and thrown away: the far, the wild, the one without a name.
#  Put "near" inside the joining terms, and all five rows remain.
#
#  Ravens only reach wardens within three days' travel; the rest get a
#  letter by road. Captain Siv wants every region with quests, and who to
#  send the raven to.
#
#  Run:  python bughunt/riddles/riddle_3_road.py
#  When it's fixed, it prints EXACTLY this:
#
#    RAVENS FOR THE WARDENS
#    Greyfen        Warden Alder Pike         68 quests
#    Ironhills      (send by road)            85 quests
#    Northern Wilds (send by road)            75 quests
#    Saltmarsh      Warden Nerys Saltmarsh    82 quests
#    Thornwood      (send by road)            90 quests

import sqlite3

con = sqlite3.connect("data/guild.db")

rows = con.execute("""
    SELECT q.region, COALESCE(r.warden, '(send by road)'), COUNT(*)
    FROM quests AS q
    LEFT JOIN regions AS r ON q.region = r.region
    WHERE r.travel_days <= 3
    GROUP BY q.region
    ORDER BY q.region
""").fetchall()

print("RAVENS FOR THE WARDENS")
for region, warden, n in rows:
    print(f"{region:<15}{warden:<24}{n:>4} quests")
