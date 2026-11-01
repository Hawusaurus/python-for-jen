# ==================================================================
#  DAVE'S LEFTOVERS #0: "welcome_v2_FINAL_final.py"
# ==================================================================
#
# Found on the shared drive in a folder called  \\DAVE\do_not_open\
# Dave wrote this welcome script in 2019, the week before he left to
# "find himself" on a narrowboat. It has never run. Not once.
#
# There are THREE mistakes. Python only tells you about ONE at a time.
#
#   1. Run it:  python bughunt/hello_bug.py
#   2. Read the error: WHICH line? WHAT kind of error?
#   3. Fix it, save, run again, and meet the next one.
#
# When it's fixed, it prints EXACTLY this:
#
#   Hello, Jen! Welcome to Brightwell.
#   jen@brightwell.co.uk
#   TEA TIME


def greeting(name)
    return "Hello, " + name + "! Welcome to Brightwell."


def company_email(username):
    domain = "brightwell.co.uk'
    return username + "@" + domain


def shout(text):
return text.upper()


print(greeting("Jen"))
print(company_email("jen"))
print(shout("tea time"))
