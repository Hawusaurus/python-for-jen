# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 09 · RIDDLE 3: "The Sort That Forgot"
# ==================================================================
#
#  I sorted the Guard from rich to poor,
#  then read the list I had before.
#  The sorted copy, shining new,
#  was never kept, and slipped from view.
#
#  The Queen wants the three best-paid members of the Guard.
#
#  Run:  python bughunt/riddles/riddle_3_sort.py
#  When it's fixed, it prints EXACTLY this:
#
#    Guards: 35
#    Guard pay bill: 1129250
#    Best paid in the Guard:
#    first_name  last_name  annual_salary
#         Silas Pennyworth          61750
#       Benedek  Northwind          50800
#           Wyn     Yarrow          49000

import pandas as pd
pd.set_option("display.width", 120)
df = pd.read_csv("data/thornmere_payroll.csv")

guard = df[df["department"] == "Guard"]
print("Guards:", len(guard))
print("Guard pay bill:", guard["annual_salary"].sum())
guard.sort_values("annual_salary", ascending=False)
top = guard.head(3)
print("Best paid in the Guard:")
print(top[["first_name", "last_name", "annual_salary"]].to_string(index=False))
