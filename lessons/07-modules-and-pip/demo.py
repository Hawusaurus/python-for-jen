# Lesson 07 demo: run from the lesson folder, venv active:  python demo.py

print("--- Three ways to import ---")
import math
from datetime import date, timedelta
import statistics as st

print("math.ceil(8 / 3)     =", math.ceil(8 / 3))
print("math.floor(8 / 3)    =", math.floor(8 / 3))
print("st.mean([1, 2, 3])   =", st.mean([1, 2, 3]))
print("st.median([5, 1, 9]) =", st.median([5, 1, 9]))

print("\n--- datetime ---")
start = date.fromisoformat("2017-03-13")
today = date(2026, 4, 5)
print("today - start        =", today - start, "   <- a timedelta, not a number")
print("(today - start).days =", (today - start).days)
print("today + 90 days      =", today + timedelta(days=90))
print(f"formatted            = {start:%d %b %Y} ({start:%A})")

print("\n--- random, repeatable ---")
import random
random.seed(1019)
print("choice:", random.choice(["Pell", "Orrin", "Siv"]))
print("sample:", random.sample(["Pell", "Orrin", "Siv", "Maren"], 2))

print("\n--- A module is a file: paytools_demo.py next to this one ---")
with open("paytools_demo.py", "w", encoding="utf-8") as f:
    f.write('"""Demo module."""\n\n'
            'print("paytools_demo is being imported")\n\n'
            'def monthly(annual):\n'
            '    """Monthly pay."""\n'
            '    return round(annual / 12, 2)\n\n'
            'if __name__ == "__main__":\n'
            '    print("self-test:", monthly(12000))\n')
import paytools_demo                   # <- runs the file once: see the print
print("paytools_demo.monthly(32500) =", paytools_demo.monthly(32500))
import paytools_demo                   # <- second import: nothing printed
print("docstring:", paytools_demo.monthly.__doc__)
print("Now run:  python paytools_demo.py   to see the self-test block")

print("\n--- A package you installed with pip ---")
from rich import print as rprint
rprint("[bold green]rich works[/bold green] inside the venv")
