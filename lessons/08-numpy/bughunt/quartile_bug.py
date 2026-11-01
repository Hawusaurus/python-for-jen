# ==================================================================
#  DAVE'S LEFTOVERS #8: "quartile_report_v3_USE_THIS_ONE.py"
# ==================================================================
#
# Dave discovered NumPy in his last month. He was very excited.
# He wrote this "quartile report" for the board, ran it once, and
# emailed Gerald the error message by mistake. Gerald still has it.
#
# THREE bugs:
#   one crashes (the error message is unusual, read all of it),
#   one gives a wrong number without crashing (compare with your Exercise 5),
#   one gets the sign wrong. Nearly right. Nearly.
#
# Run it from inside the lesson folder:
#   python bughunt/quartile_bug.py
#
# When it's fixed, it prints EXACTLY this:
#
#   Upper quartile starts at: £19.86
#   Full-time earning over £20/h: 44
#   Mean gap: 19.7%
#
# Fix ONE bug per commit and explain it in the message, like a detective:
#   git commit -m "Bug hunt: <what was wrong and why>"

import csv
import numpy as np

salaries = []
hours = []
genders = []
with open("data/brightwell_payroll.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        salaries.append(float(row["annual_salary"]))
        hours.append(float(row["weekly_hours"]))
        genders.append(row["gender"])

salaries = np.array(salaries)
hours = np.array(hours)
genders = np.array(genders)
hourly = salaries / 52 / hours

q3 = np.percentile(hourly, 0.75)
print(f"Upper quartile starts at: £{q3:.2f}")

high_full_time = (hourly > 20) and (hours == 37.5)
print("Full-time earning over £20/h:", high_full_time.sum())

women = hourly[genders == "F"].mean()
men = hourly[genders == "M"].mean()
gap = (women - men) / men * 100
print(f"Mean gap: {gap:.1f}%")
