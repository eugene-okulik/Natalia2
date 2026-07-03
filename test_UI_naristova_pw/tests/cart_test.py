def test_check_text_for_empty_cart(cart_page):
    cart_page.open_page()
    cart_page.check_empty_cart_text()


def test_search_field_exist(cart_page):
    cart_page.open_page()
    cart_page.open_search_field()
    cart_page.check_search_input_is_visible()


def test_breadcrumbs(cart_page):
    cart_page.open_page()
    cart_page.check_breadcrumbs()
