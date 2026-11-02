# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 06 · RIDDLE 3: "The Silent Sieve"
# ==================================================================
#
#    My net was wide; it caught it all,
#    the fish, the boots, the castle wall.
#    It caught my own mistake as well,
#    and kept it quiet. Who can tell?
#
#  Dalvric's 'unbreakable' salary total for the clean Roll. It never
#  crashes. It also never adds anything up.
#
#  Run:  python bughunt/riddles/riddle_3_sieve.py
#  When it's fixed, it prints EXACTLY this:
#
#    Read 200 rows, skipped 0
#    Total salary: 6,399,850 cr

import csv

total = 0
read = 0
skipped = 0
with open("data/thornmere_payroll.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        try:
            total += float(row["annual salary"])
            read += 1
        except Exception:
            skipped += 1

print(f"Read {read} rows, skipped {skipped}")
print(f"Total salary: {total:,.0f} cr")
