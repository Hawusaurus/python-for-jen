"""Exercise 3: f-strings (number formats, the Python way)

An f-string has an f before the quote and puts values in {curly braces}:

    name = "Jane"
    f"Hello, {name}!"            ->  "Hello, Jane!"

After a colon you can add a format, much like Excel's custom number formats:

    f"{2708.333:.2f}"            ->  "2708.33"      (2 decimals)
    f"{32500:,}"                 ->  "32,500"       (thousands separator)
    f"{2708.333:,.2f}"           ->  "2,708.33"     (both)
    f"{0.125:.1%}"               ->  "12.5%"        (percent, 1 decimal)
    f"{'abc':<6}"                ->  "abc   "       (left-align in 6 chars)
    f"{'abc':>6}"                ->  "   abc"       (right-align in 6 chars)
    f"{7:03d}"                   ->  "007"          (pad with zeros)
"""


def welcome_message(name, start_year):
    """welcome_message("Jane", 2019)  ->  "Welcome, Jane! You joined in 2019." """
    pass  # TODO: replace this line with your code


def money(amount):
    """Format as pounds with thousands separator and 2 decimals.

    money(2708.333)  ->  "£2,708.33"
    money(50)        ->  "£50.00"
    """
    pass  # TODO: replace this line with your code


def as_percent(fraction):
    """Format a fraction as a percentage with 1 decimal.

    as_percent(0.125)  ->  "12.5%"
    as_percent(0.08)   ->  "8.0%"
    """
    pass  # TODO: replace this line with your code


def salary_band(band_min, band_max):
    """salary_band(25000, 32000)  ->  "£25,000 to £32,000"

    No decimals here: use the format  ,.0f
    """
    pass  # TODO: replace this line with your code


def payslip_line(label, amount):
    """One line of a payslip: the label left-aligned in 15 characters,
    then the amount formatted like money() right-aligned in 12 characters.

    payslip_line("Basic pay", 2708.333)  ->  "Basic pay         £2,708.33"
                                              |<--- 15 --->||<--- 12 -->|

    Tip: you can call money() from inside this function.
    """
    pass  # TODO: replace this line with your code
