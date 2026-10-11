"""Network practice: changing a real response, blocking images, listening to requests, slow
responses and more API calls."""

from playwright.sync_api import Page, Route, expect


def discount_prices(page: Page, base_url: str) -> list[str]:
    """Let /api/products reach the real server, but halve every price in the response before the
    page sees it. Open shop.html and return the prices the page shows, like ["$499.5", ...]."""
    def halve(route: Route):
        response = route.fetch()
        products = response.json()
        for product in products:
            product["price"] = product["price"] / 2
        route.fulfill(response=response, json=products)

    page.route("**/api/products", halve)
    page.goto(f"{base_url}/shop.html")
    page.get_by_test_id("product").first.wait_for()
    return page.locator(".price").all_inner_texts()


def block_images(page: Page, base_url: str) -> int:
    """Abort every image request, open shop.html and return how many requests you aborted."""
    blocked = []

    def handle(route: Route):
        if route.request.resource_type == "image":
            blocked.append(route.request.url)
            route.abort()
        else:
            route.continue_()

    page.route("**/*", handle)
    page.goto(f"{base_url}/shop.html", wait_until="networkidle")
    return len(blocked)


def list_api_calls(page: Page, base_url: str) -> list[str]:
    """Listen to every request the page makes, open shop.html, wait for the network to go idle, and
    return the paths (like "/api/products") of the requests whose URL contains "/api/"."""
    urls = []
    page.on("request", lambda request: urls.append(request.url))
    page.goto(f"{base_url}/shop.html", wait_until="networkidle")
    return [url.removeprefix(base_url) for url in urls if "/api/" in url]


def slow_api_shows_loading(page: Page, base_url: str) -> None:
    """Hold back /api/products until you have checked the page. Open shop.html, assert the text
    "Loading products…" is visible, then let the request continue and assert it is hidden."""
    held = []
    page.route("**/api/products", lambda route: held.append(route))
    page.goto(f"{base_url}/shop.html")
    loading = page.get_by_text("Loading products…")
    expect(loading).to_be_visible()
    while not held:  # the route handler runs while Playwright waits, so wait a little
        page.wait_for_timeout(50)
    held[0].continue_()
    expect(loading).to_be_hidden()


def api_login_then_me(page: Page, base_url: str) -> str:
    """With page.request, POST tom / secret to /api/login, then GET /api/me. page.request shares
    cookies with the page, so the second call is signed in. Return the "username" from /api/me."""
    login = page.request.post(f"{base_url}/api/login", data={"username": "tom", "password": "secret"})
    assert login.ok
    return page.request.get(f"{base_url}/api/me").json()["username"]


def api_delete_user(page: Page, base_url: str) -> int:
    """DELETE base_url + "/api/users/2" with page.request and return the status code."""
    return page.request.delete(f"{base_url}/api/users/2").status


def api_bad_request(page: Page, base_url: str) -> tuple[int, str]:
    """POST {} (no name) to /api/users with page.request and return the status and the "error"
    message from the body."""
    response = page.request.post(f"{base_url}/api/users", data={})
    return response.status, response.json()["error"]
