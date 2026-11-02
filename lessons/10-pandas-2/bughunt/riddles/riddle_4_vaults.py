# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 10 · RIDDLE 4: "The Fill That Faded"
# ==================================================================
#
#  I wrote the missing vault in ink and saw the gap made whole,
#  but when I looked a moment on, the blank was back, the hole.
#  A change that's not kept anywhere is just a passing thought;
#  the column never heard of it, and so the fix was naught.
#
#  Orrin's table of guilds, their headcount and their vault. A guild with
#  no vault on record should show VLT-999, not a blank.
#
#  Run:  python bughunt/riddles/riddle_4_vaults.py
#  When it's fixed, it prints EXACTLY this:
#
#    GUILDS AND THEIR VAULTS
#    department  headcount   vault
#    Apothecary         15 VLT-999
#    Clockworks         20 VLT-400
#         Forge         60 VLT-100
#         Guard         35 VLT-200
#       Harbour         25 VLT-110
#      Kitchens         12 VLT-310
#       Library         15 VLT-500
#      Treasury         18 VLT-300
#    Guilds without a vault on record: 1

import pandas as pd

df = pd.read_csv("data/thornmere_payroll.csv")
guilds = pd.read_csv("data/guilds.csv")

counts = df["department"].value_counts().rename("headcount").reset_index()
table = counts.merge(guilds[["department", "vault"]], on="department", how="left")
table["vault"].fillna("VLT-999")

print("GUILDS AND THEIR VAULTS")
print(table.sort_values("department").to_string(index=False))
missing = (table["vault"] == "VLT-999").sum()
print("Guilds without a vault on record:", missing)
