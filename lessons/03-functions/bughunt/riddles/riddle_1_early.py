# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 03 · RIDDLE 1: "The Spell Cast Too Early"
# ==================================================================
#
#  You called on my name before I was penned,
#  and asked for an answer I couldn't yet lend;
#  the scroll is read downward, from top to the toe:
#  first write the spell down, and then let it go.
#
#  Pell's share helper. Dalvric put the most important line at the very top,
#  where he could see it.
#
#  Run:  python bughunt/riddles/riddle_1_early.py
#  When it's fixed, it prints EXACTLY this:
#
#    Wren's share of the troll reward: 1215.0 cr
#    Bram's share of the ghoul reward: 413.33 cr
#    The ghoul quest per day: 177.14 cr
#    Thea's share of the rat reward: 120.0 cr

print("Wren's share of the troll reward:", share(4860, 4), "cr")


def share(reward, party_size):
    """Each hero's share, rounded to 2 decimals."""
    return round(reward / party_size, 2)


def per_day(reward, days):
    """Reward per day on the road, rounded to 2 decimals."""
    return round(reward / days, 2)


print("Bram's share of the ghoul reward:", share(1240, 3), "cr")
print("The ghoul quest per day:", per_day(1240, 7), "cr")
print("Thea's share of the rat reward:", share(240, 2), "cr")
