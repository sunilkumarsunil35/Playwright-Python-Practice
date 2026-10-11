"""Locators practice: CSS and XPath, nth/first/last, filtering, chaining and lists."""

from playwright.sync_api import Page


def css_and_xpath(page: Page, base_url: str) -> tuple[str, str]:
    """Open the home page. Return the first language in the list with id "langs" found with a CSS
    selector, and the last one found with an XPath selector, as a tuple."""
    page.goto(f"{base_url}/index.html")
    first = page.locator("#langs li").first.inner_text()
    last = page.locator("xpath=//ul[@id='langs']/li[last()]").inner_text()
    return first, last


def first_and_last_rows(page: Page, base_url: str) -> tuple[str, str]:
    """Open table.html and return the product names in the first and last body rows."""
    page.goto(f"{base_url}/table.html")
    rows = page.locator("#products tbody tr")
    return rows.first.locator("td").first.inner_text(), rows.last.locator("td").first.inner_text()


def price_of(page: Page, base_url: str, product: str) -> int:
    """Open table.html and return the price (third column) of the row that contains `product`."""
    # filter(has_text=...) narrows a list of rows; nth(2) picks the third cell (0-based).
    page.goto(f"{base_url}/table.html")
    row = page.locator("#products tbody tr").filter(has_text=product)
    return int(row.locator("td").nth(2).inner_text())


def choose_plan(page: Page, base_url: str, plan: str) -> str:
    """Open the home page, click "Choose" inside the pricing card whose heading is `plan` and
    return the text of the paragraph with id "plan"."""
    # Chain: first find the card, then the button inside it. Every card has a "Choose" button.
    page.goto(f"{base_url}/index.html")
    card = page.locator("article.card").filter(has=page.get_by_role("heading", name=plan))
    card.get_by_role("button", name="Choose").click()
    return page.locator("#plan").inner_text()


def menu_link_names(page: Page, base_url: str) -> list[str]:
    """Open the home page and return the text of every link in the main menu, in order."""
    page.goto(f"{base_url}/index.html")
    return page.get_by_role("navigation", name="Main").get_by_role("link").all_inner_texts()


def logo_source(page: Page, base_url: str) -> str:
    """Open the home page and return the src attribute of the image whose alt text is
    "Playwright Practice logo"."""
    page.goto(f"{base_url}/index.html")
    return page.get_by_alt_text("Playwright Practice logo").get_attribute("src")
