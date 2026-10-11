import pytest

from common.target import load

P = load("pom", "practice")


@pytest.fixture
def shop(page, base_url):
    return P.ShopPage(page, base_url).open()


@pytest.fixture
def table(page, base_url):
    return P.TablePage(page, base_url).open()


@pytest.fixture
def widgets(page, base_url):
    return P.WidgetsPage(page, base_url).open()


def test_shop_names(shop):
    assert shop.names() == ["Laptop", "Keyboard", "Mouse", "Monitor"]


def test_shop_cart_and_checkout(shop):
    shop.add_to_cart("Mouse")
    shop.add_to_cart("Keyboard")
    assert shop.cart_count() == 2
    assert shop.checkout("Sunil", "sunil@example.com") == "Order confirmed for Sunil (2 items)"


@pytest.mark.parametrize("query, names", [("Furniture", ["Desk", "Chair"]), ("mon", ["Monitor"]), ("zzz", [])])
def test_table_search(table, query, names):
    table.search(query)
    assert table.visible_names() == names


def test_table_sort_and_stock(table):
    table.sort_by_price()
    assert table.visible_names() == ["Mouse", "Keyboard", "Chair", "Monitor", "Desk", "Laptop"]
    assert table.out_of_stock() == ["Chair"]


def test_widgets(widgets):
    widgets.agree()
    widgets.choose_size("Small")
    assert widgets.summary() == "Agreed: yes | Size: Small"
    widgets.agree(False)
    assert widgets.summary() == "Agreed: no | Size: Small"
