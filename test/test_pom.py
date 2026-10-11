"""Tests for the page objects. They also show the pytest patterns you will use every day:

- a fixture that builds a page object and opens the page (`login_page`, `todos`)
- parametrize, to run one test with several inputs
- tests that read like steps because the page object hides the locators
"""

import pytest

from common.target import load

P = load("pom", "problems")


@pytest.fixture
def login_page(page, base_url):
    return P.LoginPage(page, base_url).open()


@pytest.fixture
def todos(page, base_url):
    return P.TodoPage(page, base_url).open()


def test_login_page_signs_in(login_page, page):
    login_page.login("tom", "secret")
    page.wait_for_url("**/account.html")


@pytest.mark.parametrize("username, password", [("tom", "wrong"), ("nobody", "secret"), ("", "")])
def test_login_page_shows_error(login_page, username, password):
    login_page.login(username, password)
    assert login_page.error_text() == "Invalid username or password"


def test_todo_page_add_and_count(todos):
    todos.add("One", "Two", "Three")
    assert todos.texts() == ["One", "Two", "Three"]
    assert todos.remaining() == "3 items left"


def test_todo_page_complete_and_filter(todos):
    todos.add("One", "Two")
    todos.complete("One")
    assert todos.remaining() == "1 item left"
    todos.show("Completed")
    assert todos.texts() == ["One"]
    todos.show("All")
    assert todos.texts() == ["One", "Two"]


def test_todo_page_delete(todos):
    todos.add("Keep", "Drop")
    todos.delete("Drop")
    assert todos.texts() == ["Keep"]
