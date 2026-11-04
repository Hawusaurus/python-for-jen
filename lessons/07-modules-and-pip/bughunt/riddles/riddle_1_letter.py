# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 07 · RIDDLE 1: "The Missing Letter"
# ==================================================================
#
#  Python searched the armoury through
#  and found no drawer by that name.
#  The smith who forged it spelled it whole:
#  count the letters on the frame.
#
#  The Quartermistress's roster summary for today's muster. It should
#  describe the heroes the way Exercise 2 described the rewards.
#
#  Run:  python bughunt/riddles/riddle_1_letter.py
#  When it's fixed, it prints EXACTLY this:
#
#    Heroes on the roster: 7
#    Mean level: 8.14
#    Median level: 7
#    Most common class: Warrior
#    Spread (std dev): 5.49
#    Lowest and highest: 3 19
#    Levels in the yard altogether: 57

import statistic as st

roster = ["Warrior", "Ranger", "Mage", "Warrior", "Cleric", "Warrior", "Bard"]
levels = [8, 3, 5, 19, 11, 7, 4]

print("Heroes on the roster:", len(levels))
print("Mean level:", round(st.mean(levels), 2))
print("Median level:", st.median(levels))
print("Most common class:", st.mode(roster))
print("Spread (std dev):", round(st.stdev(levels), 2))
print("Lowest and highest:", min(levels), max(levels))
print("Levels in the yard altogether:", sum(levels))
