# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 10 · RIDDLE 2: "The Warden Who Wasn't"
# ==================================================================
#
#  I filled the blanks with a captain's name, in ink both neat and new,
#  then never put the page back in, so the blanks came back on cue.
#  The groupby walked the column through and, finding blanks once more,
#  it left the Thornwood quests outside, like boots outside the door.
#
#  Thornwood has no warden, so Captain Siv reads its ravens herself.
#  The tally of ravens per warden should say so. It doesn't.
#
#  Run:  python bughunt/riddles/riddle_2_warden.py
#  When it's fixed, it prints EXACTLY this:
#
#    RAVENS PER WARDEN
#    Captain Siv (acting)         90
#    Warden Alder Pike            68
#    Warden Corwin Northwind      75
#    Warden Hild Stonebridge      85
#    Warden Nerys Saltmarsh       82
#    Total                       400

import pandas as pd

quests = pd.read_csv("data/quests.csv")
regions = pd.read_csv("data/regions.csv")

merged = quests.merge(regions, on="region", how="left")
merged["warden"].fillna("Captain Siv (acting)")

ravens = merged.groupby("warden")["quest_id"].count()
print("RAVENS PER WARDEN")
for warden, n in ravens.items():
    print(f"{warden:<25}{n:>6}")
print(f"{'Total':<25}{ravens.sum():>6}")
