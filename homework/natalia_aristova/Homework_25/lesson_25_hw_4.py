from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver


def test_ruby(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    start = driver.find_element(By.CSS_SELECTOR, '#start button')
    start.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'finish')))
    finish_text = driver.find_element(By.ID, 'finish')
    assert finish_text.text == 'Hello World!'
