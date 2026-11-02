# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 00 · RIDDLE 2: "The Gate Left Open"
# ==================================================================
#
#  I open wide but never close,
#  and so the spell beyond me goes
#  on running past the line's last end:
#  shut what you opened, careful friend.
#
#  Orrin found this sum scratched inside the Clockworks.
#  It should tell the guards how many crowns a year a month's pay makes.
#
#  Run:  python bughunt/riddles/riddle_2_gate.py
#  When it's fixed, it prints EXACTLY this:
#
#    The Clockworks pay sheet
#    -----------------------
#    A month's pay is 2708.33 crowns
#    A year's pay is 32499.96 crowns
#    That is 624.9992307692307 crowns a week
#    -----------------------
#    Done.

monthly_pay = 2708.33
weeks = 52
months = 12
print("The Clockworks pay sheet")
print("-----------------------")
print("A month's pay is", monthly_pay, "crowns")
print("A year's pay is", monthly_pay * months, "crowns"
print("That is", monthly_pay * months / weeks, "crowns a week")
print("-----------------------")
print("Done.")
