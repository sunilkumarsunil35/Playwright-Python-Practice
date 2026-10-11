# Exercise file. Fill in each function, then run: sh run-tests.sh --mine -k context
# Stuck? The worked answer is in src/solutions/context/practice.py

"""Contexts practice: color scheme, geolocation, locale and time zone, offline mode, cookies and
running JavaScript in the page."""

from playwright.sync_api import Browser, Page


def dark_mode(browser: Browser, base_url: str) -> str:
    """Create a context that prefers a dark color scheme, open emulation.html and return #scheme."""
    raise NotImplementedError("Your turn: write this one")


def fake_location(browser: Browser, base_url: str) -> str:
    """Create a context at latitude 12.9716, longitude 77.5946 (Bengaluru) with the "geolocation"
    permission granted. Open emulation.html, click "Where am I?" and return #geo once it changes
    from "Unknown"."""
    raise NotImplementedError("Your turn: write this one")


def german_locale(browser: Browser, base_url: str) -> tuple[str, str, str]:
    """Create a context with locale "de-DE" and time zone "Europe/Berlin". Open emulation.html and
    return the texts of #locale, #timezone and #date."""
    raise NotImplementedError("Your turn: write this one")


def go_offline(page: Page, base_url: str) -> str:
    """Open emulation.html, switch the context offline and return #online once it says
    "offline". Switch back online before returning."""
    raise NotImplementedError("Your turn: write this one")


def sign_in_with_cookie(page: Page, base_url: str) -> str:
    """Skip the login form: add the cookie session="session-ana" for base_url to the page's context,
    open account.html and return its <h1> text once it starts with "Signed in as"."""
    raise NotImplementedError("Your turn: write this one")


def run_javascript(page: Page, base_url: str) -> dict:
    """Open the home page and use page.evaluate() to return a dict with the number of links on the
    page ("links") and the page's language attribute ("lang")."""
    raise NotImplementedError("Your turn: write this one")
