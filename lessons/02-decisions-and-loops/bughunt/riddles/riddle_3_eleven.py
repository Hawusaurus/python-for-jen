# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 02 · RIDDLE 3: "Twelve Moons, Eleven Payments"
# ==================================================================
#
#  Twelve moons rise in a Thornmere year,
#  yet one is always missing here;
#  the range stops short, it doesn't wait.
#  Look at the end. Is it too late?
#
#  Mistress Pell's pension plan: 135 crowns every month for a year.
#  The total is always one month short.
#
#  Run:  python bughunt/riddles/riddle_3_eleven.py
#  When it's fixed, it prints EXACTLY this:
#
#    Half-way total: 810 cr
#    Months paid: 12
#    Pension for the year: 1620 cr

pension = 135
total = 0
paid = 0
for month in range(1, 12):
    total = total + pension
    paid = paid + 1
    if month == 6:
        print("Half-way total:", total, "cr")
print("Months paid:", paid)
print("Pension for the year:", total, "cr")
if paid != 12:
    print("Mistress Pell will want a word.")
