# ==================================================================
#  PAGES FROM THE GRIMOIRE, PAGE 10: "pivot_magic.py"
# ==================================================================
#
# Found in Dalvric's locked "Dalvric working" tab of the Treasury
# workbook, pasted into a cell as text. Orrin recovered it. It's meant
# to be the pay gap by guild, with each guild's vault next to it, for
# the Privy Council. It has never produced anything for the Council.
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
#   gender          F      M  gap_pct    vault
#   department                                
#   Kitchens    14.17  25.81     45.1  VLT-310
#   Harbour     11.56  18.07     36.0  VLT-110
#   Clockworks  17.05  23.86     28.5  VLT-400
#   Guard       14.52  19.05     23.8  VLT-200
#   Library     15.16  19.10     20.6  VLT-500
#   Treasury    16.72  19.81     15.6  VLT-300
#   Forge       14.03  15.88     11.6  VLT-100
#   Apothecary  17.23  18.91      8.9      NaN
#
# Fix ONE bug per commit and explain it in the message, like a detective:
#   git commit -m "Bug hunt: <what was wrong and why>"

import pandas as pd

pd.set_option("display.width", 120)
df = pd.read_csv("data/thornmere_payroll.csv")
guilds = pd.read_csv("data/guilds.csv")

df = df.merge(guilds, on="department", how="inner")
print("People in report:", len(df))

df["hourly"] = df["annual_salary"] / 52 / df["weekly_hours"]

table = df.groupby("department", "gender")["hourly"].mean().unstack().round(2)
table["gap_pct"] = ((table["M"] - table["F"]) / table["F"] * 100).round(1)

vaults = df.groupby("department")["vault"].first()
table["vault"] = vaults

print(table.sort_values("gap_pct", ascending=False))
