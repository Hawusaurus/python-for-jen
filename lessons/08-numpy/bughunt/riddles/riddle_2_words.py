# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 08 · RIDDLE 2: "The Numbers That Were Words"
# ==================================================================
#
#  The file hands over only text,
#  however much it looks like sums.
#  You stacked the words into a column:
#  turn them to numbers as each comes.
#
#  Captain Siv asked how many big rewards are on the board. Dalvric's
#  answer has been waiting by the window since the last full moon.
#
#  Run:  python bughunt/riddles/riddle_2_words.py
#  When it's fixed, it prints EXACTLY this:
#
#    Quests: 400
#    Rewards over 1,000 cr: 43
#    Average reward: 587.72
#    Biggest reward: 4540.0

import csv
import numpy as np

rewards = []
with open("data/quests.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        rewards.append(row["reward"])

rewards = np.array(rewards)
print("Quests:", len(rewards))
print("Rewards over 1,000 cr:", (rewards > 1000).sum())
print("Average reward:", round(rewards.mean(), 2))
print("Biggest reward:", rewards.max())
