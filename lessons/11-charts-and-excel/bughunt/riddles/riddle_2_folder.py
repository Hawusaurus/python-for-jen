# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 11 · RIDDLE 2: "The Road to Nowhere"
# ==================================================================
#
#  I built a house called output and I swept its floor with care,
#  then sent the painting somewhere else: a house that isn't there.
#  The error names the road it tried; compare it, letter, line,
#  with the road the house was built on, and the picture will be fine.
#
#  A histogram of hourly rates for the Council pack: ten bins, saved
#  next to the other charts.
#
#  Run:  python bughunt/riddles/riddle_2_folder.py
#  When it's fixed, it prints EXACTLY this:
#
#    Bins: 10
#    Saved my_work/output/riddle2_hourly.png

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

Path("my_work/output").mkdir(parents=True, exist_ok=True)
df = pd.read_csv("data/thornmere_payroll.csv")

df["hourly"] = df["annual_salary"] / 52 / df["weekly_hours"]
path = "my_work/ouptut/riddle2_hourly.png"

fig, ax = plt.subplots(figsize=(8, 4))
ax.hist(df["hourly"], bins=10)
ax.set_title("Hourly rate, crowns")
fig.savefig(path)

print("Bins:", len(ax.patches))
print("Saved", path)
