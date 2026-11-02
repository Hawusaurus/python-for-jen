# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 05 · RIDDLE 2: "The Scroll That Would Not Take Ink"
# ==================================================================
#
#    I took the scroll to set down lines,
#    but held it as one reads the signs.
#    A reader's grip lets nothing in:
#    no quill, no ink, no word within.
#
#  Quartermistress Pell's packing list for the Ironhills party. The
#  page should write it to a file, then read it back to check.
#
#  Run:  python bughunt/riddles/riddle_2_ink.py
#  When it's fixed, it prints EXACTLY this:
#
#    rope (2)
#    torches (6)
#    rations (12)
#    Lines written: 3

kit = {"rope": 2, "torches": 6, "rations": 12}

with open("my_work/riddle_kit_list.txt", "r", encoding="utf-8") as f:
    for item, number in kit.items():
        f.write(f"{item} ({number})\n")

with open("my_work/riddle_kit_list.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()

for line in lines:
    print(line)
print("Lines written:", len(lines))
