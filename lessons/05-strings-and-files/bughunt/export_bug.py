# ==================================================================
#  PAGES FROM THE GRIMOIRE, PAGE 5: "roll_stats_WORKING.py"
# ==================================================================
#
# Dalvric's monthly tally of the Roll of the Realm. Mistress Pell says it
# "worked in his tower". It has never worked anywhere else.
#
# THREE bugs:
#   one crashes before it reads a single row (read the error!),
#   one gives a wrong count without crashing,
#   one loses the pennies. Compare the last line letter by letter.
#
# Run it from inside the lesson folder:
#   python bughunt/export_bug.py
#
# When it's fixed, it prints EXACTLY this:
#
#   Subjects: 200
#   Full-time: 174
#   Total salary: 6,399,850 cr
#   Average salary: 31,999.25 cr
#
# Fix ONE bug per commit and explain it in the message.

import csv

count = 0
full_time = 0
total = 0

with open("data/thornmere_payroll.cvs", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        count += 1
        total += int(row["annual_salary"])
        if row["weekly_hours"] == 37.5:
            full_time += 1

average = total // count

print(f"Subjects: {count}")
print(f"Full-time: {full_time}")
print(f"Total salary: {total:,} cr")
print(f"Average salary: {average:,.2f} cr")
