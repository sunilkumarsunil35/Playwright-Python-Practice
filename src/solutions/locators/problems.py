"""Locators: how Playwright finds elements.

Prefer user-facing locators (role, label, placeholder, text, test id) over CSS or XPath. They read
like the page, and they keep working when the markup changes.
"""

from playwright.sync_api import Page


def click_button_by_role(page: Page, base_url: str) -> str:
    """Open the home page, click the "Say hello" button found by its role, and return the text of
    the greeting paragraph (id "greeting")."""
    page.goto(f"{base_url}/index.html")
    page.get_by_role("button", name="Say hello").click()
    return page.locator("#greeting").inner_text()


def fill_by_label(page: Page, base_url: str) -> str:
    """Open login.html, fill "tom" into the field labelled "Username" and return the field's
    current value."""
    # get_by_label() follows <label for="..."> to its input. input_value() reads what is typed.
    page.goto(f"{base_url}/login.html")
    field = page.get_by_label("Username")
    field.fill("tom")
    return field.input_value()


def search_by_placeholder(page: Page, base_url: str) -> str:
    """Open table.html, type "Electronics" into the box whose placeholder is "Search products" and
    return the row counter text (id "row-count"), like "Showing 2 of 6"."""
    page.goto(f"{base_url}/table.html")
    page.get_by_placeholder("Search products").fill("Electronics")
    return page.locator("#row-count").inner_text()


def read_by_test_id(page: Page, base_url: str) -> str:
    """Open the home page and return the text of the element with data-testid="cart-count"."""
    page.goto(f"{base_url}/index.html")
    return page.get_by_test_id("cart-count").inner_text()


def find_by_text(page: Page, base_url: str) -> bool:
    """Open the home page and return whether the text "All systems operational" is visible."""
    page.goto(f"{base_url}/index.html")
    return page.get_by_text("All systems operational").is_visible()
