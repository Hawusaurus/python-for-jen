# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 09 · RIDDLE 1: "The Wrong Hands"
# ==================================================================
#
#  Some things you open, some you call;
#  I used the wrong hands, that is all.
#  The error grumbles, short and terse:
#  read its last line. Then read this verse.
#
#  Mistress Pell wants a peek at the first three rows of the Roll.
#
#  Run:  python bughunt/riddles/riddle_1_head.py
#  When it's fixed, it prints EXACTLY this:
#
#    Rows: 200
#    Columns: 12
#    Guilds: 8
#      employee_id first_name department
#    0      TM1092        Nye      Guard
#    1      TM1178       Hild    Library
#    2      TM1105      Maren      Guard
#
#        employee_id first_name department
#    198      TM1118     Gideon      Guard
#    199      TM1077       Wren    Harbour

import pandas as pd
pd.set_option("display.width", 120)
df = pd.read_csv("data/thornmere_payroll.csv")

print("Rows:", len(df))
print("Columns:", len(df.columns))
print("Guilds:", df["department"].nunique())
print(df.head[3][["employee_id", "first_name", "department"]])
print()
print(df.tail(2)[["employee_id", "first_name", "department"]])
