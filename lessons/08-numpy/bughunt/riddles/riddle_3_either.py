# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 08 · RIDDLE 3: "The Wider Gate"
# ==================================================================
#
#  I asked for guards who work part time
#  and got half the realm. Was that a crime?
#  One stroke means "or", the other "and";
#  the Grimoire chose the wider band.
#
#  Lady Siv wants the part-timers IN the Guard: how many, and what they earn.
#
#  Run:  python bughunt/riddles/riddle_3_either.py
#  When it's fixed, it prints EXACTLY this:
#
#    Part-time guards: 6
#    Their average salary: 17966.67

import csv
import numpy as np

salaries = []
hours = []
departments = []
with open("data/thornmere_payroll.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        salaries.append(float(row["annual_salary"]))
        hours.append(float(row["weekly_hours"]))
        departments.append(row["department"])
salaries = np.array(salaries)
hours = np.array(hours)
departments = np.array(departments)

part_guard = (departments == "Guard") | (hours < 37.5)
print("Part-time guards:", part_guard.sum())
print("Their average salary:", salaries[part_guard].mean().round(2))
