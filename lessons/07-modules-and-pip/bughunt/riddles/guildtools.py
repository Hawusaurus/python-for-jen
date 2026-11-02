"""Guild helpers for the Armoury. Import me, don't run me."""


def guild_dues(salary, rate=0.02):
    """Yearly guild dues in crowns, rounded to 2 decimals."""
    return round(salary * rate, 2)


def crowns(amount):
    """Crowns with thousands separators and 2 decimals."""
    return f"{amount:,.2f} cr"
