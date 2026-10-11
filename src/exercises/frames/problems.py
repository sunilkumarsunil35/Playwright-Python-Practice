# Exercise file. Fill in each function, then run: sh run-tests.sh --mine -k frames
# Stuck? The worked answer is in src/solutions/frames/problems.py

"""Dialogs, frames and tabs: things that live outside the main page.

- Dialogs (alert, confirm, prompt): Playwright dismisses them by default. Register a handler with
  page.once("dialog", ...) before the click that opens one.
- Frames: an <iframe> is a separate document. Reach into it with frame_locator().
- Tabs and popups: catch the new page with expect_page() or expect_popup().
"""

from playwright.sync_api import BrowserContext, Dialog, Page


def read_alert(page: Page, base_url: str) -> str:
    """Open dialogs.html, click "Show alert", accept the alert and return its message."""
    raise NotImplementedError("Your turn: write this one")


def cancel_confirm(page: Page, base_url: str) -> str:
    """Open dialogs.html, click "Show confirm", press Cancel and return the text of #dialog-out."""
    raise NotImplementedError("Your turn: write this one")


def answer_prompt(page: Page, base_url: str, name: str) -> str:
    """Open dialogs.html, click "Show prompt", answer it with `name` and return the text of
    #dialog-out."""
    raise NotImplementedError("Your turn: write this one")


def fill_form_in_iframe(page: Page, base_url: str, name: str) -> str:
    """Open frames.html. Inside the "Signup form" iframe (id "form-frame"), fill "Name" with `name`,
    click "Join" and return the text of #joined inside the frame."""
    raise NotImplementedError("Your turn: write this one")


def open_link_in_new_tab(context: BrowserContext, page: Page, base_url: str) -> str:
    """Open tabs.html and click "Open help in new tab" (it has target="_blank"). Return the new
    tab's <h1> text."""
    raise NotImplementedError("Your turn: write this one")
