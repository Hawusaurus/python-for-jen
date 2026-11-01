# Lesson 02 demo: run it with  python demo.py
# or copy sections into the REPL one by one.

print("--- The napkin as code ---")
months = 14
rating = 4
if months < 12:
    rate = 0
elif rating >= 4:
    rate = 0.08
elif rating == 3:
    rate = 0.04
else:
    rate = 0
print("rate =", rate)
# if rating = 3:      # <- uncomment to see the SyntaxError

print("\n--- for: one item at a time ---")
for name in "Orrin,Pell,Siv".split(","):
    print("Hello", name)

print("\n--- range ---")
print(list(range(5)), list(range(1, 6)), list(range(0, 20, 5)))
for month in range(1, 13):
    print(month, end=" ")
print()

print("\n--- several pieces per item ---")
for record in "Orrin/36500/3;Pell/31000/4".split(";"):
    name, salary, rating = record.split("/")
    print(name, "earns", salary, "rated", rating)

print("\n--- the loop recipe: before / inside / after ---")
total = 0
count = 0
highest = 0
for text in "31000,36500,28000".split(","):
    salary = int(text)
    total += salary
    count += 1
    if salary > highest:
        highest = salary
print("total", total, "count", count, "highest", highest, "average", total / count)

print("\n--- the Dalvric version (total = 0 inside the loop) ---")
for text in "31000,36500,28000".split(","):
    total = 0
    total += int(text)
print("total", total, "  <- only the last one. That's the bug hunt.")

print("\n--- while ---")
salary = 28000
years = 0
while salary < 35000:
    salary *= 1.03
    years += 1
print("years to 35k:", years)

print("\n--- continue and break ---")
for text in "2024,left,2019,STOP,2015".split(","):
    if text == "left":
        continue
    if text == "STOP":
        break
    print("start year", text)
