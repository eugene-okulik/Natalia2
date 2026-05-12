from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()
driver.get('https://www.qa-practice.com/elements/input/simple')
search_input = driver.find_element(By.NAME, 'text_string')
search_input.send_keys('cat')
search_input.submit()
search_result_text = driver.find_element(By.ID, 'result-text')
print(search_result_text.text)
