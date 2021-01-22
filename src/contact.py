from selenium.webdriver.common.by import By

from src.base_page import BasePage


class Contact(BasePage):
    def go_to_dep(self):
        pass

    def go_to_add_member(self):
        pass

    def get_member_list(self):
        '''返回成员列表'''
        member_list = self.driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        name_list = []
        for i in member_list:
            name_list.append(i.text)

        return name_list

    def get_depar_list(self):
        '''返回部门列表'''
        depar_list = self.driver.find_elements(By.CSS_SELECTOR,'.jstree-anchor')
        deparname_list = []
        for i in deparname_list:
            depar_list.append(i.text)