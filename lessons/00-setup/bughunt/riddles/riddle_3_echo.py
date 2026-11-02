# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 00 · RIDDLE 3: "The Echo in the Hall"
# ==================================================================
#
#  Ask me a number, I'll answer a word,
#  the strangest reply you have ever heard;
#  wrapped up in quotes I am only a name,
#  unwrap me and I'll tell the sum, not the same.
#
#  Lady Siv asked this page how many guards are on the Roll.
#  It answered her with a word instead of a number.
#
#  Run:  python bughunt/riddles/riddle_3_echo.py
#  When it's fixed, it prints EXACTLY this:
#
#    The Roll of the Realm, by trade
#    Guards on the Roll: 35
#    Apprentices on the Roll: 12
#    Cooks on the Roll: 9
#    Scribes on the Roll: 15
#    Everyone: 71

guards = 35
apprentices = 12
cooks = 9
scribes = 15
everyone = guards + apprentices + cooks + scribes
print("The Roll of the Realm, by trade")
print("Guards on the Roll:", "guards")
print("Apprentices on the Roll:", apprentices)
print("Cooks on the Roll:", cooks)
print("Scribes on the Roll:", scribes)
print("Everyone:", everyone)
