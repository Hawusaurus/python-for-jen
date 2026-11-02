# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 03 · RIDDLE 5: "The Total That Left Early"
# ==================================================================
#
#  One looked outside instead of in,
#  and judged the wrong one from within;
#  one left the feast before the end.
#  Two faults. Now find them both, my friend.
#
#  Lady Siv's bonus helper: 400 crowns for everyone with 12 months or more.
#  It pays one person, then goes home.
#
#  Run:  python bughunt/riddles/riddle_5_early_return.py
#  When it's fixed, it prints EXACTLY this:
#
#    Is a 6-month apprentice eligible? False
#    Total bonus: 1200 cr

months = 6


def eligible(months_served):
    """True if the subject has served 12 months or more."""
    return months >= 12


def total_bonus(records):
    """Sum of 400 cr for every eligible subject in 'name/months;...'."""
    total = 0
    for record in records.split(";"):
        name, months_text = record.split("/")
        if eligible(int(months_text)):
            total = total + 400
        return total


roll = "Maren/14;Jory/30;Bram/60;Wren/3"
print("Is a 6-month apprentice eligible?", eligible(months))
print("Total bonus:", total_bonus(roll), "cr")
