# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 03 · RIDDLE 1: "The Spell Cast Too Early"
# ==================================================================
#
#  You called my name before my birth,
#  and wondered what my words were worth;
#  the scroll is read from top to toe:
#  first write me down, then let me go.
#
#  Mistress Pell's monthly pay helper.
#  Dalvric put the important line at the very top, where he could see it.
#
#  Run:  python bughunt/riddles/riddle_1_early.py
#  When it's fixed, it prints EXACTLY this:
#
#    Maren's monthly pay: 2708.33 cr
#    Bram's monthly pay: 3041.67 cr
#    Bram's weekly pay: 701.92 cr
#    Wren's monthly pay: 2500.0 cr

print("Maren's monthly pay:", monthly(32500), "cr")


def monthly(annual_salary):
    """Annual salary -> monthly pay, rounded to 2 decimals."""
    return round(annual_salary / 12, 2)




def weekly(annual_salary):
    """Annual salary -> weekly pay, rounded to 2 decimals."""
    return round(annual_salary / 52, 2)


print("Bram's monthly pay:", monthly(36500), "cr")
print("Bram's weekly pay:", weekly(36500), "cr")
print("Wren's monthly pay:", monthly(30000), "cr")
