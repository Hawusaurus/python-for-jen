# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 06 · RIDDLE 2: "The Wrong Ward"
# ==================================================================
#
#    I warded the door against the thief,
#    but in came the flood and drowned my sheaf.
#    A ward is cast for one foe's name;
#    see who is knocking, then do the same.
#
#  Orrin's check of the weekly hours in the broken scroll. It should
#  name the bad row and count the good ones.
#
#  Run:  python bughunt/riddles/riddle_2_ward.py
#  When it's fixed, it prints EXACTLY this:
#
#    Bad hours for TM1120
#    Rows with good hours: 199

import csv

good = 0
with open("data/thornmere_payroll_broken.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        try:
            float(row["weekly_hours"])
            good += 1
        except TypeError:
            print("Bad hours for", row["employee_id"])

print("Rows with good hours:", good)
