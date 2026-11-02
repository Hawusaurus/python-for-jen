# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 07 · RIDDLE 4: "The Month Without a Name"
# ==================================================================
#
#  The day is right, the year is fair,
#  the month has lost its name somewhere.
#  Pell wants words where numbers stand:
#  one letter's wrong, in the format's hand.
#
#  Mistress Pell's payday reminder. She wants the month spelled out, the way
#  it is in the first line.
#
#  Run:  python bughunt/riddles/riddle_4_payday.py
#  When it's fixed, it prints EXACTLY this:
#
#    Today is Sunday 05 April 2026.
#    Payday: 25 April 2026 (20 days away)
#    Payday: 25 May 2026 (50 days away)
#    Payday: 25 June 2026 (81 days away)
#    Paydays before Midsummer: 3

from datetime import date

today = date(2026, 4, 5)
print(f"Today is {today:%A %d %B %Y}.")
paydays = 0
for month in range(4, 7):
    payday = date(2026, month, 25)
    days = (payday - today).days
    print(f"Payday: {payday:%d %m %Y} ({days} days away)")
    paydays = paydays + 1
print("Paydays before Midsummer:", paydays)
