# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 08 · RIDDLE 1: "The Middle That Hides"
# ==================================================================
#
#  The column knows its sum, its mean,
#  its smallest coin, its largest sheen.
#  But ask the column for its middle
#  and it shrugs. Ask its maker. That's the riddle.
#
#  Mistress Pell's three-line summary of the Roll. The third line never printed.
#
#  Run:  python bughunt/riddles/riddle_1_median.py
#  When it's fixed, it prints EXACTLY this:
#
#    Subjects on the Roll: 200
#    Average salary: 31999.25
#    Median salary: 29375.0

import csv
import numpy as np

salaries = []
with open("data/thornmere_payroll.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        salaries.append(float(row["annual_salary"]))
salaries = np.array(salaries)

print("Subjects on the Roll:", salaries.size)
print("Average salary:", salaries.mean().round(2))
print("Median salary:", salaries.median())
