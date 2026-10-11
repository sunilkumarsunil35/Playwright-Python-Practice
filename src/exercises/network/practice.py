# Exercise file. Fill in each function, then run: sh run-tests.sh --mine -k network
# Stuck? The worked answer is in src/solutions/network/practice.py

"""Network practice: changing a real response, blocking images, listening to requests, slow
responses and more API calls."""

from playwright.sync_api import Page, Route, expect


def discount_prices(page: Page, base_url: str) -> list[str]:
    """Let /api/products reach the real server, but halve every price in the response before the
    page sees it. Open shop.html and return the prices the page shows, like ["$499.5", ...]."""
    raise NotImplementedError("Your turn: write this one")


def block_images(page: Page, base_url: str) -> int:
    """Abort every image request, open shop.html and return how many requests you aborted."""
    raise NotImplementedError("Your turn: write this one")


def list_api_calls(page: Page, base_url: str) -> list[str]:
    """Listen to every request the page makes, open shop.html, wait for the network to go idle, and
    return the paths (like "/api/products") of the requests whose URL contains "/api/"."""
    raise NotImplementedError("Your turn: write this one")


def slow_api_shows_loading(page: Page, base_url: str) -> None:
    """Hold back /api/products until you have checked the page. Open shop.html, assert the text
    "Loading products…" is visible, then let the request continue and assert it is hidden."""
    raise NotImplementedError("Your turn: write this one")


def api_login_then_me(page: Page, base_url: str) -> str:
    """With page.request, POST tom / secret to /api/login, then GET /api/me. page.request shares
    cookies with the page, so the second call is signed in. Return the "username" from /api/me."""
    raise NotImplementedError("Your turn: write this one")


def api_delete_user(page: Page, base_url: str) -> int:
    """DELETE base_url + "/api/users/2" with page.request and return the status code."""
    raise NotImplementedError("Your turn: write this one")


def api_bad_request(page: Page, base_url: str) -> tuple[int, str]:
    """POST {} (no name) to /api/users with page.request and return the status and the "error"
    message from the body."""
    raise NotImplementedError("Your turn: write this one")
