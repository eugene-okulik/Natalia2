from playwright.sync_api import BrowserContext
from test_UI_naristova_pw.pages.cart_page import Cart
from test_UI_naristova_pw.pages.category_page import Category
from test_UI_naristova_pw.pages.item_page import Item
import pytest


@pytest.fixture()
def cart_page(page):
    return Cart(page)


@pytest.fixture()
def category_page(page):
    return Category(page)


@pytest.fixture()
def item_page(page):
    return Item(page)


@pytest.fixture()
def page(context: BrowserContext):
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page
