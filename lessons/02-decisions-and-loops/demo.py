# Lesson 02 demo: run it with  python demo.py
# or copy sections into the REPL one by one.

print("--- The napkin as code ---")
quests_done = 14
difficulty = 4
if quests_done < 3:
    rate = 0
elif difficulty >= 4:
    rate = 0.25
elif difficulty == 3:
    rate = 0.10
else:
    rate = 0
print("rate =", rate)
# if difficulty = 3:      # <- uncomment to see the SyntaxError

print("\n--- for: one item at a time ---")
for hero in "Wren,Bram,Thea".split(","):
    print("Welcome back", hero)

print("\n--- range ---")
print(list(range(5)), list(range(1, 6)), list(range(0, 20, 5)))
for day in range(1, 13):
    print(day, end=" ")
print()

print("\n--- several pieces per item ---")
for record in "Wren/3100/4;Bram/3650/3".split(";"):
    name, reward, difficulty = record.split("/")
    print(name, "led a quest worth", reward, "at difficulty", difficulty)

print("\n--- the loop recipe: before / inside / after ---")
total = 0
count = 0
highest = 0
for text in "3100,3650,2800".split(","):
    reward = int(text)
    total += reward
    count += 1
    if reward > highest:
        highest = reward
print("total", total, "count", count, "highest", highest, "average", total / count)

print("\n--- the Dalvric version (total = 0 inside the loop) ---")
for text in "3100,3650,2800".split(","):
    total = 0
    total += int(text)
print("total", total, "  <- only the last one. That's the bug hunt.")

print("\n--- while ---")
bounty = 2800
months = 0
while bounty < 3500:
    bounty *= 1.03
    months += 1
print("months until the Wyrm bounty passes 3,500:", months)

print("\n--- continue and break ---")
for text in "2024,gone,2019,STOP,2015".split(","):
    if text == "gone":
        continue
    if text == "STOP":
        break
    print("joined", text)
