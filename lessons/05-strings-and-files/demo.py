# Lesson 05 demo: run from the lesson folder with  python demo.py

print("--- Split and join ---")
name_field = "Robinson, Max"
last, first = name_field.split(", ")
print(first, last)
words = "Keeping   Britain dry".split()
print(words)
print("-".join(words))

print("\n--- Write a file, read it back ---")
with open("my_work/demo_note.txt", "w", encoding="utf-8") as f:
    f.write("Umbrellas sold: 1952\n")
    f.write("Rainy days: 203\n")
with open("my_work/demo_note.txt", encoding="utf-8") as f:
    for line in f:
        print(repr(line))          # see the \n at the end

print("\n--- Why not split(',') on a CSV? ---")
line = '" EMP1092 ","Robinson, Max",Sales,37.5,"£41,900",,Male,2018-09-16'
print(len(line.split(",")), "pieces with split(',')  <- wrong, the name has a comma")

print("\n--- csv.DictReader ---")
import csv
with open("data/staff_export_messy.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    print(reader.fieldnames)
    for row in list(reader)[:3]:
        print(row["Employee Ref"], "|", row["Name"], "|", repr(row["Salary"]))

print("\n--- Everything is text until you convert it ---")
salary_text = "£41,900"
salary = float(salary_text.replace("£", "").replace(",", ""))
print(salary_text, "->", salary, type(salary))

print("\n--- csv.DictWriter ---")
rows = [{"id": "EMP1092", "name": "Max Robinson"}, {"id": "EMP1178", "name": "Imogen Shaw"}]
with open("my_work/demo_out.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["id", "name"])
    w.writeheader()
    w.writerows(rows)
print(open("my_work/demo_out.csv", encoding="utf-8").read(), end="")

print("\n--- pathlib ---")
from pathlib import Path
for p in sorted(Path("data").glob("*.csv")):
    print(p.name, p.stat().st_size, "bytes")
print(Path("my_work") / "demo_out.csv", "exists:", (Path("my_work") / "demo_out.csv").exists())
