# Lesson 04 demo: run it with  python demo.py
# or copy sections into the REPL one by one.

print("--- A list is a column ---")
staff = ["Priya Patel", "Mo Khan", "Siobhan Walsh"]
print(staff[0], "|", staff[-1], "|", staff[1:3], "|", len(staff))
staff.append("Tom Brown")
print(staff)
print("Mo Khan" in staff, "Dave" in staff)

salaries = [31000, 36500, 28000, 24500]
print(sum(salaries), max(salaries), min(salaries), sum(salaries) / len(salaries))
print(sorted(salaries, reverse=True)[:2])
print("salaries.sort() returns:", salaries.sort(), "  <- Dave printed this once")
print(salaries)

print("\n--- The loop recipe, with a list ---")
above = []
for s in salaries:
    if s > 30000:
        above.append(s)
print(above)

print("\n--- A dictionary is a row with headers ---")
employee = {"name": "Priya Patel", "department": "Payroll", "salary": 31000}
print(employee["name"], employee["salary"])
employee["salary"] = 32000
employee["rating"] = 4
print(employee)
# print(employee["Name"])     # <- uncomment: KeyError. Keys are exact.
print(employee.get("bonus", 0), "  <- .get: XLOOKUP with an if-not-found")
for key, value in employee.items():
    print(f"  {key:<12}{value}")

print("\n--- A dictionary is also a lookup table ---")
managers = {"IT": "Mo Khan", "Payroll": "Priya Patel"}
print(managers["IT"], "|", managers.get("HR", "no manager yet"))

print("\n--- A list of dictionaries is a table ---")
staff = [
    {"name": "Priya Patel", "dept": "Payroll", "salary": 31000},
    {"name": "Mo Khan", "dept": "IT", "salary": 36500},
    {"name": "Chloe Evans", "dept": "IT", "salary": 29000},
]
total = 0
top = staff[0]
for person in staff:
    total += person["salary"]
    if person["salary"] > top["salary"]:
        top = person
print("total", total, "| top", top["name"])

print("\n--- COUNTIF: counting with a dictionary ---")
count = {}
for person in staff:
    dept = person["dept"]
    if dept in count:
        count[dept] += 1
    else:
        count[dept] = 1
print(count)

print("\n--- Group by: dictionary of lists ---")
by_dept = {}
for person in staff:
    dept = person["dept"]
    if dept not in by_dept:
        by_dept[dept] = []
    by_dept[dept].append(person["salary"])
print(by_dept)
for dept, values in by_dept.items():
    print(f"  {dept:<9} average £{sum(values) / len(values):,.2f}")
