# Lesson 07 demo: run from the lesson folder, venv active:  python demo.py

print("--- Three ways to import ---")
import math
from datetime import date, timedelta
import statistics as st

rewards = [260, 550, 620, 2710]
print("math.ceil(8 / 3)     =", math.ceil(8 / 3), "  <- parties of three for 8 heroes")
print("math.floor(8 / 3)    =", math.floor(8 / 3), "  <- full parties")
print("st.mean(rewards)     =", st.mean(rewards), "<- one Wyrm drags it up")
print("st.median(rewards)   =", st.median(rewards))

print("\n--- datetime ---")
start = date.fromisoformat("2014-06-21")
today = date(2026, 4, 5)
print("today - start        =", today - start, "   <- a timedelta, not a number")
print("(today - start).days =", (today - start).days)
print("today + 90 days      =", today + timedelta(days=90))
print(f"formatted            = {start:%d %b %Y} ({start:%A})")

print("\n--- random, repeatable ---")
import random
random.seed(1019)
print("choice:", random.choice(["Wren", "Bram", "Tamsin"]))
print("sample:", random.sample(["Wren", "Bram", "Tamsin", "Osric"], 2))

print("\n--- A module is a file: questkit_demo.py next to this one ---")
with open("questkit_demo.py", "w", encoding="utf-8") as f:
    f.write('"""Demo module."""\n\n'
            'print("questkit_demo is being imported")\n\n'
            'def share(paid, party_size):\n'
            '    """One hero\'s share; the leader takes two."""\n'
            '    return round(paid / (party_size + 1), 2)\n\n'
            'if __name__ == "__main__":\n'
            '    print("self-test:", share(550, 4))\n')
import questkit_demo                   # <- runs the file once: see the print
print("questkit_demo.share(550, 4) =", questkit_demo.share(550, 4))
import questkit_demo                   # <- second import: nothing printed
print("docstring:", questkit_demo.share.__doc__)
print("Now run:  python questkit_demo.py   to see the self-test block")

print("\n--- A package you installed with pip ---")
from rich import print as rprint
rprint("[bold green]rich works[/bold green] inside the venv")
