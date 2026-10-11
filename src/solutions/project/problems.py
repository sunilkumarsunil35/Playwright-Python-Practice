"""End-to-end project: whole user journeys, plus tracing and video for debugging failures."""

from pathlib import Path

from playwright.sync_api import Browser, Page


def todo_journey(page: Page, base_url: str) -> tuple[list[str], str]:
    """On todo.html: add "Buy milk", "Write tests" and "Read docs", complete "Write tests", delete
    "Read docs", then click "Clear completed". Return the remaining todo texts and the counter."""
    page.goto(f"{base_url}/todo.html")
    box = page.get_by_placeholder("What needs to be done?")
    for text in ["Buy milk", "Write tests", "Read docs"]:
        box.fill(text)
        box.press("Enter")
    page.get_by_label("Toggle Write tests").check()
    page.get_by_role("button", name="Delete Read docs").click()
    page.get_by_role("button", name="Clear completed").click()
    return page.get_by_test_id("todo-item").locator("label").all_inner_texts(), page.get_by_test_id("todo-count").inner_text()


def todo_filters(page: Page, base_url: str) -> tuple[list[str], list[str]]:
    """On todo.html: add "A", "B" and "C" and complete "B". Return the texts shown under the
    "Active" filter, then under the "Completed" filter."""
    page.goto(f"{base_url}/todo.html")
    box = page.get_by_placeholder("What needs to be done?")
    for text in ["A", "B", "C"]:
        box.fill(text)
        box.press("Enter")
    page.get_by_label("Toggle B", exact=True).check()
    labels = page.get_by_test_id("todo-item").locator("label")
    page.get_by_role("button", name="Active").click()
    active = labels.all_inner_texts()
    page.get_by_role("button", name="Completed", exact=True).click()
    completed = labels.all_inner_texts()
    return active, completed


def record_trace(browser: Browser, base_url: str, path: Path) -> Path:
    """In a new context, start tracing with screenshots and snapshots, sign in as tom / secret on
    login.html, then stop tracing and save it to `path` (a .zip). Return `path`.

    Open the result with: playwright show-trace <path>
    """
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    try:
        page = context.new_page()
        page.goto(f"{base_url}/login.html")
        page.get_by_label("Username").fill("tom")
        page.get_by_label("Password").fill("secret")
        page.get_by_role("button", name="Sign in").click()
        page.wait_for_url("**/account.html")
    finally:
        context.tracing.stop(path=path)
        context.close()
    return path


def record_video(browser: Browser, base_url: str, folder: Path) -> Path:
    """Create a context that records video into `folder`, open the home page, click "Say hello",
    close the context (that writes the file) and return the video's path."""
    context = browser.new_context(record_video_dir=folder)
    page = context.new_page()
    page.goto(f"{base_url}/index.html")
    page.get_by_role("button", name="Say hello").click()
    context.close()
    return Path(page.video.path())
