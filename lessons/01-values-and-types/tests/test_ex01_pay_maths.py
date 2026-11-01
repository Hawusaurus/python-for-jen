from ex01_pay_maths import (
    monthly_salary, pro_rata_salary, hourly_rate,
    full_weeks, remaining_days, salary_after_raises,
)


def test_monthly_salary():
    assert monthly_salary(32500) == 2708.33
    assert monthly_salary(24000) == 2000.0


def test_pro_rata_salary():
    assert pro_rata_salary(30000, 22.5, 37.5) == 18000.0
    assert pro_rata_salary(41000, 30, 37.5) == 32800.0


def test_hourly_rate():
    assert hourly_rate(30000, 37.5) == 15.38
    assert hourly_rate(52000, 40) == 25.0


def test_full_weeks():
    assert full_weeks(17) == 2
    assert full_weeks(6) == 0
    assert full_weeks(14) == 2


def test_remaining_days():
    assert remaining_days(17) == 3
    assert remaining_days(14) == 0


def test_full_weeks_returns_whole_number():
    assert type(full_weeks(17)) is int, "Use // instead of /"


def test_salary_after_raises():
    assert salary_after_raises(30000, 3, 2) == 31827.0
    assert salary_after_raises(30000, 3, 0) == 30000.0
    assert salary_after_raises(25000, 2, 3) == 26530.2
