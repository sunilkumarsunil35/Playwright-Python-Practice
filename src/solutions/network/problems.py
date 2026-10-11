"""Network: watching, mocking and blocking requests, and testing an API directly.

- page.route(pattern, handler) intercepts matching requests. The handler fulfills them with your
  own response, lets them continue, or aborts them.
- page.request (or playwright.request.new_context()) sends HTTP calls without a page.
"""

import json

from playwright.sync_api import Page, Playwright, Route


def mock_products(page: Page, base_url: str) -> list[str]:
    """Make /api/products return just [{"id": 1, "name": "Teapot", "price": 12}] before opening
    shop.html. Return the product names the page shows."""
    page.route("**/api/products", lambda route: route.fulfill(json=[{"id": 1, "name": "Teapot", "price": 12}]))
    page.goto(f"{base_url}/shop.html")
    products = page.get_by_test_id("product")
    products.first.wait_for()
    return products.locator(".name").all_inner_texts()


def break_products(page: Page, base_url: str) -> str:
    """Make every request to /api/products fail (abort it), open shop.html and return the text of
    the error alert."""
    page.route("**/api/products", lambda route: route.abort())
    page.goto(f"{base_url}/shop.html")
    alert = page.get_by_role("alert")
    alert.wait_for()
    return alert.inner_text()


def capture_login_request(page: Page, base_url: str) -> dict:
    """Open login.html and sign in as tom / secret while waiting for the POST to /api/login.
    Return that request's JSON body as a dict."""
    page.goto(f"{base_url}/login.html")
    page.get_by_label("Username").fill("tom")
    page.get_by_label("Password").fill("secret")
    with page.expect_request("**/api/login") as request_info:
        page.get_by_role("button", name="Sign in").click()
    return json.loads(request_info.value.post_data)


def api_list_users(playwright: Playwright, base_url: str) -> list[str]:
    """Without any page, GET base_url + "/api/users" with an APIRequestContext and return the
    "name" of every user. Dispose of the context when done."""
    api = playwright.request.new_context(base_url=base_url)
    try:
        response = api.get("/api/users")
        assert response.ok
        return [user["name"] for user in response.json()]
    finally:
        api.dispose()


def api_create_user(page: Page, base_url: str, name: str) -> tuple[int, dict]:
    """With page.request, POST {"name": name, "job": "tester"} as JSON to base_url + "/api/users".
    Return a tuple of the status code and the JSON body."""
    response = page.request.post(f"{base_url}/api/users", data={"name": name, "job": "tester"})
    return response.status, response.json()
