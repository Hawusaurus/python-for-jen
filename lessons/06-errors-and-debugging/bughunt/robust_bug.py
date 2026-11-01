# ==================================================================
#  DAVE'S LEFTOVERS #6: "payroll_total_ROBUST.py"
# ==================================================================
#
# Dave's "robust" version of the payroll total. He added error handling
# in 2019 after the export broke. The export is still broken. So is this.
#
# THREE bugs:
#   one is a SyntaxError in the error handling itself (Python 2 habits),
#   one double-counts money without anyone noticing,
#   one is off by exactly one.
#
# Run it from inside the lesson folder:
#   python bughunt/robust_bug.py
#
# When it's fixed, it prints EXACTLY this:
#
#   Total salary: £6,322,500
#   Skipped 3 rows: EMP1178, EMP1037, EMP1120
#
# Fix ONE bug per commit and explain it in the message.

import csv

total = 0
skipped = 1
skipped_ids = []

with open("data/brightwell_payroll_broken.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        try:
            salary = float(row["annual_salary"])
            hours = float(row["weekly_hours"])
        except ValueError, TypeError:
            skipped += 1
            skipped_ids.append(row["employee_id"])
        total += salary

print(f"Total salary: £{total:,.0f}")
print(f"Skipped {skipped} rows: {', '.join(skipped_ids)}")
