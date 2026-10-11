# Exercise file. Fill in each function, then run: sh run-tests.sh --mine -k frames
# Stuck? The worked answer is in src/solutions/frames/practice.py

"""Dialogs, frames and tabs practice: popups, nested frames, downloads and switching tabs."""

from pathlib import Path

from playwright.sync_api import Page


def accept_confirm(page: Page, base_url: str) -> str:
    """Open dialogs.html, click "Show confirm", press OK and return the text of #dialog-out."""
    raise NotImplementedError("Your turn: write this one")


def read_popup(page: Page, base_url: str) -> str:
    """Open tabs.html and click "Open popup window" (it calls window.open). Return the text of
    #from in the popup."""
    raise NotImplementedError("Your turn: write this one")


def nested_frame_text(page: Page, base_url: str) -> str:
    """Open frames.html and return the text of #secret, which lives in an iframe (#inner-frame)
    inside another iframe (#outer-frame)."""
    raise NotImplementedError("Your turn: write this one")


def count_frames(page: Page, base_url: str) -> int:
    """Open frames.html, wait for it to load fully and return len(page.frames). The main page
    counts as a frame too."""
    raise NotImplementedError("Your turn: write this one")


def download_report(page: Page, base_url: str, folder: Path) -> str:
    """Open downloads.html, click "Download report", save the file into `folder` under the name the
    server suggests and return the file's text."""
    raise NotImplementedError("Your turn: write this one")


def close_tab_and_return(page: Page, base_url: str) -> tuple[int, str]:
    """Open tabs.html, open the help link in a new tab, close that tab, and return a tuple of how
    many pages the context has now and the original page's title."""
    raise NotImplementedError("Your turn: write this one")
