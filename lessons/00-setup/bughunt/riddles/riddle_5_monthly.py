# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 00 · RIDDLE 5: "The Clipped Coin and the Squashed Word"
# ==================================================================
#
#  Two tricks are hiding on this page:
#  one clips the coin and steals the change,
#  one squeezes words without a space.
#  Find both, and put them in their place.
#
#  Dalvric's last welcome note for new apprentices.
#  It has two mistakes. Neither one makes Python complain.
#
#  Run:  python bughunt/riddles/riddle_5_monthly.py
#  When it's fixed, it prints EXACTLY this:
#
#    Welcome, Bram!
#    You have joined the Forge guild.
#    Your salary is 32500 crowns a year
#    Your monthly pay is 2708.3333333333335 crowns
#    Paid on the last day of every month.
#    Biscuit says hello.

name = "Bram"
guild = "Forge"
salary = 32500
months = 12
print("Welcome," + name + "!")
print("You have joined the " + guild + " guild.")
print("Your salary is", salary, "crowns a year")
print("Your monthly pay is", salary // months, "crowns")
print("Paid on the last day of every month.")
print("Biscuit says hello.")
