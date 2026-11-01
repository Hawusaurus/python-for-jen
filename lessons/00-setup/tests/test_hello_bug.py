import hello_bug


def test_greeting():
    assert hello_bug.greeting("Jen") == "Hello, Jen! Welcome to Python."


def test_company_email():
    assert hello_bug.company_email("jen") == "jen@brightwell.co.uk"


def test_shout():
    assert hello_bug.shout("pay day") == "PAY DAY"
