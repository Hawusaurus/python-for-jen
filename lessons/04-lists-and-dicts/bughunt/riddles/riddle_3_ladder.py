# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 04 · RIDDLE 3: "The Wrong End of the Ladder"
# ==================================================================
#
#    The Queen asked who stood tallest in pay;
#    the ledger bowed the other way.
#    It climbed the ladder from the ground
#    and crowned the smallest three it found.
#
#  Queen Aldara wants the three highest wages in the Forge, and their
#  sum. This page answers a different question.
#
#  Run:  python bughunt/riddles/riddle_3_ladder.py
#  When it's fixed, it prints EXACTLY this:
#
#    Wages on the scroll: 7
#    Top three wages: [52800, 41000, 36500]
#    Together: 130,300 cr
#    Everyone else: [31000, 29000, 27300, 24500]
#    Gap between top and bottom: 28,300 cr

salaries = [24500, 41000, 29000, 36500, 31000, 52800, 27300]
count = len(salaries)

ranked = sorted(salaries)
top_three = ranked[:3]
rest = ranked[3:]

print("Wages on the scroll:", count)
print("Top three wages:", top_three)
print(f"Together: {sum(top_three):,} cr")
print("Everyone else:", rest)
print(f"Gap between top and bottom: {ranked[0] - ranked[-1]:,} cr")
