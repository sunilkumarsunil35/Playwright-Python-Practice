# Exercise file. Fill in each function, then run: sh run-tests.sh --mine -k assertions
# Stuck? The worked answer is in src/solutions/assertions/practice.py

"""Assertions practice: attributes, classes, partial text, lists of texts, values, negation and
reading a failure message."""

import re

from playwright.sync_api import Page, expect


def check_attribute_and_class(page: Page, base_url: str) -> None:
    """Open the home page. Assert the status badge (id "status") has the attribute
    data-state="ok" and has the class "online"."""
    raise NotImplementedError("Your turn: write this one")


def check_contains_text(page: Page, base_url: str) -> None:
    """Open the home page and assert the <h1> contains the word "practice" (any case)."""
    raise NotImplementedError("Your turn: write this one")


def check_list_of_texts(page: Page, base_url: str) -> None:
    """Open the home page and assert the language list items are exactly, in order:
    Python, JavaScript, Java, .NET."""
    raise NotImplementedError("Your turn: write this one")


def check_input_value(page: Page, base_url: str) -> None:
    """Open widgets.html. Assert the "Volume" slider's value is "50" and the "Bio" box's value is
    "I like Java."."""
    raise NotImplementedError("Your turn: write this one")


def check_not(page: Page, base_url: str) -> None:
    """Open the home page. Assert the greeting (id "greeting") does NOT have the text
    "Hello, Playwright!" yet, click "Say hello", then assert that it does."""
    raise NotImplementedError("Your turn: write this one")


def failure_message(page: Page, base_url: str) -> str:
    """Open the home page and assert the <h1> has the text "Wrong heading", with a 500 ms timeout.
    It fails. Catch the AssertionError and return its message, so you learn to read one."""
    raise NotImplementedError("Your turn: write this one")
