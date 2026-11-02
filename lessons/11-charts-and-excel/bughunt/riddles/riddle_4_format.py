# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 11 · RIDDLE 4: "The Wrong Column Dressed"
# ==================================================================
#
#  I dressed the crowns in finest form, with commas and with "cr",
#  but put the robes on someone else: the guild names, near and far.
#  The salaries stand plain and bare, the names wear money's coat;
#  count the columns, A, B, C, and check which one I wrote.
#
#  The Roll sheet: five subjects, their guild and their salary, the
#  salaries formatted as crowns.
#
#  Run:  python bughunt/riddles/riddle_4_format.py
#  When it's fixed, it prints EXACTLY this:
#
#    C1: annual_salary
#    C2 format: #,##0 "cr"
#    B2 format: General

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

Path("my_work/output").mkdir(parents=True, exist_ok=True)
df = pd.read_csv("data/thornmere_payroll.csv")
from openpyxl import load_workbook

path = "my_work/output/riddle4_roll.xlsx"
roll = df[["employee_id", "department", "annual_salary"]].head(5)
roll.to_excel(path, sheet_name="Roll", index=False)

wb = load_workbook(path)
ws = wb["Roll"]
for cell in ws["B"][1:]:
    cell.number_format = '#,##0 "cr"'
wb.save(path)

ws = load_workbook(path)["Roll"]
print("C1:", ws["C1"].value)
print("C2 format:", ws["C2"].number_format)
print("B2 format:", ws["B2"].number_format)
