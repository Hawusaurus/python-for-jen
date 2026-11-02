# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 01 · RIDDLE 4: "The Answer That Said No"
# ==================================================================
#
#  I lowered my voice, then asked you loud,
#  and wondered why you weren't allowed;
#  if all I hold is lower case,
#  compare me with the same small face.
#
#  Lady Siv's pension sign-up form. Every subject who answered Yes
#  is marked as not a member. Including Lady Siv.
#
#  Run:  python bughunt/riddles/riddle_4_yes.py
#  When it's fixed, it prints EXACTLY this:
#
#    Name: Lady Siv Larkspur
#    Raw answer: ' YES '
#    Member of the pension scheme: True
#    Pension if a member: 2,060.00 cr a year

name = "Lady Siv Larkspur"
answer = " YES "
salary = 41200
rate = 0.05
is_member = answer.strip().lower() == "Yes"
pension = salary * rate
print("Name:", name)
print("Raw answer:", repr(answer))
print("Member of the pension scheme:", is_member)
print("Pension if a member:", f"{pension:,.2f} cr a year")
