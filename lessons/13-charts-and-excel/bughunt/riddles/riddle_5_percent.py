# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 13 · RIDDLE 5: "Nine Thousand Percent"
# ==================================================================
#
#  The rate was a fraction, then someone was kind
#  and made it a hundred times bigger, then signed
#  a percent on the wrong pile of numbers as well.
#  Two wrongs in one ledger: one sum, and one cell.
#
#  Queen Aldara wants the success rate per region as a proper Excel
#  percentage, so she can say "55.9%" without counting. The workbook
#  currently claims Thornwood took on nine thousand percent of its quests.
#
#  Run:  python bughunt/riddles/riddle_5_percent.py
#  When it's fixed, it prints EXACTLY this:
#
#    Greyfen: B2=68 [General], C2=0.559 [0.0%]
#    Thornwood: B6=90 [General], C6=0.711 [0.0%]

import pandas as pd
from openpyxl import load_workbook
from pathlib import Path

Path("my_work/output").mkdir(parents=True, exist_ok=True)
quests = pd.read_csv("data/quests.csv")
quests["is_success"] = quests["outcome"] == "Success"

table = quests.groupby("region").agg(quests=("quest_id", "count"),
                                     success_rate=("is_success", "mean"))
table["success_rate"] = (table["success_rate"] * 100).round(1)
path = "my_work/output/riddle_5.xlsx"
table.to_excel(path, sheet_name="Regions")

wb = load_workbook(path)
ws = wb["Regions"]
for row in ws.iter_rows(min_row=2, min_col=2, max_col=2):
    for cell in row:
        cell.number_format = "0.0%"
wb.save(path)

for r in (2, 6):
    b, c = ws[f"B{r}"], ws[f"C{r}"]
    print(f"{ws[f'A{r}'].value}: B{r}={b.value} [{b.number_format}], "
          f"C{r}={c.value} [{c.number_format}]")
