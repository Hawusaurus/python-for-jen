# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 09 · RIDDLE 4: "The Uninvited Column"
# ==================================================================
#
#  I sent a copy to the scribe,
#  who added numbers to the tribe:
#  a column no one ever named.
#  The row labels are to be blamed.
#
#  Westmarch's roll, saved for the Scriptorium as my_work/riddle_westmarch.csv
#  and read back in to check it.
#
#  Run:  python bughunt/riddles/riddle_4_unnamed.py
#  When it's fixed, it prints EXACTLY this:
#
#    Columns in the copy: ['employee_id', 'first_name', 'annual_salary']
#    Rows in the copy: 67
#    Westmarch pay bill: 2233000
#    First in the copy: Nell

import pandas as pd
pd.set_option("display.width", 120)
df = pd.read_csv("data/thornmere_payroll.csv")

westmarch = df[df["location"] == "Westmarch"][["employee_id", "first_name", "annual_salary"]]
westmarch.to_csv("my_work/riddle_westmarch.csv")
back = pd.read_csv("my_work/riddle_westmarch.csv")
print("Columns in the copy:", list(back.columns))
print("Rows in the copy:", len(back))
print("Westmarch pay bill:", back["annual_salary"].sum())
print("First in the copy:", back.iloc[0]["first_name"])
