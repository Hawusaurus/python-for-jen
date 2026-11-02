# ==================================================================
#  PAGES FROM THE GRIMOIRE, PAGE 4: "roll_of_the_realm_FINAL_v3_(2).py"
# ==================================================================
#
# Dalvric's Roll of the Realm. Last run: the week he sailed west. It
# found the wrong top earner, then crashed looking for a guild that
# definitely exists, then (once Orrin "fixed" it) reported a headcount
# of 1 for every guild in the realm.
#
# THREE bugs:
#   one crashes (read the error message, and read it twice),
#   one picks the wrong top earner without crashing,
#   one makes every guild count come out as 1.
#
# Run it from inside the lesson folder:
#   python bughunt/staff_list_bug.py
#
# When it's fixed, it prints EXACTLY this:
#
#   Highest paid: Elowen Fairweather
#   Clockworks: Orrin Ironfoot
#   {'Treasury': 1, 'Clockworks': 2, 'Guard': 1, 'Harbour': 1}
#
# Fix ONE bug per commit and explain it in the message, like a detective:
#   git commit -m "Bug hunt: <what was wrong and why>"

staff = [
    {"name": "Pell Marchbank", "dept": "Treasury", "salary": 31000},
    {"name": "Orrin Ironfoot", "dept": "Clockworks", "salary": 36500},
    {"name": "Elowen Fairweather", "dept": "Guard", "salary": 41000},
    {"name": "Bram Kettleby", "dept": "Harbour", "salary": 24500},
    {"name": "Wren Thistlewood", "dept": "Clockworks", "salary": 29000},
]

# --- Part 1: who earns the most? ---
top = staff[0]
for person in staff:
    if person["salary"] > top["salary"]:
        top = staff[0]
print("Highest paid:", top["name"])

# --- Part 2: the guildmaster of the Clockworks ---
managers = {"Treasury": "Pell Marchbank", "Clockworks": "Orrin Ironfoot", "Guard": "Elowen Fairweather"}
print("Clockworks:", managers["clockworks"])

# --- Part 3: headcount per guild ---
headcount = {}
for person in staff:
    dept = person["dept"]
    if dept in headcount:
        headcount[dept] = 1
    else:
        headcount[dept] = 1
print(headcount)
