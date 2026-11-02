# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 09 · RIDDLE 2: "The Sheet That Isn't There"
# ==================================================================
#
#  The workbook opens, the tabs are there,
#  but one is asked for by a name
#  it never had. Look at the tabs:
#  the spelling must be just the same.
#
#  Orrin's check that the old ledger workbook and the CSV still agree,
#  before the Royal Auditors arrive and check it themselves.
#
#  Run:  python bughunt/riddles/riddle_2_sheet.py
#  When it's fixed, it prints EXACTLY this:
#
#    Quests in the CSV: 400
#    Quests in the workbook: 400
#    Same columns: True
#    Same crowns paid: True
#    Notes on the Notes sheet: 5
#    First note: Ledger of quests, kept by the Quartermistress. Rewards in crowns.

import pandas as pd

csv_quests = pd.read_csv("data/quests.csv")
xl_quests = pd.read_excel("data/guild_ledger.xlsx", sheet_name="Quest")
notes = pd.read_excel("data/guild_ledger.xlsx", sheet_name="Notes")

print("Quests in the CSV:", len(csv_quests))
print("Quests in the workbook:", len(xl_quests))
print("Same columns:", list(csv_quests.columns) == list(xl_quests.columns))
print("Same crowns paid:", csv_quests["paid"].sum() == xl_quests["paid"].sum())
print("Notes on the Notes sheet:", len(notes))
print("First note:", notes["note"].tolist()[0])
