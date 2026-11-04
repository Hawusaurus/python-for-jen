# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 10 · RIDDLE 5: "The King's Ransom"
# ==================================================================
#
#  I cut the purses into four and named them, small to grand,
#  but wrote the names in mirror-script, the wrong way round, by hand.
#  Then asked the grid to share things out, but down the columns, not the row:
#  each band should say how often it won, and that is all Siv wants to know.
#
#  Captain Siv's question: do the richest notices come home less often?
#  For each reward band, the share of quests that ended in Success.
#  Two bugs on this page.
#
#  Run:  python bughunt/riddles/riddle_5_ransom.py
#  When it's fixed, it prints EXACTLY this:
#
#    SUCCESS BY REWARD BAND
#    Pittance        73%
#    Fair            67%
#    Handsome        64%
#    King's ransom   54%
#    All quests      65%

import pandas as pd

quests = pd.read_csv("data/quests.csv")

order = ["Pittance", "Fair", "Handsome", "King's ransom"]
quests["band"] = pd.qcut(quests["reward"], 4, labels=["King's ransom", "Handsome", "Fair", "Pittance"])

share = pd.crosstab(quests["band"], quests["outcome"], normalize="columns")
print("SUCCESS BY REWARD BAND")
for band in order:
    print(f"{band:<15} {share.loc[band, 'Success']:.0%}")
print(f"{'All quests':<15} {(quests['outcome'] == 'Success').mean():.0%}")
