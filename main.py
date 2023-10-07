from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

driver.get('https://www.saucedemo.com/')
driver.implicitly_wait(5) 

user_name_field = driver.find_element('id', 'user-name')
user_name_field.send_keys("kuy")

password_field = driver.find_element('id', 'password')
password_field.send_keys("sus")

# login_button = driver.find_element_by_id('login-button')
login_button = driver.find_element('id', 'login-button')
login_button.click()


time.sleep(2)

driver.close()