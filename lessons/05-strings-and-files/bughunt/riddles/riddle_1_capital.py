# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 05 · RIDDLE 1: "The Capital Mistake"
# ==================================================================
#
#    I called the column by its name,
#    but dressed it up in grander frame:
#    a capital it never wore,
#    so Python shut and barred the door.
#
#  Captain Siv wants to know how often the guild has gone after
#  trolls, and what it was paid for the trouble.
#
#  Run:  python bughunt/riddles/riddle_1_capital.py
#  When it's fixed, it prints EXACTLY this:
#
#    Troll quests: 31
#    Paid for trolls: 20,870 cr
import csv

count = 0
paid = 0
with open("data/quests.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        if row["Monster"] == "Trolls":
            count += 1
            paid += int(row["paid"])

print("Troll quests:", count)
print(f"Paid for trolls: {paid:,} cr")
