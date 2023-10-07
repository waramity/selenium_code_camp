from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

driver.get('https://www.saucedemo.com/')
driver.implicitly_wait(5) 

time.sleep(2)
username_field = driver.find_element(By.ID, 'user-name')
username_field.send_keys('standard_user')

time.sleep(2)
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys('secret_sauce')

time.sleep(2)
login_button = driver.find_element(By.ID, 'login-button')
login_button.click()

time.sleep(2)
add_to_cart_button = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
add_to_cart_button.click()

time.sleep(2)
cart_button = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
cart_button.click()

time.sleep(2)
checkout_button = driver.find_element(By.ID, 'checkout')
checkout_button.click()

time.sleep(2)
first_name_field = driver.find_element(By.ID, 'first-name')
first_name_field.send_keys('test')

time.sleep(2)
last_name_field = driver.find_element(By.ID, 'last-name')
last_name_field.send_keys('test2')

time.sleep(2)
postal_field = driver.find_element(By.ID, 'postal-code')
postal_field.send_keys('11111')

time.sleep(2)
continue_button = driver.find_element(By.ID, 'continue')
continue_button.click()

time.sleep(2)
finish_button = driver.find_element(By.ID, 'finish')
finish_button.click()

time.sleep(2)

driver.close()