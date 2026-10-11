# Exercise file. Fill in each function, then run: sh run-tests.sh --mine -k pom
# Stuck? The worked answer is in src/solutions/pom/problems.py

"""Page objects: wrap a page in a class so tests read like steps and locators live in one place.

A test then says `login.login("tom", "secret")` instead of repeating three locator lines. When the
page changes, you fix the page object, not every test. See test/test_pom.py for how the tests use
these with pytest fixtures and parametrize.
"""

from playwright.sync_api import Page


class LoginPage:
    """The sign-in page, login.html."""

    def __init__(self, page: Page, base_url: str):
        """Keep the page and base_url, and create the locators the methods need."""
        raise NotImplementedError("Your turn: write this one")

    def open(self) -> "LoginPage":
        """Go to the login page and return self, so calls can be chained."""
        raise NotImplementedError("Your turn: write this one")

    def login(self, username: str, password: str) -> None:
        """Fill in both fields and click "Sign in"."""
        raise NotImplementedError("Your turn: write this one")

    def error_text(self) -> str:
        """Wait for the error alert and return its text."""
        raise NotImplementedError("Your turn: write this one")


class TodoPage:
    """The todo app, todo.html."""

    def __init__(self, page: Page, base_url: str):
        """Keep the page and base_url, and create the locators the methods need."""
        raise NotImplementedError("Your turn: write this one")

    def open(self) -> "TodoPage":
        """Go to the todo page and return self."""
        raise NotImplementedError("Your turn: write this one")

    def add(self, *texts: str) -> None:
        """Add each text as a new todo."""
        raise NotImplementedError("Your turn: write this one")

    def complete(self, text: str) -> None:
        """Tick the checkbox of the todo `text`."""
        raise NotImplementedError("Your turn: write this one")

    def delete(self, text: str) -> None:
        """Click the Delete button of the todo `text`."""
        raise NotImplementedError("Your turn: write this one")

    def show(self, name: str) -> None:
        """Click the filter button `name`: "All", "Active" or "Completed"."""
        raise NotImplementedError("Your turn: write this one")

    def texts(self) -> list[str]:
        """Return the text of every todo shown, in order."""
        raise NotImplementedError("Your turn: write this one")

    def remaining(self) -> str:
        """Return the counter text, like "2 items left"."""
        raise NotImplementedError("Your turn: write this one")
