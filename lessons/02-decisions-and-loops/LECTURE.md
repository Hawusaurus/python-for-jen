# Lesson 02: Decisions and loops (lecture notes for Lars)

**Goal:** Jen can write `if/elif/else`, `for` over items and `range()`, `while`,
and the set-up-before / update-inside / use-after loop recipe. Plus the
indentation rule, which is the biggest syntactic shift from VBA.

Run `demo.py` section by section, or type into the REPL. Type the napkin rule
live and make the classic mistakes on purpose (missing colon, `=` instead of `==`).

---

## [Opener, 1 min] The napkin

Read Captain Siv's letter from `GUIDE.pdf`. The Queen's rules for her royal
purse are on a napkin pinned to the notice board with a dagger. The last time
the Grimoire ran the purse it paid everyone, including Biscuit, and the total
was minus forty crowns. Today: rules as code, applied to every quest the same way.

## [0–4 min] `if` / `elif` / `else`: the napkin as code

```python
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
print(rate)
```

- The **colon** opens a block, the **4 spaces** are the block. No `End If`.
  Un-indent and you're back outside. Show it: move `print(rate)` in and out.
- **First true wins.** Swap the first two checks and show a novice on a
  difficulty-5 quest getting a purse. That's the bug hunt, so don't fix it on screen.
- Type `if difficulty = 3:` on purpose. Read the SyntaxError together.
- VBA: `If … ElseIf … Else … End If`. Same shape, less typing.

## [4–8 min] `for`: drag the formula down

```python
for hero in "Wren,Bram,Thea".split(","):
    print("Welcome back", hero)

for day in range(1, 13):
    print(day)
```

- `for x in things:` is `For Each`. One item per trip, in the loop variable.
- `range(1, 13)` is 1 to 12. Same "up to but not including" rule as slicing.
  Show `range(5)` and `range(0, 20, 5)`.
- `.split(",")` on a text gives the pieces to loop over. Say: "a list; we
  do those properly in lesson 04. For now it's the thing `for` eats."
- Multiple assignment: `name, reward, difficulty = "Wren/3100/4".split("/")`.
  Three pieces, three variables. Used in the sheet's Given lines.

## [8–11 min] The loop recipe: before, inside, after

```python
total = 0
for reward in "3100,3650,2800".split(","):
    total += int(reward)
print(total)
```

- Set up **before**, update **inside**, use **after**. Draw three boxes.
- Move `total = 0` inside the loop and run it. Total = last reward. That's
  Dalvric's minus forty crowns, in spirit.
- `+=`: `total += x` is `total = total + x`.
- Counters and "highest so far" follow the same recipe.

## [11–13 min] `while`: until something changes

```python
bounty = 2800
months = 0
while bounty < 3500:
    bounty *= 1.03
    months += 1
print(months)
```

- Use `while` when you don't know how many trips. `Do While … Loop`.
- Remove `months += 1`? Still ends. Remove `bounty *= 1.03`? Infinite loop.
  Run it, hit Ctrl+C, and tell her she'll do this to herself in exercise 5.
- `continue` skips to the next trip, `break` leaves the loop. One line each.

## [13–15 min] Handover

Open `EXERCISES.pdf`. Do the first line of exercise 1 live: create
`my_work/ex1_purse_rule.py`, type the Given lines, type `if quests_done < 3:`
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
