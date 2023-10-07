import time
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# options = webdriver.ChromeOptions()

# options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
# driver.get("https://www.saucedemo.com/")
# driver=webdriver.Chrome(executable_path=chrome_driver_path,options=options)

def launchBrowser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    # chrome_options = Options()
    # chrome_options.binary_location="../Google Chrome"
    # chrome_options.add_argument("disable-infobars");
    # driver = webdriver.Chrome(chrome_options=chrome_options)
    driver=webdriver.Chrome(options=options)

    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(30)
    time.sleep(10)
    while(True):
        pass
launchBrowser()
