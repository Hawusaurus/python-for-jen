# ==================================================================
#  DAVE'S LEFTOVERS #4: "staff_list_FINAL_v3_(2).py"
# ==================================================================
#
# Dave's staff list. Last run: 2019. It found the wrong top earner,
# then crashed looking for a department that definitely exists,
# then (once Mo "fixed" it) reported a headcount of 1 for everyone.
#
# THREE bugs:
#   one crashes (read the error message, and read it twice),
#   one picks the wrong top earner without crashing,
#   one makes every department count come out as 1.
#
# Run it from inside the lesson folder:
#   python bughunt/staff_list_bug.py
#
# When it's fixed, it prints EXACTLY this:
#
#   Highest paid: Amara Okafor
#   IT: Mo Khan
#   {'Payroll': 1, 'IT': 2, 'Sales': 1, 'Warehouse': 1}
#
# Fix ONE bug per commit and explain it in the message, like a detective:
#   git commit -m "Bug hunt: <what was wrong and why>"

staff = [
    {"name": "Priya Patel", "dept": "Payroll", "salary": 31000},
    {"name": "Mo Khan", "dept": "IT", "salary": 36500},
    {"name": "Amara Okafor", "dept": "Sales", "salary": 41000},
    {"name": "Tom Brown", "dept": "Warehouse", "salary": 24500},
    {"name": "Chloe Evans", "dept": "IT", "salary": 29000},
]

# --- Part 1: who earns the most? ---
top = staff[0]
for person in staff:
    if person["salary"] > top["salary"]:
        top = staff[0]
print("Highest paid:", top["name"])

# --- Part 2: the IT manager ---
managers = {"Payroll": "Priya Patel", "IT": "Mo Khan", "Sales": "Amara Okafor"}
print("IT:", managers["It"])

# --- Part 3: headcount per department ---
headcount = {}
for person in staff:
    dept = person["dept"]
    if dept in headcount:
        headcount[dept] = 1
    else:
        headcount[dept] = 1
print(headcount)
