# Lesson 06 demo: run from the lesson folder with  python demo.py
# It crashes on purpose at the very end. That's the point.

print("--- The parade of errors (caught, so we can see them all) ---")
experiments = [
    ("float('n/a')", lambda: float("n/a")),
    ("float(None)", lambda: float(None)),
    ("{}['salary']", lambda: {}["salary"]),
    ("[1, 2, 3][9]", lambda: [1, 2, 3][9]),
    ("1 / 0", lambda: 1 / 0),
    ("open('nope.csv')", lambda: open("nope.csv")),
    ("'abc'.uper()", lambda: "abc".uper()),
]
for label, action in experiments:
    try:
        action()
    except Exception as e:
        print(f"{label:<18} -> {type(e).__name__}: {e}")

print("\n--- try / except / else / finally ---")
total = 0
checked = 0
for text in ["32500", "n/a", "41000"]:
    try:
        salary = float(text)          # only the risky line
    except ValueError:
        print("could not read", repr(text))
    else:
        total += salary               # only if it worked
    finally:
        checked += 1                  # always
print("total", total, "checked", checked)

print("\n--- raise: refuse nonsense early ---")
def check_grade(grade):
    if not 1 <= grade <= 6:
        raise ValueError(f"grade must be 1-6, got {grade}")
    return grade

for g in [3, 7]:
    try:
        print("OK", check_grade(g))
    except ValueError as e:
        print("Rejected:", e)

print("\n--- print debugging: watch the pool ---")
bonuses = {"Pell": 1200, "Orrin": 950, "Siv": 1500, "Biscuit": 0}
for name, bonus in bonuses.items():
    pool = 0                          # <- the bug
    if bonus > 0:
        pool += bonus
    print("  ", name, bonus, "pool is now", pool)
print("Bonus pool:", pool, "  <- wrong. The print inside the loop shows why.")

print("\n--- An uncaught error: read the traceback bottom-up ---")
subjects = ["Pell", "Orrin", "Siv"]
for i in range(4):
    print(subjects[i])
