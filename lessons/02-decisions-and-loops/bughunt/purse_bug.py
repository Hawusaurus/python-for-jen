# ==================================================================
#  PAGES FROM THE GRIMOIRE, PAGE 2: "royal_purse_USE_THIS_ONE.py"
# ==================================================================
#
# Dalvric's royal purse run. Captain Siv ran it once. Everyone got a purse.
# EVERYONE. Including three novices on their very first rat hunt, and
# Biscuit (who is on the roster as a joke, which is a different problem).
# The total came to minus forty crowns.
#
# THREE bugs:
#   one crashes (read the error message!),
#   one gives a purse to the wrong people (check the rules below),
#   one makes the total wrong even when every line is right.
#
# Run it from inside the lesson folder:
#   python bughunt/purse_bug.py
#
# When it's fixed, it prints EXACTLY this:
#
#   Wren Hawkridge    775.00
#   Jory Pike           0.00
#   Bram Ironfoot     365.00
#   Biscuit             0.00
#   ------------------------
#   Total           1,140.00
#
# Rules: no purse for novices (fewer than 3 quests done). Otherwise a
# quarter of the reward on top for difficulty 4 or 5, a tenth for
# difficulty 3, nothing below that.
#
# Fix ONE bug per commit and explain it in the message, like a detective:
#   git commit -m "Bug hunt: <what was wrong and why>"

records = "Wren Hawkridge/3100/4/14;Jory Pike/2450/2/30;Bram Ironfoot/3650/3/60;Biscuit/400/5/0"

for record in records.split(";"):
    total = 0
    name, reward_text, difficulty_text, quests_text = record.split("/")
    reward = int(reward_text)
    difficulty = int(difficulty_text)
    quests_done = int(quests_text)
    if difficulty => 4:
        rate = 0.25
    elif quests_done < 3:
        rate = 0
    elif difficulty == 3:
        rate = 0.10
    else:
        rate = 0
    purse = reward * rate
    total = total + purse
    print(f"{name:<14}{purse:>10,.2f}")

print("-" * 24)
print(f"{'Total':<14}{total:>10,.2f}")
