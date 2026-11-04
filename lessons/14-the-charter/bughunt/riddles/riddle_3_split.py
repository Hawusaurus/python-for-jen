# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 14 · RIDDLE 3: "The Leader's Share"
# ==================================================================
#
#  The leader takes a double share, the rest of them take one,
#  so count the heads, then add a head, and only then you're done.
#  But arithmetic is greedy and will grab the nearest pair:
#  if you want the sum done first, then you must tell it there.
#
#  Quartermistress Pell wants to check one split by hand: quest Q0002,
#  four heroes, 550 cr. Dalvric's split pays out more than the quest did.
#
#  Run:  python bughunt/riddles/riddle_3_split.py
#  When it's fixed, it prints EXACTLY this:
#
#    Q0002: 550 cr for 4 heroes
#    Leader: 220.00 cr, each other hero: 110.00 cr
#    Total paid out: 550.00 cr
#    Matches the ledger: True

import pandas as pd


def split_loot(paid, heroes):
    """Leader gets two shares, everyone else one."""
    one_share = paid / heroes + 1
    return 2 * one_share, one_share


quests = pd.read_csv("data/quests.csv").set_index("quest_id")
party = pd.read_csv("data/party.csv")
quest = quests.loc["Q0002"]
leader, other = split_loot(quest["paid"], quest["party_size"])
total = leader + other * (quest["party_size"] - 1)
print(f"Q0002: {quest['paid']} cr for {quest['party_size']} heroes")
print(f"Leader: {leader:,.2f} cr, each other hero: {other:,.2f} cr")
print(f"Total paid out: {total:,.2f} cr")
shares = sorted(party.loc[party["quest_id"] == "Q0002", "loot_share"])
print("Matches the ledger:", shares == sorted([leader] + [other] * (quest["party_size"] - 1)))
