# ==================================================================
#  DAVE'S LEFTOVERS #9: "headcount_for_gerald_FINAL(2).py"
# ==================================================================
#
# Dave's last ever script. Gerald asked for "a quick headcount by site
# with the London pay bill". Dave emailed this at 02:14, subject line
# "should work", and was never seen again.
#
# THREE bugs:
#   one crashes (the error names the thing it can't find; look closely),
#   one gives a wrong number without crashing (compare with Exercise 3),
#   one is a sorting detail. Gerald reads top to bottom.
#
# Run it from inside the lesson folder:
#   python bughunt/headcount_bug.py
#
# When it's fixed, it prints EXACTLY this:
#
#   Headcount: 200
#   London headcount: 40
#   London pay bill: 1206300
#   Highest paid in London: Luke Edwards 48450
#   Lowest paid in London: Deepa Thompson 20150
#
# Fix ONE bug per commit and explain it in the message, like a detective:
#   git commit -m "Bug hunt: <what was wrong and why>"

import pandas as pd

df = pd.read_csv("data/brightwell_payroll.csv")

print("Headcount:", len(df))

london = df[df["Location"] != "London"]
print("London headcount:", len(london))
print("London pay bill:", london["annual_salary"].sum())

by_pay = london.sort_values("annual_salary", ascending=True)
top = by_pay.iloc[0]
bottom = by_pay.iloc[-1]
print("Highest paid in London:", top["first_name"], top["last_name"], top["annual_salary"])
print("Lowest paid in London:", bottom["first_name"], bottom["last_name"], bottom["annual_salary"])
