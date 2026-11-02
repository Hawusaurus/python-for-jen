# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 03 · RIDDLE 3: "The Raise That Never Came"
# ==================================================================
#
#  I did the sums, I did them right,
#  then handed back the old, not bright;
#  the new was made, then left behind:
#  return the one you meant to find.
#
#  Queen Aldara promised every guard a 3% raise.
#  Dalvric's raise function works very hard and changes nothing.
#
#  Run:  python bughunt/riddles/riddle_3_raise.py
#  When it's fixed, it prints EXACTLY this:
#
#    Guard: Bram Ironfoot
#    Before: 31,000.00 cr
#    After a 3% raise: 31,930.00 cr
#    After two raises: 32,887.90 cr

def with_raise(salary, percent):
    """Salary after a raise of `percent` %."""
    new_salary = salary * (1 + percent / 100)
    return round(salary, 2)


def money(amount):
    """Crowns with thousands separator and 2 decimals."""
    return f"{amount:,.2f} cr"


guard = "Bram Ironfoot"
salary = 31000
print("Guard:", guard)
print("Before:", money(salary))
print("After a 3% raise:", money(with_raise(salary, 3)))
print("After two raises:", money(with_raise(with_raise(salary, 3), 3)))
