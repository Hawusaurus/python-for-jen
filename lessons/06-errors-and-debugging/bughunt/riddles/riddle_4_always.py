# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 06 · RIDDLE 4: "Always, Always"
# ==================================================================
#
#    One door for luck and one for woe,
#    and one through which all travellers go.
#    I set my count beside the last
#    and counted every soul that passed.
#
#  Lady Siv wants to know how many salaries in the broken scroll are
#  usable. The page says: all of them. It is wrong.
#
#  Run:  python bughunt/riddles/riddle_4_always.py
#  When it's fixed, it prints EXACTLY this:
#
#    Good salaries: 198
#    Bad salaries: 2

import csv

good = 0
bad = 0
with open("data/thornmere_payroll_broken.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        try:
            float(row["annual_salary"])
        except ValueError:
            bad += 1
        finally:
            good += 1

print(f"Good salaries: {good}")
print(f"Bad salaries: {bad}")
