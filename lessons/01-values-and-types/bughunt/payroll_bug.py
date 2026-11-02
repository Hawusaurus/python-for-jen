# ==================================================================
#  PAGES FROM THE GRIMOIRE, PAGE 1: "wage_helpers_DO_NOT_TOUCH.py"
# ==================================================================
#
# Shortly before he sailed west, Dalvric grew excited about Python and
# translated a corner of the Grimoire. Then he left. Since then:
#   - the raise calculation crashes,
#   - for three months nobody in the realm paid any crown tax
#     (the Royal Auditors have questions),
#   - and the pay scroll line looks... almost right. Mistress Pell says "almost".
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
#   Salary after 2 years: 31,827.00 cr
#   Osric Kettleby: gross 2345.50 cr, tax 469.10 cr, net 1876.40 cr
#
# Fix ONE bug per commit and explain it in the message, like a detective:
#   git commit -m "Bug hunt: <what was wrong and why>"


# --- Part 1: yearly raises, compounded ---
salary = 30000
raise_percent = 3
years = 2

growth = 1 + raise_percent / 100
new_salary = round(salary * growth ^ years, 2)
print(f"Salary after {years} years: {new_salary:,.2f} cr")


# --- Part 2: one pay scroll line ---
name = "Osric Kettleby"
gross_monthly = 2345.5
tax_percent = 20

tax = gross_monthly * (tax_percent // 100)
net = gross_monthly - tax
print(f"{name}: gross {gross_monthly} cr, tax {tax:.2f} cr, net {net:.2f} cr")
