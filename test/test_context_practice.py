from common.target import load

P = load("context", "practice")


def test_dark_mode(browser, base_url):
    assert P.dark_mode(browser, base_url) == "dark"


def test_fake_location(browser, base_url):
    assert P.fake_location(browser, base_url) == "12.9716, 77.5946"


def test_german_locale(browser, base_url):
    assert P.german_locale(browser, base_url) == ("de-DE", "Europe/Berlin", "15.1.2026")


def test_go_offline(page, base_url):
    assert P.go_offline(page, base_url) == "offline"


def test_sign_in_with_cookie(page, base_url):
    assert P.sign_in_with_cookie(page, base_url) == "Signed in as ana"


def test_run_javascript(page, base_url):
    assert P.run_javascript(page, base_url) == {"links": 12, "lang": "en"}
