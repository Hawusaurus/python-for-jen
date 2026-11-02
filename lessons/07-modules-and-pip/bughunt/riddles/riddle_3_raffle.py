# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 07 · RIDDLE 3: "Bram Always Wins"
# ==================================================================
#
#  I plant the same seed every round,
#  so the same flower breaks the ground.
#  Sow it once, before the race,
#  and luck will show a different face.
#
#  Biscuit draws the Midwinter raffle. Bram has won every prize three years
#  running, and the court has started to talk.
#
#  Run:  python bughunt/riddles/riddle_3_raffle.py
#  When it's fixed, it prints EXACTLY this:
#
#    Biscuit's Midwinter raffle:
#      a roast chestnut: Pell
#      a warm scarf: Siv
#      a day off: Orrin
#    Lucky this year: Pell, Siv, Orrin

import random

court = ["Pell", "Orrin", "Siv", "Bram", "Wren", "Tamsin", "Osric"]

winners = []
print("Biscuit's Midwinter raffle:")
for prize in ["a roast chestnut", "a warm scarf", "a day off"]:
    random.seed(1019)
    winner = random.choice(court)
    winners.append(winner)
    print(f"  {prize}: {winner}")
print("Lucky this year:", ", ".join(winners))
