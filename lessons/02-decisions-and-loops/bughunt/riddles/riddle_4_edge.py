# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 02 · RIDDLE 4: "The Edge of the Band"
# ==================================================================
#
#  She stood exactly on the line
#  and asked, "Is gold now also mine?"
#  The sign said "more", but she was "same":
#  let equal also share the name.
#
#  Captain Siv's reward bands: gold starts at 1,500 crowns.
#  Quest Q0102 pays exactly 1,500 and somehow ends up in silver.
#
#  Run:  python bughunt/riddles/riddle_4_edge.py
#  When it's fixed, it prints EXACTLY this:
#
#    Q0101  1,350 cr  silver
#    Q0102  1,500 cr  gold
#    Q0103  4,120 cr  gold
#    Q0104  5,200 cr  dragon
#    Gold quests: 2

records = "Q0101/1350;Q0102/1500;Q0103/4120;Q0104/5200"
gold = 0
for record in records.split(";"):
    quest_id, reward_text = record.split("/")
    reward = int(reward_text)
    if reward >= 5000:
        band = "dragon"
    elif reward > 1500:
        band = "gold"
        gold = gold + 1
    else:
        band = "silver"
    print(f"{quest_id:<6} {reward:>5,} cr  {band}")
print("Gold quests:", gold)
