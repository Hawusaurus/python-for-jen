# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 13 · RIDDLE 1: "The Missing Tab"
# ==================================================================
#
#  I wrote a tab and named it with a crown upon its head,
#  then went to fetch it humbly, and it would not come instead.
#  The workbook swears it's never heard of anyone so small:
#  a letter's height can be the gap between a name and none at all.
#
#  Orrin found this page taped inside the Vault door. It should count
#  the quests per region and read them back out of the workbook.
#
#  Run:  python bughunt/riddles/riddle_1_tab.py
#  When it's fixed, it prints EXACTLY this:
#
#    Sheets: ['Regions']
#    Greyfen          68
#    Ironhills        85
#    Northern Wilds   75
#    Saltmarsh        82
#    Thornwood        90

import pandas as pd
from openpyxl import load_workbook
from pathlib import Path

Path("my_work/output").mkdir(parents=True, exist_ok=True)
quests = pd.read_csv("data/quests.csv")

per_region = quests["region"].value_counts().sort_index()
path = "my_work/output/riddle_1.xlsx"
per_region.to_frame("quests").to_excel(path, sheet_name="Regions")

wb = load_workbook(path)
ws = wb["regions"]
print("Sheets:", wb.sheetnames)
for row in ws.iter_rows(min_row=2, values_only=True):
    print(f"{row[0]:<15}{row[1]:>4}")
