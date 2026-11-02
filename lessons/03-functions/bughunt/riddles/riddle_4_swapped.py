# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 03 · RIDDLE 4: "The Swapped Scales"
# ==================================================================
#
#  Put him on the left, put her on the right,
#  the scale tips over in plain sight;
#  the order of the words you pass
#  is the order that they take their place.
#
#  The pay gap for the Privy Council: gap = (men - women) / men.
#  Dalvric's version says women earn more. They don't.
#
#  Run:  python bughunt/riddles/riddle_4_swapped.py
#  When it's fixed, it prints EXACTLY this:
#
#    Men: 20.0 cr/h  Women: 17.4 cr/h
#    Gap: 13.0 %
#    Men are paid 13.0% more per hour.

def gap_percent(male_hourly, female_hourly):
    """Pay gap in %, as a share of men's pay, rounded to 1 decimal."""
    return round((male_hourly - female_hourly) / male_hourly * 100, 1)


def gap_sentence(gap):
    """One sentence a queen can say out loud."""
    if gap > 0:
        return f"Men are paid {gap}% more per hour."
    return f"Women are paid {-gap}% more per hour."


men = 20.00
women = 17.40
print("Men:", men, "cr/h  Women:", women, "cr/h")
gap = gap_percent(women, men)
print("Gap:", gap, "%")
print(gap_sentence(gap))
