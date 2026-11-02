# ==================================================================
#  PAGES FROM THE GRIMOIRE, PAGE 0: "welcome_v2_FINAL_final.py"
# ==================================================================
#
# Found in a locked drawer of the Treasury labelled  DALVRIC - DO NOT OPEN
# Dalvric wrote this welcome script the week before he sailed west to
# "find himself beyond the sea". It has never run. Not once.
#
# There are THREE mistakes. Python only tells you about ONE at a time.
#
#   1. Run it:  python bughunt/hello_bug.py
#   2. Read the error: WHICH line? WHAT kind of error?
#   3. Fix it, save, run again, and meet the next one.
#
# When it's fixed, it prints EXACTLY this:
#
#   Hello, Jen! Welcome to Thornmere.
#   jen@thornmere.realm
#   TEA TIME


def greeting(name)
    return "Hello, " + name + "! Welcome to Thornmere."


def raven_address(username):
    domain = "thornmere.realm'
    return username + "@" + domain


def shout(text):
return text.upper()


print(greeting("Jen"))
print(raven_address("jen"))
print(shout("tea time"))
