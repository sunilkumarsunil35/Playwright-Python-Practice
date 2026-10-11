# Exercise file. Fill in each function, then run: sh run-tests.sh --mine -k locators
# Stuck? The worked answer is in src/solutions/locators/problems.py

"""Locators: how Playwright finds elements.

Prefer user-facing locators (role, label, placeholder, text, test id) over CSS or XPath. They read
like the page, and they keep working when the markup changes.
"""

from playwright.sync_api import Page


def click_button_by_role(page: Page, base_url: str) -> str:
    """Open the home page, click the "Say hello" button found by its role, and return the text of
    the greeting paragraph (id "greeting")."""
    raise NotImplementedError("Your turn: write this one")


def fill_by_label(page: Page, base_url: str) -> str:
    """Open login.html, fill "tom" into the field labelled "Username" and return the field's
    current value."""
    raise NotImplementedError("Your turn: write this one")


def search_by_placeholder(page: Page, base_url: str) -> str:
    """Open table.html, type "Electronics" into the box whose placeholder is "Search products" and
    return the row counter text (id "row-count"), like "Showing 2 of 6"."""
    raise NotImplementedError("Your turn: write this one")


def read_by_test_id(page: Page, base_url: str) -> str:
    """Open the home page and return the text of the element with data-testid="cart-count"."""
    raise NotImplementedError("Your turn: write this one")


def find_by_text(page: Page, base_url: str) -> bool:
    """Open the home page and return whether the text "All systems operational" is visible."""
    raise NotImplementedError("Your turn: write this one")
