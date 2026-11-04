# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 03 · RIDDLE 5: "The Purse That Left Early"
# ==================================================================
#
#  One asked the hall, and not its guest,
#  and so judged every hero less;
#  one packed its bags after course number one.
#  Two faults to mend before you're done.
#
#  The Queen gives 150 crowns to every veteran (10 quests or more).
#  Dalvric's helper pays nobody, then goes home early anyway.
#
#  Run:  python bughunt/riddles/riddle_5_veterans.py
#  When it's fixed, it prints EXACTLY this:
#
#    Is a hero with 2 quests a veteran? False
#    Veterans' purse: 450 cr

quests_done = 2


def is_veteran(quests):
    """True if the hero has done 10 quests or more."""
    return quests_done >= 10


def veteran_purse(records):
    """150 cr from the Queen for every veteran in 'name/quests;...'."""
    total = 0
    for record in records.split(";"):
        name, quests_text = record.split("/")
        if is_veteran(int(quests_text)):
            total = total + 150
        return total


roster = "Wren/42;Jory/12;Bram/30;Thea/3"
print("Is a hero with 2 quests a veteran?", is_veteran(quests_done))
print("Veterans' purse:", veteran_purse(roster), "cr")
