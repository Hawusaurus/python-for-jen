# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 07 · RIDDLE 1: "The Name at the Door"
# ==================================================================
#
#  I brought the tool but left its box,
#  then called the box. Nobody knocks.
#  Choose one way in and keep it true:
#  the name you bring is the name you use.
#
#  Mistress Pell found this page pinned inside the Armoury door. It should
#  count the Guard, give the median guard salary and name the roster's ends.
#
#  Run:  python bughunt/riddles/riddle_1_prefix.py
#  When it's fixed, it prints EXACTLY this:
#
#    Guards on the roster: 9
#    Median guard salary: 29,000 cr
#    First and last on the roster: Bram and Thea
#    Spread between highest and lowest: 17,550 cr

from statistics import median

salaries = [24950, 26550, 29000, 31750, 37650, 41900, 28200, 24350, 40450]
names = ["Bram", "Wren", "Osric", "Tamsin", "Jory", "Nye", "Maren", "Ivo", "Thea"]

middle = statistics.median(salaries)
print("Guards on the roster:", len(names))
print(f"Median guard salary: {middle:,} cr")
print("First and last on the roster:", names[0], "and", names[-1])
spread = max(salaries) - min(salaries)
print(f"Spread between highest and lowest: {spread:,} cr")
