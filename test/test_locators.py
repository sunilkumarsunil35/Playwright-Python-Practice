from common.target import load

P = load("locators", "problems")


def test_click_button_by_role(page, base_url):
    assert P.click_button_by_role(page, base_url) == "Hello, Playwright!"


def test_fill_by_label(page, base_url):
    assert P.fill_by_label(page, base_url) == "tom"


def test_search_by_placeholder(page, base_url):
    assert P.search_by_placeholder(page, base_url) == "Showing 2 of 6"


def test_read_by_test_id(page, base_url):
    assert P.read_by_test_id(page, base_url) == "3"


def test_find_by_text(page, base_url):
    assert P.find_by_text(page, base_url) is True
