# Lesson 01: Exercises

```bash
git checkout lesson-01
git pull
pytest lessons/01-values-and-types
```

Everything is red at first. Work through the files **in order**. Each one
starts with a short explanation, so read it before writing code.

| File | Topic | Time |
|---|---|---|
| `ex01_pay_maths.py` | arithmetic, `//`, `%`, `**`, `round` | 10 min |
| `ex02_names_and_text.py` | string methods | 10 min |
| `ex03_fstrings.py` | formatting numbers | 10 min |
| `ex04_conversions.py` | text → numbers and back | 10 min |
| `ex05_true_or_false.py` | comparisons, `and` / `or` / `not` | 5 min |
| `ex06_slicing.py` | LEFT / RIGHT / MID the Python way | 10 min |
| `ex07_pay_gap.py` ⭐ | stretch: your first pay gap numbers | 15 min |
| `bughunt/payroll_bug.py` 🐞 | find three bugs | 15 min |

## How to work

You only ever replace the line `pass  # TODO: ...` with your own code.
Each function has examples in its description. Make those come out right.

Run only the tests for one file:

```bash
pytest lessons/01-values-and-types/tests/test_ex01_pay_maths.py
```

Try things out in the REPL before writing them into the file. Type
`python`, then for example `"  emp-0042 ".strip().upper()`.

You can also try a function directly:

```bash
python -i lessons/01-values-and-types/exercises/ex01_pay_maths.py
>>> monthly_salary(32500)
```

## Stuck?

1. Read the test failure. It shows what you returned and what was expected.
2. If your function returned `None`, you forgot `return`.
3. Try the expression in the REPL with the example values.
4. Still stuck after 10 minutes? Skip it, move on, and mention it in the PR.

## Done?

```bash
git add .
git commit -m "Lesson 01: exercises"
git push
```

Then open a pull request from `lesson-01` into `main`. Commit the bug hunt
fixes separately, one commit per bug, explaining each bug in the message.
