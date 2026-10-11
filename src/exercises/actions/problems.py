# Exercise file. Fill in each function, then run: sh run-tests.sh --mine -k actions
# Stuck? The worked answer is in src/solutions/actions/problems.py

"""Actions: clicking, typing, checking, selecting and hovering.

Every action waits until the element is visible, enabled and still, so you rarely need waits.
"""

from playwright.sync_api import Page


def log_in(page: Page, base_url: str, username: str, password: str) -> str:
    """Open login.html, sign in with `username` and `password`, and return the account page's
    <h1> text, like "Signed in as tom"."""
    raise NotImplementedError("Your turn: write this one")


def tick_and_pick(page: Page, base_url: str) -> str:
    """Open widgets.html, tick "I agree to the terms", pick the "Large" size and return the text
    of the paragraph with id "choices"."""
    raise NotImplementedError("Your turn: write this one")


def select_country(page: Page, base_url: str, country: str) -> str:
    """Open widgets.html, choose `country` (a visible name like "Germany") in the "Country"
    dropdown and return the text of the paragraph with id "country-out"."""
    raise NotImplementedError("Your turn: write this one")


def type_and_press_enter(page: Page, base_url: str, text: str) -> str:
    """Open widgets.html, type `text` into "Type and press Enter", press Enter and return the
    text of the paragraph with id "key-log"."""
    raise NotImplementedError("Your turn: write this one")


def hover_menu(page: Page, base_url: str) -> str:
    """Open widgets.html, hover over "Products" to show its menu, click "Laptops" and return the
    text of the paragraph with id "menu-out"."""
    raise NotImplementedError("Your turn: write this one")
