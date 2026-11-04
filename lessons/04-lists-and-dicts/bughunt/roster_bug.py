# ==================================================================
#  PAGES FROM THE GRIMOIRE, PAGE 4: "the_roster_FINAL_v3_(2).py"
# ==================================================================
#
# Dalvric's guild roster. Last run: the week he sailed west. It named
# the wrong hero as the most experienced, then crashed looking up a
# region that is definitely on the map, then (once Orrin "fixed" it)
# reported exactly 1 hero in every class.
#
# THREE bugs:
#   one crashes (read the error message, and read it twice),
#   one picks the wrong hero without crashing,
#   one makes every class count come out as 1.
#
# Run it from inside the lesson folder:
#   python bughunt/roster_bug.py
#
# When it's fixed, it prints EXACTLY this:
#
#   Highest level: Wren Hawkridge
#   Ironhills: Hild Stonebridge
#   {'Warrior': 2, 'Ranger': 2, 'Mage': 1, 'Bard': 1}
#
# Fix ONE bug per commit and explain it in the message, like a detective:
#   git commit -m "Bug hunt: <what was wrong and why>"

roster = [
    {"name": "Bram Ironfoot", "class": "Warrior", "level": 11},
    {"name": "Wren Hawkridge", "class": "Ranger", "level": 19},
    {"name": "Tamsin Larkspur", "class": "Mage", "level": 9},
    {"name": "Garrick Oldcastle", "class": "Warrior", "level": 14},
    {"name": "Piran Dovecote", "class": "Bard", "level": 4},
    {"name": "Kestrel Wildmoor", "class": "Ranger", "level": 7},
]

# --- Part 1: who is the most experienced? ---
top = roster[0]
for hero in roster:
    if hero["level"] > top["level"]:
        top = roster[0]
print("Highest level:", top["name"])

# --- Part 2: the warden of the Ironhills ---
wardens = {"Greyfen": "Alder Pike", "Ironhills": "Hild Stonebridge", "Northern Wilds": "Corwin Northwind"}
print("Ironhills:", wardens["ironhills"])

# --- Part 3: heroes per class ---
headcount = {}
for hero in roster:
    c = hero["class"]
    if c in headcount:
        headcount[c] = 1
    else:
        headcount[c] = 1
print(headcount)
