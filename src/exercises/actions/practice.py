# Exercise file. Fill in each function, then run: sh run-tests.sh --mine -k actions
# Stuck? The worked answer is in src/solutions/actions/practice.py

"""Actions practice: double and right clicks, multi-select, sliders, slow typing, uploads and
drag-and-drop."""

from pathlib import Path

from playwright.sync_api import Page


def double_click(page: Page, base_url: str) -> str:
    """Open widgets.html, double-click "Double-click me" and return the text of #dbl-out."""
    raise NotImplementedError("Your turn: write this one")


def right_click(page: Page, base_url: str) -> str:
    """Open widgets.html, right-click the "Right-click me" box and return the text of #ctx-out."""
    raise NotImplementedError("Your turn: write this one")


def pick_fruits(page: Page, base_url: str, fruits: list[str]) -> str:
    """Open widgets.html, select every value in `fruits` (like ["apple", "cherry"]) in the
    "Fruits" list and return the text of #fruits-out."""
    raise NotImplementedError("Your turn: write this one")


def set_volume(page: Page, base_url: str, value: int) -> str:
    """Open widgets.html, set the "Volume" slider to `value` and return the text of #volume-out."""
    raise NotImplementedError("Your turn: write this one")


def type_slowly(page: Page, base_url: str, text: str) -> str:
    """Open widgets.html, type `text` into "Type and press Enter" one key at a time, 50 ms apart,
    and return the text of #char-count."""
    raise NotImplementedError("Your turn: write this one")


def replace_bio(page: Page, base_url: str, text: str) -> str:
    """Open widgets.html, clear the "Bio" box, write `text` in it and return its value."""
    raise NotImplementedError("Your turn: write this one")


def upload_file(page: Page, base_url: str, file: Path) -> str:
    """Open widgets.html, upload `file` with the "Upload files" input and return the text of
    #upload-out (it lists the uploaded file names)."""
    raise NotImplementedError("Your turn: write this one")


def drag_and_drop(page: Page, base_url: str) -> str:
    """Open widgets.html, drag "Item A" onto "Drop here" and return the drop zone's text."""
    raise NotImplementedError("Your turn: write this one")
