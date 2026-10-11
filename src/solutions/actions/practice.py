"""Actions practice: double and right clicks, multi-select, sliders, slow typing, uploads and
drag-and-drop."""

from pathlib import Path

from playwright.sync_api import Page


def double_click(page: Page, base_url: str) -> str:
    """Open widgets.html, double-click "Double-click me" and return the text of #dbl-out."""
    page.goto(f"{base_url}/widgets.html")
    page.get_by_role("button", name="Double-click me").dblclick()
    return page.locator("#dbl-out").inner_text()


def right_click(page: Page, base_url: str) -> str:
    """Open widgets.html, right-click the "Right-click me" box and return the text of #ctx-out."""
    page.goto(f"{base_url}/widgets.html")
    page.get_by_text("Right-click me").click(button="right")
    return page.locator("#ctx-out").inner_text()


def pick_fruits(page: Page, base_url: str, fruits: list[str]) -> str:
    """Open widgets.html, select every value in `fruits` (like ["apple", "cherry"]) in the
    "Fruits" list and return the text of #fruits-out."""
    page.goto(f"{base_url}/widgets.html")
    page.get_by_label("Fruits").select_option(fruits)
    return page.locator("#fruits-out").inner_text()


def set_volume(page: Page, base_url: str, value: int) -> str:
    """Open widgets.html, set the "Volume" slider to `value` and return the text of #volume-out."""
    # fill() works on <input type="range"> too.
    page.goto(f"{base_url}/widgets.html")
    page.get_by_label("Volume").fill(str(value))
    return page.locator("#volume-out").inner_text()


def type_slowly(page: Page, base_url: str, text: str) -> str:
    """Open widgets.html, type `text` into "Type and press Enter" one key at a time, 50 ms apart,
    and return the text of #char-count."""
    # press_sequentially() fires a key event per character, like a real person typing.
    page.goto(f"{base_url}/widgets.html")
    page.get_by_label("Type and press Enter").press_sequentially(text, delay=50)
    return page.locator("#char-count").inner_text()


def replace_bio(page: Page, base_url: str, text: str) -> str:
    """Open widgets.html, clear the "Bio" box, write `text` in it and return its value."""
    page.goto(f"{base_url}/widgets.html")
    bio = page.get_by_label("Bio")
    bio.clear()
    bio.fill(text)
    return bio.input_value()


def upload_file(page: Page, base_url: str, file: Path) -> str:
    """Open widgets.html, upload `file` with the "Upload files" input and return the text of
    #upload-out (it lists the uploaded file names)."""
    page.goto(f"{base_url}/widgets.html")
    page.get_by_label("Upload files").set_input_files(file)
    return page.locator("#upload-out").inner_text()


def drag_and_drop(page: Page, base_url: str) -> str:
    """Open widgets.html, drag "Item A" onto "Drop here" and return the drop zone's text."""
    page.goto(f"{base_url}/widgets.html")
    page.locator("#drag-item").drag_to(page.locator("#drop-zone"))
    return page.locator("#drop-zone").inner_text()
