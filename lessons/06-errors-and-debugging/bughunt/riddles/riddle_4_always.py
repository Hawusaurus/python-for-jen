# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 06 · RIDDLE 4: "The Ward That Always Holds"
# ==================================================================
#
#    Come fair or foul, I always run;
#    I count the wreck as one more won.
#    Put me where only good men tread,
#    and let the stumbling count instead.
#
#  Captain Siv wants the difficulty checked on every quest: how many
#  are fine, how many are not. The page thinks they're all fine.
#
#  Run:  python bughunt/riddles/riddle_4_always.py
#  When it's fixed, it prints EXACTLY this:
#
#    Good difficulties: 399
#    Bad difficulties: 1
import csv

good = 0
bad = 0
with open("data/quests_broken.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        try:
            difficulty = int(row["difficulty"])
        except ValueError:
            bad += 1
        finally:
            good += 1

print("Good difficulties:", good)
print("Bad difficulties:", bad)
