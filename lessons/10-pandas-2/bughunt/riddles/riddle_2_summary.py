# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 10 · RIDDLE 2: "The Middle That Wasn't Spelled"
# ==================================================================
#
#  Three things I asked the counting-spell: how many, middle, most.
#  It knew the first, it knew the last; the middle was a ghost.
#  A word misspelled is not a word the Ledger understands;
#  read slowly what the error says, then fix it with your hands.
#
#  Lady Siv wants, for every guild: the headcount, the median salary
#  and the highest salary, as one PivotTable-style summary.
#
#  Run:  python bughunt/riddles/riddle_2_summary.py
#  When it's fixed, it prints EXACTLY this:
#
#    SALARIES BY GUILD (crowns)
#                count  median    max
#    department
#    Apothecary     15   31300  50150
#    Clockworks     20   39925  60800
#    Forge          60   28650  50500
#    Guard          35   28200  61750
#    Harbour        25   28950  47450
#    Kitchens       12   31250  63650
#    Library        15   29000  51600
#    Treasury       18   29275  68750
#
#    Highest median: Clockworks
#    Biggest guild:  Forge

import pandas as pd

pd.set_option("display.width", 120)
df = pd.read_csv("data/thornmere_payroll.csv")

summary = df.groupby("department")["annual_salary"].agg(["count", "medain", "max"])
summary = summary.round(0).astype(int)

print("SALARIES BY GUILD (crowns)")
print(summary.to_string())
print()
print("Highest median:", summary["median"].idxmax())
print("Biggest guild: ", summary["count"].idxmax())
