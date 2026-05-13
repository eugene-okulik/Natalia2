from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()
driver.get('https://demoqa.com/automation-practice-form')
first_name = driver.find_element(By.ID, 'firstName')
first_name.send_keys('Masha')
last_name = driver.find_element(By.ID, 'lastName')
last_name.send_keys('Ivanova')
email = driver.find_element(By.ID, 'userEmail')
email.send_keys('masha@test.com')
gender = driver.find_element(By.ID, 'gender-radio-2')
gender.click()
user_number = driver.find_element(By.ID, 'userNumber')
user_number.send_keys('1111111111')
date = driver.find_element(By.ID, 'dateOfBirthInput')
for _ in range(4):
    date.send_keys(Keys.BACKSPACE)
date.send_keys('1980')
date.send_keys(Keys.ENTER)
subjects = driver.find_element(By.XPATH, '//div[@id="subjectsContainer"]//input')
subjects.send_keys('Math')
subjects.send_keys(Keys.ENTER)
hobby1 = driver.find_element(By.ID, 'hobbies-checkbox-1')
hobby1.click()
hobby2 = driver.find_element(By.ID, 'hobbies-checkbox-2')
hobby2.click()
hobby3 = driver.find_element(By.ID, 'hobbies-checkbox-3')
hobby3.click()
current_address = driver.find_element(By.ID, 'currentAddress')
current_address.send_keys('Moscow')
state = driver.find_element(By.ID, 'react-select-3-input')
state.send_keys('NCR')
state.send_keys(Keys.ENTER)
city = driver.find_element(By.ID, 'react-select-4-input')
city.send_keys('Delhi')
city.send_keys(Keys.ENTER)
submit_button = driver.find_element(By.ID, 'submit')
submit_button.click()
modal_body = driver.find_element(By.CLASS_NAME, 'modal-body')
print(modal_body.text)
