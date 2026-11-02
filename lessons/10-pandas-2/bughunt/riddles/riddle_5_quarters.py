# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 10 · RIDDLE 5: "The Mirror of Quarters"
# ==================================================================
#
#  Four rooms I built from low to high and labelled every door,
#  but read the labels back to front: the top became the floor.
#  Then counting who stood in each room, I turned the sums askew:
#  I shared them out across the rooms, not each room through and through.
#
#  Lady Siv's pay quartiles: what share of each quarter of the hourly
#  pay ladder is women. Two bugs on this page.
#
#  Run:  python bughunt/riddles/riddle_5_quarters.py
#  When it's fixed, it prints EXACTLY this:
#
#    WOMEN IN EACH PAY QUARTILE (hourly)
#    Lower         72% women
#    Lower middle  46% women
#    Upper middle  30% women
#    Upper         18% women
#    Whole realm   42% women

import pandas as pd

df = pd.read_csv("data/thornmere_payroll.csv")
df["hourly"] = df["annual_salary"] / 52 / df["weekly_hours"]

order = ["Lower", "Lower middle", "Upper middle", "Upper"]
df["quartile"] = pd.qcut(df["hourly"], 4, labels=["Upper", "Upper middle", "Lower middle", "Lower"])

share = pd.crosstab(df["quartile"], df["gender"], normalize="columns")
print("WOMEN IN EACH PAY QUARTILE (hourly)")
for q in order:
    print(f"{q:<13} {share.loc[q, 'F']:.0%} women")
print(f"{'Whole realm':<13} {(df['gender'] == 'F').mean():.0%} women")
