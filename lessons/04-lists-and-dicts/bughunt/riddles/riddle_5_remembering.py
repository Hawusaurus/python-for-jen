# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 04 · RIDDLE 5: "The Party That Remembered"
# ==================================================================
#
#    A pack left hanging by the door
#    keeps every party's boots from before;
#    and one who counts from one, not none,
#    leaves the first day's march undone.
#
#  Two helpers from the Grimoire: one signs heroes up for a party,
#  one adds up the days on the road. Both are wrong. (Two bugs.)
#
#  Run:  python bughunt/riddles/riddle_5_remembering.py
#  When it's fixed, it prints EXACTLY this:
#
#    Ironhills party: ['Bram Ironfoot', 'Wren Hawkridge']
#    Greyfen party: ['Piran Dovecote']
#    Days on the road: 23


def sign_up(name, party=[]):
    party.append(name)
    return party


ironhills = sign_up("Bram Ironfoot")
ironhills = sign_up("Wren Hawkridge", ironhills)
greyfen = sign_up("Piran Dovecote")

print("Ironhills party:", ironhills)
print("Greyfen party:", greyfen)

days = [4, 7, 5, 7]
total = 0
for i in range(1, len(days)):
    total += days[i]
print("Days on the road:", total)
