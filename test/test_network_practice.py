from playwright.sync_api import expect

from common.target import load

P = load("network", "practice")


def test_discount_prices(page, base_url):
    assert P.discount_prices(page, base_url) == ["$499.5", "$24.5", "$12.5", "$99.5"]


def test_block_images(page, base_url):
    assert P.block_images(page, base_url) == 1


def test_list_api_calls(page, base_url):
    assert P.list_api_calls(page, base_url) == ["/api/products"]


def test_slow_api_shows_loading(page, base_url):
    P.slow_api_shows_loading(page, base_url)
    expect(page.get_by_test_id("product")).to_have_count(4)


def test_api_login_then_me(page, base_url):
    assert P.api_login_then_me(page, base_url) == "tom"


def test_api_delete_user(page, base_url):
    assert P.api_delete_user(page, base_url) == 204


def test_api_bad_request(page, base_url):
    assert P.api_bad_request(page, base_url) == (400, "name is required")
