from common.target import load

P = load("basics", "practice")


def test_back_and_forward(page, base_url):
    assert P.back_and_forward(page, base_url) == ["Playwright Practice", "Todo", "Playwright Practice", "Todo"]


def test_url_after_redirect(page, base_url):
    assert P.url_after_redirect(page, base_url) == f"{base_url}/login.html"


def test_count_menu_links(page, base_url):
    assert P.count_menu_links(page, base_url) == 12


def test_read_meta_description(page, base_url):
    assert P.read_meta_description(page, base_url) == "A practice site for learning Playwright with Python"


def test_phone_sized_viewport(page, base_url):
    assert P.phone_sized_viewport(page, base_url) == "375x667"


def test_screenshot_of_pricing(page, base_url, tmp_path):
    path = P.screenshot_of_pricing(page, base_url, tmp_path / "pricing.png")
    data = path.read_bytes()
    assert data[:8] == b"\x89PNG\r\n\x1a\n"
    width = int.from_bytes(data[16:20], "big")
    assert width < 1280, "screenshot the Pricing section only, not the whole page"
