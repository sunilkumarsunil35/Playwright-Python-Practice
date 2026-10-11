from playwright.sync_api import expect

from common.target import load

P = load("waits", "practice")


def test_wait_for_counter(page, base_url):
    assert P.wait_for_counter(page, base_url) >= 5


def test_wait_for_redirect(page, base_url):
    assert P.wait_for_redirect(page, base_url) == f"{base_url}/login.html?next=account"


def test_wait_for_network_idle(page, base_url):
    assert P.wait_for_network_idle(page, base_url) == 4


def test_wait_for_text_change(page, base_url):
    P.wait_for_text_change(page, base_url)
    expect(page.locator("#ready-status")).to_have_text("Ready")


def test_wait_for_removal(page, base_url):
    assert P.wait_for_removal(page, base_url) == 0


def test_load_all_items(page, base_url):
    assert P.load_all_items(page, base_url) == 15
