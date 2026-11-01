# ==================================================================
#  DAVE'S LEFTOVERS #2: "bonus_run_2019_USE_THIS_ONE.py"
# ==================================================================
#
# Dave's bonus run. Siobhan ran it once in 2019. Everyone got a bonus.
# EVERYONE. Including the three people who had been there a week,
# and Biscuit (who was on the staff list as a joke, which is a
# different problem). The total came to minus forty pounds.
#
# THREE bugs:
#   one crashes (read the error message!),
#   one makes the wrong people get a bonus (check the rules below),
#   one makes the total wrong even when every line is right.
#
# Run it from inside the lesson folder:
#   python bughunt/bonus_bug.py
#
# When it's fixed, it prints EXACTLY this:
#
#   Priya Patel     2,480.00
#   Tom Brown           0.00
#   Mo Khan         1,460.00
#   Biscuit             0.00
#   ------------------------
#   Total           3,940.00
#
# Rules: no bonus under 12 months of service. Otherwise 8% for a
# rating of 4 or more, 4% for a rating of 3, nothing below that.
#
# Fix ONE bug per commit and explain it in the message, like a detective:
#   git commit -m "Bug hunt: <what was wrong and why>"

records = "Priya Patel/31000/4/14;Tom Brown/24500/2/30;Mo Khan/36500/3/60;Biscuit/400/5/3"

for record in records.split(";"):
    total = 0
    name, salary_text, rating_text, months_text = record.split("/")
    salary = int(salary_text)
    rating = int(rating_text)
    months = int(months_text)
    if rating => 4:
        rate = 0.08
    elif months < 12:
        rate = 0
    elif rating == 3:
        rate = 0.04
    else:
        rate = 0
    bonus = salary * rate
    total = total + bonus
    print(f"{name:<14}{bonus:>10,.2f}")

print("-" * 24)
print(f"{'Total':<14}{total:>10,.2f}")
