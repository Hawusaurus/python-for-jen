# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 04 · RIDDLE 2: "Half a Pair"
# ==================================================================
#
#    I asked the book for name and level;
#    it gave me names, the little devil.
#    Two hands held out, but one was bare,
#    and so the spell fell through the air.
#
#  Captain Siv wants the party's levels read out before they ride
#  for the Ironhills. This page was meant to do it.
#
#  Run:  python bughunt/riddles/riddle_2_pairs.py
#  When it's fixed, it prints EXACTLY this:
#
#    Bram Ironfoot      level 11
#    Wren Hawkridge     level 19
#    Garrick Oldcastle  level 14
#    Party level: 44

levels = {
    "Bram Ironfoot": 11,
    "Wren Hawkridge": 19,
    "Garrick Oldcastle": 14,
}

total = 0
for name, level in levels:
    print(f"{name:<19}level {level}")
    total += level
print("Party level:", total)
