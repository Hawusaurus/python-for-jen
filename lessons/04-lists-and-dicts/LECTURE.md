# Lesson 04: Lists and dictionaries (lecture notes for Lars)

**Goal:** Jen sees a list as a column, a dictionary as a row with headers,
and a list of dictionaries as a table. She can index, slice, append, look
up, loop, count, and build new containers with the loop recipe.

Do this one in the REPL. Build a column, a row and a table live, and poke
at them. `demo.py` has the same sequence if you'd rather run it.

---

## [Opener, 1 min] Where do the heroes go?

Read Quartermistress Pell's raven from `GUIDE.pdf`. She's been typing the
roster into text with slashes; Orrin made the face. Today: proper containers,
and the shapes pandas will use later.

## [0–4 min] Lists: a column

```python
heroes = ["Bram Ironfoot", "Wren Hawkridge", "Tamsin Larkspur"]
heroes[0]; heroes[-1]; heroes[1:3]; len(heroes)
heroes.append("Piran Dovecote")
"Wren Hawkridge" in heroes
rewards = [320, 1240, 150, 610]
sum(rewards), max(rewards), sum(rewards) / len(rewards)
sorted(rewards, reverse=True)[:2]
```

- Positions from 0, negative from the end, slices: exactly like letters in
  a string. A string is a list of characters; a list is a row of anything.
- `sorted(x)` returns a copy; `x.sort()` sorts in place and returns `None`.
  Show `print(rewards.sort())`. That's one of Dalvric's.
- The loop recipe with a list: `big = []` before, `append` inside, use after.
  "`total = 0` for lists."

## [4–8 min] Dictionaries: a row with headers

```python
hero = {"name": "Wren Hawkridge", "class": "Ranger", "level": 19}
hero["name"]
hero["level"] = 20
hero["pet"] = "a hawk called Tuesday"
hero["gold"]                 # KeyError
hero.get("gold", 0)
for key in hero: print(key, hero[key])
for key, value in hero.items(): ...
```

- Curly braces, `key: value`, lookup by name. VBA: `Scripting.Dictionary`,
  but built in and used everywhere.
- Keys are exact and case-sensitive: `hero["Name"]` is a KeyError.
  That's the bug hunt's crash.
- `.get(key, fallback)` is XLOOKUP with an if-not-found. No `#N/A`.
- A dictionary is also a lookup table: `wardens = {"Greyfen": "Alder Pike", …}`.
  Thornwood has no warden: `.get("Thornwood", "no warden yet")`.

## [8–12 min] Nesting: a table

```python
party = [
    {"name": "Bram Ironfoot", "class": "Warrior", "level": 11},
    {"name": "Wren Hawkridge", "class": "Ranger", "level": 19},
]
for hero in party:
    print(hero["name"], hero["level"])
```

- A list of dictionaries is a sheet: `for hero in party` is "for each row".
- Total, max and filter are the loop recipe again. Do "highest level" live:
  `top = party[0]`, replace when bigger. The bug hunt writes `top = roster[0]`
  inside the loop; don't show that.
- The COUNTIF loop: `if c in count: count[c] += 1 else: count[c] = 1`.
  Say out loud: this is the most common five lines in data work, and pandas
  will make it one line in lesson 10. Today she writes it by hand so that
  the one line means something later.
- Dictionary of lists: the same loop with `append`. That's "group by".

## [12–15 min] Handover

Open `EXERCISES.pdf`. Do exercise 1 (a) in the REPL together. Point out the
f-string quoting rule (`f"{hero['name']}"`) because it will bite her in
exercise 4. Leave her with `CHEATSHEET.pdf` open.

The bug hunt is `bughunt/roster_bug.py`. Mention `bughunt/riddles/`: five optional
one-bug riddles (the last has two) for fast finishers or homework; your answers are
in `instructor/solutions/04-lists-and-dicts/riddles/`.

---

## Excel/VBA → Python cheat table (show at the end)

| Excel / VBA | Python |
|---|---|
| a column, `Array(…)` | list `[…]` |
| a row with headers, `Scripting.Dictionary` | dict `{key: value}` |
| a sheet | list of dicts |
| `XLOOKUP(key, keys, values, "n/a")` | `d.get(key, "n/a")` |
| `COUNTIF` per category | counting loop |
| `SUM`, `MAX`, `MIN`, `AVERAGE` | `sum`, `max`, `min`, `sum/len` |
| `SORT` | `sorted(x)` |
| Filter | loop + `append` |
| `UBound(arr) + 1` | `len(x)` |

**Questions to check understanding:**
- When would you use a list and when a dictionary?
- What does `hero.get("gold", 0)` do that `hero["gold"]` doesn't?
- What does `print(rewards.sort())` print?
