# Lesson 06 demo: run from the lesson folder with  python demo.py
# It crashes on purpose at the very end. That's the point.

print("--- The parade of errors (caught, so we can see them all) ---")
experiments = [
    ("float('n/a')", lambda: float("n/a")),
    ("float(None)", lambda: float(None)),
    ("{}['reward']", lambda: {}["reward"]),
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
for text in ["1240", "n/a", "610"]:
    try:
        reward = float(text)          # only the risky line
    except ValueError:
        print("could not read", repr(text))
    else:
        total += reward               # only if it worked
    finally:
        checked += 1                  # always
print("total", total, "checked", checked)

print("\n--- raise: refuse nonsense early ---")
def check_difficulty(difficulty):
    if not 1 <= difficulty <= 5:
        raise ValueError(f"difficulty must be 1-5, got {difficulty}")
    return difficulty

for d in [3, 7]:
    try:
        print("OK", check_difficulty(d))
    except ValueError as e:
        print("Rejected:", e)

print("\n--- print debugging: watch the pool ---")
loot = {"Bram": 1240, "Wren": 2480, "Piran": 310, "Biscuit": 0}
for name, share in loot.items():
    pool = 0                          # <- the bug
    if share > 0:
        pool += share
    print("  ", name, share, "pool is now", pool)
print("Loot pool:", pool, "  <- wrong. The print inside the loop shows why.")

print("\n--- An uncaught error: read the traceback bottom-up ---")
heroes = ["Bram", "Wren", "Piran"]
for i in range(4):
    print(heroes[i])
