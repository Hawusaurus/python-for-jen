"""Exercise 6: Slicing (Excel's LEFT, RIGHT, MID)

Python counts positions from 0, Excel from 1.

    text = "FIN-0042"
             01234567       <- Python positions

    text[0]       "F"         first character
    text[-1]      "2"         last character
    text[0:3]     "FIN"       from 0 up to (NOT including) 3
    text[:3]      "FIN"       same, start can be left out
    text[4:]      "0042"      from 4 to the end
    text[-4:]     "0042"      the last 4
    len(text)     8           (LEN)
    text.find("-")  3         position of "-"  (FIND, minus 1)

Rule of thumb: text[a:b] has b - a characters.
"""


def excel_left(text, n):
    """Like Excel's LEFT(text, n).   excel_left("Brightwell", 6)  ->  "Bright" """
    pass  # TODO: replace this line with your code


def excel_right(text, n):
    """Like Excel's RIGHT(text, n).  excel_right("EMP0042", 4)  ->  "0042"

    Assume n is at least 1.
    """
    pass  # TODO: replace this line with your code


def excel_mid(text, start, n):
    """Like Excel's MID(text, start, n), where start counts from 1 like Excel.

    excel_mid("Brightwell", 3, 4)  ->  "ight"
    """
    pass  # TODO: replace this line with your code


def department_code(employee_ref):
    """The department is everything before the dash.

    department_code("FIN-0042")  ->  "FIN"
    department_code("HR-0007")   ->  "HR"
    """
    pass  # TODO: replace this line with your code


def employee_number(employee_ref):
    """The number after the dash, as an int.

    employee_number("FIN-0042")  ->  42
    """
    pass  # TODO: replace this line with your code
