# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 01 · RIDDLE 5: "The Twice-Counted Hundred"
# ==================================================================
#
#  One mark too few, one hundred too many:
#  the reference lost all but a penny,
#  the gap grew vast beyond belief.
#  Two culprits here. Bring both to grief.
#
#  The Queen's pay gap line for the Privy Council, written by Dalvric.
#  It gives the wrong reference and a gap no one would believe.
#
#  Run:  python bughunt/riddles/riddle_5_gap.py
#  When it's fixed, it prints EXACTLY this:
#
#    For the Privy Council
#    ---------------------
#    Report 0042: the gap is 13.0%.
#    Women earn 87 pennies for every crown men earn.

ref = "TM0042"
male_hourly = 20.00
female_hourly = 17.40
gap = (male_hourly - female_hourly) / male_hourly * 100
pennies = round(female_hourly / male_hourly * 100)
number = ref[-4]
print("For the Privy Council")
print("---------------------")
print(f"Report {number}: the gap is {gap:.1%}.")
print(f"Women earn {pennies} pennies for every crown men earn.")
