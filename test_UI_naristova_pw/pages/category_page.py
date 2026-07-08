from playwright.sync_api import expect
from test_UI_naristova_pw.pages.base_page import BasePage
from test_UI_naristova_pw.pages.locators import category_desk_locators as cat_loc


class Category(BasePage):
    page_url = 'shop/category/desks-1'

    def search_table(self, text):
        self.search(cat_loc.search_field, text)

    def check_search_alert(self, text):
        found_item = self.find(cat_loc.found_table).first
        expect(found_item).to_contain_text(text)

    def click_checkbox(self, locator):
        checkbox = self.find(locator)
        checkbox.click()

    def check_item(self, locator, text):
        found_item = self.find(locator).first
        expect(found_item).to_have_text(text)

    def add_item_to_cart(self):
        cart = self.find(cat_loc.cart).first
        table = self.find(cat_loc.table)
        table.hover()
        cart.click()

    def check_added_item(self):
        table_name = self.find(cat_loc.table_name).first
        modal = self.find(cat_loc.modal)
        table_name_text = table_name.text_content()
        expect(modal).to_contain_text(table_name_text)
