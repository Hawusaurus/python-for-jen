# ==================================================================
#  PAGES FROM THE GRIMOIRE, PAGE 6: "ledger_total_ROBUST.py"
# ==================================================================
#
# Dalvric's "robust" total of every reward on the guild ledger. He
# added the warding spells after the Scriptorium's copy broke one
# full moon. The copy is still broken. So is this.
#
# THREE bugs:
#   one crashes inside the error handling itself (a misspelt ward),
#   one double-counts crowns without anyone noticing,
#   one is off by exactly one.
#
# Run it from inside the lesson folder:
#   python bughunt/robust_bug.py
#
# When it's fixed, it prints EXACTLY this:
#
#   Total of all rewards: 233,490 cr
#   Skipped 4 rows: Q0005, Q0018, Q0092, Q0121
#
# Fix ONE bug per commit and explain it in the message.

import csv

total = 0
skipped = 1
skipped_ids = []

with open("data/quests_broken.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        try:
            reward = float(row["reward"])
        except (ValueError, TypError):
            skipped += 1
            skipped_ids.append(row["quest_id"])
        total += reward

print(f"Total of all rewards: {total:,.0f} cr")
print(f"Skipped {skipped} rows: {', '.join(skipped_ids)}")
