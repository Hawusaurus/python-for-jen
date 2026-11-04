# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 14 · RIDDLE 2: "The Quickest Troll"
# ==================================================================
#
#  I searched the ledger high and low for every won affray,
#  and found not one, which can't be right; the trolls lost many a day.
#  The ledger writes its victories with a capital held high:
#  look small, and every triumph there will simply pass you by.
#
#  Captain Siv wants the fastest troll hunt the guild ever won, so she
#  can pin it on the notice board as an example. Dalvric's page says none.
#
#  Run:  python bughunt/riddles/riddle_2_trolls.py
#  When it's fixed, it prints EXACTLY this:
#
#    Troll hunts won: 13
#    Fastest: Q0393 in 6 days (Thornwood, 1,330 cr)

import pandas as pd

quests = pd.read_csv("data/quests.csv")
won = quests[(quests["monster"] == "Trolls") & (quests["outcome"] == "success")]
print("Troll hunts won:", len(won))

fastest = won.sort_values(["days", "quest_id"]).iloc[0]
print(f"Fastest: {fastest['quest_id']} in {fastest['days']} days "
      f"({fastest['region']}, {fastest['reward']:,} cr)")
