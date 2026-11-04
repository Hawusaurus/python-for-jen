"""demo_helpers.py: a tiny module, imported by demo.py. Functions compute, scripts print."""


def per_day(paid, days):
    """Crowns actually paid per day spent on the quest."""
    return paid / days


def success_rate(outcomes):
    """Share of 'Success' in a list of outcomes, in %, 1 decimal."""
    wins = sum(1 for o in outcomes if o == "Success")
    return round(wins / len(outcomes) * 100, 1)
