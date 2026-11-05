# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 00 · RIDDLE 2: "The Bracket Left Ajar"
# ==================================================================
#
#  I open my arms at the start of a call
#  and wait for my partner to close it all;
#  without it the spell runs on past the end.
#  Go find where I'm waiting, alone, for my friend.
#
#  Orrin found this sum scratched inside the Clockworks.
#  It should tell the rat-catchers what their reward comes to.
#
#  Run:  python bughunt/riddles/riddle_2_bracket.py
#  When it's fixed, it prints EXACTLY this:
#
#    The rat-catchers' sums
#    ----------------------
#    Reward: 1000 crowns
#    After the guild's cut: 900 crowns
#    Each hero gets 300.0 crowns
#    ----------------------
#    Done.

reward = 1000
heroes = 3
guild_cut = 100
print("The rat-catchers' sums")
print("----------------------")
print("Reward:", reward, "crowns")
print("After the guild's cut:", reward - guild_cut, "crowns") #oooh a missing bracket!
print("Each hero gets", (reward - guild_cut) / heroes, "crowns")
print("----------------------")
print("Done.")
