# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 05 · RIDDLE 3: "One Head Too Many"
# ==================================================================
#
#    Four hundred quests the scribes set down,
#    yet one more turned up when I came round.
#    The extra one has no reward:
#    it's just the names along the board.
#
#  Orrin wanted a quick count of the ledger without the csv module,
#  "just to see". This is what he got.
#
#  Run:  python bughunt/riddles/riddle_3_header.py
#  When it's fixed, it prints EXACTLY this:
#
#    Quests in the ledger: 400
#    First quest: Q0001
#    Last quest: Q0400

with open("data/quests.csv", encoding="utf-8") as f:
    lines = f.readlines()

count = len(lines)
first = lines[1].split(",")[0]
last = lines[-1].split(",")[0]

print("Quests in the ledger:", count)
print("First quest:", first)
print("Last quest:", last)
