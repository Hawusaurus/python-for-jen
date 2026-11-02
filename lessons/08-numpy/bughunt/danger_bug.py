# ==================================================================
#  PAGES FROM THE GRIMOIRE, PAGE 8: "danger_report_v3_USE_THIS_ONE.py"
# ==================================================================
#
# Dalvric discovered NumPy in his last month at the guild. He was very
# excited. He wrote this "danger report" for the Privy Council, ran it
# once, and sent the Queen the error message by raven, by mistake.
# She still has it.
#
# THREE bugs:
#   one crashes (the error message is unusual, read all of it),
#   one gives a wrong number without crashing (compare with your Exercise 5),
#   one gets the sign wrong. Nearly right. Nearly.
#
# Run it from inside the lesson folder:
#   python bughunt/danger_bug.py
#
# When it's fixed, it prints EXACTLY this:
#
#   Top quarter starts at: 72.98 cr a day
#   Hard quests that succeeded: 67
#   Success falls by 46 points from difficulty 1 to 5
#
# Fix ONE bug per commit and explain it in the message, like a detective:
#   git commit -m "Bug hunt: <what was wrong and why>"

import csv
import numpy as np

paid = []
days = []
difficulty = []
outcomes = []
with open("data/quests.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        paid.append(float(row["paid"]))
        days.append(float(row["days"]))
        difficulty.append(int(row["difficulty"]))
        outcomes.append(row["outcome"])

paid = np.array(paid)
days = np.array(days)
difficulty = np.array(difficulty)
success = np.array(outcomes) == "Success"
per_day = paid / days

q3 = np.percentile(per_day, 0.75)
print(f"Top quarter starts at: {q3:.2f} cr a day")

hard_and_won = (difficulty >= 4) and success
print("Hard quests that succeeded:", hard_and_won.sum())

easy = success[difficulty == 1].mean() * 100
hardest = success[difficulty == 5].mean() * 100
print(f"Success falls by {hardest - easy:.0f} points from difficulty 1 to 5")
