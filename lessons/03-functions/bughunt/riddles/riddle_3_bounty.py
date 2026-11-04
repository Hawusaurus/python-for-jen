# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 03 · RIDDLE 3: "The Bounty That Never Grew"
# ==================================================================
#
#  A fresh new number came to be,
#  then stayed indoors where none could see;
#  the stale old one walked out instead.
#  Send out the new one in its stead.
#
#  Queen Aldara raises the Wyrm bounty 3% every month nobody slays it.
#  Dalvric's helper works very hard and changes nothing.
#
#  Run:  python bughunt/riddles/riddle_3_bounty.py
#  When it's fixed, it prints EXACTLY this:
#
#    Bounty on the Wyrm of the Northern Wilds
#    Now: 3,100.00 cr
#    After one month: 3,193.00 cr
#    After two months: 3,288.79 cr

def with_growth(bounty, percent):
    """The bounty after it grows by `percent` %."""
    new_bounty = bounty * (1 + percent / 100)
    return round(bounty, 2)


def money(amount):
    """Crowns with thousands separator and 2 decimals."""
    return f"{amount:,.2f} cr"


monster = "the Wyrm of the Northern Wilds"
bounty = 3100
print("Bounty on", monster)
print("Now:", money(bounty))
print("After one month:", money(with_growth(bounty, 3)))
print("After two months:", money(with_growth(with_growth(bounty, 3), 3)))
