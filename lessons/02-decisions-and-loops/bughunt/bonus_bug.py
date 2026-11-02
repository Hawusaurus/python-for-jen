# ==================================================================
#  PAGES FROM THE GRIMOIRE, PAGE 2: "bonus_run_USE_THIS_ONE.py"
# ==================================================================
#
# Dalvric's bonus run. Lady Siv ran it once. Everyone got a bonus.
# EVERYONE. Including the three apprentices who had been in the realm
# a week, and Biscuit (who was on the Roll as a joke, which is a
# different problem). The total came to minus forty crowns.
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
#   Maren Ashdown   2,480.00
#   Jory Pike           0.00
#   Bram Ironfoot   1,460.00
#   Biscuit             0.00
#   ------------------------
#   Total           3,940.00
#
# Rules: no bonus under 12 months of service. Otherwise 8% for a
# rating of 4 or more, 4% for a rating of 3, nothing below that.
#
# Fix ONE bug per commit and explain it in the message, like a detective:
#   git commit -m "Bug hunt: <what was wrong and why>"

records = "Maren Ashdown/31000/4/14;Jory Pike/24500/2/30;Bram Ironfoot/36500/3/60;Biscuit/400/5/3"

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
