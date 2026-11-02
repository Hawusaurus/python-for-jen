# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 11 · RIDDLE 3: "The Book That Kept One Page"
# ==================================================================
#
#  Two pages for the Council's book: by guild, and then by town.
#  I wrote the first, then wrote the second, and the first fell down.
#  Each time I wrote, I bound a fresh new book and threw the old;
#  to keep both pages, write them both inside one binding's hold.
#
#  Mistress Pell's Council workbook: the pay bill by guild on one sheet,
#  by town on another.
#
#  Run:  python bughunt/riddles/riddle_3_sheets.py
#  When it's fixed, it prints EXACTLY this:
#
#    Sheets: ['By guild', 'By town']
#    Saved my_work/output/riddle3_council.xlsx

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

Path("my_work/output").mkdir(parents=True, exist_ok=True)
df = pd.read_csv("data/thornmere_payroll.csv")
from openpyxl import load_workbook

path = "my_work/output/riddle3_council.xlsx"
by_guild = df.groupby("department")["annual_salary"].sum().reset_index()
by_town = df.groupby("location")["annual_salary"].sum().reset_index()

by_guild.to_excel(path, sheet_name="By guild", index=False)
by_town.to_excel(path, sheet_name="By town", index=False)

wb = load_workbook(path)
print("Sheets:", wb.sheetnames)
print("Saved", path)
