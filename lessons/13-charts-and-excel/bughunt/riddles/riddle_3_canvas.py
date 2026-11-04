# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 13 · RIDDLE 3: "One Canvas, Two Paintings"
# ==================================================================
#
#  The first picture was finished and hung on the wall,
#  the second was painted on top of it all.
#  Eight monsters, five regions, all tangled as one:
#  begin a fresh canvas before you've begun.
#
#  Captain Siv asked for two pictures: quests per monster and quests
#  per region. The second one came back looking oddly crowded.
#
#  Run:  python bughunt/riddles/riddle_3_canvas.py
#  When it's fixed, it prints EXACTLY this:
#
#    Monster chart: 8 bars
#    Region chart: 5 bars

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

Path("my_work/output").mkdir(parents=True, exist_ok=True)
quests = pd.read_csv("data/quests.csv")

monsters = quests["monster"].value_counts()
plt.figure(figsize=(8, 4))
plt.bar(monsters.index, monsters.values)
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("my_work/output/riddle_3_monsters.png")
print("Monster chart:", len(plt.gca().patches), "bars")

regions = quests["region"].value_counts()
plt.bar(regions.index, regions.values)
plt.tight_layout()
plt.savefig("my_work/output/riddle_3_regions.png")
print("Region chart:", len(plt.gca().patches), "bars")
