from playwright.sync_api import Page


def test_by_role(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.get_by_placeholder('First Name').fill('Masha')
    page.get_by_placeholder('Last Name').fill('Ivanova')
    page.get_by_placeholder('name@example.com').fill('ivanova@test.com')
    page.locator('//*[@id="gender-radio-2"]').click()
    page.get_by_placeholder('Mobile Number').fill('1111111111')
    calendar = page.locator('//*[@id="dateOfBirthInput"]')
    calendar.click()
    for _ in range(4):
        calendar.press('Backspace')
    calendar.press_sequentially('1980', delay=500)
    calendar.press('Enter')
    subjects = page.locator('//div[@id="subjectsContainer"]//input')
    subjects.fill('Math')
    subjects.press('Enter')
    page.locator('//*[@id="hobbies-checkbox-1"]').click()
    page.locator('//*[@id="currentAddress"]').fill('Moscow')
    state = page.locator('//*[@id="react-select-3-input"]')
    state.fill('NCR')
    state.press('Enter')
    city = page.locator('//*[@id="react-select-4-input"]')
    city.fill('Delhi')
    city.press('Enter')
    page.get_by_role('button', name='Submit').click()
