# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 13 · RIDDLE 2: "The Queen's Blue"
# ==================================================================
#
#  The painter's brush will take a mark before the colour's name;
#  the ledger-keeper's will not, and calls the little mark a shame.
#  Two crafts, one blue, and each insists its spelling is the true:
#  so drop the thing that paints the brush, and let the ledger through.
#
#  Quartermistress Pell wants the header row of the monster workbook
#  in the Queen's own blue, with white writing. Dalvric tried.
#
#  Run:  python bughunt/riddles/riddle_2_blue.py
#  When it's fixed, it prints EXACTLY this:
#
#    Header cells painted: 4
#    A1 fill: 001F3A5F, bold: True

import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill
from pathlib import Path

Path("my_work/output").mkdir(parents=True, exist_ok=True)
quests = pd.read_csv("data/quests.csv")

table = quests.groupby("monster").agg(quests=("quest_id", "count"),
                                      reward=("reward", "mean"),
                                      paid=("paid", "sum"))
path = "my_work/output/riddle_2.xlsx"
table.to_excel(path, sheet_name="Monsters")

wb = load_workbook(path)
ws = wb["Monsters"]
painted = 0
for cell in ws[1]:
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="#1F3A5F")
    painted += 1
wb.save(path)
print("Header cells painted:", painted)
print(f"A1 fill: {ws['A1'].fill.fgColor.rgb}, bold: {ws['A1'].font.bold}")
