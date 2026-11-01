# ==================================================================
#  PAGES FROM THE GRIMOIRE, PAGE 12: the last page
# ==================================================================
#
# The final page. Before he sailed west, Dalvric copied the Grimoire's
# pay gap incantation into Python "so it would outlast him". Every year
# since, it has told the Privy Council the same figure: a gap of 24.6%.
# It has never agreed with your numbers. The Queen would like to know
# who is right.
#
# THREE bugs:
#   one crashes (read the error message!),
#   one divides by the wrong thing (check the Accord's definition),
#   one calls something a median that isn't one.
#
# Run it from inside the lesson folder:
#   python bughunt/grimoire_bug.py
#
# When it's fixed, it prints EXACTLY this:
#
#   THE GRIMOIRE'S PAY GAP, CHECKED
#   Mean hourly gap:   19.7%
#   Median hourly gap: 18.7%
#   The Grimoire agrees with the Keeper. The Grimoire may now close.
#
# Fix ONE bug per commit and explain it in the message.

import pandas as pd

df = pd.read_csv("data/thornmere_payroll.csv")
df["hourly_rate"] = df["annual_salary"] / 52 / df["weekly_hours"]

men = df.loc[df["Gender"] == "M", "hourly_rate"]
women = df.loc[df["gender"] == "F", "hourly_rate"]

mean_gap = round((men.mean() - women.mean()) / women.mean() * 100, 1)
median_gap = round((men.mean() - women.mean()) / men.mean() * 100, 1)

print("THE GRIMOIRE'S PAY GAP, CHECKED")
print(f"Mean hourly gap:   {mean_gap}%")
print(f"Median hourly gap: {median_gap}%")
if mean_gap == 19.7 and median_gap == 18.7:
    print("The Grimoire agrees with the Keeper. The Grimoire may now close.")
else:
    print("The Grimoire disagrees with the Keeper. Somebody is wrong.")
