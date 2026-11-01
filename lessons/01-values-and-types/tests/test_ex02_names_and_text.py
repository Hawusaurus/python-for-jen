from ex02_names_and_text import (
    full_name, initials, tidy_name, email_address, clean_employee_id,
)


def test_full_name():
    assert full_name("Jane", "Smith") == "Jane Smith"


def test_initials():
    assert initials("Jane", "Smith") == "J.S."
    assert initials("omar", "khan") == "o.k."


def test_tidy_name():
    assert tidy_name("  jANE smITH ") == "Jane Smith"
    assert tidy_name("PRIYA PATEL") == "Priya Patel"


def test_email_address():
    assert email_address("Jane", "Smith") == "jane.smith@brightwell.co.uk"


def test_email_address_with_space_in_name():
    assert email_address("Anne Marie", "Brown") == "annemarie.brown@brightwell.co.uk"
    assert email_address("Tom", "Van Dyke") == "tom.vandyke@brightwell.co.uk"


def test_clean_employee_id():
    assert clean_employee_id("  emp-0042 ") == "EMP0042"
    assert clean_employee_id("EMP0007") == "EMP0007"
