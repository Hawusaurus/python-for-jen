# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 05 · RIDDLE 4: "The Ledger That Forgot"
# ==================================================================
#
#    Three guilds I wrote, three lines of gold,
#    but only one the scroll would hold.
#    Each time I opened it anew,
#    I wiped the page and started through.
#
#  Guild totals for the Queen, written to a file and read back. Two
#  of the three guilds have vanished.
#
#  Run:  python bughunt/riddles/riddle_4_forgetful.py
#  When it's fixed, it prints EXACTLY this:
#
#    Forge: 1,680,500 cr
#    Guard: 1,121,450 cr
#    Library: 489,300 cr
#    Lines on the scroll: 3
#    Grand total: 3,291,250 cr

totals = {"Forge": 1680500, "Guard": 1121450, "Library": 489300}

for guild, total in totals.items():
    with open("my_work/riddle_guild_totals.txt", "w", encoding="utf-8") as f:
        f.write(f"{guild}: {total:,} cr\n")

with open("my_work/riddle_guild_totals.txt", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:
    print(line.strip())
print("Lines on the scroll:", len(lines))
print(f"Grand total: {sum(totals.values()):,} cr")
