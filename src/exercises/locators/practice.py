# Exercise file. Fill in each function, then run: sh run-tests.sh --mine -k locators
# Stuck? The worked answer is in src/solutions/locators/practice.py

"""Locators practice: CSS and XPath, nth/first/last, filtering, chaining and lists."""

from playwright.sync_api import Page


def css_and_xpath(page: Page, base_url: str) -> tuple[str, str]:
    """Open the home page. Return the first language in the list with id "langs" found with a CSS
    selector, and the last one found with an XPath selector, as a tuple."""
    raise NotImplementedError("Your turn: write this one")


def first_and_last_rows(page: Page, base_url: str) -> tuple[str, str]:
    """Open table.html and return the product names in the first and last body rows."""
    raise NotImplementedError("Your turn: write this one")


def price_of(page: Page, base_url: str, product: str) -> int:
    """Open table.html and return the price (third column) of the row that contains `product`."""
    raise NotImplementedError("Your turn: write this one")


def choose_plan(page: Page, base_url: str, plan: str) -> str:
    """Open the home page, click "Choose" inside the pricing card whose heading is `plan` and
    return the text of the paragraph with id "plan"."""
    raise NotImplementedError("Your turn: write this one")


def menu_link_names(page: Page, base_url: str) -> list[str]:
    """Open the home page and return the text of every link in the main menu, in order."""
    raise NotImplementedError("Your turn: write this one")


def logo_source(page: Page, base_url: str) -> str:
    """Open the home page and return the src attribute of the image whose alt text is
    "Playwright Practice logo"."""
    raise NotImplementedError("Your turn: write this one")
