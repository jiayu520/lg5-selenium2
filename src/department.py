from selenium.webdriver.common.by import By

from src.base_page import BasePage
from src.contact import Contact


class Depar(BasePage):
    def add_depar(self):
        self.find(By.CSS_SELECTOR,'[name=name]').send_keys('质量保障')
        self.find(By.CSS_SELECTOR,'.js_toggle_party_list').click()
        self.find(By.CSS_SELECTOR,'.ww_dialog_body [id=1688851845822206_anchor]').click()
        self.find(By.CSS_SELECTOR,'[id=__dialog__MNDialog__] div>div>a:nth-child(1)').click()
        return Contact(self.driver)
