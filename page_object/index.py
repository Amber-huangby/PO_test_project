from selenium.webdriver.common.by import By

from page_object.add_member import AddMember
from page_object.basepage import BasePage


class Index(BasePage):

    def go_to_add_member(self):
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_item').click()
        return AddMember(self.driver)
