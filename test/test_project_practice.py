from common.target import load

P = load("project", "practice")


def test_todos_survive_reload(page, base_url):
    assert P.todos_survive_reload(page, base_url) == ["Persist me", "Me too"]


def test_edit_todo(page, base_url):
    assert P.edit_todo(page, base_url) == ["Fixed"]


def test_checkout_journey(page, base_url):
    assert P.checkout_journey(page, base_url) == "Order confirmed for Sunil (2 items)"


def test_logout_journey(page, base_url):
    assert P.logout_journey(page, base_url) == f"{base_url}/login.html?next=account"


def test_languages_aria_snapshot(page, base_url):
    assert P.languages_aria_snapshot(page, base_url) == (
        '- list:\n  - listitem: Python\n  - listitem: JavaScript\n  - listitem: Java\n  - listitem: .NET'
    )


def test_check_aria_snapshot(page, base_url):
    P.check_aria_snapshot(page, base_url)
    assert page.url.endswith("index.html")
