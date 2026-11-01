import about_me


def test_name_filled_in():
    assert about_me.NAME != "Your name here", "Put your own name into NAME"
    assert len(about_me.NAME) > 0


def test_favourite_function_filled_in():
    assert about_me.FAVOURITE_EXCEL_FUNCTION != "Your favourite function here"
    assert len(about_me.FAVOURITE_EXCEL_FUNCTION) > 0


def test_automation_wish_filled_in():
    assert not about_me.WHAT_I_WANT_TO_AUTOMATE.startswith("One boring task")
    assert len(about_me.WHAT_I_WANT_TO_AUTOMATE) > 10, "Tell me a bit more!"
