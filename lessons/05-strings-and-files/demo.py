# Lesson 05 demo: run from the lesson folder with  python demo.py

print("--- Split and join ---")
name_field = "Hawkridge, Wren"
last, first = name_field.split(", ")
print(first, last)
words = "Copying   the notice   board".split()
print(words)
print("-".join(words))
print(int("4 heroes".split()[0]), int("3/5".split("/")[0]))

print("\n--- Write a file, read it back ---")
with open("my_work/demo_note.txt", "w", encoding="utf-8") as f:
    f.write("Notices copied: 1019\n")
    f.write("Ink pots used: 203\n")
with open("my_work/demo_note.txt", encoding="utf-8") as f:
    for line in f:
        print(repr(line))          # see the \n at the end

print("\n--- Why not split(',') on a CSV? ---")
line = '0015,RID THE MILL OF WYRM AT CINDERHALL MINE,Northern Wilds,5/5,"4,540 cr",5,30/01/2024,failed'
print(len(line.split(",")), "pieces with split(',')  <- wrong, the reward has a comma")

print("\n--- csv.DictReader ---")
import csv
with open("data/notice_board_messy.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    print(reader.fieldnames)
    for row in list(reader)[:3]:
        print(repr(row["Quest"]), "|", row["Region"], "|", repr(row["Reward"]))

print("\n--- Everything is text until you convert it ---")
reward_text = "4,540 cr"
reward = float(reward_text.replace("cr", "").replace(",", "").strip())
print(reward_text, "->", reward, type(reward))

print("\n--- csv.DictWriter ---")
rows = [{"quest_id": "Q0001", "region": "Thornwood"}, {"quest_id": "Q0002", "region": "Saltmarsh"}]
with open("my_work/demo_out.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["quest_id", "region"])
    w.writeheader()
    w.writerows(rows)
print(open("my_work/demo_out.csv", encoding="utf-8").read(), end="")

print("\n--- pathlib ---")
from pathlib import Path
for p in sorted(Path("data").glob("*.csv")):
    print(p.name, p.stat().st_size, "bytes")
print(Path("my_work") / "demo_out.csv", "exists:", (Path("my_work") / "demo_out.csv").exists())
