# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 12 · RIDDLE 2: "The Tangled Conditions"
# ==================================================================
#
#  Two questions in a single breath: a woman, and a bonus too.
#  I asked them both without their walls, and Python tangled through:
#  it tried to join a letter with a column full of crowns.
#  Give each question its own brackets, and the tangle settles down.
#
#  Lady Siv: how many women received a bonus, and what was their
#  median bonus?
#
#  Run:  python bughunt/riddles/riddle_2_bonus_women.py
#  When it's fixed, it prints EXACTLY this:
#
#    BONUSES OF THE REALM
#    All bonuses paid: 224,370 cr
#    Women who received a bonus: 38
#    Men who received a bonus:   78
#    Women's median bonus: 1,235.00 cr
#    Men's median bonus:   1,785.00 cr

import pandas as pd

df = pd.read_csv("data/thornmere_payroll.csv")

women_got = df[df["gender"] == "F" & df["bonus"] > 0]
men_got = df[(df["gender"] == "M") & (df["bonus"] > 0)]

print("BONUSES OF THE REALM")
print(f"All bonuses paid: {df['bonus'].sum():,.0f} cr")
print("Women who received a bonus:", len(women_got))
print("Men who received a bonus:  ", len(men_got))
print(f"Women's median bonus: {women_got['bonus'].median():,.2f} cr")
print(f"Men's median bonus:   {men_got['bonus'].median():,.2f} cr")
