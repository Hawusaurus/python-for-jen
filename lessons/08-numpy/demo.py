# Lesson 08 demo: run from the lesson folder with  python demo.py
# or copy sections into the REPL one by one.
import csv
import numpy as np

salaries = []
hours = []
genders = []
with open("data/thornmere_payroll.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        salaries.append(float(row["annual_salary"]))
        hours.append(float(row["weekly_hours"]))
        genders.append(row["gender"])

print("--- The loop vs the line ---")
monthly_loop = []
for s in salaries:
    monthly_loop.append(s / 12)
salaries = np.array(salaries)
hours = np.array(hours)
genders = np.array(genders)
monthly = salaries / 12
print(monthly_loop[:3])
print(monthly[:3])
print(salaries.shape, salaries.dtype)

print("\n--- Summaries ---")
print(salaries.min(), salaries.max(), round(salaries.mean(), 2), salaries.sum())
print(np.median(salaries))
print(np.percentile(salaries, 75))
print(np.percentile(salaries, [25, 50, 75]))
print(salaries.mean)   # <- the classic mistake: no brackets

print("\n--- Masks ---")
high = salaries > 40000
print(high[:5])
print("count:", high.sum(), " share:", high.mean())
print("their mean:", salaries[high].mean())
women = genders == "F"
print("women's mean:", salaries[women].mean().round(2))
print("high-earning women:", (high & women).sum())
# print((salaries > 40000) and (genders == "F"))   # <- uncomment to see the error

print("\n--- Axis ---")
pay = np.array([
    [2800, 2800, 2800, 2900, 2900, 2900],
    [3100, 3100, 3100, 3100, 3300, 3300],
    [2500, 2500, 2600, 2600, 2600, 2600],
])
print(pay.sum(), pay.sum(axis=0), pay.sum(axis=1))
print(pay[1, 3], pay[:, 2])

print("\n--- The gap in four lines ---")
hourly = salaries / 52 / hours
m = hourly[genders == "M"].mean()
f = hourly[genders == "F"].mean()
print(f"Mean gender pay gap: {(m - f) / m * 100:.1f}%")
