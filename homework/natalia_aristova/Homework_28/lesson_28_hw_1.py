from playwright.sync_api import Page


def test_by_role(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    username = page.get_by_role('textbox', name='username')
    username.press_sequentially('masha', delay=500)
    password = page.get_by_role('textbox', name='password')
    password.press_sequentially('masha@text.com', delay=500)
    login_button = page.get_by_role('button')
    login_button.click()
