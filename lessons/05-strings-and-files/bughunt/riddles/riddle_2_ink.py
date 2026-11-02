# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 05 · RIDDLE 2: "The Scroll That Would Not Take Ink"
# ==================================================================
#
#    I opened the scroll to add a line,
#    but held it as if to read, not sign.
#    A page you open just to look
#    won't let you write into the book.
#
#  Orrin's notice board: write three notices to a file, then read
#  them back with numbers.
#
#  Run:  python bughunt/riddles/riddle_2_ink.py
#  When it's fixed, it prints EXACTLY this:
#
#    1. Raven post closes at dusk.
#    2. Guild dues are due on the first.
#    3. Biscuit is not to be fed crowns.

notices = ["Raven post closes at dusk.",
           "Guild dues are due on the first.",
           "Biscuit is not to be fed crowns."]

with open("my_work/notices.txt", "r", encoding="utf-8") as f:
    for line in notices:
        f.write(line + "\n")

number = 1
with open("my_work/notices.txt", encoding="utf-8") as f:
    for line in f:
        print(f"{number}. {line.strip()}")
        number += 1
