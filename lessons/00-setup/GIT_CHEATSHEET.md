# Git cheat sheet

## The idea in four words

| Git word | Think of it as |
|---|---|
| **repository** (repo) | A folder that remembers its whole history |
| **commit** | A save point with a note saying what changed |
| **branch** | A parallel copy you can work on without touching the original |
| **pull request** (PR) | "I've made changes on my branch, please review and merge them" (like sending a document with Track Changes on) |

`main` is the "approved" version. Lessons are branches. When you finish a
lesson, you open a PR, Lars reviews it, and the lesson gets merged into `main`.

## Everyday commands

```bash
git status                      # What have I changed? Run this a lot.
git checkout lesson-01          # Switch to the lesson-01 branch
git pull                        # Download the newest changes from GitHub
git add .                       # Mark all changed files for the next commit
git commit -m "Short message"   # Create a save point
git push                        # Upload your commits to GitHub
git log --oneline               # Show the history, one line per commit
```

## Good commit messages

Say *what* changed and, if it isn't obvious, *why*:

- ✅ `Exercise 3: format payslip lines with f-strings`
- ✅ `Bug hunt: use ** instead of ^ for powers`
- ❌ `stuff`
- ❌ `asdf`

Commit small and often. Every finished exercise is a good save point.

## Something went wrong?

| Situation | Do this |
|---|---|
| "Your local changes would be overwritten" | `git status`, then commit your changes first |
| I want to throw away my changes to one file | `git restore path/to/file.py` |
| I'm lost | `git status`, and send Lars a screenshot |

Doing everything in the VS Code "Source Control" panel (the branch icon on
the left) is also fine. It runs the same commands for you.
