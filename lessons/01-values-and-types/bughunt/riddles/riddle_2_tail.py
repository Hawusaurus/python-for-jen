# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 01 · RIDDLE 2: "The Number With a Tail"
# ==================================================================
#
#  A number arrived with a word at its heel
#  and asked to be counted. It wasn't, for real.
#  The spell won't convert what still carries its tail:
#  snip off what's not number, and count without fail.
#
#  The Scriptorium copied the length of the troll quest as "9 days".
#  Orrin needs it as a number to work out the reward per day.
#
#  Run:  python bughunt/riddles/riddle_2_tail.py
#  When it's fixed, it prints EXACTLY this:
#
#    Quest: Drive off trolls at Larkspur pass
#    Days on the road: 9
#    Weeks on the road: 1.3
#    Reward per day: 540.00 cr

quest = "Drive off trolls at Larkspur pass"
days_text = "9 days"
reward_text = "4860"
days = int(days_text)
reward = float(reward_text)
print("Quest:", quest)
print("Days on the road:", days)
print("Weeks on the road:", round(days / 7, 1))
print(f"Reward per day: {reward / days:,.2f} cr")
