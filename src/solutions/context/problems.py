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
    context = browser.new_context()
    try:
        page = context.new_page()
        page.goto(f"{base_url}/login.html")
        page.get_by_label("Username").fill("tom")
        page.get_by_label("Password").fill("secret")
        page.get_by_role("button", name="Sign in").click()
        page.wait_for_url("**/account.html")
        context.storage_state(path=path)
        return path
    finally:
        context.close()


def reuse_signed_in_state(browser: Browser, base_url: str, path: Path) -> str:
    """Start a new context from the storage state file at `path`, open account.html and return its
    <h1> text once it starts with "Signed in as"."""
    context = browser.new_context(storage_state=path)
    try:
        page = context.new_page()
        page.goto(f"{base_url}/account.html")
        heading = page.get_by_role("heading", name="Signed in as")
        heading.wait_for()
        return heading.inner_text()
    finally:
        context.close()


def two_users_at_once(browser: Browser, base_url: str) -> tuple[str, str]:
    """Sign in as tom in one context and as ana (password "hunter2") in a second context, both
    through login.html. Return the account page <h1> text of each, as (tom's, ana's)."""
    def sign_in(username, password):
        context = browser.new_context()
        page = context.new_page()
        page.goto(f"{base_url}/login.html")
        page.get_by_label("Username").fill(username)
        page.get_by_label("Password").fill(password)
        page.get_by_role("button", name="Sign in").click()
        heading = page.get_by_role("heading", name="Signed in as")
        heading.wait_for()
        return context, heading

    tom_context, tom = sign_in("tom", "secret")
    ana_context, ana = sign_in("ana", "hunter2")
    try:
        return tom.inner_text(), ana.inner_text()
    finally:
        tom_context.close()
        ana_context.close()


def emulate_iphone(playwright: Playwright, browser: Browser, base_url: str) -> tuple[str, str]:
    """Create a context from the "iPhone 13" device preset, open emulation.html and return the texts
    of #viewport and #ua."""
    # playwright.devices holds viewport, user agent, touch and scale settings for real devices.
    context = browser.new_context(**playwright.devices["iPhone 13"])
    try:
        page = context.new_page()
        page.goto(f"{base_url}/emulation.html")
        return page.locator("#viewport").inner_text(), page.locator("#ua").inner_text()
    finally:
        context.close()
