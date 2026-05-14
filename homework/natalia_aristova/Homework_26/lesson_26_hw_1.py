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
    ActionChains(driver).key_down(Keys.CONTROL).click(table).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    add_to_cart = driver.find_element(By.ID, 'add_to_cart')
    add_to_cart.click()
    continue_shopping = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[text()="Continue Shopping"]')))
    continue_shopping.click()
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@class="col-6 d-flex flex-column align-items-start"]')))
    driver.close()
    driver.switch_to.window(tabs[0])
    basket = driver.find_element(By.XPATH, '//*[@class="fa fa-shopping-cart fa-stack"]')
    basket.click()
    item = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@class="d-inline align-top h6 fw-bold"]')))
    assert item.text == 'Customizable Desk (Steel, White)'
