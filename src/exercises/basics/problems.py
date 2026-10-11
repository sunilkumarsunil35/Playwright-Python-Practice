# Exercise file. Fill in each function, then run: sh run-tests.sh --mine -k basics
# Stuck? The worked answer is in src/solutions/basics/problems.py

"""Basics: the browser, context and page objects, opening pages and reading simple things back.

Every function gets a Playwright `page` (a browser tab) and `base_url`, the address of the practice
site, for example "http://127.0.0.1:53211".
"""

from pathlib import Path

from playwright.sync_api import Page, Playwright


def open_and_get_title(page: Page, base_url: str) -> str:
    """Open the home page (base_url + "/index.html") and return the page title."""
    raise NotImplementedError("Your turn: write this one")


def get_heading_text(page: Page, base_url: str) -> str:
    """Open the home page and return the text of its <h1> heading."""
    raise NotImplementedError("Your turn: write this one")


def navigate_by_link(page: Page, base_url: str) -> str:
    """Open the home page, click the "Login" link in the menu and return the new page URL."""
    raise NotImplementedError("Your turn: write this one")


def take_screenshot(page: Page, base_url: str, path: Path) -> Path:
    """Open the home page, save a full-page PNG screenshot to `path` and return `path`."""
    raise NotImplementedError("Your turn: write this one")


def title_with_new_browser(playwright: Playwright, base_url: str) -> str:
    """Do it all by hand: launch Chromium, open a new context and page, read the home page title,
    close the browser and return the title.

    `playwright` is what `with sync_playwright() as playwright:` gives you in a plain script.
    """
    raise NotImplementedError("Your turn: write this one")
