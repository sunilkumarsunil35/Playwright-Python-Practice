from common.target import load

P = load("waits", "problems")


def test_wait_for_new_element(page, base_url):
    assert P.wait_for_new_element(page, base_url) == "Hello World!"


def test_wait_until_enabled(page, base_url):
    assert P.wait_until_enabled(page, base_url) == "Submitted"


def test_wait_for_spinner(page, base_url):
    assert P.wait_for_spinner(page, base_url) == "Data loaded: 42"


def test_wait_for_api_response(page, base_url):
    assert P.wait_for_api_response(page, base_url) == [f"Item {i}" for i in range(1, 6)]
