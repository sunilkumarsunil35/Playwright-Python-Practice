"""Assertions practice: attributes, classes, partial text, lists of texts, values, negation and
reading a failure message."""

import re

from playwright.sync_api import Page, expect


def check_attribute_and_class(page: Page, base_url: str) -> None:
    """Open the home page. Assert the status badge (id "status") has the attribute
    data-state="ok" and has the class "online"."""
    page.goto(f"{base_url}/index.html")
    status = page.locator("#status")
    expect(status).to_have_attribute("data-state", "ok")
    expect(status).to_have_class(re.compile(r"\bonline\b"))


def check_contains_text(page: Page, base_url: str) -> None:
    """Open the home page and assert the <h1> contains the word "practice" (any case)."""
    page.goto(f"{base_url}/index.html")
    expect(page.locator("h1")).to_contain_text(re.compile("practice", re.IGNORECASE))


def check_list_of_texts(page: Page, base_url: str) -> None:
    """Open the home page and assert the language list items are exactly, in order:
    Python, JavaScript, Java, .NET."""
    # Passing a list to to_have_text() checks every item and the count at once.
    page.goto(f"{base_url}/index.html")
    expect(page.locator("#langs li")).to_have_text(["Python", "JavaScript", "Java", ".NET"])


def check_input_value(page: Page, base_url: str) -> None:
    """Open widgets.html. Assert the "Volume" slider's value is "50" and the "Bio" box's value is
    "I like Java."."""
    page.goto(f"{base_url}/widgets.html")
    expect(page.get_by_label("Volume")).to_have_value("50")
    expect(page.get_by_label("Bio")).to_have_value("I like Java.")


def check_not(page: Page, base_url: str) -> None:
    """Open the home page. Assert the greeting (id "greeting") does NOT have the text
    "Hello, Playwright!" yet, click "Say hello", then assert that it does."""
    page.goto(f"{base_url}/index.html")
    greeting = page.locator("#greeting")
    expect(greeting).not_to_have_text("Hello, Playwright!")
    page.get_by_role("button", name="Say hello").click()
    expect(greeting).to_have_text("Hello, Playwright!")


def failure_message(page: Page, base_url: str) -> str:
    """Open the home page and assert the <h1> has the text "Wrong heading", with a 500 ms timeout.
    It fails. Catch the AssertionError and return its message, so you learn to read one."""
    page.goto(f"{base_url}/index.html")
    try:
        expect(page.locator("h1")).to_have_text("Wrong heading", timeout=500)
    except AssertionError as error:
        return str(error)
    return ""
