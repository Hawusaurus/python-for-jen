# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 09 · RIDDLE 5: "The Raise That Never Came"
# ==================================================================
#
#  I gave the Guard a thousand more,
#  but only to a copied store;
#  the Roll itself stayed as it stood.
#  And then I counted guilds. Not good.
#
#  The Queen grants every guard 1,000 crowns more, and asks how many guilds have
#  part-timers. TWO bugs this time. Python may mutter a warning; read it.
#
#  Run:  python bughunt/riddles/riddle_5_raise.py
#  When it's fixed, it prints EXACTLY this:
#
#    Guard pay bill before: 1129250
#    Guard pay bill after:  1164250
#    Part-timers: 26
#    Guilds with part-timers: 8

import pandas as pd
pd.set_option("display.width", 120)
df = pd.read_csv("data/thornmere_payroll.csv")

guard = df["department"] == "Guard"
print("Guard pay bill before:", df.loc[guard, "annual_salary"].sum())
df[guard]["annual_salary"] = df["annual_salary"] + 1000
print("Guard pay bill after: ", df.loc[guard, "annual_salary"].sum())

part = df[df["weekly_hours"] < 37.5]
print("Part-timers:", len(part))
print("Guilds with part-timers:", part["department"].count())
