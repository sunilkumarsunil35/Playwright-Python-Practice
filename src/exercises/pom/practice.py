# Exercise file. Fill in each function, then run: sh run-tests.sh --mine -k pom
# Stuck? The worked answer is in src/solutions/pom/practice.py

"""Page objects practice: the shop, the products table and the widgets page."""

from playwright.sync_api import Page


class ShopPage:
    """The shop, shop.html."""

    def __init__(self, page: Page, base_url: str):
        """Keep the page and base_url, and create the locators the methods need."""
        raise NotImplementedError("Your turn: write this one")

    def open(self) -> "ShopPage":
        """Go to the shop, wait for the products to show and return self."""
        raise NotImplementedError("Your turn: write this one")

    def names(self) -> list[str]:
        """Return the names of all products shown."""
        raise NotImplementedError("Your turn: write this one")

    def add_to_cart(self, name: str) -> None:
        """Click "Add to cart" for the product `name`."""
        raise NotImplementedError("Your turn: write this one")

    def cart_count(self) -> int:
        """Return the number in "Cart: N" as an int."""
        raise NotImplementedError("Your turn: write this one")

    def checkout(self, full_name: str, email: str) -> str:
        """Click "Checkout", fill "Full name" and "Email", click "Place order" and return the
        confirmation text."""
        raise NotImplementedError("Your turn: write this one")


class TablePage:
    """The products table, table.html."""

    def __init__(self, page: Page, base_url: str):
        """Keep the page and base_url, and create the locators the methods need."""
        raise NotImplementedError("Your turn: write this one")

    def open(self) -> "TablePage":
        """Go to the table page and return self."""
        raise NotImplementedError("Your turn: write this one")

    def search(self, text: str) -> None:
        """Type `text` into the search box."""
        raise NotImplementedError("Your turn: write this one")

    def visible_names(self) -> list[str]:
        """Return the names (first column) of the rows that are visible, in order."""
        raise NotImplementedError("Your turn: write this one")

    def sort_by_price(self) -> None:
        """Click "Sort by price" once (cheapest first)."""
        raise NotImplementedError("Your turn: write this one")

    def out_of_stock(self) -> list[str]:
        """Return the names of rows with the class "out-of-stock"."""
        raise NotImplementedError("Your turn: write this one")


class WidgetsPage:
    """The widgets page, widgets.html."""

    def __init__(self, page: Page, base_url: str):
        """Keep the page and base_url, and create the locators the methods need."""
        raise NotImplementedError("Your turn: write this one")

    def open(self) -> "WidgetsPage":
        """Go to the widgets page and return self."""
        raise NotImplementedError("Your turn: write this one")

    def agree(self, yes: bool = True) -> None:
        """Tick (or untick when yes is False) "I agree to the terms"."""
        raise NotImplementedError("Your turn: write this one")

    def choose_size(self, size: str) -> None:
        """Pick the size radio button `size`: "Small", "Medium" or "Large"."""
        raise NotImplementedError("Your turn: write this one")

    def summary(self) -> str:
        """Return the text of #choices."""
        raise NotImplementedError("Your turn: write this one")
