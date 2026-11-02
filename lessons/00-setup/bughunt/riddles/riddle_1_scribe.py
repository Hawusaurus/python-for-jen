# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 00 · RIDDLE 1: "The Shouting Scribe"
# ==================================================================
#
#  A scribe who shouts in capitals loud
#  is never heard above the crowd;
#  the spell knows names in humble type,
#  so tame the letter, make it right.
#
#  Mistress Pell found this greeting pinned to the Treasury door.
#  It should welcome the new Keeper. It welcomes no one.
#
#  Run:  python bughunt/riddles/riddle_1_scribe.py
#  When it's fixed, it prints EXACTLY this:
#
#    Welcome to the Royal Treasury of Thornmere!
#    Our new Keeper of the Ledger is Jen
#    Your Paymaster is Mistress Pell
#    The Clockworks are kept by Orrin
#    The dragon is called Biscuit
#    Please do not feed the dragon.

keeper = "Jen"
paymaster = "Mistress Pell"
engineer = "Orrin"
dragon = "Biscuit"
print("Welcome to the Royal Treasury of Thornmere!")
Print("Our new Keeper of the Ledger is", keeper)
print("Your Paymaster is", paymaster)
print("The Clockworks are kept by", engineer)
print("The dragon is called", dragon)
print("Please do not feed the dragon.")
