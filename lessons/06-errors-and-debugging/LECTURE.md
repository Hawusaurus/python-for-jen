# Lesson 06: Errors and debugging (lecture notes for Lars)

**Goal:** Jen reads tracebacks without panic, catches the errors she expects
(narrowly), raises her own, and has a method for finding logic bugs. Today's
demo is mostly *breaking things on purpose* and reading the wreckage together.

Run `demo.py` from the lesson folder. It crashes on purpose at the end; that's
the point. Have VS Code open for the debugger section.

---

## [Opener, 1 min] The Full Moon

Read Orrin's raven from `GUIDE.pdf`. The moon is full, the Grimoire has
failed again, the Scriptorium's copy has "n/a" in row 2, the script stopped
dead, and Mistress Pell sent a traceback with nothing but "???". Dalvric's
answer to all errors was `On Error Resume Next`, which is how a grade 7 got
a 40% bonus.

## [0–4 min] Anatomy of a traceback

Type this live and run it:

```python
subjects = ["Pell", "Orrin", "Siv"]
for i in range(4):
    print(subjects[i])
```

Read the traceback **bottom-up**, out loud:
- Last line: `IndexError: list index out of range`. The *what*.
- The line above: `File "...", line 3` and the code. The *where*.
- "most recent call last": with functions, the stack reads top-down to the
  crash. Show one with a function inside a function if there's time.

Then the parade of types, one line each in the REPL:
`float("n/a")` (ValueError), `float(None)` (TypeError), `{}["x"]` (KeyError),
`1/0`, `open("nope.csv")`, `salry` (NameError), `"abc".uper()` (AttributeError).
Say the names. She'll meet all of them on the sheet.

## [4–8 min] try / except / else / finally

```python
try:
    salary = float(text)        # ONLY the risky line
except ValueError:
    print("could not read", repr(text))
else:
    total += salary             # only if it worked
finally:
    checked += 1                # always
```

- VBA comparison: `On Error GoTo handler`, but scoped to one block, and you
  pick *which* errors. `except:` with nothing after it is `On Error Resume
  Next`: everything vanishes, including the bugs you'd want to see.
- Several types: separate blocks, or a tuple `except (ValueError, TypeError)`.
- `as e` keeps the message. `type(e).__name__` gives the type as text, handy
  for logging.
- Why `else`? So the success code isn't inside `try`, where its own errors
  would be caught by accident. (This is bug 2 in today's bug hunt.)

## [8–11 min] raise

```python
def check_grade(grade):
    if not 1 <= grade <= 6:
        raise ValueError(f"grade must be 1–6, got {grade}")
    return grade
```

Your own code should refuse nonsense *early*, with a message a human can
read. A clear crash now beats a wrong bonus at Midsummer. Show that the
`ValueError` from `raise` is caught by the same `except ValueError` as the
ones Python raises.

## [11–14 min] Debugging: print and the debugger

Type the bonus-pool loop from Exercise 6 (with `pool = 0` inside the loop).
It prints 0 cr. Add `print(name, bonus, pool)` inside the loop, run, watch the
pool reset. That's the whole method: *look at the actual values*.

Then the same in VS Code: breakpoint on `pool += bonus`, F5, F10 to step,
Variables panel on the left. Two minutes, no more. She'll use it when print
isn't enough.

## [14–15 min] Handover

Mention `bughunt/riddles/`: five optional one-bug riddles (the last has two) for fast finishers or homework.

Open `EXERCISES.pdf`. Exercise 1 is typed *with* its bug on purpose. Remind
her: today a crash is a success, as long as she can say what type it was.

---

## VBA → Python cheat table (show at the end)

| VBA | Python |
|---|---|
| `On Error GoTo handler` | `try:` … `except SomeError:` |
| `On Error Resume Next` | bare `except: pass` (don't) |
| `Err.Number`, `Err.Description` | `type(e).__name__`, `str(e)` |
| `Err.Raise 5, , "bad grade"` | `raise ValueError("bad grade")` |
| `Resume Next` after the handler | the `else:` block |
| `Debug.Print x` | `print(repr(x))` |
| F8 (step), F9 (breakpoint) | F10 (step), click the gutter |

**Questions to check understanding:**
- `float("n/a")` and `float(None)`: which error is which, and why?
- Why does the success code go in `else` rather than at the end of `try`?
- When should a script crash on purpose?
