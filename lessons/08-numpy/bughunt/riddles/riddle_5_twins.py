# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 08 · RIDDLE 5: "Two Names, One Purse"
# ==================================================================
#
#  Two names, one purse: I raised the second
#  and found the first had changed, unreckoned.
#  Then lifted all the low to a floor,
#  but built a lid and not a door.
#
#  The Queen's 3 % raise, and a top-up so that nobody earns under 13.5 cr an
#  hour. TWO bugs this time, and neither one crashes.
#
#  Run:  python bughunt/riddles/riddle_5_twins.py
#  When it's fixed, it prints EXACTLY this:
#
#    Wage bill before the raise: 6399850.0
#    Wage bill after the raise: 6591845.5
#    Below 13.5 cr/h before the top-up: 46
#    Lowest hourly rate after the top-up: 13.5

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

raised = salaries
raised *= 1.03
print("Wage bill before the raise:", salaries.sum().round(2))
print("Wage bill after the raise:", raised.sum().round(2))

hourly = raised / 52 / hours
topped_up = np.minimum(hourly, 13.5)
print("Below 13.5 cr/h before the top-up:", (hourly < 13.5).sum())
print("Lowest hourly rate after the top-up:", topped_up.min().round(2))
