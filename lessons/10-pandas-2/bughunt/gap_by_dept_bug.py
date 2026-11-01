# ==================================================================
#  DAVE'S LEFTOVERS #10: "pivot_magic.py"
# ==================================================================
#
# Found in Dave's locked "Dave working" tab, pasted into a cell as text.
# Mo recovered it. It's meant to be the pay gap by department, with the
# cost centre next to it, for the board pack. It has never produced a
# board pack.
#
# THREE bugs:
#   one crashes (the error mentions a "level name"; think about how groupby wants TWO keys),
#   one quietly loses people (count them: there should be 200),
#   one gets the percentage subtly wrong (compare with your Exercise 3).
#
# Run it from inside the lesson folder:
#   python bughunt/gap_by_dept_bug.py
#
# When it's fixed, it prints EXACTLY this:
#
#   People in report: 200
#   gender          F      M  gap_pct cost_centre
#   department
#   HR          14.17  25.81     45.1      CC-310
#   Warehouse   11.56  18.07     36.0      CC-110
#   IT          17.05  23.86     28.5      CC-400
#   Sales       14.52  19.05     23.8      CC-200
#   Marketing   15.16  19.10     20.6      CC-500
#   Finance     16.72  19.81     15.6      CC-300
#   Production  14.03  15.88     11.6      CC-100
#   Design      17.23  18.91      8.9         NaN
#
# Fix ONE bug per commit and explain it in the message, like a detective:
#   git commit -m "Bug hunt: <what was wrong and why>"

import pandas as pd

pd.set_option("display.width", 120)
df = pd.read_csv("data/brightwell_payroll.csv")
depts = pd.read_csv("data/departments.csv")

df = df.merge(depts, on="department", how="inner")
print("People in report:", len(df))

df["hourly"] = df["annual_salary"] / 52 / df["weekly_hours"]

table = df.groupby("department", "gender")["hourly"].mean().unstack().round(2)
table["gap_pct"] = ((table["M"] - table["F"]) / table["F"] * 100).round(1)

cost_centres = df.groupby("department")["cost_centre"].first()
table["cost_centre"] = cost_centres

print(table.sort_values("gap_pct", ascending=False))
