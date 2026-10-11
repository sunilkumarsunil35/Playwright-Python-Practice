from common.target import load

P = load("network", "problems")


def test_mock_products(page, base_url):
    assert P.mock_products(page, base_url) == ["Teapot"]


def test_break_products(page, base_url):
    assert P.break_products(page, base_url) == "Failed to load products"


def test_capture_login_request(page, base_url):
    assert P.capture_login_request(page, base_url) == {"username": "tom", "password": "secret"}


def test_api_list_users(playwright, base_url):
    assert P.api_list_users(playwright, base_url) == ["Leanne Graham", "Ervin Howell", "Clementine Bauch"]


def test_api_create_user(page, base_url):
    assert P.api_create_user(page, base_url, "Sunil") == (201, {"id": 101, "name": "Sunil", "job": "tester"})
