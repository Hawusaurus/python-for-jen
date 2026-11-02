# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 06 · RIDDLE 2: "The Wrong Ward"
# ==================================================================
#
#    I hung a ward against the rain,
#    and wondered why I'm soaked again.
#    The storm that came was not the one
#    my careful charm was cast upon.
#
#  Captain Siv's party sizes, as the Scriptorium wrote them down.
#  The page should skip the unreadable ones and add up the rest.
#
#  Run:  python bughunt/riddles/riddle_2_ward.py
#  When it's fixed, it prints EXACTLY this:
#
#    Heroes sent out: 15
#    Unreadable: 1

sizes = ["4", "3", "five", "2", "6"]

total = 0
skipped = 0
for text in sizes:
    try:
        total += int(text)
    except TypeError:
        skipped += 1

print("Heroes sent out:", total)
print("Unreadable:", skipped)
