# Exercise file. Fill in each function, then run: sh run-tests.sh --mine -k basics
# Stuck? The worked answer is in src/solutions/basics/practice.py

"""Basics practice: navigation history, redirects, viewport, attributes and element screenshots."""

from pathlib import Path

from playwright.sync_api import Page


def back_and_forward(page: Page, base_url: str) -> list[str]:
    """Open index.html, then todo.html. Go back, then forward. Return the page title after each
    of the four steps, in order: ["Playwright Practice", "Todo", "Playwright Practice", "Todo"]."""
    raise NotImplementedError("Your turn: write this one")


def url_after_redirect(page: Page, base_url: str) -> str:
    """Open base_url + "/redirect". The server redirects you. Return the final URL."""
    raise NotImplementedError("Your turn: write this one")


def count_menu_links(page: Page, base_url: str) -> int:
    """Open the home page and return how many links the main menu (<nav>) has."""
    raise NotImplementedError("Your turn: write this one")


def read_meta_description(page: Page, base_url: str) -> str:
    """Open the home page and return the content of <meta name="description">."""
    raise NotImplementedError("Your turn: write this one")


def phone_sized_viewport(page: Page, base_url: str) -> str:
    """Resize the page to 375 x 667 (an iPhone SE), open emulation.html and return the text of the
    element with id "viewport" (it shows the size the page sees, like "375x667")."""
    raise NotImplementedError("Your turn: write this one")


def screenshot_of_pricing(page: Page, base_url: str, path: Path) -> Path:
    """Open the home page and save a screenshot of just the "Pricing" section to `path`."""
    raise NotImplementedError("Your turn: write this one")
