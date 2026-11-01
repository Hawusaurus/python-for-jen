"""Exercise 5: True or False

Comparisons give back True or False (type `bool`):

    ==   equal               (VBA uses = for both assigning AND comparing;
    !=   not equal            Python uses = to assign, == to compare)
    <  <=  >  >=

Combine with  and, or, not  (all lowercase).

Python lets you chain comparisons, which reads like maths:
    25000 <= salary <= 32000

You don't need `if` here: just return the comparison itself.
    return hours >= 35        # already True or False
"""


def is_full_time(weekly_hours):
    """Full time means 35 hours a week or more.

    is_full_time(37.5)  ->  True
    is_full_time(22.5)  ->  False
    """
    pass  # TODO: replace this line with your code


def eligible_for_bonus(months_of_service, performance_rating):
    """Eligible if employed for at least 12 months AND rating is 3 or higher.

    eligible_for_bonus(18, 4)  ->  True
    eligible_for_bonus(6, 5)   ->  False
    """
    pass  # TODO: replace this line with your code


def within_band(salary, band_min, band_max):
    """Is the salary inside the band (limits included)?

    within_band(28000, 25000, 32000)  ->  True
    within_band(32000, 25000, 32000)  ->  True
    within_band(33000, 25000, 32000)  ->  False
    """
    pass  # TODO: replace this line with your code


def needs_review(salary, band_min, band_max):
    """A salary needs review if it is OUTSIDE its band.

    needs_review(33000, 25000, 32000)  ->  True
    """
    pass  # TODO: replace this line with your code


def same_person(name_a, name_b):
    """Do two names match, ignoring capitals and surrounding spaces?

    same_person("Jane Smith", " jane SMITH ")  ->  True
    """
    pass  # TODO: replace this line with your code
