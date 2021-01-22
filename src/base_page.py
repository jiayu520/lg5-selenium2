import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage():
    def __init__(self,base_driver:webdriver=None):
        if base_driver == None:
            self.driver = webdriver.Chrome()
            self._cookie()
        else:
            self.driver = base_driver
            # self._cookie()
        self.driver.implicitly_wait(3)

    def _cookie(self):
        self.driver.get("https://work.weixin.qq.com/")
        with open('../test_case/cookie.json', 'r') as f:
            cookies = json.load(f)
            # print(cookies)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        sleep(5)
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
    def find(self,selector,path):
        return self.driver.find_element(selector,path)
