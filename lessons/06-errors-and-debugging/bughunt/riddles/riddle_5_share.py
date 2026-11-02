# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 06 · RIDDLE 5: "The Empty Hour"
# ==================================================================
#
#    When hours are none, the sum will break,
#    so ward that door for safety's sake.
#    And when you share the pot around,
#    share only with the ones you found.
#
#  The average hourly rate across the broken scroll. It crashes on
#  one row, and when it doesn't, it's too low. (Two bugs.)
#
#  Run:  python bughunt/riddles/riddle_5_share.py
#  When it's fixed, it prints EXACTLY this:
#
#    Usable rows: 196 of 200
#    Average hourly rate: 17.12 cr

import csv


def hourly(row):
    salary = float(row["annual_salary"])
    hours = float(row["weekly_hours"])
    return salary / 52 / hours


rates = []
rows = 0
with open("data/thornmere_payroll_broken.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        rows += 1
        try:
            rates.append(hourly(row))
        except ValueError:
            pass

average = sum(rates) / rows
print(f"Usable rows: {len(rates)} of {rows}")
print(f"Average hourly rate: {average:.2f} cr")
