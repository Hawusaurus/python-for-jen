# ==================================================================
#  PAGES FROM THE GRIMOIRE, PAGE 1: "loot_helpers_DO_NOT_TOUCH.py"
# ==================================================================
#
# Shortly before he sailed west, Dalvric grew excited about Python and
# translated a corner of the Grimoire. Then he left. Since then:
#   - the Wyrm bounty calculation crashes,
#   - for three months no hero has paid the guild its cut
#     (the Royal Auditors have questions),
#   - and the loot line looks... almost right. Pell says "almost".
#
# THREE bugs:
#   one crashes (read the error message!),
#   one gives a wrong number without crashing,
#   one is so small you'll have to compare letter by letter.
#
# Run it from inside the lesson folder:
#   python bughunt/loot_bug.py
#
# When it's fixed, it prints EXACTLY this:
#
#   Wyrm bounty after 2 months: 2,205.00 cr
#   Osric Kettleby: loot 2345.50 cr, guild cut 469.10 cr, keeps 1876.40 cr
#
# Fix ONE bug per commit and explain it in the message, like a detective:
#   git commit -m "Bug hunt: <what was wrong and why>"


# --- Part 1: the Wyrm bounty grows every month nobody slays it ---
bounty = 2000
growth_percent = 5
months = 2

growth = 1 + growth_percent / 100
new_bounty = round(bounty * growth ^ months, 2)
print(f"Wyrm bounty after {months} months: {new_bounty:,.2f} cr")


# --- Part 2: one hero's loot line ---
name = "Osric Kettleby"
loot = 2345.5
cut_percent = 20

cut = loot * (cut_percent // 100)
keeps = loot - cut
print(f"{name}: loot {loot} cr, guild cut {cut:.2f} cr, keeps {keeps:.2f} cr")
