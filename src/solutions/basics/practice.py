"""Basics practice: navigation history, redirects, viewport, attributes and element screenshots."""

from pathlib import Path

from playwright.sync_api import Page


def back_and_forward(page: Page, base_url: str) -> list[str]:
    """Open index.html, then todo.html. Go back, then forward. Return the page title after each
    of the four steps, in order: ["Playwright Practice", "Todo", "Playwright Practice", "Todo"]."""
    titles = []
    page.goto(f"{base_url}/index.html")
    titles.append(page.title())
    page.goto(f"{base_url}/todo.html")
    titles.append(page.title())
    page.go_back()
    titles.append(page.title())
    page.go_forward()
    titles.append(page.title())
    return titles


def url_after_redirect(page: Page, base_url: str) -> str:
    """Open base_url + "/redirect". The server redirects you. Return the final URL."""
    # goto() follows HTTP redirects; page.url is where the browser ended up.
    page.goto(f"{base_url}/redirect")
    return page.url


def count_menu_links(page: Page, base_url: str) -> int:
    """Open the home page and return how many links the main menu (<nav>) has."""
    page.goto(f"{base_url}/index.html")
    return page.locator("nav a").count()


def read_meta_description(page: Page, base_url: str) -> str:
    """Open the home page and return the content of <meta name="description">."""
    # Elements in <head> are not visible, but get_attribute() still reads them.
    page.goto(f"{base_url}/index.html")
    return page.locator('meta[name="description"]').get_attribute("content")


def phone_sized_viewport(page: Page, base_url: str) -> str:
    """Resize the page to 375 x 667 (an iPhone SE), open emulation.html and return the text of the
    element with id "viewport" (it shows the size the page sees, like "375x667")."""
    page.set_viewport_size({"width": 375, "height": 667})
    page.goto(f"{base_url}/emulation.html")
    return page.locator("#viewport").inner_text()


def screenshot_of_pricing(page: Page, base_url: str, path: Path) -> Path:
    """Open the home page and save a screenshot of just the "Pricing" section to `path`."""
    # Locators have their own screenshot(); it crops to the element.
    page.goto(f"{base_url}/index.html")
    page.get_by_role("region", name="Pricing").screenshot(path=path)
    return path
