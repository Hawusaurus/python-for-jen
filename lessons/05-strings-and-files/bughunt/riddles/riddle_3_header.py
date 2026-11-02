# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 05 · RIDDLE 3: "One Head Too Many"
# ==================================================================
#
#    Forty souls the scribes set down,
#    yet forty-one the count came round.
#    The first line names, but is not named:
#    a crown upon the roll, unclaimed.
#
#  How many subjects are in the Scriptorium's copy? The scribes say
#  forty. This page disagrees.
#
#  Run:  python bughunt/riddles/riddle_3_header.py
#  When it's fixed, it prints EXACTLY this:
#
#    Lines in the file: 41
#    Subjects in the Scriptorium copy: 40
#    Number of columns: 8
#    Columns: Employee Ref, Name, Guild, Hours, Salary, Bonus, Gender, Start
#    First entry: TM1092 ,"Pennyworth, Nye",Guard,37.5,"41,900 cr",,Male,2018-09-16
#    Last entry: TM1030 ,"amberlyn, osric",Forge,37.5,"29,050 cr",,m,27/06/2022

with open("data/scriptorium_export_messy.csv", encoding="utf-8") as f:
    lines = f.readlines()

columns = lines[0].strip().split(",")
count = len(lines)

print("Lines in the file:", len(lines))
print("Subjects in the Scriptorium copy:", count)
print("Number of columns:", len(columns))
print("Columns:", ", ".join(columns))
print("First entry:", lines[1].strip())
print("Last entry:", lines[-1].strip())
