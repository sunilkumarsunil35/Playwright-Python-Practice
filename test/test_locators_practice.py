import pytest

from common.target import load

P = load("locators", "practice")


def test_css_and_xpath(page, base_url):
    assert P.css_and_xpath(page, base_url) == ("Python", ".NET")


def test_first_and_last_rows(page, base_url):
    assert P.first_and_last_rows(page, base_url) == ("Laptop", "Chair")


@pytest.mark.parametrize("product, price", [("Keyboard", 49), ("Desk", 350)])
def test_price_of(page, base_url, product, price):
    assert P.price_of(page, base_url, product) == price


@pytest.mark.parametrize("plan", ["Free", "Pro", "Team"])
def test_choose_plan(page, base_url, plan):
    assert P.choose_plan(page, base_url, plan) == f"You chose {plan}"


def test_menu_link_names(page, base_url):
    assert P.menu_link_names(page, base_url) == [
        "Home", "Login", "Todo", "Widgets", "Table", "Dynamic",
        "Dialogs", "Frames", "Tabs", "Downloads", "Shop", "Emulation",
    ]


def test_logo_source(page, base_url):
    assert P.logo_source(page, base_url) == "logo.svg"
