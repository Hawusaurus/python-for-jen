# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 12 · RIDDLE 3: "The Mirror Gap"
# ==================================================================
#
#  The men earn more per hour, they say, and yet my sum says no:
#  a gap that sinks below the floor, with women high, men low.
#  The Accord subtracts in one direction, and it starts from the men;
#  turn the subtraction back around and count it all again.
#
#  The Accord's first figure: the mean hourly pay gap, and which way it
#  points.
#
#  Run:  python bughunt/riddles/riddle_3_sign.py
#  When it's fixed, it prints EXACTLY this:
#
#    Mean hourly gap: 19.7%
#    Men are paid more per hour, on average.

import pandas as pd

df = pd.read_csv("data/thornmere_payroll.csv")
df["hourly"] = df["annual_salary"] / 52 / df["weekly_hours"]
men = df.loc[df["gender"] == "M", "hourly"]
women = df.loc[df["gender"] == "F", "hourly"]

gap = (women.mean() - men.mean()) / men.mean() * 100
print(f"Mean hourly gap: {gap:.1f}%")
if gap > 0:
    print("Men are paid more per hour, on average.")
else:
    print("Women are paid more per hour, on average.")
