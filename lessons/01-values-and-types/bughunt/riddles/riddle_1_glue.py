# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 01 · RIDDLE 1: "The Glue That Would Not Stick"
# ==================================================================
#
#  A word and a number were told to hold hands;
#  the word was quite willing, the number had plans.
#  Lend the number a word's coat to wear for the day,
#  and the two will walk on in the very same way.
#
#  Pell wanted a one-line note about the guild's star for the Roster.
#  The page refuses to run at all.
#
#  Run:  python bughunt/riddles/riddle_1_glue.py
#  When it's fixed, it prints EXACTLY this:
#
#    Wren Hawkridge is a level 19 hero
#    Class: Ranger
#    Levels to the top: 1
#    Halfway there at level 9.5

first = "wren"
last = "hawkridge"
level = 19
hero_class = "Ranger"
name = first.title() + " " + last.title()
note = name + " is a level " + level + " hero"
print(note)
print("Class:", hero_class)
print("Levels to the top:", 20 - level)
print("Halfway there at level", level / 2)
