from selenium import webdriver

def launchBrowser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    web_driver = webdriver.Chrome(options=options)

    web_driver.get("https://www.saucedemo.com/")
    web_driver.implicitly_wait(30) 

launchBrowser()
