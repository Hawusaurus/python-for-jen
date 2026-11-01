from ex05_true_or_false import (
    is_full_time, eligible_for_bonus, within_band, needs_review, same_person,
)


def test_is_full_time():
    assert is_full_time(37.5) is True
    assert is_full_time(35) is True
    assert is_full_time(22.5) is False


def test_eligible_for_bonus():
    assert eligible_for_bonus(18, 4) is True
    assert eligible_for_bonus(12, 3) is True
    assert eligible_for_bonus(6, 5) is False
    assert eligible_for_bonus(24, 2) is False


def test_within_band():
    assert within_band(28000, 25000, 32000) is True
    assert within_band(25000, 25000, 32000) is True
    assert within_band(32000, 25000, 32000) is True
    assert within_band(33000, 25000, 32000) is False
    assert within_band(24999, 25000, 32000) is False


def test_needs_review():
    assert needs_review(33000, 25000, 32000) is True
    assert needs_review(28000, 25000, 32000) is False


def test_same_person():
    assert same_person("Jane Smith", " jane SMITH ") is True
    assert same_person("Jane Smith", "Jane Smyth") is False
