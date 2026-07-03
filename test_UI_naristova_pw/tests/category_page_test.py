from test_UI_naristova_pw.pages.locators import category_desk_locators as cat_loc


def test_table_category_search_by_valid_text_returns_results(category_page):
    category_page.open_page()
    category_page.search_table('Cust')
    category_page.check_search_alert('Cust')


def test_steel_table_searching_returns_valid_table(category_page):
    category_page.open_page()
    category_page.click_checkbox(cat_loc.steel_checkbox)
    category_page.check_item(cat_loc.steel_table, 'Customizable Desk')


def test_selected_table_is_displayed_in_modal(category_page):
    category_page.open_page()
    category_page.add_item_to_cart()
    category_page.check_added_item()
