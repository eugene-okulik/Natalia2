from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest


@pytest.fixture()
def driver():
    options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver


def test_ruby(driver):
    input_data = '2'
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    submit_button = driver.find_element(By.ID, 'submit-id-submit')
    select = driver.find_element(By.ID, 'id_choose_language')
    select.click()
    dropdown = Select(select)
    dropdown.select_by_value(input_data)
    submit_button.click()
    result = driver.find_element(By.ID, 'result-text')
    assert result.text == 'Ruby'
