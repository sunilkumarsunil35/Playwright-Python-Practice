import pytest

from common.target import load

P = load("actions", "problems")


@pytest.mark.parametrize("username, password", [("tom", "secret"), ("ana", "hunter2")])
def test_log_in(page, base_url, username, password):
    assert P.log_in(page, base_url, username, password) == f"Signed in as {username}"


def test_tick_and_pick(page, base_url):
    assert P.tick_and_pick(page, base_url) == "Agreed: yes | Size: Large"


@pytest.mark.parametrize("country, code", [("Germany", "DE"), ("Japan", "JP")])
def test_select_country(page, base_url, country, code):
    assert P.select_country(page, base_url, country) == f"Selected: {code}"


def test_type_and_press_enter(page, base_url):
    assert P.type_and_press_enter(page, base_url, "hello") == "You typed: hello"


def test_hover_menu(page, base_url):
    assert P.hover_menu(page, base_url) == "You picked Laptops"
