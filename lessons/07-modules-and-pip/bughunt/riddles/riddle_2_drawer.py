# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 07 · RIDDLE 2: "The Drawer with the Wrong Label"
# ==================================================================
#
#  The drawer is right, the label wrong:
#  you call a name that's half as long.
#  The module answers, short and dry,
#  "I keep no such thing." Ask it why.
#
#  Orrin's dues calculator for the Forge guild. It uses the helper module
#  guildtools.py that lies next to it. Read that file too.
#
#  Run:  python bughunt/riddles/riddle_2_drawer.py
#  When it's fixed, it prints EXACTLY this:
#
#    Bram Ironfoot        838.00 cr
#    Wren Thistlewood     531.00 cr
#    Osric Vance          635.00 cr
#    Total              2,004.00 cr

import guildtools

members = {"Bram Ironfoot": 41900, "Wren Thistlewood": 26550, "Osric Vance": 31750}

total = 0
for name, salary in members.items():
    dues = guildtools.dues(salary)
    total = total + dues
    print(f"{name:<18}{guildtools.crowns(dues):>12}")
print(f"{'Total':<18}{guildtools.crowns(total):>12}")
