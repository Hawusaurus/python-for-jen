# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 03 · RIDDLE 4: "The Swapped Scales"
# ==================================================================
#
#  The first goes first, the second next:
#  that's how a function reads its text.
#  Swap the pair, and sums grow strange:
#  more wins than tries? Undo the change.
#
#  Captain Siv's troll report for the Privy Council.
#  Dalvric's version says the heroes won more troll quests than they ever went on.
#
#  Run:  python bughunt/riddles/riddle_4_swapped.py
#  When it's fixed, it prints EXACTLY this:
#
#    Troll quests: 40  Won: 33
#    Success rate: 82.5 %
#    Our heroes beat the trolls more often than not.

def success_rate(wins, tries):
    """Share of quests won, in %, rounded to 1 decimal."""
    return round(wins / tries * 100, 1)


def rate_sentence(monster, rate):
    """One sentence a queen can say out loud."""
    if rate > 100:
        return "Impossible. Call the Royal Auditors."
    if rate >= 50:
        return f"Our heroes beat the {monster} more often than not."
    return f"The {monster} win more often than not."


tries = 40
wins = 33
print("Troll quests:", tries, " Won:", wins)
rate = success_rate(tries, wins)
print("Success rate:", rate, "%")
print(rate_sentence("trolls", rate))
