# Exercise file. Fill in each function, then run: sh run-tests.sh --mine -k network
# Stuck? The worked answer is in src/solutions/network/problems.py

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
    raise NotImplementedError("Your turn: write this one")


def break_products(page: Page, base_url: str) -> str:
    """Make every request to /api/products fail (abort it), open shop.html and return the text of
    the error alert."""
    raise NotImplementedError("Your turn: write this one")


def capture_login_request(page: Page, base_url: str) -> dict:
    """Open login.html and sign in as tom / secret while waiting for the POST to /api/login.
    Return that request's JSON body as a dict."""
    raise NotImplementedError("Your turn: write this one")


def api_list_users(playwright: Playwright, base_url: str) -> list[str]:
    """Without any page, GET base_url + "/api/users" with an APIRequestContext and return the
    "name" of every user. Dispose of the context when done."""
    raise NotImplementedError("Your turn: write this one")


def api_create_user(page: Page, base_url: str, name: str) -> tuple[int, dict]:
    """With page.request, POST {"name": name, "job": "tester"} as JSON to base_url + "/api/users".
    Return a tuple of the status code and the JSON body."""
    raise NotImplementedError("Your turn: write this one")
