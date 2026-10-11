# Exercise file. Fill in each function, then run: sh run-tests.sh --mine -k context
# Stuck? The worked answer is in src/solutions/context/problems.py

"""Contexts, sign-in reuse and emulation.

A BrowserContext is a fresh, isolated browser profile: its own cookies, storage and settings. You
can create many from one browser. Sign in once, save the context's storage state to a file, and
start later contexts already signed in.
"""

from pathlib import Path

from playwright.sync_api import Browser, Playwright


def save_signed_in_state(browser: Browser, base_url: str, path: Path) -> Path:
    """In a new context, sign in through login.html as tom / secret, wait for account.html, save the
    context's storage state to `path`, close the context and return `path`."""
    raise NotImplementedError("Your turn: write this one")


def reuse_signed_in_state(browser: Browser, base_url: str, path: Path) -> str:
    """Start a new context from the storage state file at `path`, open account.html and return its
    <h1> text once it starts with "Signed in as"."""
    raise NotImplementedError("Your turn: write this one")


def two_users_at_once(browser: Browser, base_url: str) -> tuple[str, str]:
    """Sign in as tom in one context and as ana (password "hunter2") in a second context, both
    through login.html. Return the account page <h1> text of each, as (tom's, ana's)."""
    raise NotImplementedError("Your turn: write this one")


def emulate_iphone(playwright: Playwright, browser: Browser, base_url: str) -> tuple[str, str]:
    """Create a context from the "iPhone 13" device preset, open emulation.html and return the texts
    of #viewport and #ua."""
    raise NotImplementedError("Your turn: write this one")
