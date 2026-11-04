# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 08 · RIDDLE 1: "The Name Called Too Tall"
# ==================================================================
#
#  The ledger's header, read it slow:
#  its names are written small and low.
#  You knocked and called a name too tall;
#  no such key hangs on the wall.
#
#  The Quartermistress wants to know how long the guild spends on the road,
#  and how many heroes come home with a bandage.
#
#  Run:  python bughunt/riddles/riddle_1_column.py
#  When it's fixed, it prints EXACTLY this:
#
#    Quests in the ledger: 400
#    Days on the road: 3109
#    Longest quest: 14 days
#    Injuries: 277
#    Quests without a scratch: 212

import csv
import numpy as np

days = []
injuries = []
with open("data/quests.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        days.append(int(row["Days"]))
        injuries.append(int(row["injuries"]))

days = np.array(days)
injuries = np.array(injuries)
print("Quests in the ledger:", len(days))
print("Days on the road:", days.sum())
print("Longest quest:", days.max(), "days")
print("Injuries:", injuries.sum())
print("Quests without a scratch:", (injuries == 0).sum())
