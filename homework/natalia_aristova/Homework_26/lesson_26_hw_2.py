from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest


@pytest.fixture()
def driver():
    options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver


def test_table(driver):
    driver.get('http://testshop.qa-practice.com/')
    table = driver.find_element(By.XPATH, '//*[@alt="Customizable Desk"]')
    table_name = (driver.find_element(By.XPATH, '//*[@class="text-primary text-decoration-none"]')).text
    cart = driver.find_element(By.XPATH, '//*[@class="btn btn-primary a-submit"]')
    actions = ActionChains(driver)
    actions.move_to_element(table)
    actions.click(cart)
    actions.perform()
    modal = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@class="modal-body oe_advanced_configurator_modal"]')))
    assert table_name in modal.text
