"""demo_helpers.py: a tiny module, imported by demo.py. Functions compute, scripts print."""


def gap_percent(men, women):
    """UK definition: (men - women) / men * 100, 1 decimal."""
    return float(round((men - women) / men * 100, 1))


def hourly_rate(annual_salary, weekly_hours):
    """Hourly rate from an annual salary."""
    return annual_salary / 52 / weekly_hours
