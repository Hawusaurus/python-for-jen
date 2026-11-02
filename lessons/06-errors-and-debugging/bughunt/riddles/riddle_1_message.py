# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 06 · RIDDLE 1: "The Message That Wasn't"
# ==================================================================
#
#    The error spoke, and I leaned near
#    to read the note it carried here.
#    I asked it for a pocket it lacks;
#    print it whole, it tells the facts.
#
#  Mistress Pell's tally of three wages, one of them unreadable. The
#  warding works; the message does not.
#
#  Run:  python bughunt/riddles/riddle_1_message.py
#  When it's fixed, it prints EXACTLY this:
#
#    Skipped: could not convert string to float: 'n/a'
#    Skipped: could not convert string to float: ''
#    Used 3, skipped 2
#    Total: 88,300 cr

values = ["31000", "n/a", "27500", "", "29800"]
total = 0
used = 0
skipped = 0

for v in values:
    try:
        total += float(v)
        used += 1
    except ValueError as e:
        print("Skipped:", e.message)
        skipped += 1

print(f"Used {used}, skipped {skipped}")
print(f"Total: {total:,.0f} cr")
