# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 04 · RIDDLE 4: "The Echo in the Ledger"
# ==================================================================
#
#    I made a copy, so I thought,
#    and changed the copy as I ought.
#    But every crown I gave the new,
#    the old one somehow gained it too.
#
#  Lady Siv's 3 % raise, applied to a copy so the old wages can be
#  shown next to the new ones. The old wages column is lying.
#
#  Run:  python bughunt/riddles/riddle_4_echo.py
#  When it's fixed, it prints EXACTLY this:
#
#    Bram   24,500 cr ->  25,235 cr
#    Wren   29,000 cr ->  29,870 cr
#    Hild   31,000 cr ->  31,930 cr
#    Extra cost per year: 2,535 cr

names = ["Bram", "Wren", "Hild"]
salaries = [24500, 29000, 31000]
rise = 1.03

raised = salaries
for i in range(len(raised)):
    raised[i] = round(raised[i] * rise)

for i in range(len(names)):
    print(f"{names[i]:<6}{salaries[i]:>7,} cr -> {raised[i]:>7,} cr")

extra = sum(raised) - sum(salaries)
print(f"Extra cost per year: {extra:,} cr")
