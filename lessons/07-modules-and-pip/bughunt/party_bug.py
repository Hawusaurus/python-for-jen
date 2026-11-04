# ==================================================================
#  PAGES FROM THE GRIMOIRE, PAGE 7: "party_planner_v3.py"
# ==================================================================
#
# Dalvric's party planner for the guild's spring muster. He wrote it
# the week he discovered "import" and was, by all accounts, very
# excited. It has never run.
#
# THREE bugs:
#   one crashes on the very first line (read the error!),
#   one rounds the wrong way, so one hero is left standing in the yard,
#   one prints something that is technically true but not what was asked.
#
# Run it from inside the lesson folder:
#   python bughunt/party_bug.py
#
# When it's fixed, it prints EXACTLY this:
#
#   Heroes at the muster: 9
#   Average level: 8.33
#   Parties of 4 needed: 3
#   Days since Dalvric sailed west: 367653
#
# Fix ONE bug per commit and explain it in the message.

import Math
import datetime
from statistics import mean

levels = [8, 3, 5, 4, 19, 11, 7, 6, 12]

print("Heroes at the muster:", len(levels))
print(f"Average level: {mean(levels):.2f}")

parties = Math.floor(len(levels) / 4)
print("Parties of 4 needed:", parties)

dalvric_left = datetime.date(1019, 8, 30)
today = datetime.date(2026, 4, 5)
print("Days since Dalvric sailed west:", today - dalvric_left)
