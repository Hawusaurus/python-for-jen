"""Exercise 1: Pay maths

Python's arithmetic, compared with Excel:

    +  -  *  /      same as Excel
    //              whole-number division: 17 // 7 is 2   (like INT(17/7))
    %               remainder:             17 % 7  is 3   (like MOD(17, 7))
    **              power:                 2 ** 3  is 8   (Excel: 2^3)
    round(x, 2)     like ROUND(x, 2)

WARNING: in Python, ^ is NOT "to the power of". Always use **.

Replace each `pass` with your code. A function hands its answer back with
`return`, just like assigning to the function name in a VBA Function.
"""


def monthly_salary(annual_salary):
    """Monthly salary from an annual salary, rounded to 2 decimal places.

    monthly_salary(32500)  ->  2708.33
    """
    pass  # TODO: replace this line with your code


def pro_rata_salary(full_time_salary, weekly_hours, full_time_hours):
    """Salary of a part-timer: full-time salary scaled by hours worked.
    Round to 2 decimal places.

    pro_rata_salary(30000, 22.5, 37.5)  ->  18000.0
    """
    pass  # TODO: replace this line with your code


def hourly_rate(annual_salary, weekly_hours):
    """Hourly rate: annual salary / 52 weeks / weekly hours, rounded to 2 dp.

    hourly_rate(30000, 37.5)  ->  15.38
    """
    pass  # TODO: replace this line with your code


def full_weeks(days):
    """How many full weeks are in a number of days?

    full_weeks(17)  ->  2
    """
    pass  # TODO: replace this line with your code


def remaining_days(days):
    """How many days are left over after the full weeks?

    remaining_days(17)  ->  3
    """
    pass  # TODO: replace this line with your code


def salary_after_raises(salary, raise_percent, years):
    """Salary after `years` yearly raises of `raise_percent` percent each,
    compounded (each raise is on top of the previous one). Round to 2 dp.

    salary_after_raises(30000, 3, 2)  ->  31827.0
    """
    pass  # TODO: replace this line with your code
