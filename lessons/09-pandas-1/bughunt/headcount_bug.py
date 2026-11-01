# ==================================================================
#  PAGES FROM THE GRIMOIRE, PAGE 9: "headcount_for_the_queen_FINAL(2).py"
# ==================================================================
#
# Dalvric's last ever script. The Queen asked for "a quick headcount by
# town with the Harbourtown pay bill". Dalvric sent this by raven at
# two in the morning, with the note "should work", and sailed west at dawn.
#
# THREE bugs:
#   one crashes (the error names the thing it can't find; look closely),
#   one gives a wrong number without crashing (compare with Exercise 3),
#   one is a sorting detail. The Queen reads top to bottom.
#
# Run it from inside the lesson folder:
#   python bughunt/headcount_bug.py
#
# When it's fixed, it prints EXACTLY this:
#
#   Headcount: 200
#   Harbourtown headcount: 40
#   Harbourtown pay bill: 1206300
#   Highest paid in Harbourtown: Leofric Thistlewood 48450
#   Lowest paid in Harbourtown: Cerys Quickwater 20150
#
# Fix ONE bug per commit and explain it in the message, like a detective:
#   git commit -m "Bug hunt: <what was wrong and why>"

import pandas as pd

df = pd.read_csv("data/thornmere_payroll.csv")

print("Headcount:", len(df))

harbour = df[df["Location"] != "Harbourtown"]
print("Harbourtown headcount:", len(harbour))
print("Harbourtown pay bill:", harbour["annual_salary"].sum())

by_pay = harbour.sort_values("annual_salary", ascending=True)
top = by_pay.iloc[0]
bottom = by_pay.iloc[-1]
print("Highest paid in Harbourtown:", top["first_name"], top["last_name"], top["annual_salary"])
print("Lowest paid in Harbourtown:", bottom["first_name"], bottom["last_name"], bottom["annual_salary"])
