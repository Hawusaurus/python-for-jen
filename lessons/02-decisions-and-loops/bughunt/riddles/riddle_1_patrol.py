# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 02 · RIDDLE 1: "The Patrol That Would Not March"
# ==================================================================
#
#  The order was given, the heroes stood still,
#  for none of them stood where a loop's lines will;
#  a line that belongs must step in from the wall:
#  give it four spaces, and off march them all.
#
#  Captain Siv's patrol list. It should name every hero on tonight's patrol.
#
#  Run:  python bughunt/riddles/riddle_1_patrol.py
#  When it's fixed, it prints EXACTLY this:
#
#    Tonight's patrol on the salt road
#    On patrol: Wren
#    On patrol: Bram
#    On patrol: Thea
#    On patrol: Corwin
#    Heroes on patrol: 4
#    The road is guarded.

heroes = "Wren,Bram,Thea,Corwin"
road = "the salt road"
count = 0
print("Tonight's patrol on", road)
for hero in heroes.split(","):
print("On patrol:", hero)
    count = count + 1
print("Heroes on patrol:", count)
if count >= 4:
    print("The road is guarded.")
else:
    print("Send more heroes!")
