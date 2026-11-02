# Lesson 11 demo: run it from the lesson folder with  python demo.py
# Writes pictures and workbooks into demo_output/. Open them as you go.

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill
from pathlib import Path

Path("demo_output").mkdir(exist_ok=True)
df = pd.read_csv("data/thornmere_payroll.csv")

print("--- 1. Bar chart: a chart is a file ---")
counts = df["department"].value_counts()
plt.figure(figsize=(8, 4))
plt.bar(counts.index, counts.values, color="#1f3a5f")
plt.title("Headcount by guild")
plt.ylabel("Subjects of the realm")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()            # <- delete this line once and look at the result
plt.savefig("demo_output/headcount.png", dpi=150)
print("wrote demo_output/headcount.png")

print("\n--- 2. Histogram: where do the salaries sit? ---")
median = df["annual_salary"].median()
plt.figure(figsize=(8, 4))
plt.hist(df["annual_salary"], bins=12, color="#e8a33d", edgecolor="white")
plt.axvline(median, color="#1f3a5f", linestyle="--", label=f"Median {median:,.0f} cr")
plt.legend()
plt.title("Annual salaries (crowns)")
plt.tight_layout()
plt.savefig("demo_output/salaries.png", dpi=150)
print("wrote demo_output/salaries.png")

print("\n--- 3. Two series side by side ---")
table = df.pivot_table(values="annual_salary", index="department",
                       columns="gender", aggfunc="mean").round(0)
print(table)
x = np.arange(len(table.index))
plt.figure(figsize=(9, 4.5))
plt.bar(x - 0.2, table["F"], 0.4, label="Women", color="#e8a33d")
plt.bar(x + 0.2, table["M"], 0.4, label="Men", color="#1f3a5f")
plt.xticks(x, table.index, rotation=30, ha="right")
plt.ylabel("Average salary (cr)")
plt.legend()
plt.tight_layout()
plt.savefig("demo_output/by_gender.png", dpi=150)
print("wrote demo_output/by_gender.png   <- look at the Harbour")

print("\n--- 4. pandas writes Excel ---")
by_dept = df.groupby("department")["annual_salary"].agg(["count", "mean"]).round(0)
top10 = df.sort_values("annual_salary", ascending=False).head(10)[
    ["employee_id", "first_name", "last_name", "annual_salary"]]
path = "demo_output/council_pack.xlsx"
with pd.ExcelWriter(path) as writer:
    by_dept.to_excel(writer, sheet_name="By guild")
    top10.to_excel(writer, sheet_name="Top 10", index=False)
print("wrote", path, "(open it: correct, and ugly)")

print("\n--- 5. openpyxl makes it pretty ---")
wb = load_workbook(path)
ws = wb["By guild"]
for cell in ws[1]:
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="1F3A5F")   # no '#' here!
for row in ws.iter_rows(min_row=2, min_col=3, max_col=3):
    for cell in row:
        cell.number_format = '#,##0.00 "cr"'
ws.column_dimensions["A"].width = 16
ws.freeze_panes = "A2"
wb.save(path)
print("rewrote", path, "(open it again)")
print("sheets:", wb.sheetnames)
