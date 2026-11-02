# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 10 · RIDDLE 1: "The Monster Census"
# ==================================================================
#
#  I named the spell but never cast it, called it, yet stayed mute;
#  a wand held up and never waved will never make a newt.
#  You asked me for the tally and I handed you the art,
#  the method, not the answer. Give the spell its little start.
#
#  Captain Siv wants every monster on the notice board, most common first,
#  with a total underneath. Dalvric got as far as the heading.
#
#  Run:  python bughunt/riddles/riddle_1_census.py
#  When it's fixed, it prints EXACTLY this:
#
#    MONSTERS ON THE NOTICE BOARD
#    Goblins           81
#    Bandits           72
#    Wolves            64
#    Ghouls            61
#    Giant Rats        42
#    Giant Spiders     42
#    Trolls            31
#    Wyrm               7
#    All quests       400

import pandas as pd

quests = pd.read_csv("data/quests.csv")
counts = quests["monster"].value_counts

print("MONSTERS ON THE NOTICE BOARD")
for monster, n in counts.items():
    print(f"{monster:<15}{n:>5}")
print(f"{'All quests':<15}{len(quests):>5}")
