# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 03 · RIDDLE 2: "The Misspelt Keyword"
# ==================================================================
#
#  You called me by a nickname, clipped and small;
#  I do not answer to that name at all.
#  The word you pass must match, letter for letter,
#  the one between my brackets. Spell it better.
#
#  Pell's guild-cut helper, with a default rate of 10%.
#  She tried the 5% rate for rat-catchers and the page refused.
#
#  Run:  python bughunt/riddles/riddle_2_keyword.py
#  When it's fixed, it prints EXACTLY this:
#
#    Standard cut: 124.0 cr
#    Rat-catchers' cut: 62.0 cr
#    To share, standard: 1116.0 cr
#    To share, rat-catchers: 1178.0 cr

def cut(reward, rate=0.10):
    """The guild's cut of a reward."""
    return round(reward * rate, 2)


def to_share(reward, rate=0.10):
    """What's left for the party after the guild's cut."""
    return round(reward - cut(reward, rate), 2)


reward = 1240
print("Standard cut:", cut(reward), "cr")
print("Rat-catchers' cut:", cut(reward, rat=0.05), "cr")
print("To share, standard:", to_share(reward), "cr")
print("To share, rat-catchers:", to_share(reward, rate=0.05), "cr")
