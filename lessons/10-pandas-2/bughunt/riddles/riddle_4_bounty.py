# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 10 · RIDDLE 4: "The Bounty That Multiplied"
# ==================================================================
#
#  One notice and one bounty, pinned up once upon the board;
#  but join it to the party and each hero brings the hoard.
#  Five heroes on a quest, and lo: five copies of the gold.
#  Count heroes where the heroes are; count crowns where crowns are told.
#
#  Captain Siv wants, per region: how many heroes she has sent, and how many
#  crowns were offered on the notices. Pell says the crowns are "ambitious".
#
#  Run:  python bughunt/riddles/riddle_4_bounty.py
#  When it's fixed, it prints EXACTLY this:
#
#    REGION          HEROES SENT   CROWNS OFFERED
#    Greyfen                 215        34,150 cr
#    Ironhills               245        56,230 cr
#    Northern Wilds          241        54,920 cr
#    Saltmarsh               235        39,320 cr
#    Thornwood               258        50,470 cr

import pandas as pd

quests = pd.read_csv("data/quests.csv")
party = pd.read_csv("data/party.csv")

trips = party.merge(quests, on="quest_id", how="left")
heroes_sent = trips.groupby("region")["hero_id"].count()
crowns = trips.groupby("region")["reward"].sum()

print(f"{'REGION':<15}{'HEROES SENT':>12}{'CROWNS OFFERED':>17}")
for region in heroes_sent.index:
    print(f"{region:<15}{heroes_sent[region]:>12}{crowns[region]:>14,} cr")
