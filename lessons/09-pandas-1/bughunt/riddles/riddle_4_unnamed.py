# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 09 · RIDDLE 4: "The Unnamed Guest"
# ==================================================================
#
#  You saved the scroll and read it back,
#  and found a guest you never named:
#  the numbers down the left came too.
#  Tell the saving not to bring them.
#
#  Orrin wants the troll quests in a CSV of their own, for the armourer.
#  He'll open it in Excel and he'd like it to look like it does here.
#
#  Run:  python bughunt/riddles/riddle_4_unnamed.py
#  When it's fixed, it prints EXACTLY this:
#
#    Troll quests saved: 31
#    Columns: ['quest_id', 'region', 'difficulty', 'outcome']
#    Columns Excel will show: 4
#      quest_id          region  difficulty  outcome
#    0    Q0064  Northern Wilds           4     Fled
#    1    Q0074  Northern Wilds           4     Fled
#    2    Q0086  Northern Wilds           5  Success

import pandas as pd

pd.set_option("display.width", 120)
df = pd.read_csv("data/quests.csv")

trolls = df[df["monster"] == "Trolls"][["quest_id", "region", "difficulty", "outcome"]]
trolls.to_csv("my_work/riddle_trolls.csv")

back = pd.read_csv("my_work/riddle_trolls.csv")
print("Troll quests saved:", len(back))
print("Columns:", list(back.columns))
print("Columns Excel will show:", len(back.columns))
print(back.head(3))
