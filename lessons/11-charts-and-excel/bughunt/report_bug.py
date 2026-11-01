# ==================================================================
#  DAVE'S LEFTOVERS #11: "board_pack_v7_USE_THIS_ONE.py"
# ==================================================================
#
# Dave's last project before the narrowboat: "the board pack in one
# click". Gerald clicked. Nothing happened. Gerald has not clicked since.
#
# THREE bugs:
#   one crashes (read the error message!),
#   one shows the wrong people with a straight face,
#   one gives a number that's a bit too low. Think about zeros.
#
# Run it from inside the lesson folder:
#   python bughunt/report_bug.py
#
# When it's fixed, it prints EXACTLY this:
#
#   Top 3 earners:
#   EMP1129 Lucy Thompson 68750
#   EMP1144 Harry Walker 63650
#   EMP1112 Tom Robinson 61750
#   Average bonus of those who got one: £1,934.22
#   Saved my_work/output/board_pack.xlsx
#
# Fix ONE bug per commit and explain it in the message.

import pandas as pd
from pathlib import Path

Path("my_work/output").mkdir(parents=True, exist_ok=True)
df = pd.read_csv("data/brightwell_payroll.csv")

# --- Part 1: top earners ---
top = df.sort_values("annual_salary", ascending=True).head(3)
print("Top 3 earners:")
for _, row in top.iterrows():
    print(row["employee_id"], row["first_name"], row["last_name"], row["annual_salary"])

# --- Part 2: average bonus ---
average_bonus = df["bonus"].mean()
print(f"Average bonus of those who got one: £{average_bonus:,.2f}")

# --- Part 3: the board pack ---
top.to_excel("my_work/output/board_pack.xlsx", sheet="Top earners", index=False)
print("Saved my_work/output/board_pack.xlsx")
