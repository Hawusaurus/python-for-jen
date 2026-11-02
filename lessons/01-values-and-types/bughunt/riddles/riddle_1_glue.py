# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 01 · RIDDLE 1: "The Glue That Would Not Stick"
# ==================================================================
#
#  Words and numbers, side by side,
#  refuse to join, however tried;
#  turn the number into text,
#  and they'll hold hands for what comes next.
#
#  Mistress Pell wanted a one-line pay note for the Roll.
#  The page refuses to run at all.
#
#  Run:  python bughunt/riddles/riddle_1_glue.py
#  When it's fixed, it prints EXACTLY this:
#
#    Maren Ashdown earns 32500 cr a year
#    Guild: Treasury
#    Monthly: 2708.33 cr
#    Weekly: 625.0 cr

first = "maren"
last = "ashdown"
salary = 32500
guild = "Treasury"
name = first.title() + " " + last.title()
note = name + " earns " + salary + " cr a year"
print(note)
print("Guild:", guild)
print("Monthly:", round(salary / 12, 2), "cr")
print("Weekly:", round(salary / 52, 2), "cr")
