"""Actions: clicking, typing, checking, selecting and hovering.

Every action waits until the element is visible, enabled and still, so you rarely need waits.
"""

from playwright.sync_api import Page


def log_in(page: Page, base_url: str, username: str, password: str) -> str:
    """Open login.html, sign in with `username` and `password`, and return the account page's
    <h1> text, like "Signed in as tom"."""
    page.goto(f"{base_url}/login.html")
    page.get_by_label("Username").fill(username)
    page.get_by_label("Password").fill(password)
    page.get_by_role("button", name="Sign in").click()
    page.wait_for_url("**/account.html")
    heading = page.get_by_role("heading", name="Signed in as")
    heading.wait_for()
    return heading.inner_text()


def tick_and_pick(page: Page, base_url: str) -> str:
    """Open widgets.html, tick "I agree to the terms", pick the "Large" size and return the text
    of the paragraph with id "choices"."""
    page.goto(f"{base_url}/widgets.html")
    page.get_by_label("I agree to the terms").check()
    page.get_by_label("Large").check()
    return page.locator("#choices").inner_text()


def select_country(page: Page, base_url: str, country: str) -> str:
    """Open widgets.html, choose `country` (a visible name like "Germany") in the "Country"
    dropdown and return the text of the paragraph with id "country-out"."""
    page.goto(f"{base_url}/widgets.html")
    page.get_by_label("Country").select_option(label=country)
    return page.locator("#country-out").inner_text()


def type_and_press_enter(page: Page, base_url: str, text: str) -> str:
    """Open widgets.html, type `text` into "Type and press Enter", press Enter and return the
    text of the paragraph with id "key-log"."""
    page.goto(f"{base_url}/widgets.html")
    box = page.get_by_label("Type and press Enter")
    box.fill(text)
    box.press("Enter")
    return page.locator("#key-log").inner_text()


def hover_menu(page: Page, base_url: str) -> str:
    """Open widgets.html, hover over "Products" to show its menu, click "Laptops" and return the
    text of the paragraph with id "menu-out"."""
    # The submenu only shows on hover, so clicking "Laptops" first would wait and time out.
    page.goto(f"{base_url}/widgets.html")
    page.get_by_role("button", name="Products").hover()
    page.get_by_role("link", name="Laptops").click()
    return page.locator("#menu-out").inner_text()
