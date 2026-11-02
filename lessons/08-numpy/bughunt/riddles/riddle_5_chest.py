# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 08 · RIDDLE 5: "One Chest, Two Names"
# ==================================================================
#
#  You gave one chest a second name
#  and filled the 'new' one: both the same.
#  And & grips first, before the 'more':
#  put brackets round, as done before.
#
#  Queen Aldara floated a 20 % danger bonus on hard quests. Pell wants the
#  cost, and how many big boosted rewards were actually won. Two bugs.
#
#  Run:  python bughunt/riddles/riddle_5_chest.py
#  When it's fixed, it prints EXACTLY this:
#
#    Rewards before: 235,090.00 cr
#    With the danger bonus: 260,326.00 cr
#    The bonus costs: 25,236.00 cr
#    Boosted rewards over 1,000 cr that were won: 28

import csv
import numpy as np

rewards = []
difficulty = []
outcomes = []
with open("data/quests.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        rewards.append(float(row["reward"]))
        difficulty.append(int(row["difficulty"]))
        outcomes.append(row["outcome"])

rewards = np.array(rewards)
difficulty = np.array(difficulty)
success = np.array(outcomes) == "Success"

boosted = rewards
hard = difficulty >= 4
boosted[hard] = boosted[hard] * 1.2
print(f"Rewards before: {rewards.sum():,.2f} cr")
print(f"With the danger bonus: {boosted.sum():,.2f} cr")
print(f"The bonus costs: {boosted.sum() - rewards.sum():,.2f} cr")

big_wins = boosted > 1000 & success
print("Boosted rewards over 1,000 cr that were won:", big_wins.sum())
