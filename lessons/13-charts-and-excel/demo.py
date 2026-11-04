# Lesson 13 demo: run it from the lesson folder with  python demo.py
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
quests = pd.read_csv("data/quests.csv")
heroes = pd.read_csv("data/heroes.csv")

print("--- 1. Bar chart: a chart is a file ---")
counts = quests["region"].value_counts()
plt.figure(figsize=(8, 4))
plt.bar(counts.index, counts.values, color="#1f3a5f")
plt.title("Quests by region")
plt.ylabel("Quests on the notice board")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()            # <- delete this line once and look at the result
plt.savefig("demo_output/quests_by_region.png", dpi=150)
print("wrote demo_output/quests_by_region.png")

print("\n--- 2. Histogram: how strong are our heroes? ---")
median = heroes["level"].median()
plt.figure(figsize=(8, 4))
plt.hist(heroes["level"], bins=19, color="#e8a33d", edgecolor="white")
plt.axvline(median, color="#1f3a5f", linestyle="--", label=f"Median level {median:.0f}")
plt.legend()
plt.title("Hero levels in the guild")
plt.xlabel("Level")
plt.tight_layout()
plt.savefig("demo_output/levels.png", dpi=150)
print("wrote demo_output/levels.png   <- who is the lonely bar on the far right?")

print("\n--- 3. Two series side by side ---")
table = quests.pivot_table(values="reward", index="region",
                           columns="outcome", aggfunc="mean").round(0)
print(table[["Success", "Failed"]])
x = np.arange(len(table.index))
plt.figure(figsize=(9, 4.5))
plt.bar(x - 0.2, table["Success"], 0.4, label="Success", color="#1f3a5f")
plt.bar(x + 0.2, table["Failed"], 0.4, label="Failed", color="#c8553d")
plt.xticks(x, table.index, rotation=30, ha="right")
plt.ylabel("Average reward (cr)")
plt.legend()
plt.tight_layout()
plt.savefig("demo_output/reward_by_outcome.png", dpi=150)
print("wrote demo_output/reward_by_outcome.png   <- the failed quests were the rich ones")

print("\n--- 4. pandas writes Excel ---")
by_region = quests.groupby("region")["reward"].agg(["count", "mean"]).round(0)
top10 = heroes.sort_values("level", ascending=False).head(10)[
    ["hero_id", "name", "class", "level"]]
path = "demo_output/council_pack.xlsx"
with pd.ExcelWriter(path) as writer:
    by_region.to_excel(writer, sheet_name="By region")
    top10.to_excel(writer, sheet_name="Top 10 heroes", index=False)
print("wrote", path, "(open it: correct, and ugly)")

print("\n--- 5. openpyxl makes it pretty ---")
wb = load_workbook(path)
ws = wb["By region"]
for cell in ws[1]:
    cell.font = Font(bold=True, color="FFFFFF")          # color, not colour!
    cell.fill = PatternFill("solid", fgColor="1F3A5F")   # no '#' here!
for row in ws.iter_rows(min_row=2, min_col=3, max_col=3):
    for cell in row:
        cell.number_format = '#,##0.00 "cr"'
ws.column_dimensions["A"].width = 16
ws.freeze_panes = "A2"
wb.save(path)
print("rewrote", path, "(open it again)")
print("sheets:", wb.sheetnames)
