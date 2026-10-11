# Exercise file. Fill in each function, then run: sh run-tests.sh --mine -k project
# Stuck? The worked answer is in src/solutions/project/practice.py

"""End-to-end project practice: persistence, editing, a checkout journey and accessibility
snapshots."""

from playwright.sync_api import Page, expect


def todos_survive_reload(page: Page, base_url: str) -> list[str]:
    """On todo.html add "Persist me" and "Me too", reload the page and return the todo texts."""
    raise NotImplementedError("Your turn: write this one")


def edit_todo(page: Page, base_url: str) -> list[str]:
    """On todo.html add "Typo", double-click its text, replace it with "Fixed", press Enter and
    return the todo texts."""
    raise NotImplementedError("Your turn: write this one")


def checkout_journey(page: Page, base_url: str) -> str:
    """On shop.html add the Laptop and the Mouse to the cart, click "Checkout", fill "Full name" with
    "Sunil" and "Email" with "sunil@example.com", place the order and return the confirmation."""
    raise NotImplementedError("Your turn: write this one")


def logout_journey(page: Page, base_url: str) -> str:
    """Sign in as tom / secret, click "Log out" on the account page, then open account.html again
    and return the URL you end up on (you are sent back to the login page)."""
    raise NotImplementedError("Your turn: write this one")


def languages_aria_snapshot(page: Page, base_url: str) -> str:
    """Open the home page and return the ARIA snapshot (the accessibility tree as YAML text) of the
    language list (id "langs")."""
    raise NotImplementedError("Your turn: write this one")


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
    raise NotImplementedError("Your turn: write this one")
