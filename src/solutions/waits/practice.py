"""Waiting practice: JavaScript conditions, URLs, load states, text changes and removed elements."""

from playwright.sync_api import Page, expect


def wait_for_counter(page: Page, base_url: str) -> int:
    """Open dynamic.html and click "Start counter". Wait until the JavaScript variable
    window.counter reaches at least 5, then return its value."""
    page.goto(f"{base_url}/dynamic.html")
    page.get_by_role("button", name="Start counter").click()
    page.wait_for_function("() => window.counter >= 5")
    return page.evaluate("() => window.counter")


def wait_for_redirect(page: Page, base_url: str) -> str:
    """Open account.html without signing in. The page sends you to the login page. Wait for the
    URL to contain "login.html" and return the full URL."""
    page.goto(f"{base_url}/account.html")
    page.wait_for_url("**/login.html*")
    return page.url


def wait_for_network_idle(page: Page, base_url: str) -> int:
    """Open shop.html, wait until the network is idle and return the number of products shown."""
    page.goto(f"{base_url}/shop.html")
    page.wait_for_load_state("networkidle")
    return page.get_by_test_id("product").count()


def wait_for_text_change(page: Page, base_url: str) -> None:
    """Open dynamic.html, click "Get ready" and assert #ready-status changes to "Ready" within
    2 seconds."""
    page.goto(f"{base_url}/dynamic.html")
    page.get_by_role("button", name="Get ready").click()
    expect(page.locator("#ready-status")).to_have_text("Ready", timeout=2000)


def wait_for_removal(page: Page, base_url: str) -> int:
    """Open dynamic.html, click "Dismiss" on the toast and wait until #toast is removed from the
    page. Return how many #toast elements are left (0)."""
    page.goto(f"{base_url}/dynamic.html")
    page.get_by_role("button", name="Dismiss").click()
    page.locator("#toast").wait_for(state="detached")
    return page.locator("#toast").count()


def load_all_items(page: Page, base_url: str) -> int:
    """Open dynamic.html and keep clicking "Load more" until the button disappears. Return how many
    items the list (id "items") has at the end."""
    page.goto(f"{base_url}/dynamic.html")
    more = page.get_by_role("button", name="Load more")
    items = page.locator("#items li")
    while more.is_visible():
        before = items.count()
        more.click()
        expect(items).not_to_have_count(before)
    return items.count()
