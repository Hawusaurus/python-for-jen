# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 05 · RIDDLE 5: "The Leaning Slash"
# ==================================================================
#
#    A slash that leans the wrong way round
#    turns letters into empty sound.
#    And when you whisper what you seek,
#    the roll that shouts will never speak.
#
#  Lady Siv wants the number of women in each guild. This page
#  finds no file, and then no women. (Two bugs.)
#
#  Run:  python bughunt/riddles/riddle_5_whisper.py
#  When it's fixed, it prints EXACTLY this:
#
#    Apothecary    8
#    Clockworks    7
#    Forge        20
#    Guard        14
#    Harbour       6
#    Kitchens      8
#    Library      11
#    Treasury      9
#    All guilds   83

import csv

women = {}
with open("data\thornmere_payroll.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        if row["gender"] == "f":
            guild = row["department"]
            women[guild] = women.get(guild, 0) + 1

for guild in sorted(women):
    print(f"{guild:<12}{women[guild]:>3}")
print(f"{'All guilds':<12}{sum(women.values()):>3}")
