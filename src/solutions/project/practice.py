"""End-to-end project practice: persistence, editing, a checkout journey and accessibility
snapshots."""

from playwright.sync_api import Page, expect


def todos_survive_reload(page: Page, base_url: str) -> list[str]:
    """On todo.html add "Persist me" and "Me too", reload the page and return the todo texts."""
    page.goto(f"{base_url}/todo.html")
    box = page.get_by_placeholder("What needs to be done?")
    for text in ["Persist me", "Me too"]:
        box.fill(text)
        box.press("Enter")
    page.reload()
    return page.get_by_test_id("todo-item").locator("label").all_inner_texts()


def edit_todo(page: Page, base_url: str) -> list[str]:
    """On todo.html add "Typo", double-click its text, replace it with "Fixed", press Enter and
    return the todo texts."""
    page.goto(f"{base_url}/todo.html")
    box = page.get_by_placeholder("What needs to be done?")
    box.fill("Typo")
    box.press("Enter")
    page.get_by_test_id("todo-item").get_by_text("Typo").dblclick()
    edit = page.get_by_label("Edit Typo")
    edit.fill("Fixed")
    edit.press("Enter")
    return page.get_by_test_id("todo-item").locator("label").all_inner_texts()


def checkout_journey(page: Page, base_url: str) -> str:
    """On shop.html add the Laptop and the Mouse to the cart, click "Checkout", fill "Full name" with
    "Sunil" and "Email" with "sunil@example.com", place the order and return the confirmation."""
    page.goto(f"{base_url}/shop.html")
    page.get_by_role("button", name="Add Laptop to cart").click()
    page.get_by_role("button", name="Add Mouse to cart").click()
    page.get_by_role("button", name="Checkout").click()
    page.get_by_label("Full name").fill("Sunil")
    page.get_by_label("Email").fill("sunil@example.com")
    page.get_by_role("button", name="Place order").click()
    confirmation = page.locator("#confirmation")
    expect(confirmation).to_contain_text("Order confirmed")
    return confirmation.inner_text()


def logout_journey(page: Page, base_url: str) -> str:
    """Sign in as tom / secret, click "Log out" on the account page, then open account.html again
    and return the URL you end up on (you are sent back to the login page)."""
    page.goto(f"{base_url}/login.html")
    page.get_by_label("Username").fill("tom")
    page.get_by_label("Password").fill("secret")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_role("button", name="Log out").click()
    page.wait_for_url("**/login.html")
    page.goto(f"{base_url}/account.html")
    page.wait_for_url("**/login.html*")
    return page.url


def languages_aria_snapshot(page: Page, base_url: str) -> str:
    """Open the home page and return the ARIA snapshot (the accessibility tree as YAML text) of the
    language list (id "langs")."""
    page.goto(f"{base_url}/index.html")
    return page.locator("#langs").aria_snapshot()


def check_aria_snapshot(page: Page, base_url: str) -> None:
    """Open the home page and assert the "Pricing" section matches this ARIA snapshot. A snapshot
    template may leave things out (here, the prices), but what it lists must appear in this order:

        - heading "Pricing" [level=2]
        - article:
          - heading "Free" [level=3]
          - button "Choose"
        - article:
          - heading "Pro" [level=3]
          - button "Choose"
        - article:
          - heading "Team" [level=3]
          - button "Choose"
    """
    page.goto(f"{base_url}/index.html")
    expect(page.get_by_role("region", name="Pricing")).to_match_aria_snapshot(
        """
        - heading "Pricing" [level=2]
        - article:
          - heading "Free" [level=3]
          - button "Choose"
        - article:
          - heading "Pro" [level=3]
          - button "Choose"
        - article:
          - heading "Team" [level=3]
          - button "Choose"
        """
    )
