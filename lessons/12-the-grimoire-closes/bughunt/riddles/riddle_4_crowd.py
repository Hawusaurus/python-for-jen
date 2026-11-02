# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 12 · RIDDLE 4: "The Wrong Crowd"
# ==================================================================
#
#  Of all the women in the realm, how many got a bonus? Ask,
#  but if you count against the wrong crowd, you will botch the task.
#  The question is "of all the women", not "of all who got one paid";
#  choose the crowd you measure by before the share is made.
#
#  The Accord's fifth and sixth figures: the share of women, and the
#  share of men, who received a bonus.
#
#  Run:  python bughunt/riddles/riddle_4_crowd.py
#  When it's fixed, it prints EXACTLY this:
#
#    THE ACCORD: WHO RECEIVED A BONUS
#    Women in the realm: 83
#    Men in the realm:   117
#    Women receiving a bonus: 45.8%
#    Men receiving a bonus:   66.7%

import pandas as pd

df = pd.read_csv("data/thornmere_payroll.csv")


def share_with_bonus(group):
    return (group["bonus"] > 0).sum() / (df["bonus"] > 0).sum() * 100


women = df[df["gender"] == "F"]
men = df[df["gender"] == "M"]
print("THE ACCORD: WHO RECEIVED A BONUS")
print("Women in the realm:", len(women))
print("Men in the realm:  ", len(men))
print(f"Women receiving a bonus: {share_with_bonus(women):.1f}%")
print(f"Men receiving a bonus:   {share_with_bonus(men):.1f}%")
