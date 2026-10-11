"""Dialogs, frames and tabs practice: popups, nested frames, downloads and switching tabs."""

from pathlib import Path

from playwright.sync_api import Page


def accept_confirm(page: Page, base_url: str) -> str:
    """Open dialogs.html, click "Show confirm", press OK and return the text of #dialog-out."""
    page.goto(f"{base_url}/dialogs.html")
    page.once("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Show confirm").click()
    return page.locator("#dialog-out").inner_text()


def read_popup(page: Page, base_url: str) -> str:
    """Open tabs.html and click "Open popup window" (it calls window.open). Return the text of
    #from in the popup."""
    page.goto(f"{base_url}/tabs.html")
    with page.expect_popup() as popup_info:
        page.get_by_role("button", name="Open popup window").click()
    popup = popup_info.value
    return popup.locator("#from").inner_text()


def nested_frame_text(page: Page, base_url: str) -> str:
    """Open frames.html and return the text of #secret, which lives in an iframe (#inner-frame)
    inside another iframe (#outer-frame)."""
    page.goto(f"{base_url}/frames.html")
    return page.frame_locator("#outer-frame").frame_locator("#inner-frame").locator("#secret").inner_text()


def count_frames(page: Page, base_url: str) -> int:
    """Open frames.html, wait for it to load fully and return len(page.frames). The main page
    counts as a frame too."""
    page.goto(f"{base_url}/frames.html")
    page.frame_locator("#outer-frame").frame_locator("#inner-frame").locator("#secret").wait_for()
    return len(page.frames)


def download_report(page: Page, base_url: str, folder: Path) -> str:
    """Open downloads.html, click "Download report", save the file into `folder` under the name the
    server suggests and return the file's text."""
    page.goto(f"{base_url}/downloads.html")
    with page.expect_download() as download_info:
        page.get_by_role("link", name="Download report").click()
    download = download_info.value
    target = folder / download.suggested_filename
    download.save_as(target)
    return target.read_text()


def close_tab_and_return(page: Page, base_url: str) -> tuple[int, str]:
    """Open tabs.html, open the help link in a new tab, close that tab, and return a tuple of how
    many pages the context has now and the original page's title."""
    page.goto(f"{base_url}/tabs.html")
    with page.context.expect_page() as info:
        page.get_by_role("link", name="Open help in new tab").click()
    info.value.close()
    return len(page.context.pages), page.title()
