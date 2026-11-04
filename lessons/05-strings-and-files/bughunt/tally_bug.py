# ==================================================================
#  PAGES FROM THE GRIMOIRE, PAGE 5: "moon_tally_DO_NOT_TOUCH.py"
# ==================================================================
#
# Dalvric's monthly tally of the guild ledger. Quartermistress Pell
# says it "worked in his tower". It has never once worked in hers.
#
# THREE bugs:
#   one crashes before a single row is read,
#   one gives a wrong count without crashing,
#   one quietly loses the pennies.
#
# Run it from inside the lesson folder:
#   python bughunt/tally_bug.py
#
# When it's fixed, it prints EXACTLY this:
#
#   Quests: 400
#   Deadly (difficulty 5): 40
#   Total paid: 146,150 cr
#   Average paid: 365.38 cr
#
# Fix ONE bug per commit and explain it in the message:
#   git commit -m "Bug hunt: <what was wrong and why>"
import csv

count = 0
deadly = 0
total = 0

with open("data/quests.cvs", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        count += 1
        if row["difficulty"] == 5:
            deadly += 1
        total += int(row["paid"])

average = total // count

print("Quests:", count)
print("Deadly (difficulty 5):", deadly)
print(f"Total paid: {total:,} cr")
print(f"Average paid: {average:,.2f} cr")
