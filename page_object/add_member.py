from selenium.webdriver.common.by import By

from page_object.basepage import BasePage


class AddMember(BasePage):
    def add_member_mesg(self):
        self.driver.find_element(By.CSS_SELECTOR, '#username').send_keys('aa')
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys('aa')
        self.driver.find_element(By.CSS_SELECTOR, '[name=mobile]').send_keys(12345678912)
        self.driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()

    def get_first_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#member_list tr:nth-child(1) td:nth-child(2)').get_attribute(
            'title')
