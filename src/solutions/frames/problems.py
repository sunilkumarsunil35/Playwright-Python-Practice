"""Dialogs, frames and tabs: things that live outside the main page.

- Dialogs (alert, confirm, prompt): Playwright dismisses them by default. Register a handler with
  page.once("dialog", ...) before the click that opens one.
- Frames: an <iframe> is a separate document. Reach into it with frame_locator().
- Tabs and popups: catch the new page with expect_page() or expect_popup().
"""

from playwright.sync_api import BrowserContext, Dialog, Page


def read_alert(page: Page, base_url: str) -> str:
    """Open dialogs.html, click "Show alert", accept the alert and return its message."""
    page.goto(f"{base_url}/dialogs.html")
    messages = []

    def handle(dialog: Dialog):
        messages.append(dialog.message)
        dialog.accept()

    page.once("dialog", handle)
    page.get_by_role("button", name="Show alert").click()
    return messages[0]


def cancel_confirm(page: Page, base_url: str) -> str:
    """Open dialogs.html, click "Show confirm", press Cancel and return the text of #dialog-out."""
    page.goto(f"{base_url}/dialogs.html")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Show confirm").click()
    return page.locator("#dialog-out").inner_text()


def answer_prompt(page: Page, base_url: str, name: str) -> str:
    """Open dialogs.html, click "Show prompt", answer it with `name` and return the text of
    #dialog-out."""
    page.goto(f"{base_url}/dialogs.html")
    page.once("dialog", lambda dialog: dialog.accept(name))
    page.get_by_role("button", name="Show prompt").click()
    return page.locator("#dialog-out").inner_text()


def fill_form_in_iframe(page: Page, base_url: str, name: str) -> str:
    """Open frames.html. Inside the "Signup form" iframe (id "form-frame"), fill "Name" with `name`,
    click "Join" and return the text of #joined inside the frame."""
    page.goto(f"{base_url}/frames.html")
    frame = page.frame_locator("#form-frame")
    frame.get_by_label("Name").fill(name)
    frame.get_by_role("button", name="Join").click()
    return frame.locator("#joined").inner_text()


def open_link_in_new_tab(context: BrowserContext, page: Page, base_url: str) -> str:
    """Open tabs.html and click "Open help in new tab" (it has target="_blank"). Return the new
    tab's <h1> text."""
    # A new tab is a new Page in the same context.
    page.goto(f"{base_url}/tabs.html")
    with context.expect_page() as new_page_info:
        page.get_by_role("link", name="Open help in new tab").click()
    new_page = new_page_info.value
    new_page.wait_for_load_state()
    return new_page.locator("h1").inner_text()
