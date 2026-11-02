# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 09 · RIDDLE 2: "The Tangled Filter"
# ==================================================================
#
#  Two questions joined by one small "&";
#  but "&" grabs first, before you planned.
#  Wrap each question in its shell
#  and the filter answers well.
#
#  Lady Siv's AutoFilter: part-timers in the Guard, by name.
#
#  Run:  python bughunt/riddles/riddle_2_tangle.py
#  When it's fixed, it prints EXACTLY this:
#
#    Guards in total: 35
#    Part-time guards: 6
#    Their average hours: 25.62
#    first_name   last_name  weekly_hours
#          Rafe    Kettleby         22.50
#          Thea     Dunmore         18.75
#         Cerys  Quickwater         30.00
#       Leofric   Saltmarsh         30.00
#          Jory    Woolpack         22.50
#        Hamish Fairweather         30.00

import pandas as pd
pd.set_option("display.width", 120)
df = pd.read_csv("data/thornmere_payroll.csv")

guards = df[df["department"] == "Guard"]
print("Guards in total:", len(guards))
part_guard = df[df["department"] == "Guard" & df["weekly_hours"] < 37.5]
print("Part-time guards:", len(part_guard))
print("Their average hours:", part_guard["weekly_hours"].mean().round(2))
print(part_guard[["first_name", "last_name", "weekly_hours"]].to_string(index=False))
