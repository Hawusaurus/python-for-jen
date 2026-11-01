# ==================================================================
#  DAVE'S LEFTOVERS #12: "MACRO9000_paygap_PYTHON_PORT.py"
# ==================================================================
#
# The final leftover. In 2019 Dave translated MACRO-9000's pay gap
# calculation into Python "so it would be future-proof". It reported a
# gap of 24.6% to the board in 2019, 2020 and 2021. It has never agreed
# with your numbers. The board would like to know who is right.
#
# THREE bugs:
#   one crashes (read the error message!),
#   one divides by the wrong thing (check the UK definition),
#   one calls something a median that isn't one.
#
# Run it from inside the lesson folder:
#   python bughunt/macro9000_bug.py
#
# When it's fixed, it prints EXACTLY this:
#
#   MACRO-9000 PAY GAP CHECK
#   Mean hourly gap:   19.7%
#   Median hourly gap: 18.7%
#   MACRO-9000 agrees with Jen. MACRO-9000 may now retire.
#
# Fix ONE bug per commit and explain it in the message.

import pandas as pd

df = pd.read_csv("data/brightwell_payroll.csv")
df["hourly_rate"] = df["annual_salary"] / 52 / df["weekly_hours"]

men = df.loc[df["Gender"] == "M", "hourly_rate"]
women = df.loc[df["gender"] == "F", "hourly_rate"]

mean_gap = round((men.mean() - women.mean()) / women.mean() * 100, 1)
median_gap = round((men.mean() - women.mean()) / men.mean() * 100, 1)

print("MACRO-9000 PAY GAP CHECK")
print(f"Mean hourly gap:   {mean_gap}%")
print(f"Median hourly gap: {median_gap}%")
if mean_gap == 19.7 and median_gap == 18.7:
    print("MACRO-9000 agrees with Jen. MACRO-9000 may now retire.")
else:
    print("MACRO-9000 disagrees with Jen. Somebody is wrong.")
