from selenium import webdriver
from Util.Create_driver.driver_instance import CreateDriver
import time
class Browser_Open():
    def __init__(self, driver):
        self.driver = driver
    def SetUp(self):
        self.driver = CreateDriver().instance
        driver = webdriver.Chrome("Drivers/chromedriver.exe")
        driver.get('https://www.facebook.com')
        time.sleep(5)


    def tearDown(self):
        self.driver.close()



