from playwright.sync_api import Page, expect, Route
import json


def test_change_request(page: Page):

    def handle_iphone_name(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = 'яблокофон 17 про'
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )

    page.route('**/shop/api/digital-mat?path=library/step0_iphone/digitalmat&fae=true**', handle_iphone_name)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.get_by_role('heading', name='iPhone 17 Pro & iPhone 17 Pro Max').click()
    iphone_header = page.locator('//*[@data-autom="DigitalMat-overlay-header-0-0"]')
    expect(iphone_header).to_have_text('яблокофон 17 про')
