from playwright.sync_api import expect

from common.target import load

P = load("assertions", "problems")


def test_check_title_and_url(page, base_url):
    P.check_title_and_url(page, base_url)
    assert page.url.endswith("index.html")


def test_check_login_error(page, base_url):
    P.check_login_error(page, base_url)
    expect(page.get_by_role("alert")).to_have_text("Invalid username or password")


def test_check_todo_count(page, base_url):
    P.check_todo_count(page, base_url)
    expect(page.get_by_test_id("todo-item")).to_have_count(3)


def test_check_form_state(page, base_url):
    P.check_form_state(page, base_url)
    expect(page.get_by_role("button", name="Continue")).to_be_enabled()


def test_check_banner_hidden(page, base_url):
    P.check_banner_hidden(page, base_url)
    expect(page.get_by_role("button", name="Accept cookies")).to_be_hidden()
