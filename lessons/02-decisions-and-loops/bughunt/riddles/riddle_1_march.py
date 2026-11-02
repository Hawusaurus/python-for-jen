# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 02 · RIDDLE 1: "The Patrol That Would Not March"
# ==================================================================
#
#  The order came, the soldiers stood,
#  but none stepped forward as they should;
#  a loop needs feet beneath its line:
#  push them in and all is fine.
#
#  Orrin's patrol roster. It should name every guard on tonight's watch.
#
#  Run:  python bughunt/riddles/riddle_1_march.py
#  When it's fixed, it prints EXACTLY this:
#
#    Tonight's watch at the West Gate
#    On watch: Bram
#    On watch: Nye
#    On watch: Wren
#    On watch: Corwin
#    Guards on watch: 4
#    The watch is set.

guards = "Bram,Nye,Wren,Corwin"
gate = "the West Gate"
count = 0
print("Tonight's watch at", gate)
for guard in guards.split(","):
print("On watch:", guard)
    count = count + 1
print("Guards on watch:", count)
if count >= 4:
    print("The watch is set.")
else:
    print("Send more guards!")
