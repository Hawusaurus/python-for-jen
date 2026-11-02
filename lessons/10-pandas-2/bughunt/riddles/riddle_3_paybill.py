# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 10 · RIDDLE 3: "The Bill That Shrank"
# ==================================================================
#
#  I asked how much each guild is paid, the whole of it, the sum;
#  the table handed back to me a smaller, gentler crumb.
#  When no one tells a PivotTable what it should do with all it sees,
#  it quietly takes the average, and says nothing, if you please.
#
#  Mistress Pell needs each guild's total pay bill for the Exchequer,
#  largest first, plus the bill for the whole realm.
#
#  Run:  python bughunt/riddles/riddle_3_paybill.py
#  When it's fixed, it prints EXACTLY this:
#
#    PAY BILL BY GUILD
#    ---------------------------
#    Forge          1,748,900 cr
#    Guard          1,129,250 cr
#    Clockworks       808,300 cr
#    Harbour          771,100 cr
#    Treasury         585,850 cr
#    Apothecary       495,250 cr
#    Library          463,650 cr
#    Kitchens         397,550 cr
#    ---------------------------
#    Whole realm    6,399,850 cr

import pandas as pd

df = pd.read_csv("data/thornmere_payroll.csv")

bill = pd.pivot_table(df, index="department", values="annual_salary")
bill = bill.sort_values("annual_salary", ascending=False)

print("PAY BILL BY GUILD")
print("-" * 27)
for guild, row in bill.iterrows():
    print(f"{guild:<12}{row['annual_salary']:>12,.0f} cr")
print("-" * 27)
print(f"{'Whole realm':<12}{bill['annual_salary'].sum():>12,.0f} cr")
