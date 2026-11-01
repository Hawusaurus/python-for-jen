"""Exercise 2: Names and text

Text in Python is called a *string* (type `str`). Useful tools:

    "Jane" + " " + "Smith"     joins strings          (Excel/VBA: &)
    "Jane"[0]                  first character, "J"   (counting starts at 0!)
    "  hi  ".strip()           remove spaces at both ends   (TRIM)
    "Hi".upper() / .lower()    UPPER / LOWER
    "jANE".title()             "Jane"                       (PROPER)
    "a-b".replace("-", "")     "ab"                         (SUBSTITUTE)

Methods can be chained:  "  emp-1 ".strip().upper()  ->  "EMP-1"
"""

COMPANY_DOMAIN = "brightwell.co.uk"


def full_name(first, last):
    """Join first and last name with a space.

    full_name("Jane", "Smith")  ->  "Jane Smith"
    """
    pass  # TODO: replace this line with your code


def initials(first, last):
    """Initials with dots.

    initials("Jane", "Smith")  ->  "J.S."
    """
    pass  # TODO: replace this line with your code


def tidy_name(name):
    """Fix messy capitalisation and surrounding spaces.

    tidy_name("  jANE smITH ")  ->  "Jane Smith"
    """
    pass  # TODO: replace this line with your code


def email_address(first, last):
    """Company email: first.last@brightwell.co.uk, all lowercase,
    with any spaces inside the names removed.

    email_address("Jane", "Smith")        ->  "jane.smith@brightwell.co.uk"
    email_address("Anne Marie", "Brown")  ->  "annemarie.brown@brightwell.co.uk"

    Use the COMPANY_DOMAIN variable defined above.
    """
    pass  # TODO: replace this line with your code


def clean_employee_id(raw_id):
    """Employee IDs come from a messy export. Clean them up:
    remove surrounding spaces, make uppercase, remove dashes.

    clean_employee_id("  emp-0042 ")  ->  "EMP0042"
    """
    pass  # TODO: replace this line with your code
