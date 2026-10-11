from playwright.sync_api import expect

from common.target import load

P = load("assertions", "practice")


def test_check_attribute_and_class(page, base_url):
    P.check_attribute_and_class(page, base_url)
    assert page.url.endswith("index.html")


def test_check_contains_text(page, base_url):
    P.check_contains_text(page, base_url)
    assert page.url.endswith("index.html")


def test_check_list_of_texts(page, base_url):
    P.check_list_of_texts(page, base_url)
    assert page.url.endswith("index.html")


def test_check_input_value(page, base_url):
    P.check_input_value(page, base_url)
    assert page.url.endswith("widgets.html")


def test_check_not(page, base_url):
    P.check_not(page, base_url)
    expect(page.locator("#greeting")).to_have_text("Hello, Playwright!")


def test_failure_message(page, base_url):
    message = P.failure_message(page, base_url)
    assert "Wrong heading" in message
    assert "Welcome to the practice site" in message
