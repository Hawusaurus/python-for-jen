# ==================================================================
#  DAVE'S LEFTOVERS #7: "team_planner_v3.py"
# ==================================================================
#
# Dave's team planner. He wrote it the week he discovered "import" and
# was, by all accounts, very excited. It has never run.
#
# THREE bugs:
#   one crashes on the very first line (read the error!),
#   one rounds the wrong way, so one team never gets a desk,
#   one prints something that is technically true but not what was asked.
#
# Run it from inside the lesson folder:
#   python bughunt/toolbox_bug.py
#
# When it's fixed, it prints EXACTLY this:
#
#   Staff: 9
#   Average salary: £31,644.44
#   Teams of 4 needed: 3
#   Days since Dave left: 2410
#
# Fix ONE bug per commit and explain it in the message.

import Math
import datetime
from statistics import mean

salaries = [24950, 26550, 29000, 31750, 37650, 41900, 28200, 24350, 40450]

print("Staff:", len(salaries))
print(f"Average salary: £{mean(salaries):,.2f}")

teams = Math.floor(len(salaries) / 4)
print("Teams of 4 needed:", teams)

dave_left = datetime.date(2019, 8, 30)
today = datetime.date(2026, 4, 5)
print("Days since Dave left:", today - dave_left)
