"""Waiting: let Playwright wait for the page instead of sleeping.

Never use time.sleep(). Actions and expect() already wait. When you need more, wait for a specific
thing: an element state, a URL, a network response or a JavaScript condition.
"""

from playwright.sync_api import Page, expect


def wait_for_new_element(page: Page, base_url: str) -> str:
    """Open dynamic.html and click "Start". About a second later an element with id "result"
    appears. Return its text."""
    page.goto(f"{base_url}/dynamic.html")
    page.get_by_role("button", name="Start", exact=True).click()
    result = page.locator("#result")
    result.wait_for()  # default state is "visible"
    return result.inner_text()


def wait_until_enabled(page: Page, base_url: str) -> str:
    """Open dynamic.html and click "Enable submit". "Submit" becomes enabled about a second later.
    Click it and return the text of #submit-out."""
    # click() waits for the button to be enabled, so no extra wait is needed.
    page.goto(f"{base_url}/dynamic.html")
    page.get_by_role("button", name="Enable submit").click()
    page.get_by_role("button", name="Submit", exact=True).click()
    return page.locator("#submit-out").inner_text()


def wait_for_spinner(page: Page, base_url: str) -> str:
    """Open dynamic.html and click "Load data". Wait until the "Loading…" spinner is hidden, then
    return the text of #data."""
    page.goto(f"{base_url}/dynamic.html")
    page.get_by_role("button", name="Load data").click()
    page.locator("#spinner").wait_for(state="hidden")
    return page.locator("#data").inner_text()


def wait_for_api_response(page: Page, base_url: str) -> list[str]:
    """Open dynamic.html and click "Load more" while waiting for the /api/items response.
    Return the "items" list from that response's JSON body."""
    # expect_response() must start before the click, so it can't miss a fast response.
    page.goto(f"{base_url}/dynamic.html")
    with page.expect_response("**/api/items?page=1") as response_info:
        page.get_by_role("button", name="Load more").click()
    return response_info.value.json()["items"]
