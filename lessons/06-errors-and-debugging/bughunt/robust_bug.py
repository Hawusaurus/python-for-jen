# ==================================================================
#  PAGES FROM THE GRIMOIRE, PAGE 6: "roll_total_ROBUST.py"
# ==================================================================
#
# Dalvric's "robust" version of the Roll total. He added the warding
# spells after the Scriptorium's copy broke one full moon. The copy is
# still broken. So is this.
#
# THREE bugs:
#   one is a SyntaxError in the error handling itself (an old incantation),
#   one double-counts crowns without anyone noticing,
#   one is off by exactly one.
#
# Run it from inside the lesson folder:
#   python bughunt/robust_bug.py
#
# When it's fixed, it prints EXACTLY this:
#
#   Total salary: 6,322,500 cr
#   Skipped 3 rows: TM1178, TM1037, TM1120
#
# Fix ONE bug per commit and explain it in the message.

import csv

total = 0
skipped = 1
skipped_ids = []

with open("data/thornmere_payroll_broken.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        try:
            salary = float(row["annual_salary"])
            hours = float(row["weekly_hours"])
        except ValueError, TypeError:
            skipped += 1
            skipped_ids.append(row["employee_id"])
        total += salary

print(f"Total salary: {total:,.0f} cr")
print(f"Skipped {skipped} rows: {', '.join(skipped_ids)}")
