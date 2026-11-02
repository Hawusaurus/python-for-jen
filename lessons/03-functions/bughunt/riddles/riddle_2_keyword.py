# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 03 · RIDDLE 2: "The Misspelt Keyword"
# ==================================================================
#
#  You called me by a nickname, short,
#  I don't answer to that sort;
#  the name you give must match the one
#  I wrote beside my brackets. Done.
#
#  Lady Siv's pension calculator with a default rate.
#  She tried the 8% scheme and the page refused.
#
#  Run:  python bughunt/riddles/riddle_2_keyword.py
#  When it's fixed, it prints EXACTLY this:
#
#    Standard scheme: 135.42 cr
#    Generous scheme: 216.67 cr
#    Net, standard: 2572.91 cr
#    Net, generous: 2491.66 cr

def pension(basic, rate=0.05):
    """Monthly pension deduction."""
    return round(basic * rate, 2)


def net(basic, rate=0.05):
    """Basic pay after the pension deduction."""
    return round(basic - pension(basic, rate), 2)


basic = 2708.33
print("Standard scheme:", pension(basic), "cr")
print("Generous scheme:", pension(basic, rat=0.08), "cr")
print("Net, standard:", net(basic), "cr")
print("Net, generous:", net(basic, rate=0.08), "cr")
