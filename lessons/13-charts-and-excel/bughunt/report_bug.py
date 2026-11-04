# ==================================================================
#  PAGES FROM THE GRIMOIRE, PAGE 13: "privy_council_pack_FINAL_v3.py"
# ==================================================================
#
# Dalvric's last working before he sailed west: "the Privy Council's
# pack in one click". The Queen clicked. Nothing happened. The Queen
# has not clicked since.
#
# THREE bugs:
#   one crashes (read the error message, then read it again),
#   one shows the wrong heroes with a straight face,
#   one gives a number that's a bit too low. Think about failed quests.
#
# Run it from inside the lesson folder:
#   python bughunt/report_bug.py
#
# When it's fixed, it prints EXACTLY this:
#
#   Top 3 heroes by loot:
#   H008 Jasper Ironfoot 4,428.68 cr
#   H070 Benedek Saltmarsh 3,833.34 cr
#   H019 Silas Goldenhand 3,502.33 cr
#   Average share when a quest paid: 145.86 cr
#   Saved my_work/output/council_pack.xlsx
#
# Fix ONE bug per commit and explain it in the message.

import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill
from pathlib import Path

Path("my_work/output").mkdir(parents=True, exist_ok=True)
heroes = pd.read_csv("data/heroes.csv")
party = pd.read_csv("data/party.csv")
loot = party.merge(heroes, on="hero_id")

# --- Part 1: the three richest heroes ---
totals = loot.groupby(["hero_id", "name"])["loot_share"].sum().reset_index()
top = totals.sort_values("loot_share", ascending=True).head(3)
print("Top 3 heroes by loot:")
for _, row in top.iterrows():
    print(row["hero_id"], row["name"], f"{row['loot_share']:,.2f} cr")

# --- Part 2: what is a share worth? ---
average_share = loot["loot_share"].mean()
print(f"Average share when a quest paid: {average_share:,.2f} cr")

# --- Part 3: the council pack, in the Queen's colours ---
path = "my_work/output/council_pack.xlsx"
top.to_excel(path, sheet_name="Top heroes", index=False)
wb = load_workbook(path)
ws = wb["Top heroes"]
for cell in ws[1]:
    cell.font = Font(bold=True, colour="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="1F3A5F")
wb.save(path)
print("Saved", path)
