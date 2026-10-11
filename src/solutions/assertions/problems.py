"""Assertions: expect() checks that retry until they pass or time out (5 seconds by default).

A plain `assert locator.inner_text() == "x"` checks once, right now. `expect(locator).to_have_text("x")`
keeps checking, so it does not fail just because the page was a moment slow.
These functions return nothing: they pass by not raising.
"""

import re

from playwright.sync_api import Page, expect


def check_title_and_url(page: Page, base_url: str) -> None:
    """Open the home page and assert that its title is "Playwright Practice" and its URL ends with
    "index.html"."""
    page.goto(f"{base_url}/index.html")
    expect(page).to_have_title("Playwright Practice")
    expect(page).to_have_url(re.compile(r".*index\.html$"))


def check_login_error(page: Page, base_url: str) -> None:
    """Open login.html, sign in as "tom" with the wrong password "nope", and assert that an alert
    with the text "Invalid username or password" becomes visible."""
    page.goto(f"{base_url}/login.html")
    page.get_by_label("Username").fill("tom")
    page.get_by_label("Password").fill("nope")
    page.get_by_role("button", name="Sign in").click()
    alert = page.get_by_role("alert")
    expect(alert).to_be_visible()
    expect(alert).to_have_text("Invalid username or password")


def check_todo_count(page: Page, base_url: str) -> None:
    """Open todo.html, add the todos "Learn locators", "Learn actions" and "Learn expect", then
    assert there are exactly 3 todo items and the counter says "3 items left"."""
    page.goto(f"{base_url}/todo.html")
    box = page.get_by_placeholder("What needs to be done?")
    for text in ["Learn locators", "Learn actions", "Learn expect"]:
        box.fill(text)
        box.press("Enter")
    expect(page.get_by_test_id("todo-item")).to_have_count(3)
    expect(page.get_by_test_id("todo-count")).to_have_text("3 items left")


def check_form_state(page: Page, base_url: str) -> None:
    """Open widgets.html. Assert "Continue" is disabled. Tick "I agree to the terms", then assert the
    box is checked, "Continue" is enabled and the "Medium" size is still checked."""
    page.goto(f"{base_url}/widgets.html")
    cont = page.get_by_role("button", name="Continue")
    expect(cont).to_be_disabled()
    page.get_by_label("I agree to the terms").check()
    expect(page.get_by_label("I agree to the terms")).to_be_checked()
    expect(cont).to_be_enabled()
    expect(page.get_by_label("Medium")).to_be_checked()


def check_banner_hidden(page: Page, base_url: str) -> None:
    """Open the home page, assert the cookie banner is visible, click "Accept cookies" and assert
    the banner is hidden."""
    page.goto(f"{base_url}/index.html")
    banner = page.get_by_role("region", name="Cookie banner")
    expect(banner).to_be_visible()
    page.get_by_role("button", name="Accept cookies").click()
    expect(banner).to_be_hidden()
