# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 00 · RIDDLE 1: "The Herald Who Shouted"
# ==================================================================
#
#  A herald stood on tiptoe, proud,
#  and roared his opening word too loud;
#  the spell will only hear it said
#  in humble letters. Check his head.
#
#  Pell, the Quartermistress, found this welcome pinned to the Guild Hall door.
#  It should greet the new Keeper. It greets no one.
#
#  Run:  python bughunt/riddles/riddle_1_herald.py
#  When it's fixed, it prints EXACTLY this:
#
#    Welcome to the Adventurers' Guild of Thornmere!
#    Our new Keeper of the Guild Ledger is Jen
#    The stores are kept by Pell, the Quartermistress
#    Quests are handed out by Captain Siv
#    The dragon is called Biscuit
#    Please do not feed the dragon.

guild = "the Adventurers' Guild of Thornmere"
keeper = "Jen"
quartermistress = "Pell"
captain = "Siv"
dragon = "Biscuit"
print("Welcome to", guild + "!")
print("Our new Keeper of the Guild Ledger is", keeper) # naughty capital letter!
print("The stores are kept by", quartermistress + ", the Quartermistress")
print("Quests are handed out by Captain", captain)
print("The dragon is called", dragon)
print("Please do not feed the dragon.")
