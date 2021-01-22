from selenium.webdriver.common.by import By

from src.base_page import BasePage
from src.contact import Contact


class AddMember(BasePage):
    def add_member(self):
        '''输入成员信息，点击保存'''
        self.find(By.ID,"username").send_keys('皮4')
        self.find(By.ID,"memberAdd_acctid").send_keys('71899973')
        self.find(By.CSS_SELECTOR,".ww_telInput_mainNumber").send_keys('13959245677')
        self.find(By.CSS_SELECTOR,".js_btn_save").click()
        return Contact(self.driver)
