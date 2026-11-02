# Lesson 02: Decisions and loops (lecture notes for Lars)

**Goal:** Jen can write `if/elif/else`, `for` over items and `range()`, `while`,
and the set-up-before / update-inside / use-after loop recipe. Plus the
indentation rule, which is the biggest syntactic shift from VBA.

Run `demo.py` section by section, or type into the REPL. Type the napkin rule
live and make the classic mistakes on purpose (missing colon, `=` instead of `==`).

---

## [Opener, 1 min] The napkin

Read Lady Siv's letter from `GUIDE.pdf`. The Queen's Midwinter bonus rules
are on a napkin pinned to the Treasury door with a dagger. The last time the
Grimoire ran the bonus it paid everyone, including Biscuit, and the total was
minus forty crowns. Today: rules as code, applied to everyone the same way.

## [0–4 min] `if` / `elif` / `else`: the napkin as code

```python
months = 14
rating = 4
if months < 12:
    rate = 0
elif rating >= 4:
    rate = 0.08
elif rating == 3:
    rate = 0.04
else:
    rate = 0
print(rate)
```

- The **colon** opens a block, the **4 spaces** are the block. No `End If`.
  Un-indent and you're back outside. Show it: move `print(rate)` in and out.
- **First true wins.** Swap the first two checks and show a new apprentice with
  a 5 getting paid. That's the bug hunt, so don't fix it on screen.
- Type `if rating = 3:` on purpose. Read the SyntaxError together.
- VBA: `If … ElseIf … Else … End If`. Same shape, less typing.

## [4–8 min] `for`: drag the formula down

```python
for name in "Orrin,Pell,Siv".split(","):
    print("Hello", name)

for month in range(1, 13):
    print(month)
```

- `for x in things:` is `For Each`. One item per trip, in the loop variable.
- `range(1, 13)` is 1 to 12. Same "up to but not including" rule as slicing.
  Show `range(5)` and `range(0, 20, 5)`.
- `.split(",")` on a text gives the pieces to loop over. Say: "a list; we
  do those properly in lesson 04. For now it's the thing `for` eats."
- Multiple assignment: `name, salary, rating = "Orrin/36500/3".split("/")`.
  Three pieces, three variables. Used in the sheet's Given lines.

## [8–11 min] The loop recipe: before, inside, after

```python
total = 0
for salary in "31000,36500,28000".split(","):
    total += int(salary)
print(total)
```

- Set up **before**, update **inside**, use **after**. Draw three boxes.
- Move `total = 0` inside the loop and run it. Total = last salary. That's
  Dalvric's minus forty crowns, in spirit.
- `+=`: `total += x` is `total = total + x`.
- Counters and "highest so far" follow the same recipe.

## [11–13 min] `while`: until something changes

```python
salary = 28000
years = 0
while salary < 35000:
    salary *= 1.03
    years += 1
print(years)
```

- Use `while` when you don't know how many trips. `Do While … Loop`.
- Remove `years += 1`? Still ends. Remove `salary *= 1.03`? Infinite loop.
  Run it, hit Ctrl+C, and tell her she'll do this to herself in exercise 5.
- `continue` skips to the next trip, `break` leaves the loop. One line each.

## [13–15 min] Handover

Open `EXERCISES.pdf`. Do the first line of exercise 1 live: create
`my_work/ex1_bonus_rule.py`, type the Given lines, type `if months_of_service < 12:`
and the colon. Leave her to it with `CHEATSHEET.pdf` open.
After the bug hunt: five optional riddles in `bughunt/riddles/` (one bug each, the last has two). Answers in `instructor/solutions/02-decisions-and-loops/riddles/`.

---

## VBA → Python cheat table (show at the end)

| VBA | Python |
|---|---|
| `If x Then … ElseIf … Else … End If` | `if x:` / `elif:` / `else:` + indentation |
| `For Each c In Range` … `Next` | `for c in things:` |
| `For i = 1 To 12` … `Next` | `for i in range(1, 13):` |
| `Do While x < y` … `Loop` | `while x < y:` |
| `Exit For` / `Exit Do` | `break` |
| `x = x + 1` | `x += 1` |
| `And`, `Or`, `Not` | `and`, `or`, `not` |
| `Mod` | `%` |

**Questions to check understanding:**
- What does `range(1, 13)` give, and why not 13?
- In an `if/elif/elif` chain with two true conditions, which runs?
- Where does `total = 0` go, and what happens if it's inside the loop?
