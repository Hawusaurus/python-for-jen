# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 07 · RIDDLE 5: "Two Patrols, One Bag"
# ==================================================================
#
#  Two patrols march from one shared bag;
#  whatever one packs, both must drag.
#  And Siv asked for the middle guard,
#  not all the pay shared out. Look hard.
#
#  Orrin's patrol builder, plus a line Lady Siv asked for. TWO bugs this time,
#  and neither one crashes.
#
#  Run:  python bughunt/riddles/riddle_5_patrols.py
#  When it's fixed, it prints EXACTLY this:
#
#    North patrol: Bram, Wren
#    South patrol: Osric, Tamsin
#    Median guard salary: 29000

import statistics


def new_patrol(captain, members=[]):
    members.append(captain)
    return members


north = new_patrol("Bram")
north.append("Wren")
south = new_patrol("Osric")
south.append("Tamsin")

print("North patrol:", ", ".join(north))
print("South patrol:", ", ".join(south))

salaries = [24950, 26550, 29000, 31750, 68750]
print("Median guard salary:", statistics.mean(salaries))
