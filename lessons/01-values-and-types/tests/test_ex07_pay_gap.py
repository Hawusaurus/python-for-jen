from ex07_pay_gap import (
    pay_gap_percent, pence_per_pound, pay_gap_sentence, format_hours,
)


def test_pay_gap_percent():
    assert pay_gap_percent(20.00, 17.40) == 13.0
    assert pay_gap_percent(18.50, 18.90) == -2.2


def test_pence_per_pound():
    assert pence_per_pound(20.00, 17.40) == 87
    assert pence_per_pound(16.00, 14.08) == 88


def test_pay_gap_sentence():
    assert pay_gap_sentence(20.00, 17.40) == (
        "Women earn 87p for every £1 that men earn (gap: 13.0%)."
    )


def test_format_hours():
    assert format_hours(7.75) == "7h 45m"
    assert format_hours(7.5) == "7h 30m"
    assert format_hours(0.25) == "0h 15m"
    assert format_hours(8) == "8h 00m"
