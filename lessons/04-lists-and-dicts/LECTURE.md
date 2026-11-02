# Lesson 04: Lists and dictionaries (lecture notes for Lars)

**Goal:** Jen sees a list as a column, a dictionary as a row with headers,
and a list of dictionaries as a table. She can index, slice, append, look
up, loop, count, and build new containers with the loop recipe.

Do this one in the REPL. Build a column, a row and a table live, and poke
at them. `demo.py` has the same sequence if you'd rather run it.

---

## [Opener, 1 min] Where do the people go?

Read Mistress Pell's raven from `GUIDE.pdf`. She's been typing the Roll into
text with slashes; Orrin made the face. Today: proper containers, and the shapes
pandas will use later.

## [0–4 min] Lists: a column

```python
staff = ["Pell Marchbank", "Orrin Ironfoot", "Siv Larkspur"]
staff[0]; staff[-1]; staff[1:3]; len(staff)
staff.append("Bram Kettleby")
"Orrin Ironfoot" in staff
salaries = [31000, 36500, 28000]
sum(salaries), max(salaries), sum(salaries) / len(salaries)
sorted(salaries, reverse=True)[:2]
```

- Positions from 0, negative from the end, slices: exactly like letters in
  a string. A string is a list of characters; a list is a row of anything.
- `sorted(x)` returns a copy; `x.sort()` sorts in place and returns `None`.
  Show `print(salaries.sort())`. That's one of Dalvric's.
- The loop recipe with a list: `above = []` before, `append` inside, use after.
  "`total = 0` for lists."

## [4–8 min] Dictionaries: a row with headers

```python
employee = {"name": "Pell Marchbank", "department": "Treasury", "salary": 31000}
employee["name"]
employee["salary"] = 32000
employee["rating"] = 4
employee["bonus"]            # KeyError
employee.get("bonus", 0)
for key in employee: print(key, employee[key])
for key, value in employee.items(): ...
```

- Curly braces, `key: value`, lookup by name. VBA: `Scripting.Dictionary`,
  but built in and used everywhere.
- Keys are exact and case-sensitive: `employee["Name"]` is a KeyError.
  That's the bug hunt's crash.
- `.get(key, fallback)` is XLOOKUP with an if-not-found. No `#N/A`.
- A dictionary is also a lookup table: `managers = {"Clockworks": "Orrin Ironfoot", …}`.

## [8–12 min] Nesting: a table

```python
staff = [
    {"name": "Pell Marchbank", "dept": "Treasury", "salary": 31000},
    {"name": "Orrin Ironfoot", "dept": "Clockworks", "salary": 36500},
]
for person in staff:
    print(person["name"], person["salary"])
```

- A list of dictionaries is a sheet: `for person in staff` is "for each row".
- Total, max and filter are the loop recipe again. Do "highest paid" live:
  `top = staff[0]`, replace when bigger. The bug hunt writes `top = staff[0]`
  inside the loop; don't show that.
- The COUNTIF loop: `if dept in count: count[dept] += 1 else: count[dept] = 1`.
  Say out loud: this is the most common five lines in data work, and pandas
  will make it one line in lesson 10. Today she writes it by hand so that
  the one line means something later.
- Dictionary of lists: the same loop with `append`. That's "group by".

## [12–15 min] Handover

Open `EXERCISES.pdf`. Do exercise 1 (a) in the REPL together. Point out the
f-string quoting rule (`f"{person['name']}"`) because it will bite her in
exercise 4. Leave her with `CHEATSHEET.pdf` open.

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
- What does `employee.get("bonus", 0)` do that `employee["bonus"]` doesn't?
- What does `print(salaries.sort())` print?
