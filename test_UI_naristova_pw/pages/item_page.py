from playwright.sync_api import expect
from test_UI_naristova_pw.pages.base_page import BasePage
from test_UI_naristova_pw.pages.locators import item_page_locators as item_loc


class Item(BasePage):
    page_url = 'shop/furn-9999-office-design-software-7?category=9'

    def add_item(self):
        add_button = self.find(item_loc.plus_button)
        add_button.click()

    def remove_item(self):
        minus_button = self.find(item_loc.remove_button)
        minus_button.click()

    def assert_item_amount(self, number):
        expect(self.find(item_loc.items_amount)).to_have_value(str(number))

    def get_breadcrumbs(self):
        return self.breadcrumbs(item_loc.breadcrumbs)

    def check_breadcrumbs(self):
        breadcrumbs_text = self.get_breadcrumbs()
        expect(breadcrumbs_text).to_contain_text('All Products')
        expect(breadcrumbs_text).to_contain_text('Multimedia')
        expect(breadcrumbs_text).to_contain_text('Office Design Software')
