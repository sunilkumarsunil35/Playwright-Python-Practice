"""Contexts practice: color scheme, geolocation, locale and time zone, offline mode, cookies and
running JavaScript in the page."""

from playwright.sync_api import Browser, Page


def dark_mode(browser: Browser, base_url: str) -> str:
    """Create a context that prefers a dark color scheme, open emulation.html and return #scheme."""
    context = browser.new_context(color_scheme="dark")
    try:
        page = context.new_page()
        page.goto(f"{base_url}/emulation.html")
        return page.locator("#scheme").inner_text()
    finally:
        context.close()


def fake_location(browser: Browser, base_url: str) -> str:
    """Create a context at latitude 12.9716, longitude 77.5946 (Bengaluru) with the "geolocation"
    permission granted. Open emulation.html, click "Where am I?" and return #geo once it changes
    from "Unknown"."""
    context = browser.new_context(geolocation={"latitude": 12.9716, "longitude": 77.5946}, permissions=["geolocation"])
    try:
        page = context.new_page()
        page.goto(f"{base_url}/emulation.html")
        page.get_by_role("button", name="Where am I?").click()
        geo = page.locator("#geo")
        geo.filter(has_not_text="Unknown").wait_for()
        return geo.inner_text()
    finally:
        context.close()


def german_locale(browser: Browser, base_url: str) -> tuple[str, str, str]:
    """Create a context with locale "de-DE" and time zone "Europe/Berlin". Open emulation.html and
    return the texts of #locale, #timezone and #date."""
    context = browser.new_context(locale="de-DE", timezone_id="Europe/Berlin")
    try:
        page = context.new_page()
        page.goto(f"{base_url}/emulation.html")
        return tuple(page.locator(sel).inner_text() for sel in ("#locale", "#timezone", "#date"))
    finally:
        context.close()


def go_offline(page: Page, base_url: str) -> str:
    """Open emulation.html, switch the context offline and return #online once it says
    "offline". Switch back online before returning."""
    page.goto(f"{base_url}/emulation.html")
    page.context.set_offline(True)
    try:
        online = page.locator("#online")
        online.filter(has_text="offline").wait_for()
        return online.inner_text()
    finally:
        page.context.set_offline(False)


def sign_in_with_cookie(page: Page, base_url: str) -> str:
    """Skip the login form: add the cookie session="session-ana" for base_url to the page's context,
    open account.html and return its <h1> text once it starts with "Signed in as"."""
    page.context.add_cookies([{"name": "session", "value": "session-ana", "url": base_url}])
    page.goto(f"{base_url}/account.html")
    heading = page.get_by_role("heading", name="Signed in as")
    heading.wait_for()
    return heading.inner_text()


def run_javascript(page: Page, base_url: str) -> dict:
    """Open the home page and use page.evaluate() to return a dict with the number of links on the
    page ("links") and the page's language attribute ("lang")."""
    page.goto(f"{base_url}/index.html")
    return page.evaluate("() => ({ links: document.links.length, lang: document.documentElement.lang })")
