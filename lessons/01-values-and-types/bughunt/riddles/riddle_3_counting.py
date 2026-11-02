# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 01 · RIDDLE 3: "Counting from One"
# ==================================================================
#
#  The clerks count from one, but the spell starts at nought,
#  and so the first letter is never quite caught;
#  the GOBLINS lost G and came back as a stranger:
#  begin where Python begins, and you're out of danger.
#
#  Orrin wanted the monster and the number from a notice reference.
#  The monster comes out with its first letter missing.
#
#  Run:  python bughunt/riddles/riddle_3_counting.py
#  When it's fixed, it prints EXACTLY this:
#
#    Clean reference: GOBLINS-0042
#    Monster: Goblins
#    Number: 42
#    Next number: 43
#    Quest ID: Q0042

ref = "  goblins-0042 "
ref = ref.strip().upper()
dash = ref.find("-")
monster = ref[1:dash]
number = int(ref[dash + 1:])
new_id = f"Q{number:04d}"
print("Clean reference:", ref)
print("Monster:", monster.title())
print("Number:", number)
print("Next number:", number + 1)
print("Quest ID:", new_id)
