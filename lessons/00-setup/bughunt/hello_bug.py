# BUG HUNT: this file has THREE mistakes.
#
# What it should do:
#   greeting("Jen")     -> "Hello, Jen! Welcome to Python."
#   company_email("jen") -> "jen@brightwell.co.uk"
#
# Run:  pytest lessons/00-setup
# Read the error: which line? what kind of error? Fix it, run again.


def greeting(name)
    return "Hello, " + name + "! Welcome to Python."


def company_email(username):
    domain = "brightwell.co.uk'
    return username + "@" + domain


def shout(text):
return text.upper()
