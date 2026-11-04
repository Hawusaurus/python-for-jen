# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 04 · RIDDLE 3: "The Wrong End of the Board"
# ==================================================================
#
#    I climbed the board to find the best,
#    but started low, like all the rest.
#    The richest three I meant to show;
#    I showed the three that sit below.
#
#  Biscuit singed half the notice board, so Pell asked for the three
#  best-paying notices to pin back up first.
#
#  Run:  python bughunt/riddles/riddle_3_ladder.py
#  When it's fixed, it prints EXACTLY this:
#
#    Notices: 7
#    Pin these first:
#      2,850 cr
#      1,240 cr
#        760 cr

rewards = [320, 1240, 150, 610, 2850, 480, 760]

print("Notices:", len(rewards))
ranked = sorted(rewards)
print("Pin these first:")
for r in ranked[:3]:
    money = f"{r:,} cr"
    print(f"  {money:>8}")
