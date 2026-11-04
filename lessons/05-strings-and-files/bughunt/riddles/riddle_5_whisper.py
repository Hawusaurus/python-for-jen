# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 05 · RIDDLE 5: "The Leaning Slash"
# ==================================================================
#
#    A slash that leans the other way
#    makes letters mean what they don't say;
#    and shouting, whispering, or plain,
#    a word must match, or count in vain.
#
#  Pell wants to know how many quests on the Scriptorium's copy of
#  the notice board ended well. The page finds no file, and then
#  hardly any successes. (Two bugs.)
#
#  Run:  python bughunt/riddles/riddle_5_whisper.py
#  When it's fixed, it prints EXACTLY this:
#
#    Notices: 40
#    Successes: 24
import csv

notices = 0
successes = 0
with open("data\notice_board_messy.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        notices += 1
        if row["Outcome"].strip() == "Success":
            successes += 1

print("Notices:", notices)
print("Successes:", successes)
