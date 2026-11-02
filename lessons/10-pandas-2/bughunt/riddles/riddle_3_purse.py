# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 10 · RIDDLE 3: "The Average Purse"
# ==================================================================
#
#  You asked the table for the hoard, the whole heap, coin by coin;
#  but nobody said how to sum, so I took the mean of the coin.
#  Left to itself, a pivot_table will average, not add:
#  the Quartermistress counts her chests, and three hundred makes her mad.
#
#  Quartermistress Pell wants the crowns the guild paid out per region,
#  all of them, for the strongroom ledger.
#
#  Run:  python bughunt/riddles/riddle_3_purse.py
#  When it's fixed, it prints EXACTLY this:
#
#    CROWNS PAID OUT, BY REGION
#    Greyfen            18,150 cr
#    Ironhills          34,730 cr
#    Northern Wilds     33,600 cr
#    Saltmarsh          26,890 cr
#    Thornwood          32,780 cr
#    Strongroom total  146,150 cr

import pandas as pd

quests = pd.read_csv("data/quests.csv")

table = quests.pivot_table(index="region", values="paid")

print("CROWNS PAID OUT, BY REGION")
for region, crowns in table["paid"].items():
    print(f"{region:<16}{crowns:>9,.0f} cr")
print(f"{'Strongroom total':<16}{table['paid'].sum():>9,.0f} cr")
