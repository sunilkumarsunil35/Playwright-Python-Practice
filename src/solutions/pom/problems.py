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
        self.page = page
        self.url = f"{base_url}/login.html"
        self.username = page.get_by_label("Username")
        self.password = page.get_by_label("Password")
        self.submit = page.get_by_role("button", name="Sign in")
        self.error = page.get_by_role("alert")

    def open(self) -> "LoginPage":
        """Go to the login page and return self, so calls can be chained."""
        self.page.goto(self.url)
        return self

    def login(self, username: str, password: str) -> None:
        """Fill in both fields and click "Sign in"."""
        self.username.fill(username)
        self.password.fill(password)
        self.submit.click()

    def error_text(self) -> str:
        """Wait for the error alert and return its text."""
        self.error.wait_for()
        return self.error.inner_text()


class TodoPage:
    """The todo app, todo.html."""

    def __init__(self, page: Page, base_url: str):
        """Keep the page and base_url, and create the locators the methods need."""
        self.page = page
        self.url = f"{base_url}/todo.html"
        self.new_todo = page.get_by_placeholder("What needs to be done?")
        self.items = page.get_by_test_id("todo-item")
        self.count = page.get_by_test_id("todo-count")

    def open(self) -> "TodoPage":
        """Go to the todo page and return self."""
        self.page.goto(self.url)
        return self

    def add(self, *texts: str) -> None:
        """Add each text as a new todo."""
        for text in texts:
            self.new_todo.fill(text)
            self.new_todo.press("Enter")

    def complete(self, text: str) -> None:
        """Tick the checkbox of the todo `text`."""
        self.page.get_by_label(f"Toggle {text}", exact=True).check()

    def delete(self, text: str) -> None:
        """Click the Delete button of the todo `text`."""
        self.page.get_by_role("button", name=f"Delete {text}", exact=True).click()

    def show(self, name: str) -> None:
        """Click the filter button `name`: "All", "Active" or "Completed"."""
        self.page.get_by_role("button", name=name, exact=True).click()

    def texts(self) -> list[str]:
        """Return the text of every todo shown, in order."""
        return self.items.locator("label").all_inner_texts()

    def remaining(self) -> str:
        """Return the counter text, like "2 items left"."""
        return self.count.inner_text()
