# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 08 · RIDDLE 4: "Down Instead of Along"
# ==================================================================
#
#  Down the columns, along the rows:
#  which way the summing river flows?
#  I added quarters, called them guilds,
#  and zip said nothing, as zip wills.
#
#  Orrin's bonus table: three guilds, four quarters. He wants one total per guild.
#
#  Run:  python bughunt/riddles/riddle_4_axis.py
#  When it's fixed, it prints EXACTLY this:
#
#    Bonus table: 3 guilds, 4 quarters
#    Forge     5,700 cr
#    Guard     4,200 cr
#    Library   2,450 cr
#    Realm    12,350 cr

import numpy as np

guilds = ["Forge", "Guard", "Library"]
bonus = np.array([[1200, 900, 1500, 2100],
                  [800, 1100, 700, 1600],
                  [400, 650, 500, 900]])

print("Bonus table:", bonus.shape[0], "guilds,", bonus.shape[1], "quarters")
per_guild = bonus.sum(axis=0)
for guild, total in zip(guilds, per_guild):
    print(f"{guild:<8}{total:>7,} cr")
print(f"{'Realm':<8}{bonus.sum():>7,} cr")
