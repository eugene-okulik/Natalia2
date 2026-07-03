from playwright.sync_api import expect
from test_UI_naristova_pw.pages.base_page import BasePage
from test_UI_naristova_pw.pages.locators import cart_page_locators as loc


class Cart(BasePage):
    page_url = 'shop/cart'


    def check_empty_cart_text(self):
        text_window = self.find(loc.empty_cart_text_loc)
        assert 'Your cart is empty!' in text_window.text_content()


    def open_search_field(self):
        loupe = self.find(loc.loupe_loc)
        loupe.click(force=True)


    def get_search_input(self):
        search_field = self.find(loc.search_window_loc)
        return search_field


    def check_search_input_is_visible(self):
        self.open_search_field()
        expect(self.find(loc.search_window_loc)).to_be_visible()


    def get_breadcrumbs(self):
        return self.breadcrumbs(loc.breadcrumbs_loc)


    def check_breadcrumbs(self):
        breadcrumbs_text = self.get_breadcrumbs()
        assert 'Order' in breadcrumbs_text
        assert 'Shipping' in breadcrumbs_text
        assert 'Payment' in breadcrumbs_text


    def cart_page_title(self):
        title = self.find(loc.cart_title_loc)
        return title.text_content()
