# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 02 · RIDDLE 2: "The Days Written Down"
# ==================================================================
#
#  The scroll said twelve, but in ink, not in sum,
#  and ranges won't march to a word's silent drum;
#  a number that's written is still only text:
#  convert it to counting, then count what comes next.
#
#  Pell's rations list for the march to the Northern Wilds, every third day.
#  The number of days came from the Scriptorium.
#
#  Run:  python bughunt/riddles/riddle_2_days.py
#  When it's fixed, it prints EXACTLY this:
#
#    After day  3:   45 cr
#    After day  6:   90 cr
#    After day  9:  135 cr
#    After day 12:  180 cr
#    Days: 12
#    Rations for the march: 180 cr
#    Pell will want a receipt.

days_text = "12"
rations = 15
total = 0
for day in range(1, days_text + 1):
    total = total + rations
    if day % 3 == 0:
        print(f"After day {day:>2}: {total:>4} cr")
print("Days:", days_text)
print("Rations for the march:", total, "cr")
if total > 150:
    print("Pell will want a receipt.")
