# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 04 · RIDDLE 5: "The Remembering Spell"
# ==================================================================
#
#    A list that waits beside the door
#    remembers all who came before.
#    And one who counts from one, not none,
#    will miss the first and think he's done.
#
#  Two small helpers from the Grimoire: one enrols people into a
#  guild, one adds up weekly hours. Both are wrong. (Two bugs.)
#
#  Run:  python bughunt/riddles/riddle_5_remembering.py
#  When it's fixed, it prints EXACTLY this:
#
#    Forge: ['Bram Kettleby', 'Wren Thistlewood']
#    Library: ['Hild Woolpack']
#    Total weekly hours: 127.5

def enrol(name, guild_list=[]):
    guild_list.append(name)
    return guild_list


forge = enrol("Bram Kettleby")
forge = enrol("Wren Thistlewood", forge)
library = enrol("Hild Woolpack")

print("Forge:", forge)
print("Library:", library)

hours = [37.5, 30, 22.5, 37.5]
total = 0
for i in range(1, len(hours)):
    total += hours[i]
print("Total weekly hours:", total)
