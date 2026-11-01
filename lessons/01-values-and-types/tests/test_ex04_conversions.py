from ex04_conversions import (
    parse_salary, parse_hours, yes_no_to_bool,
    percent_text_to_fraction, make_employee_id,
)


def test_parse_salary():
    assert parse_salary("£32,500.00") == 32500.0
    assert parse_salary("£950") == 950.0


def test_parse_salary_returns_a_number():
    assert type(parse_salary("£1,000")) is float


def test_parse_hours():
    assert parse_hours(" 22.5 ") == 22.5
    assert parse_hours("40") == 40.0


def test_yes_no_to_bool():
    assert yes_no_to_bool(" Yes ") is True
    assert yes_no_to_bool("YES") is True
    assert yes_no_to_bool("no") is False
    assert yes_no_to_bool("maybe") is False


def test_percent_text_to_fraction():
    assert percent_text_to_fraction("12.5%") == 0.125
    assert percent_text_to_fraction(" 3% ") == 0.03


def test_make_employee_id():
    assert make_employee_id(42) == "EMP0042"
    assert make_employee_id(1234) == "EMP1234"
