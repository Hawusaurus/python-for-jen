# ==================================================================
#  PAGES FROM THE GRIMOIRE, PAGE 10: "war_table.py"
# ==================================================================
#
# Found pinned under the big map on the War Table, with a candle
# stain where Region 5 should be. Dalvric wrote it to show Captain Siv
# every region at a glance: how many quests, how often the party came
# home victorious, and which warden to send the raven to.
# Siv says it "has never once told me anything I could act on".
#
# THREE bugs:
#   one crashes (the error mentions a "level name"; think about how groupby wants TWO keys),
#   one quietly loses quests (count them: there should be 400),
#   one gets every percentage subtly wrong (compare with your Exercise 4).
#
# Run it from inside the lesson folder:
#   python bughunt/war_table.py
#
# When it's fixed, it prints EXACTLY this:
#
#   Quests on the war table: 400
#   outcome         quests  success_pct                   warden
#   region
#   Thornwood           90         71.1              (no warden)
#   Saltmarsh           82         69.5   Warden Nerys Saltmarsh
#   Northern Wilds      75         64.0  Warden Corwin Northwind
#   Ironhills           85         61.2  Warden Hild Stonebridge
#   Greyfen             68         55.9        Warden Alder Pike
#
# Fix ONE bug per commit and explain it in the message, like a detective:
#   git commit -m "Bug hunt: <what was wrong and why>"

import pandas as pd

pd.set_option("display.width", 120)
quests = pd.read_csv("data/quests.csv")
regions = pd.read_csv("data/regions.csv")

quests = quests.merge(regions, on="region", how="inner")
quests["warden"] = quests["warden"].fillna("(no warden)")
print("Quests on the war table:", len(quests))

table = quests.groupby("region", "outcome")["quest_id"].count().unstack(fill_value=0)
table["quests"] = table.sum(axis=1)
table["success_pct"] = (table["Success"] / (table["Success"] + table["Failed"]) * 100).round(1)

wardens = quests.groupby("region")["warden"].first()
table["warden"] = wardens

print(table[["quests", "success_pct", "warden"]].sort_values("success_pct", ascending=False))
