from playwright.sync_api import Page, expect, Dialog


def test_alert(page: Page):
    def accept_alert(alert: Dialog):
        print(alert.message)
        alert.accept()
    page.on('dialog', accept_alert)
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.locator('//*[@href="#"]').click()
    result_text = page.locator('#result-text')
    expect(result_text).to_have_text('Ok')
