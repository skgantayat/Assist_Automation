from selenium import webdriver
from Util.Create_driver import browser_instance
from Util.Create_driver import driver_instance
import unittest
import time


class Login_page():
    def __init__(self, driver):
        self.driver = driver

    def get_mobile_link(self):
        try:
            return self.driver.find_element_by_xpath("html/body/div[1]/div[2]/header/div/div[1]/div[2]/div/div[1]/ul/li[1]/a")

        except:
            return None
    # def get_password_textbox(self):
    #     try:
    #         return self.driver.find_element_by_id('pass')
    #     except:
    #         return None
    #
    # def get_login_button(self):
    #     try:
    #         return self.driver.find_element_by_xpath('//*[@id="u_0_3"]')
    #     except:
    #         return None
