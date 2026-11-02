# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 09 · RIDDLE 3: "The Sort That Didn't Stick"
# ==================================================================
#
#  You sorted well, then let it go:
#  the tidy copy blew away.
#  The ledger you print is the one you kept,
#  still in the order of yesterday.
#
#  The Quartermistress wants the five newest members of the guild for the
#  welcome dinner. Biscuit is doing the seating plan.
#
#  Run:  python bughunt/riddles/riddle_3_sort.py
#  When it's fixed, it prints EXACTLY this:
#
#    Newest members of the guild:
#                       name    class      joined
#    76    Jasper Longstride  Warrior  2023-11-16
#    119        Jory Redfern     Bard  2023-11-02
#    25      Edric Marchbank  Warrior  2023-10-12
#    10   Kellan Nightingale   Ranger  2023-10-08
#    50      Doran Mossgrove   Ranger  2023-05-28
#
#    Classes at the welcome dinner: Warrior, Bard, Warrior, Ranger, Ranger
#    Joined most recently: Jasper Longstride

import pandas as pd

pd.set_option("display.width", 120)
heroes = pd.read_csv("data/heroes.csv")

heroes.sort_values("joined", ascending=False)
newest = heroes.head(5)
print("Newest members of the guild:")
print(newest[["name", "class", "joined"]])
print()
print("Classes at the welcome dinner:", ", ".join(newest["class"]))
print("Joined most recently:", newest["name"].tolist()[0])
