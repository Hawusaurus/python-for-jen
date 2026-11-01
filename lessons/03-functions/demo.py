# Lesson 03 demo: run it with  python demo.py
# or copy sections into the REPL one by one.

print("--- Before: last week's bonus loop ---")
total = 0
for record in "Priya/31000/4/14;Tom/24500/2/30;Biscuit/400/5/3".split(";"):
    name, salary_text, rating_text, months_text = record.split("/")
    salary, rating, months = int(salary_text), int(rating_text), int(months_text)
    if months < 12:
        rate = 0
    elif rating >= 4:
        rate = 0.08
    elif rating == 3:
        rate = 0.04
    else:
        rate = 0
    total += salary * rate
print("total", total)


print("\n--- def and return ---")
def monthly_salary(annual_salary):
    """One twelfth of the salary, in pence."""
    return round(annual_salary / 12, 2)

print(monthly_salary(32500))
print(monthly_salary)            # the recipe, not the result
help(monthly_salary)


print("\n--- return is not print ---")
def money_print(x):
    print(f"£{x:,.2f}")

def money(x):
    return f"£{x:,.2f}"

result = money_print(5)
print("money_print gave back:", result)
print(money(5) + " net")
# print(money_print(5) + " net")   # <- uncomment: TypeError, None + str


print("\n--- After: the napkin as a function ---")
def bonus_rate(months, rating):
    """Gerald's napkin. Change it HERE and only here."""
    if months < 12:
        return 0
    if rating >= 4:
        return 0.08
    if rating == 3:
        return 0.04
    return 0

def bonus(salary, months, rating):
    return salary * bonus_rate(months, rating)

total = 0
for record in "Priya/31000/4/14;Tom/24500/2/30;Biscuit/400/5/3".split(";"):
    name, salary, rating, months = record.split("/")
    total += bonus(int(salary), int(months), int(rating))
print("total", total)


print("\n--- defaults and keywords ---")
def percent(x, decimals=1):
    return f"{x * 100:.{decimals}f}%"

print(percent(0.125), percent(0.125, 0), percent(0.125, decimals=2))


print("\n--- scope ---")
rate = 0.05

def pension(basic):
    deduction = basic * rate      # can read the outer rate
    return deduction

def pension_with_rate(basic, rate):   # its own rate
    return basic * rate

print(pension(2000), pension_with_rate(2000, 0.08), rate)
# print(deduction)   # <- uncomment: NameError, it only exists inside pension()
