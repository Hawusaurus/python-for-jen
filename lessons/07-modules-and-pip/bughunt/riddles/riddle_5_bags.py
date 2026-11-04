# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 07 · RIDDLE 5: "The Bag That Remembers"
# ==================================================================
#
#  One bag, made once, is handed round
#  and keeps what every hero stowed.
#  One die that stops before its six
#  will never roll the top it's owed.
#
#  The Quartermistress packs bags for the Thornwood patrol while Biscuit
#  insists on rolling dice. Two bugs on this page.
#
#  Run:  python bughunt/riddles/riddle_5_bags.py
#  When it's fixed, it prints EXACTLY this:
#
#    Wren carries: bow, arrows, cloak
#    Bram carries: axe, shield
#    Biscuit's ten dice: [4, 3, 6, 5, 6, 3, 2, 4, 1, 3]
#    Sixes: 2

import random

random.seed(12)


def pack(items, bag=[]):
    """Put the items in a bag and hand it over. Every hero gets their own bag."""
    for item in items:
        bag.append(item)
    return bag


wren = pack(["bow", "arrows", "cloak"])
bram = pack(["axe", "shield"])
print("Wren carries:", ", ".join(wren))
print("Bram carries:", ", ".join(bram))

rolls = []
for throw in range(10):
    rolls.append(random.randrange(1, 6))
print("Biscuit's ten dice:", rolls)
print("Sixes:", rolls.count(6))
