from ex06_slicing import (
    excel_left, excel_right, excel_mid, department_code, employee_number,
)


def test_excel_left():
    assert excel_left("Brightwell", 6) == "Bright"


def test_excel_right():
    assert excel_right("EMP0042", 4) == "0042"
    assert excel_right("Brightwell", 4) == "well"


def test_excel_mid():
    assert excel_mid("Brightwell", 3, 4) == "ight"
    assert excel_mid("Brightwell", 1, 6) == "Bright"


def test_department_code():
    assert department_code("FIN-0042") == "FIN"
    assert department_code("HR-0007") == "HR"
    assert department_code("SALES-1203") == "SALES"


def test_employee_number():
    assert employee_number("FIN-0042") == 42
    assert employee_number("SALES-1203") == 1203
