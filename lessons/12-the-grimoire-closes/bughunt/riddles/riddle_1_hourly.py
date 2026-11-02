# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 12 · RIDDLE 1: "The Missing Letter"
# ==================================================================
#
#  To learn what every hour is worth, divide the year by weeks and hours;
#  but one name lost its final letter, and the Ledger lost its powers.
#  It tells you plainly what it sought and could not find at all;
#  read the column names again, as written on the wall.
#
#  The Accord's first step: every subject's hourly rate, and the mean
#  hourly rate for women and for men.
#
#  Run:  python bughunt/riddles/riddle_1_hourly.py
#  When it's fixed, it prints EXACTLY this:
#
#    HOURLY RATES OF THE REALM
#    Subjects counted: 200
#    Lowest hourly rate:      10.26 cr
#    Highest hourly rate:     35.26 cr
#    Men, mean hourly rate:   18.62 cr
#    Women, mean hourly rate: 14.95 cr

import pandas as pd

df = pd.read_csv("data/thornmere_payroll.csv")
df["hourly"] = df["annual_salary"] / 52 / df["weekly_hour"]

men = df.loc[df["gender"] == "M", "hourly"]
women = df.loc[df["gender"] == "F", "hourly"]
print("HOURLY RATES OF THE REALM")
print("Subjects counted:", len(df))
print(f"Lowest hourly rate:      {df['hourly'].min():.2f} cr")
print(f"Highest hourly rate:     {df['hourly'].max():.2f} cr")
print(f"Men, mean hourly rate:   {men.mean():.2f} cr")
print(f"Women, mean hourly rate: {women.mean():.2f} cr")
