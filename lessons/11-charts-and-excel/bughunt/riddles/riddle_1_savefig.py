# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 11 · RIDDLE 1: "The Painter's Misspoken Word"
# ==================================================================
#
#  The painter drew eight handsome bars and reached to save the frame,
#  but called upon a word with one extra stroke inside its name.
#  The canvas knows no such command and says so, loud and clear;
#  look up what it really knows: the answer's very near.
#
#  Orrin's chart of how many subjects serve in each guild, for the
#  Council pack.
#
#  Run:  python bughunt/riddles/riddle_1_savefig.py
#  When it's fixed, it prints EXACTLY this:
#
#    Bars drawn: 8
#    Saved my_work/output/riddle1_guilds.png

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

Path("my_work/output").mkdir(parents=True, exist_ok=True)
df = pd.read_csv("data/thornmere_payroll.csv")

counts = df["department"].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(counts.index, counts.values)
ax.set_title("Subjects per guild")
fig.save_fig("my_work/output/riddle1_guilds.png")

print("Bars drawn:", len(ax.patches))
print("Saved my_work/output/riddle1_guilds.png")
