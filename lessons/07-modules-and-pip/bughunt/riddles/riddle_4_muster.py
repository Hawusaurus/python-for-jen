# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 07 · RIDDLE 4: "The Month That Kept Time"
# ==================================================================
#
#  The day is true, the year is right,
#  the month reads zero, every line.
#  One letter's standing up too tall:
#  it's reading minutes off the time.
#
#  The Quartermistress's muster reminder for the notice board. The first
#  line shows the date exactly the way she wants it.
#
#  Run:  python bughunt/riddles/riddle_4_muster.py
#  When it's fixed, it prints EXACTLY this:
#
#    Today is Sunday 05/04/2026.
#    Muster: Sat 25/04/2026 (20 days away)
#    Muster: Mon 25/05/2026 (50 days away)
#    Muster: Thu 25/06/2026 (81 days away)
#    Muster: Sat 25/07/2026 (111 days away)
#    Musters before the Charter hearing: 4

from datetime import date

today = date(2026, 4, 5)
print(f"Today is {today:%A %d/%m/%Y}.")
musters = 0
for month in range(4, 8):
    muster = date(2026, month, 25)
    days = (muster - today).days
    print(f"Muster: {muster:%a %d/%M/%Y} ({days} days away)")
    musters = musters + 1
print("Musters before the Charter hearing:", musters)
