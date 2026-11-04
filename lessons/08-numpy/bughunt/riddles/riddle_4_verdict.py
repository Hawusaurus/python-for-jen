# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 08 · RIDDLE 4: "The Swapped Verdict"
# ==================================================================
#
#  Ask a question, then say what's paid
#  if yes, and then what's paid if no.
#  Dalvric wrote his answers backwards:
#  the winners starve, the losers go.
#
#  The Privy Council asked: what would the guild pay if parties that fled
#  got nothing at all? Pell needs it before the Auditors do.
#
#  Run:  python bughunt/riddles/riddle_4_verdict.py
#  When it's fixed, it prints EXACTLY this:
#
#    Paid out (ledger):       146,150.00 cr
#    Without the fled money:  132,340.00 cr
#    The fled money came to:  13,810.00 cr

import csv
import numpy as np

rewards = []
paid = []
outcomes = []
with open("data/quests.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        rewards.append(float(row["reward"]))
        paid.append(float(row["paid"]))
        outcomes.append(row["outcome"])

rewards = np.array(rewards)
paid = np.array(paid)
outcomes = np.array(outcomes)

no_fled_money = np.where(outcomes == "Success", 0, rewards)
print(f"Paid out (ledger):       {paid.sum():,.2f} cr")
print(f"Without the fled money:  {no_fled_money.sum():,.2f} cr")
print(f"The fled money came to:  {paid.sum() - no_fled_money.sum():,.2f} cr")
