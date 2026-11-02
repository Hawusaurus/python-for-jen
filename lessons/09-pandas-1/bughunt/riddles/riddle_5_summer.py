# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 09 · RIDDLE 5: "The Summer That Came Late"
# ==================================================================
#
#  Text compares by letters, so
#  a month needs both its digits shown;
#  and one line asks the whole great ledger
#  what summer should have said alone.
#
#  Queen Aldara wants a word on last summer (June to August 2025). Dalvric's
#  answer came back too short, and somehow too good. Two bugs.
#
#  Run:  python bughunt/riddles/riddle_5_summer.py
#  When it's fixed, it prints EXACTLY this:
#
#    Quests posted in summer 2025: 51
#    Won: 35
#    Crowns paid: 16620
#    Best crowns per quest-day: 123.0
#    Monsters met: 7

import pandas as pd

df = pd.read_csv("data/quests.csv")

summer = df[df["posted"] >= "2025-6-01"]
summer = summer[summer["posted"] <= "2025-08-31"]
won = summer[summer["outcome"] == "Success"]

print("Quests posted in summer 2025:", len(summer))
print("Won:", len(won))
print("Crowns paid:", summer["paid"].sum())
print("Best crowns per quest-day:", round((df["paid"] / df["days"]).max(), 2))
print("Monsters met:", summer["monster"].nunique())
