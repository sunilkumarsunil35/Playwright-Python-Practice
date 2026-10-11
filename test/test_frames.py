from common.target import load

P = load("frames", "problems")


def test_read_alert(page, base_url):
    assert P.read_alert(page, base_url) == "Hello from an alert!"


def test_cancel_confirm(page, base_url):
    assert P.cancel_confirm(page, base_url) == "You pressed Cancel"


def test_answer_prompt(page, base_url):
    assert P.answer_prompt(page, base_url, "Sunil") == "Hello, Sunil"


def test_fill_form_in_iframe(page, base_url):
    assert P.fill_form_in_iframe(page, base_url, "Sunil") == "Thanks for joining, Sunil!"


def test_open_link_in_new_tab(context, page, base_url):
    assert P.open_link_in_new_tab(context, page, base_url) == "Help center"
