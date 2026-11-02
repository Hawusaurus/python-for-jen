# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 01 · RIDDLE 3: "Counting from One"
# ==================================================================
#
#  The scribes count one, the spell counts nought,
#  and so the first is never caught;
#  the Guard lost G, the name went wrong:
#  start where the counting starts along.
#
#  Orrin wanted the guild and the number from a Roll reference.
#  The guild comes out with its first letter missing.
#
#  Run:  python bughunt/riddles/riddle_3_counting.py
#  When it's fixed, it prints EXACTLY this:
#
#    Clean reference: GUARD-0042
#    Guild: GUARD
#    Number: 42
#    Next number: 43
#    Roll ID: TM0042

ref = "  guard-0042 "
ref = ref.strip().upper()
dash = ref.find("-")
guild = ref[1:dash]
number = int(ref[dash + 1:])
new_id = f"TM{number:04d}"
print("Clean reference:", ref)
print("Guild:", guild)
print("Number:", number)
print("Next number:", number + 1)
print("Roll ID:", new_id)
