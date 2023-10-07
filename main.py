from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.saucedemo.com/")
# driver.implicitly_wait(3) 

# login_button = driver.find_element_by_id('login-button')
login_button = driver.find_element("id", 'login-button')
login_button.click()

time.sleep(2)

driver.close()