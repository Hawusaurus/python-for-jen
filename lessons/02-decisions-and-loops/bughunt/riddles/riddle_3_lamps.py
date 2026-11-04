# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 02 · RIDDLE 3: "Twelve Nights, Eleven Lamps"
# ==================================================================
#
#  Twelve nights the harbour light should burn,
#  but one goes dark at every turn;
#  the range stops short before the end.
#  See where it stops, and stretch it, friend.
#
#  The lighthouse at Harbourtown burns 135 crowns of oil a night, for twelve nights.
#  Pell's total is always one night short.
#
#  Run:  python bughunt/riddles/riddle_3_lamps.py
#  When it's fixed, it prints EXACTLY this:
#
#    Half-way total: 810 cr
#    Nights lit: 12
#    Oil for the twelve nights: 1620 cr

oil = 135
total = 0
nights = 0
for night in range(1, 12):
    total = total + oil
    nights = nights + 1
    if night == 6:
        print("Half-way total:", total, "cr")
print("Nights lit:", nights)
print("Oil for the twelve nights:", total, "cr")
if nights != 12:
    print("Pell will want a word.")
