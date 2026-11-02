# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 02 · RIDDLE 2: "The Moons Written Down"
# ==================================================================
#
#  The scroll said twelve, but wrote it so
#  that counting loops refuse to go;
#  a word is not a number, friend:
#  convert it first, then count to end.
#
#  Mistress Pell's guild-dues reminder, one line per month.
#  The number of months came from the Scriptorium.
#
#  Run:  python bughunt/riddles/riddle_2_moons.py
#  When it's fixed, it prints EXACTLY this:
#
#    After month  3:   45 cr
#    After month  6:   90 cr
#    After month  9:  135 cr
#    After month 12:  180 cr
#    Months: 12
#    Dues for the year: 180 cr
#    Guild dues are above 150 cr this year.

months_text = "12"
dues = 15
total = 0
for month in range(1, months_text + 1):
    total = total + dues
    if month % 3 == 0:
        print(f"After month {month:>2}: {total:>4} cr")
print("Months:", months_text)
print("Dues for the year:", total, "cr")
if total > 150:
    print("Guild dues are above 150 cr this year.")
