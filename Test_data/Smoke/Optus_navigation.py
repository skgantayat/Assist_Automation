from selenium import webdriver
from Util.Create_driver.driver_instance import CreateDriver
from Util.Create_driver.browser_instance import Browser_Open
from Common.homepage import Login_page
import unittest

class Login_US100(unittest.TestCase):
    def test_login_success(self):
        self.driver = CreateDriver().instance()
        self.browser = Browser_Open(self.driver)
        self.login_page = Login_page(self.driver)

        self.login_page.get_mobile_link().click()
        # self.login_page.get_username_textbox().send_keys("pyaribindu")
        # self.login_page.get_password_textbox().send_keys("Welcome@123")
        # self.login_page.get_login_button().click()

