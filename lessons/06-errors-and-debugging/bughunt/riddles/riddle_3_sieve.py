# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 06 · RIDDLE 3: "The Sieve That Kept Nothing"
# ==================================================================
#
#    My net was wide, it caught it all:
#    the fish, the weed, the boots, the shawl.
#    So when my own mistake swam through,
#    the net just caught that mistake too.
#
#  Pell wants to know how many rewards in this moon's broken copy of
#  the ledger can be read. The page says none of them can.
#
#  Run:  python bughunt/riddles/riddle_3_sieve.py
#  When it's fixed, it prints EXACTLY this:
#
#    Readable rewards: 396
#    Unreadable rewards: 4
import csv

readable = 0
unreadable = 0
with open("data/quests_broken.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        try:
            reward = float(row["Reward"])
        except Exception:
            unreadable += 1
        else:
            readable += 1

print("Readable rewards:", readable)
print("Unreadable rewards:", unreadable)
