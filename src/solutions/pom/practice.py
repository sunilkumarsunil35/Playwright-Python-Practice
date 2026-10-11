"""Page objects practice: the shop, the products table and the widgets page."""

from playwright.sync_api import Page


class ShopPage:
    """The shop, shop.html."""

    def __init__(self, page: Page, base_url: str):
        """Keep the page and base_url, and create the locators the methods need."""
        self.page = page
        self.url = f"{base_url}/shop.html"
        self.products = page.get_by_test_id("product")
        self.cart = page.locator("#cart-count")

    def open(self) -> "ShopPage":
        """Go to the shop, wait for the products to show and return self."""
        self.page.goto(self.url)
        self.products.first.wait_for()
        return self

    def names(self) -> list[str]:
        """Return the names of all products shown."""
        return self.products.locator(".name").all_inner_texts()

    def add_to_cart(self, name: str) -> None:
        """Click "Add to cart" for the product `name`."""
        self.page.get_by_role("button", name=f"Add {name} to cart").click()

    def cart_count(self) -> int:
        """Return the number in "Cart: N" as an int."""
        return int(self.cart.inner_text().split(":")[1])

    def checkout(self, full_name: str, email: str) -> str:
        """Click "Checkout", fill "Full name" and "Email", click "Place order" and return the
        confirmation text."""
        self.page.get_by_role("button", name="Checkout").click()
        self.page.get_by_label("Full name").fill(full_name)
        self.page.get_by_label("Email").fill(email)
        self.page.get_by_role("button", name="Place order").click()
        confirmation = self.page.locator("#confirmation")
        confirmation.filter(has_text="Order confirmed").wait_for()
        return confirmation.inner_text()


class TablePage:
    """The products table, table.html."""

    def __init__(self, page: Page, base_url: str):
        """Keep the page and base_url, and create the locators the methods need."""
        self.page = page
        self.url = f"{base_url}/table.html"
        self.rows = page.locator("#products tbody tr")
        self.search_box = page.get_by_placeholder("Search products")

    def open(self) -> "TablePage":
        """Go to the table page and return self."""
        self.page.goto(self.url)
        return self

    def search(self, text: str) -> None:
        """Type `text` into the search box."""
        self.search_box.fill(text)

    def visible_names(self) -> list[str]:
        """Return the names (first column) of the rows that are visible, in order."""
        return [row.locator("td").first.inner_text() for row in self.rows.all() if row.is_visible()]

    def sort_by_price(self) -> None:
        """Click "Sort by price" once (cheapest first)."""
        self.page.get_by_role("button", name="Sort by price").click()

    def out_of_stock(self) -> list[str]:
        """Return the names of rows with the class "out-of-stock"."""
        return self.page.locator("#products tbody tr.out-of-stock td:first-child").all_inner_texts()


class WidgetsPage:
    """The widgets page, widgets.html."""

    def __init__(self, page: Page, base_url: str):
        """Keep the page and base_url, and create the locators the methods need."""
        self.page = page
        self.url = f"{base_url}/widgets.html"
        self.choices = page.locator("#choices")

    def open(self) -> "WidgetsPage":
        """Go to the widgets page and return self."""
        self.page.goto(self.url)
        return self

    def agree(self, yes: bool = True) -> None:
        """Tick (or untick when yes is False) "I agree to the terms"."""
        self.page.get_by_label("I agree to the terms").set_checked(yes)

    def choose_size(self, size: str) -> None:
        """Pick the size radio button `size`: "Small", "Medium" or "Large"."""
        self.page.get_by_label(size, exact=True).check()

    def summary(self) -> str:
        """Return the text of #choices."""
        return self.choices.inner_text()
