# ==================================================================
#  PAGES FROM THE GRIMOIRE, PAGE 9: "ironhills_for_the_queen_FINAL(2).py"
# ==================================================================
#
# Dalvric's last ever script. The Queen asked for "a quick word on the
# Ironhills: how many quests, what we paid, the biggest and the smallest".
# Dalvric sent this by raven at two in the morning, with the note
# "should work", and sailed west at dawn.
#
# THREE bugs:
#   one crashes (the error names the thing it can't find; look closely),
#   one gives a wrong number without crashing (the Ironhills are not that busy),
#   one is a sorting detail. The Queen reads top to bottom.
#
# Run it from inside the lesson folder:
#   python bughunt/ironhills_bug.py
#
# When it's fixed, it prints EXACTLY this:
#
#   Quests in the ledger: 400
#   Ironhills quests: 85
#   Ironhills crowns paid: 34730
#   Biggest reward in the Ironhills: Q0346 Wyrm 3530
#   Smallest reward in the Ironhills: Q0204 Giant Rats 140
#
# Fix ONE bug per commit and explain it in the message, like a detective:
#   git commit -m "Bug hunt: <what was wrong and why>"

import pandas as pd

df = pd.read_csv("data/quests.csv")

print("Quests in the ledger:", len(df))

hills = df[df["Region"] != "Ironhills"]
print("Ironhills quests:", len(hills))
print("Ironhills crowns paid:", hills["paid"].sum())

by_reward = hills.sort_values("reward", ascending=True)
top = by_reward.iloc[0]
bottom = by_reward.iloc[-1]
print("Biggest reward in the Ironhills:", top["quest_id"], top["monster"], top["reward"])
print("Smallest reward in the Ironhills:", bottom["quest_id"], bottom["monster"], bottom["reward"])
