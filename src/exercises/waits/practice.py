# Exercise file. Fill in each function, then run: sh run-tests.sh --mine -k waits
# Stuck? The worked answer is in src/solutions/waits/practice.py

"""Waiting practice: JavaScript conditions, URLs, load states, text changes and removed elements."""

from playwright.sync_api import Page, expect


def wait_for_counter(page: Page, base_url: str) -> int:
    """Open dynamic.html and click "Start counter". Wait until the JavaScript variable
    window.counter reaches at least 5, then return its value."""
    raise NotImplementedError("Your turn: write this one")


def wait_for_redirect(page: Page, base_url: str) -> str:
    """Open account.html without signing in. The page sends you to the login page. Wait for the
    URL to contain "login.html" and return the full URL."""
    raise NotImplementedError("Your turn: write this one")


def wait_for_network_idle(page: Page, base_url: str) -> int:
    """Open shop.html, wait until the network is idle and return the number of products shown."""
    raise NotImplementedError("Your turn: write this one")


def wait_for_text_change(page: Page, base_url: str) -> None:
    """Open dynamic.html, click "Get ready" and assert #ready-status changes to "Ready" within
    2 seconds."""
    raise NotImplementedError("Your turn: write this one")


def wait_for_removal(page: Page, base_url: str) -> int:
    """Open dynamic.html, click "Dismiss" on the toast and wait until #toast is removed from the
    page. Return how many #toast elements are left (0)."""
    raise NotImplementedError("Your turn: write this one")


def load_all_items(page: Page, base_url: str) -> int:
    """Open dynamic.html and keep clicking "Load more" until the button disappears. Return how many
    items the list (id "items") has at the end."""
    raise NotImplementedError("Your turn: write this one")
