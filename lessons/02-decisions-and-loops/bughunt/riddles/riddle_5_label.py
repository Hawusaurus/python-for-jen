# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 02 · RIDDLE 5: "The Label That Was Lost"
# ==================================================================
#
#  A name was given, then taken away,
#  for a second "if" had the final say;
#  and a count kept shouting inside every lap.
#  Two faults to find before you close the trap.
#
#  Captain Siv's danger report: difficulty 4 or 5 is deadly, 3 is risky, below is safe.
#  Dalvric's version calls nothing deadly and can't stop counting.
#
#  Run:  python bughunt/riddles/riddle_5_label.py
#  When it's fixed, it prints EXACTLY this:
#
#    Q0101  deadly
#    Q0102  safe
#    Q0103  risky
#    Q0104  deadly
#    Deadly quests: 2

records = "Q0101/5;Q0102/2;Q0103/3;Q0104/4"
deadly = 0
for record in records.split(";"):
    quest_id, difficulty_text = record.split("/")
    difficulty = int(difficulty_text)
    if difficulty >= 4:
        label = "deadly"
        deadly = deadly + 1
    if difficulty == 3:
        label = "risky"
    else:
        label = "safe"
    print(f"{quest_id:<7}{label}")
    print("Deadly quests:", deadly)
