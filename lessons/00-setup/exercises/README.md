# Lesson 00: Exercises

Make sure you're on the right branch first:

```bash
git checkout lesson-00
```

## 1. Talk to Python (10 min)

Open a terminal, type `python`, and try these. Before pressing Enter, guess
what will come out.

```python
32500 / 12
32500 // 12
2 ** 10
"pay" + "slip"
"ha" * 3
len("Brightwell Ltd")
```

Type `exit()` to leave.

## 2. Your first script (5 min)

Create a file `exercises/hello.py` containing:

```python
print("Hello from Python!")
print("A monthly salary of £32,500 a year is", 32500 / 12)
```

Run it with `python lessons/00-setup/exercises/hello.py`, or with the ▶ button in VS Code.

## 3. About you (10 min)

Open `about_me.py` and fill in the three values. Then run the tests:

```bash
pytest lessons/00-setup/tests/test_about_me.py
```

All three tests should turn green.

(If you run `pytest lessons/00-setup` without the file name, it stops with
an ERROR. That's the broken bug hunt file. Next step.)

## 4. Bug hunt (15 min)

`bughunt/hello_bug.py` contains **three** small mistakes. Python will
complain about them one at a time. Run the tests, read the error message
carefully (which **line**? what **kind** of error?), fix it, and repeat.

Everything is green when `pytest lessons/00-setup` shows only PASSED.

## 5. Commit, push, pull request (10 min)

```bash
git status
git add .
git commit -m "Lesson 00: setup done, about me, bug hunt fixed"
git push
```

On GitHub, open a pull request from `lesson-00` into `main`. In the
description, write which of the three bugs was hardest to spot and why.
