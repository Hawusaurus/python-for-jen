# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 09 · RIDDLE 1: "Four Names, One Pair of Hands"
# ==================================================================
#
#  You asked the ledger for four at once
#  but gave it just one pair of hands.
#  A list of names wants its own brackets,
#  or the table never understands.
#
#  Captain Siv wants every Wyrm quest on one page: where, how much,
#  and how it ended. (Badly, mostly.)
#
#  Run:  python bughunt/riddles/riddle_1_brackets.py
#  When it's fixed, it prints EXACTLY this:
#
#    Wyrm quests: 7
#        quest_id          region  reward outcome
#    14     Q0015  Northern Wilds    4540  Failed
#    24     Q0025       Thornwood    2420    Fled
#    48     Q0049       Saltmarsh    2960    Fled
#    162    Q0163       Ironhills    3420  Failed
#    164    Q0165         Greyfen    2510    Fled
#    340    Q0341       Thornwood    2530  Failed
#    345    Q0346       Ironhills    3530  Failed
#    Wyrm rewards altogether: 21910
#    Crowns actually paid: 1970
#    Heroes sent: 35
#    Heroes injured: 14

import pandas as pd

pd.set_option("display.width", 120)
df = pd.read_csv("data/quests.csv")

wyrm = df[df["monster"] == "Wyrm"]
print("Wyrm quests:", len(wyrm))
print(wyrm["quest_id", "region", "reward", "outcome"])
print("Wyrm rewards altogether:", wyrm["reward"].sum())
print("Crowns actually paid:", wyrm["paid"].sum())
print("Heroes sent:", wyrm["party_size"].sum())
print("Heroes injured:", wyrm["injuries"].sum())
