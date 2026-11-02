# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 11 · RIDDLE 5: "The Double Portrait"
# ==================================================================
#
#  Two portraits for the Queen: the women first, and then the men.
#  The women's frame came back quite bare; small letters failed again.
#  The men were painted over hers, two crowds upon one wall;
#  a fresh new canvas for each one, and capitals for all.
#
#  Two histograms of hourly rates, one for the women of the realm, one
#  for the men. Two bugs on this page.
#
#  Run:  python bughunt/riddles/riddle_5_portraits.py
#  When it's fixed, it prints EXACTLY this:
#
#    Women: 83
#    Men: 117
#    Bars in women chart: 10
#    Bars in men chart: 10

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

Path("my_work/output").mkdir(parents=True, exist_ok=True)
df = pd.read_csv("data/thornmere_payroll.csv")

df["hourly"] = df["annual_salary"] / 52 / df["weekly_hours"]
women = df.loc[df["gender"] == "f", "hourly"]
men = df.loc[df["gender"] == "M", "hourly"]
print("Women:", len(women))
print("Men:", len(men))

fig, ax = plt.subplots()
ax.hist(women, bins=10)
fig.savefig("my_work/output/riddle5_women.png")
print("Bars in women chart:", len(ax.patches))

ax.hist(men, bins=10)
fig.savefig("my_work/output/riddle5_men.png")
print("Bars in men chart:", len(ax.patches))
