# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 04 · RIDDLE 2: "Two by Two"
# ==================================================================
#
#    I asked the roll for pairs of two,
#    a name, a wage, as couples do.
#    It gave me names and nothing more;
#    the wages waited by another door.
#
#  Orrin's attempt at a wage table for the Privy Council. It should
#  print one line per person and a total.
#
#  Run:  python bughunt/riddles/riddle_2_pairs.py
#  When it's fixed, it prints EXACTLY this:
#
#    Name                     Wage
#    -----------------------------
#    Pell Marchbank      31,000 cr
#    Orrin Ironfoot      36,500 cr
#    Siv Larkspur        38,200 cr
#    -----------------------------
#    Total              105,700 cr
#    Average          35,233.33 cr

wages = {"Pell Marchbank": 31000, "Orrin Ironfoot": 36500, "Siv Larkspur": 38200}
total = 0
count = 0

print(f"{'Name':<16}{'Wage':>13}")
print("-" * 29)
for name, salary in wages:
    print(f"{name:<16}{salary:>10,} cr")
    total += salary
    count += 1

print("-" * 29)
print(f"{'Total':<16}{total:>10,} cr")
print(f"{'Average':<16}{total / count:>10,.2f} cr")
