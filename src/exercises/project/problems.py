# Exercise file. Fill in each function, then run: sh run-tests.sh --mine -k project
# Stuck? The worked answer is in src/solutions/project/problems.py

"""End-to-end project: whole user journeys, plus tracing and video for debugging failures."""

from pathlib import Path

from playwright.sync_api import Browser, Page


def todo_journey(page: Page, base_url: str) -> tuple[list[str], str]:
    """On todo.html: add "Buy milk", "Write tests" and "Read docs", complete "Write tests", delete
    "Read docs", then click "Clear completed". Return the remaining todo texts and the counter."""
    raise NotImplementedError("Your turn: write this one")


def todo_filters(page: Page, base_url: str) -> tuple[list[str], list[str]]:
    """On todo.html: add "A", "B" and "C" and complete "B". Return the texts shown under the
    "Active" filter, then under the "Completed" filter."""
    raise NotImplementedError("Your turn: write this one")


def record_trace(browser: Browser, base_url: str, path: Path) -> Path:
    """In a new context, start tracing with screenshots and snapshots, sign in as tom / secret on
    login.html, then stop tracing and save it to `path` (a .zip). Return `path`.

    Open the result with: playwright show-trace <path>
    """
    raise NotImplementedError("Your turn: write this one")


def record_video(browser: Browser, base_url: str, folder: Path) -> Path:
    """Create a context that records video into `folder`, open the home page, click "Say hello",
    close the context (that writes the file) and return the video's path."""
    raise NotImplementedError("Your turn: write this one")
