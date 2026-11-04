# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 04 · RIDDLE 4: "The Echo"
# ==================================================================
#
#    I made a copy, so I thought,
#    and changed the copy, as I ought.
#    But every change came echoing back:
#    one list, two names, one single track.
#
#  The Queen doubled the reward on every notice for the Midsummer
#  fair. Pell wants the old and new rewards side by side.
#
#  Run:  python bughunt/riddles/riddle_4_echo.py
#  When it's fixed, it prints EXACTLY this:
#
#    Old rewards: [260, 550, 620]
#    Fair rewards: [520, 1100, 1240]
#    Old total: 1430 cr
#    Fair total: 2860 cr

rewards = [260, 550, 620]

fair = rewards
for i in range(len(fair)):
    fair[i] = fair[i] * 2

print("Old rewards:", rewards)
print("Fair rewards:", fair)
print("Old total:", sum(rewards), "cr")
print("Fair total:", sum(fair), "cr")
