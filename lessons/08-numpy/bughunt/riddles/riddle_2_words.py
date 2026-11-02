# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 08 · RIDDLE 2: "Coins That Were Words"
# ==================================================================
#
#  I read the scroll and kept each line
#  exactly as the scribe's design.
#  "41900": a word, not gold.
#  You cannot halve a word, I'm told.
#
#  Dalvric's monthly wage bill. It should divide every salary by 12.
#
#  Run:  python bughunt/riddles/riddle_2_words.py
#  When it's fixed, it prints EXACTLY this:
#
#    First three monthly salaries: [3491.67 2212.5  2079.17]
#    Monthly wage bill: 533320.83

import csv
import numpy as np

salaries = []
with open("data/thornmere_payroll.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        salaries.append(row["annual_salary"])
salaries = np.array(salaries)

monthly = salaries / 12
print("First three monthly salaries:", monthly[:3].round(2))
print("Monthly wage bill:", monthly.sum().round(2))
