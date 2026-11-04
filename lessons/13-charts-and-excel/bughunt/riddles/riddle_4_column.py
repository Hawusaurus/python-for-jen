# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 13 · RIDDLE 4: "The Phantom Column"
# ==================================================================
#
#  A column crept in that nobody ordered,
#  a stowaway number where names should have bordered.
#  It shoved every heading one cell to the right:
#  tell pandas to leave its row numbers out of sight.
#
#  Orrin wanted the five highest-level heroes in a workbook, then the
#  first row read back to check it. The check is very confused.
#
#  Run:  python bughunt/riddles/riddle_4_column.py
#  When it's fixed, it prints EXACTLY this:
#
#    Headers: ['name', 'class', 'level']
#    Top hero: Wren Hawkridge, Ranger, level 19

import pandas as pd
from openpyxl import load_workbook
from pathlib import Path

Path("my_work/output").mkdir(parents=True, exist_ok=True)
heroes = pd.read_csv("data/heroes.csv")

top5 = heroes.sort_values("level", ascending=False).head(5)[["name", "class", "level"]]
path = "my_work/output/riddle_4.xlsx"
top5.to_excel(path, sheet_name="Top heroes")

wb = load_workbook(path)
ws = wb["Top heroes"]
print("Headers:", [cell.value for cell in ws[1]])
print(f"Top hero: {ws['A2'].value}, {ws['B2'].value}, level {ws['C2'].value}")
