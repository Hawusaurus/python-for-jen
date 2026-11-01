# ==================================================================
#  DAVE'S LEFTOVERS #1: "payroll_helpers_DO_NOT_TOUCH.py"
# ==================================================================
#
# In 2019 Dave got excited about Python and translated a bit of
# MACRO-9000. Then he left. Since then:
#   - the raise calculation crashes,
#   - for three months nobody at Brightwell paid any income tax
#     (HMRC has questions),
#   - and the payslip line looks... almost right. Priya says "almost".
#
# THREE bugs:
#   one crashes (read the error message!),
#   one gives a wrong number without crashing,
#   one is so small you'll have to compare letter by letter.
#
# Run it from inside the lesson folder:
#   python bughunt/payroll_bug.py
#
# When it's fixed, it prints EXACTLY this:
#
#   Salary after 2 years: £31,827.00
#   Omar Khan: gross £2345.50, tax £469.10, net £1876.40
#
# Fix ONE bug per commit and explain it in the message, like a detective:
#   git commit -m "Bug hunt: <what was wrong and why>"


# --- Part 1: yearly raises, compounded ---
salary = 30000
raise_percent = 3
years = 2

growth = 1 + raise_percent / 100
new_salary = round(salary * growth ^ years, 2)
print(f"Salary after {years} years: £{new_salary:,.2f}")


# --- Part 2: one payslip line ---
name = "Omar Khan"
gross_monthly = 2345.5
tax_percent = 20

tax = gross_monthly * (tax_percent // 100)
net = gross_monthly - tax
print(f"{name}: gross £{gross_monthly}, tax £{tax:.2f}, net £{net:.2f}")
