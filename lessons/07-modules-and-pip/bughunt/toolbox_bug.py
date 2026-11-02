# ==================================================================
#  PAGES FROM THE GRIMOIRE, PAGE 7: "patrol_planner_v3.py"
# ==================================================================
#
# Dalvric's patrol planner for the Royal Guard. He wrote it the week he
# discovered "import" and was, by all accounts, very excited. It has
# never run.
#
# THREE bugs:
#   one crashes on the very first line (read the error!),
#   one rounds the wrong way, so one patrol never gets a captain,
#   one prints something that is technically true but not what was asked.
#
# Run it from inside the lesson folder:
#   python bughunt/toolbox_bug.py
#
# When it's fixed, it prints EXACTLY this:
#
#   Guards: 9
#   Average salary: 31,644.44 cr
#   Patrols of 4 needed: 3
#   Days since Dalvric sailed west: 367653
#
# Fix ONE bug per commit and explain it in the message.

import Math
import datetime
from statistics import mean

salaries = [24950, 26550, 29000, 31750, 37650, 41900, 28200, 24350, 40450]

print("Guards:", len(salaries))
print(f"Average salary: {mean(salaries):,.2f} cr")

patrols = Math.floor(len(salaries) / 4)
print("Patrols of 4 needed:", patrols)

dalvric_left = datetime.date(1019, 8, 30)
today = datetime.date(2026, 4, 5)
print("Days since Dalvric sailed west:", today - dalvric_left)
