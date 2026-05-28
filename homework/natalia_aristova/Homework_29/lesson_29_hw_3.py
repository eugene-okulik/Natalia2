from playwright.sync_api import Page, expect, BrowserContext


def test_alert(page: Page, context: BrowserContext):
    page.goto('https://demoqa.com/dynamic-properties')
    color_change_button = page.locator('#colorChange')
    expect(color_change_button).to_have_class('mt-4 text-danger btn btn-primary', timeout=10000)
    color_change_button.click()
