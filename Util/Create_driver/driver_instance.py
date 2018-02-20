import json
from selenium import webdriver

class CreateDriver():
    def instance(self):
        data = json.load(open('Config/config.json'))
        browser_info = data['browser']
        url = data['url']
        if browser_info =='firefox':
            driver = webdriver.Firefox()
        elif browser_info == 'chrome':
            chrome_path = 'Drivers/chromedriver.exe'
            driver = webdriver.Chrome(chrome_path)
        # driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get(url)
        return driver