from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from src.add_member import AddMember
from src.base_page import BasePage
from src.contact import Contact
from src.department import Depar


class MainPage(BasePage):
    def go_to_add_member(self):
        #self.driver.find_element(By.CSS_SELECTOR,"ww_indexImg_AddMember").click()
        #self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()

        self.find(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        sleep(5)
        return AddMember(self.driver)

    def go_to_contact(self):
        self.find(By.ID,'menu_contacts').click()
        return Contact(self.driver)

    def go_to_depar(self):

        self.find(By.CSS_SELECTOR, '.member_colLeft_top_addBtn').click()
        self.find(By.CSS_SELECTOR, ".js_create_party").click()
        return Depar(self.driver)
