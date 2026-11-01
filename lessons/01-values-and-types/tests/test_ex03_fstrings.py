from ex03_fstrings import (
    welcome_message, money, as_percent, salary_band, payslip_line,
)


def test_welcome_message():
    assert welcome_message("Jane", 2019) == "Welcome, Jane! You joined in 2019."


def test_money():
    assert money(2708.333) == "£2,708.33"
    assert money(50) == "£50.00"
    assert money(1234567.891) == "£1,234,567.89"


def test_as_percent():
    assert as_percent(0.125) == "12.5%"
    assert as_percent(0.08) == "8.0%"


def test_salary_band():
    assert salary_band(25000, 32000) == "£25,000 to £32,000"


def test_payslip_line():
    assert payslip_line("Basic pay", 2708.333) == "Basic pay         £2,708.33"
    assert payslip_line("Pension", 135.42) == "Pension             £135.42"


def test_payslip_line_has_fixed_width():
    assert len(payslip_line("Tax", 1.0)) == 27
