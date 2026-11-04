# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 07 · RIDDLE 2: "The Name Without a House"
# ==================================================================
#
#  Two tools came in without their kin;
#  the house of math stayed out.
#  Yet every line calls 'math' by name,
#  and Python asks what that's about.
#
#  Captain Siv's wagon count for the Ironhills expedition. Orrin wrote the
#  first line; Dalvric wrote the rest.
#
#  Run:  python bughunt/riddles/riddle_2_house.py
#  When it's fixed, it prints EXACTLY this:
#
#    Crates of rations: 23
#    Wagons needed: 4
#    Full wagons: 3
#    Tents needed: 4
#    Heroes in the last tent: 2

from math import ceil, floor

crates = 23
per_wagon = 6
heroes = 14
per_tent = 4

print("Crates of rations:", crates)
print("Wagons needed:", math.ceil(crates / per_wagon))
print("Full wagons:", math.floor(crates / per_wagon))
print("Tents needed:", math.ceil(heroes / per_tent))
print("Heroes in the last tent:", heroes - math.floor(heroes / per_tent) * per_tent)
