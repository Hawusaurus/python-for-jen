# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 00 · RIDDLE 3: "The Echo in the Hall"
# ==================================================================
#
#  Ask for a count and I give you a name,
#  the word on the label, the tag, not the game;
#  a word in its quotes is a word, nothing more:
#  unwrap it to find what was counted before.
#
#  Captain Siv asked this page how many warriors are on the roster.
#  It answered her with a word instead of a number.
#
#  Run:  python bughunt/riddles/riddle_3_echo.py
#  When it's fixed, it prints EXACTLY this:
#
#    The guild roster, by class
#    Warriors: 24
#    Rangers: 18
#    Mages: 16
#    Bards: 12
#    Everyone: 70

warriors = 24
rangers = 18
mages = 16
bards = 12
everyone = warriors + rangers + mages + bards
print("The guild roster, by class")
print("Warriors:", "warriors")
print("Rangers:", rangers)
print("Mages:", mages)
print("Bards:", bards)
print("Everyone:", everyone)
