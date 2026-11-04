# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 01 · RIDDLE 5: "The Twice-Counted Hundred"
# ==================================================================
#
#  One slice too thin, one hundred too many:
#  the number shrank down to a lone single penny,
#  the rate swelled up past all belief.
#  Two culprits here. Bring both to grief.
#
#  The Queen's line about the guild's record, for the Privy Council, written by Dalvric.
#  It gives the wrong report number and a success rate no one would believe.
#
#  Run:  python bughunt/riddles/riddle_5_rate.py
#  When it's fixed, it prints EXACTLY this:
#
#    For the Privy Council
#    ---------------------
#    Report 0042: the success rate is 64.8%.
#    Heroes win 65 of every 100 quests.

ref = "Q0042"
quests = 400
successes = 259
rate = successes / quests * 100
number = ref[-4]
print("For the Privy Council")
print("---------------------")
print(f"Report {number}: the success rate is {rate:.1%}.")
print(f"Heroes win {round(rate)} of every 100 quests.")
