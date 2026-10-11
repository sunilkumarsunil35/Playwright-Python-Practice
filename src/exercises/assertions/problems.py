# Exercise file. Fill in each function, then run: sh run-tests.sh --mine -k assertions
# Stuck? The worked answer is in src/solutions/assertions/problems.py

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
    raise NotImplementedError("Your turn: write this one")


def check_login_error(page: Page, base_url: str) -> None:
    """Open login.html, sign in as "tom" with the wrong password "nope", and assert that an alert
    with the text "Invalid username or password" becomes visible."""
    raise NotImplementedError("Your turn: write this one")


def check_todo_count(page: Page, base_url: str) -> None:
    """Open todo.html, add the todos "Learn locators", "Learn actions" and "Learn expect", then
    assert there are exactly 3 todo items and the counter says "3 items left"."""
    raise NotImplementedError("Your turn: write this one")


def check_form_state(page: Page, base_url: str) -> None:
    """Open widgets.html. Assert "Continue" is disabled. Tick "I agree to the terms", then assert the
    box is checked, "Continue" is enabled and the "Medium" size is still checked."""
    raise NotImplementedError("Your turn: write this one")


def check_banner_hidden(page: Page, base_url: str) -> None:
    """Open the home page, assert the cookie banner is visible, click "Accept cookies" and assert
    the banner is hidden."""
    raise NotImplementedError("Your turn: write this one")
