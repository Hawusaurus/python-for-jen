# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 12 · RIDDLE 5: "The Last Two Lies"
# ==================================================================
#
#  The quarters of the ladder climb by what each hour is worth,
#  not by the year, which part-time hours shrink upon this earth.
#  And when you weigh the bonus gap, weigh only those who got,
#  for half the women's purses hold no coin, and middles count for naught.
#
#  Two figures from the Accord: the share of women in each pay quartile,
#  and the median bonus gap. Two bugs on this page.
#
#  Run:  python bughunt/riddles/riddle_5_last_two.py
#  When it's fixed, it prints EXACTLY this:
#
#    Lower         72% women
#    Lower middle  46% women
#    Upper middle  30% women
#    Upper         18% women
#    Median bonus gap: 30.8%

import pandas as pd

df = pd.read_csv("data/thornmere_payroll.csv")
df["hourly"] = df["annual_salary"] / 52 / df["weekly_hours"]

order = ["Lower", "Lower middle", "Upper middle", "Upper"]
df["quartile"] = pd.qcut(df["annual_salary"], 4, labels=order)
share = pd.crosstab(df["quartile"], df["gender"], normalize="index")
for q in order:
    print(f"{q:<13} {share.loc[q, 'F']:.0%} women")

got = df[df["bonus"] >= 0]
m = got.loc[got["gender"] == "M", "bonus"].median()
f = got.loc[got["gender"] == "F", "bonus"].median()
print(f"Median bonus gap: {(m - f) / m * 100:.1f}%")
