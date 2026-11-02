# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 05 · RIDDLE 1: "The Capital Mistake"
# ==================================================================
#
#    I called the column by its name,
#    but gave it a crown it never claimed.
#    The header's humble, small and plain:
#    speak to it softly, then try again.
#
#  Mistress Pell wants the first entry on the Roll of the Realm.
#
#  Run:  python bughunt/riddles/riddle_1_capital.py
#  When it's fixed, it prints EXACTLY this:
#
#    Entries on the roll: 200
#    First on the roll: Nye Pennyworth
#    Guild: Guard
#    Title: Master
#    Hours a week: 37.5
#    Salary: 41900 cr
#    Started: 2018-09-16

import csv

with open("data/thornmere_payroll.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

print("Entries on the roll:", len(rows))

first = rows[0]
print("First on the roll:", first["first_name"], first["last_name"])
print("Guild:", first["Department"])
print("Title:", first["job_title"])
print("Hours a week:", first["weekly_hours"])
print("Salary:", first["annual_salary"], "cr")
print("Started:", first["start_date"])
