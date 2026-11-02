# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 04 · RIDDLE 1: "The Last in Line"
# ==================================================================
#
#    Five heroes queue outside the gate;
#    I walk the line and do not wait,
#    but step one pace beyond the last
#    and greet the air where none have passed.
#
#  Found pinned under Quartermistress Pell's inkpot. It should name
#  the first, middle and last hero in the queue for the notice board.
#
#  Run:  python bughunt/riddles/riddle_1_last_hero.py
#  When it's fixed, it prints EXACTLY this:
#
#    Heroes in the queue: 5
#     - Bram Ironfoot
#     - Tamsin Larkspur
#     - Wren Hawkridge
#     - Piran Dovecote
#     - Hild Stonebridge
#    First: Bram Ironfoot
#    Middle: Wren Hawkridge
#    Last: Hild Stonebridge

queue = ["Bram Ironfoot", "Tamsin Larkspur", "Wren Hawkridge", "Piran Dovecote", "Hild Stonebridge"]

count = len(queue)
print("Heroes in the queue:", count)
for name in queue:
    print(" -", name)

print("First:", queue[0])
print("Middle:", queue[count // 2])
print("Last:", queue[count])
