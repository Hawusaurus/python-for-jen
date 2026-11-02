# Lesson 04 demo: run it with  python demo.py
# or copy sections into the REPL one by one.

print("--- A list is a column ---")
heroes = ["Bram Ironfoot", "Wren Hawkridge", "Tamsin Larkspur"]
print(heroes[0], "|", heroes[-1], "|", heroes[1:3], "|", len(heroes))
heroes.append("Piran Dovecote")
print(heroes)
print("Wren Hawkridge" in heroes, "Dalvric" in heroes)

rewards = [320, 1240, 150, 610]
print(sum(rewards), max(rewards), min(rewards), sum(rewards) / len(rewards))
print(sorted(rewards, reverse=True)[:2])
print("rewards.sort() returns:", rewards.sort(), "  <- Dalvric printed this once")
print(rewards)

print("\n--- The loop recipe, with a list ---")
big = []
for r in rewards:
    if r > 500:
        big.append(r)
print(big)

print("\n--- A dictionary is a row with headers ---")
hero = {"name": "Wren Hawkridge", "class": "Ranger", "level": 19}
print(hero["name"], hero["level"])
hero["level"] = 20
hero["pet"] = "a hawk called Tuesday"
print(hero)
# print(hero["Name"])     # <- uncomment: KeyError. Keys are exact.
print(hero.get("gold", 0), "  <- .get: XLOOKUP with an if-not-found")
for key, value in hero.items():
    print(f"  {key:<8}{value}")

print("\n--- A dictionary is also a lookup table ---")
wardens = {"Greyfen": "Alder Pike", "Ironhills": "Hild Stonebridge"}
print(wardens["Ironhills"], "|", wardens.get("Thornwood", "no warden yet"))

print("\n--- A list of dictionaries is a table ---")
party = [
    {"name": "Bram Ironfoot", "class": "Warrior", "level": 11, "loot": 1240},
    {"name": "Wren Hawkridge", "class": "Ranger", "level": 19, "loot": 2480},
    {"name": "Garrick Oldcastle", "class": "Warrior", "level": 14, "loot": 1240},
]
total = 0
top = party[0]
for h in party:
    total += h["loot"]
    if h["level"] > top["level"]:
        top = h
print("total loot", total, "| most experienced", top["name"])

print("\n--- COUNTIF: counting with a dictionary ---")
count = {}
for h in party:
    c = h["class"]
    if c in count:
        count[c] += 1
    else:
        count[c] = 1
print(count)

print("\n--- Group by: dictionary of lists ---")
by_class = {}
for h in party:
    c = h["class"]
    if c not in by_class:
        by_class[c] = []
    by_class[c].append(h["level"])
print(by_class)
for c, levels in by_class.items():
    print(f"  {c:<8} average level {sum(levels) / len(levels):.1f}")
