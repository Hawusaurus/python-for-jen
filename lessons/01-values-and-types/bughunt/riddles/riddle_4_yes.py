# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 01 · RIDDLE 4: "The Answer That Said No"
# ==================================================================
#
#  You whispered my answer in letters so small,
#  then checked it against a word standing tall;
#  the small and the tall will not match, though they rhyme:
#  compare like with like, and you'll get it in time.
#
#  Captain Siv's sign-up sheet for the ghoul hunt. Everyone who answered YES
#  is marked as not joining. Including Captain Siv.
#
#  Run:  python bughunt/riddles/riddle_4_yes.py
#  When it's fixed, it prints EXACTLY this:
#
#    Name: Captain Siv
#    Raw answer: ' YES '
#    Joins the ghoul hunt: True
#    Share if she joins: 279.00 cr

name = "Captain Siv"
answer = " YES "
reward = 1240
cut_rate = 0.10
party = 4
joins = answer.strip().lower() == "Yes"
share = reward * (1 - cut_rate) / party
print("Name:", name)
print("Raw answer:", repr(answer))
print("Joins the ghoul hunt:", joins)
print("Share if she joins:", f"{share:,.2f} cr")
