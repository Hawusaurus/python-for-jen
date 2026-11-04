# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 06 · RIDDLE 1: "The Message That Wasn't"
# ==================================================================
#
#    I caught the error, held it tight,
#    and asked it for its note to write.
#    It had no pocket by that name;
#    the asking was what broke the frame.
#
#  Orrin wanted a polite note instead of a crash when a reward can't
#  be read. The note itself crashes.
#
#  Run:  python bughunt/riddles/riddle_1_message.py
#  When it's fixed, it prints EXACTLY this:
#
#    Reward: 1240.0
#    Could not read: could not convert string to float: 'n/a'
#    Reward: 610.0

rewards = ["1,240", "n/a", "610"]

for text in rewards:
    try:
        reward = float(text.replace(",", ""))
    except ValueError as e:
        print("Could not read:", e.message)
    else:
        print("Reward:", reward)
