# Exercise file. Fill in each function, then run: sh run-tests.sh --mine -k waits
# Stuck? The worked answer is in src/solutions/waits/problems.py

"""Waiting: let Playwright wait for the page instead of sleeping.

Never use time.sleep(). Actions and expect() already wait. When you need more, wait for a specific
thing: an element state, a URL, a network response or a JavaScript condition.
"""

from playwright.sync_api import Page, expect


def wait_for_new_element(page: Page, base_url: str) -> str:
    """Open dynamic.html and click "Start". About a second later an element with id "result"
    appears. Return its text."""
    raise NotImplementedError("Your turn: write this one")


def wait_until_enabled(page: Page, base_url: str) -> str:
    """Open dynamic.html and click "Enable submit". "Submit" becomes enabled about a second later.
    Click it and return the text of #submit-out."""
    raise NotImplementedError("Your turn: write this one")


def wait_for_spinner(page: Page, base_url: str) -> str:
    """Open dynamic.html and click "Load data". Wait until the "Loading…" spinner is hidden, then
    return the text of #data."""
    raise NotImplementedError("Your turn: write this one")


def wait_for_api_response(page: Page, base_url: str) -> list[str]:
    """Open dynamic.html and click "Load more" while waiting for the /api/items response.
    Return the "items" list from that response's JSON body."""
    raise NotImplementedError("Your turn: write this one")
