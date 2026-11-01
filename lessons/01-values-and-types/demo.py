# Lesson 01 demo: run it with  python lessons/01-values-and-types/demo.py
# or copy sections into the REPL one by one.

print("--- Variables ---")
annual_salary = 32500
name = "Maren Ashdown"
print(name, "earns", annual_salary)

print("\n--- Numbers ---")
print("32500 / 12   =", 32500 / 12)
print("32500 // 12  =", 32500 // 12)
print("32500 % 12   =", 32500 % 12)
print("2 ** 10      =", 2 ** 10)
print("2 ^ 10       =", 2 ^ 10, "  <- NOT a power!")
print("0.1 + 0.2    =", 0.1 + 0.2)
print("round(2.5)   =", round(2.5), "  round(3.5) =", round(3.5))

print("\n--- Strings ---")
first = "  mAREN "
last = "ashdown"
clean = first.strip().title() + " " + last.title()
print(repr(clean))
ref = "TRE-0042"
print(ref[0], ref[:3], ref[-4:], len(ref))

print("\n--- Types ---")
print(type(42), type(4.2), type("42"), type(True), type(None))
hours_from_file = "37.5"
print(float(hours_from_file) * 52, "hours per year")
# print("5" + 3)   # <- uncomment to see the TypeError

print("\n--- f-strings ---")
monthly = annual_salary / 12
print(f"Monthly pay: {monthly:,.2f} cr")
print(f"Pay gap: {0.131:.1%}")
print(f"{'Basic pay':<15}{f'{monthly:,.2f} cr':>12}")
print(f"{'Guild dues':<15}{f'{monthly * 0.05:,.2f} cr':>12}")
print(f"TM{42:04d}")

print("\n--- Booleans ---")
salary = 28000
print(salary == 28000, 25000 <= salary <= 32000, salary != 28000)
print(salary > 30000 or name == "Maren Ashdown")
