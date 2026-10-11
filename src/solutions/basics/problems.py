"""Basics: the browser, context and page objects, opening pages and reading simple things back.

Every function gets a Playwright `page` (a browser tab) and `base_url`, the address of the practice
site, for example "http://127.0.0.1:53211".
"""

from pathlib import Path

from playwright.sync_api import Page, Playwright


def open_and_get_title(page: Page, base_url: str) -> str:
    """Open the home page (base_url + "/index.html") and return the page title."""
    # page.goto() loads a URL and waits for the "load" event. page.title() reads <title>.
    page.goto(f"{base_url}/index.html")
    return page.title()


def get_heading_text(page: Page, base_url: str) -> str:
    """Open the home page and return the text of its <h1> heading."""
    # page.locator() takes a CSS selector. inner_text() returns the text a user sees.
    page.goto(f"{base_url}/index.html")
    return page.locator("h1").inner_text()


def navigate_by_link(page: Page, base_url: str) -> str:
    """Open the home page, click the "Login" link in the menu and return the new page URL."""
    # get_by_role("link", name=...) finds a link by its visible name. click() waits for it first.
    page.goto(f"{base_url}/index.html")
    page.get_by_role("link", name="Login").click()
    page.wait_for_url("**/login.html")
    return page.url


def take_screenshot(page: Page, base_url: str, path: Path) -> Path:
    """Open the home page, save a full-page PNG screenshot to `path` and return `path`."""
    page.goto(f"{base_url}/index.html")
    page.screenshot(path=path, full_page=True)
    return path


def title_with_new_browser(playwright: Playwright, base_url: str) -> str:
    """Do it all by hand: launch Chromium, open a new context and page, read the home page title,
    close the browser and return the title.

    `playwright` is what `with sync_playwright() as playwright:` gives you in a plain script.
    """
    # Browser -> BrowserContext (an isolated incognito-like profile) -> Page (a tab).
    browser = playwright.chromium.launch(headless=True)
    try:
        context = browser.new_context()
        page = context.new_page()
        page.goto(f"{base_url}/index.html")
        return page.title()
    finally:
        browser.close()
