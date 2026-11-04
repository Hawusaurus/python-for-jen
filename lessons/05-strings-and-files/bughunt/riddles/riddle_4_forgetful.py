# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 05 · RIDDLE 4: "The Scroll That Forgot"
# ==================================================================
#
#    Five regions' tallies, line by line,
#    I wrote them down, and all looked fine;
#    but each new start wiped clean the last,
#    and only one line held on fast.
#
#  The Queen wants the quest count per region on a scroll she can
#  read at dusk. The page writes it, then reads it back.
#
#  Run:  python bughunt/riddles/riddle_4_forgetful.py
#  When it's fixed, it prints EXACTLY this:
#
#    Greyfen: 68 quests
#    Ironhills: 85 quests
#    Northern Wilds: 75 quests
#    Saltmarsh: 82 quests
#    Thornwood: 90 quests
import csv

counts = {}
with open("data/quests.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        counts[row["region"]] = counts.get(row["region"], 0) + 1

for region in sorted(counts):
    with open("my_work/riddle_region_counts.txt", "w", encoding="utf-8") as out:
        out.write(f"{region}: {counts[region]} quests\n")

with open("my_work/riddle_region_counts.txt", encoding="utf-8") as f:
    print(f.read(), end="")
