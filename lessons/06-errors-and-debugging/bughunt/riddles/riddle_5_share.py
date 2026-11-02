# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 06 · RIDDLE 5: "A Day of Nothing"
# ==================================================================
#
#    A quest that took no days at all
#    divides the world and makes it fall;
#    and when you share among the few,
#    don't count the ones who never knew.
#
#  The Queen asked for the average reward per day on the road, from
#  this moon's broken ledger. It crashes, and once it doesn't, the
#  average is too low. (Two bugs.)
#
#  Run:  python bughunt/riddles/riddle_5_share.py
#  When it's fixed, it prints EXACTLY this:
#
#    Quests in the ledger: 400
#    Usable: 395
#    Average reward per day: 74.30 cr
import csv

per_day = []
rows = 0
with open("data/quests_broken.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        rows += 1
        try:
            per_day.append(float(row["reward"]) / float(row["days"]))
        except (ValueError, TypeError):
            pass

print("Quests in the ledger:", rows)
print("Usable:", len(per_day))
print(f"Average reward per day: {sum(per_day) / rows:.2f} cr")
