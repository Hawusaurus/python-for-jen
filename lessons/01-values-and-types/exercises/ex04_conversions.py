"""Exercise 4: Converting between types

Everything read from a file, a form or a CSV arrives as TEXT, even "32500".
You must convert it before you can calculate with it:

    int("42")        ->  42        whole number
    float("37.5")    ->  37.5      decimal number
    str(42)          ->  "42"      back to text

    type(42)         ->  <class 'int'>      ask Python what something is

Python never converts silently, unlike Excel:
    "5" + 3   is an ERROR, not 8.
"""


def parse_salary(text):
    """Turn a salary as exported from the HR system into a number.

    parse_salary("£32,500.00")  ->  32500.0
    parse_salary("£950")        ->  950.0
    """
    pass  # TODO: replace this line with your code


def parse_hours(text):
    """parse_hours(" 22.5 ")  ->  22.5"""
    pass  # TODO: replace this line with your code


def yes_no_to_bool(text):
    """Survey answers: "Yes"/"yes"/" YES " mean True, anything else False.

    yes_no_to_bool(" Yes ")  ->  True
    yes_no_to_bool("no")     ->  False
    """
    pass  # TODO: replace this line with your code


def percent_text_to_fraction(text):
    """parse a percentage as text.

    percent_text_to_fraction("12.5%")  ->  0.125
    percent_text_to_fraction(" 3% ")   ->  0.03
    """
    pass  # TODO: replace this line with your code


def make_employee_id(number):
    """Build an ID: "EMP" followed by the number padded to 4 digits.

    make_employee_id(42)    ->  "EMP0042"
    make_employee_id(1234)  ->  "EMP1234"
    """
    pass  # TODO: replace this line with your code
