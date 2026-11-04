# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 08 · RIDDLE 3: "The Wrong Way Down"
# ==================================================================
#
#  Five regions down and five across,
#  the square will never make a fuss;
#  but sum it down when you meant along,
#  and every region's count is wrong.
#
#  Orrin's count of quests per region, from a table the Scriptorium copied
#  out by hand. The last line is right. Look at the lines above it.
#
#  Run:  python bughunt/riddles/riddle_3_axis.py
#  When it's fixed, it prints EXACTLY this:
#
#    Greyfen          68 quests
#    Ironhills        85 quests
#    Northern Wilds   75 quests
#    Saltmarsh        82 quests
#    Thornwood        90 quests
#    Busiest region: Thornwood
#    Per difficulty: [ 34 110 128  88  40]

import numpy as np

regions = ["Greyfen", "Ironhills", "Northern Wilds", "Saltmarsh", "Thornwood"]
# Rows: the regions above.  Columns: quests of difficulty 1, 2, 3, 4, 5.
quests = np.array([
    [5, 14, 21, 19, 9],
    [9, 22, 28, 19, 7],
    [3, 21, 27, 15, 9],
    [8, 26, 27, 16, 5],
    [9, 27, 25, 19, 10],
])

per_region = quests.sum(axis=0)
for i in range(len(regions)):
    print(f"{regions[i]:<15} {per_region[i]:>3} quests")
print("Busiest region:", regions[per_region.argmax()])
print("Per difficulty:", quests.sum(axis=0))
