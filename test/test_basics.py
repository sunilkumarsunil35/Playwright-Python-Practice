from common.target import load

P = load("basics", "problems")


def test_open_and_get_title(page, base_url):
    assert P.open_and_get_title(page, base_url) == "Playwright Practice"


def test_get_heading_text(page, base_url):
    assert P.get_heading_text(page, base_url) == "Welcome to the practice site"


def test_navigate_by_link(page, base_url):
    assert P.navigate_by_link(page, base_url) == f"{base_url}/login.html"


def test_take_screenshot(page, base_url, tmp_path):
    path = P.take_screenshot(page, base_url, tmp_path / "home.png")
    assert path.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n"


def test_title_with_new_browser(playwright, base_url):
    assert P.title_with_new_browser(playwright, base_url) == "Playwright Practice"
