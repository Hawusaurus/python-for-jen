# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 00 · RIDDLE 5: "The Shaved Coin and the Squashed Word"
# ==================================================================
#
#  Two quiet tricks are on this scroll:
#  one shaves the pennies off the whole,
#  one jams two words without a gap.
#  Find both before you close the map.
#
#  Dalvric's last welcome note for new heroes.
#  It has two mistakes. Neither one makes Python complain.
#
#  Run:  python bughunt/riddles/riddle_5_split.py
#  When it's fixed, it prints EXACTLY this:
#
#    Welcome, Bram!
#    You have joined the guild as a Warrior.
#    Your first quest pays 1000 crowns
#    Split 3 ways, that is 333.3333333333333 crowns each
#    Paid when the monster is gone.
#    Biscuit says hello.

name = "Bram"
hero_class = "Warrior"
reward = 1000
party = 3
print("Welcome, " + name + "!") # got to put a little space after the comma here!
print("You have joined the guild as a " + hero_class + ".")
print("Your first quest pays", reward, "crowns")
print("Split", party, "ways, that is", reward / party, "crowns each") #it had two /
print("Paid when the monster is gone.")
print("Biscuit says hello.")
