"""Exercise 7 (stretch): A first look at the pay gap

UK gender pay gap reporting defines the gap as the difference between men's
and women's average hourly pay, as a percentage of MEN's pay:

    gap % = (male hourly - female hourly) / male hourly * 100

This is a preview of the final project, where we'll compute it from a whole
payroll file with pandas.
"""


def pay_gap_percent(male_hourly, female_hourly):
    """Pay gap in percent, rounded to 1 decimal.

    pay_gap_percent(20.00, 17.40)  ->  13.0
    pay_gap_percent(18.50, 18.90)  ->  -2.2     (negative: women earn more)
    """
    pass  # TODO: replace this line with your code


def pence_per_pound(male_hourly, female_hourly):
    """For every £1 men earn, how many pence do women earn? Whole number.

    pence_per_pound(20.00, 17.40)  ->  87
    """
    pass  # TODO: replace this line with your code


def pay_gap_sentence(male_hourly, female_hourly):
    """pay_gap_sentence(20.00, 17.40)
    ->  "Women earn 87p for every £1 that men earn (gap: 13.0%)."

    Reuse the two functions above.
    """
    pass  # TODO: replace this line with your code


def format_hours(hours):
    """Show decimal hours as hours and minutes, minutes always 2 digits.

    format_hours(7.75)  ->  "7h 45m"
    format_hours(7.5)   ->  "7h 30m"
    format_hours(0.25)  ->  "0h 15m"

    Hint: int(7.75) is 7. Work out the minutes from what's left over.
    """
    pass  # TODO: replace this line with your code
