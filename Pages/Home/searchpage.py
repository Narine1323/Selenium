import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Pages.Common.baseClass import BaseClass

class SearchPage(BaseClass):
    def __init__(self, driver):
        BaseClass.__init__(self, driver)

    def search_field(self):
        search_field = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_field.send_keys("jenga")
        search_field.send_keys(Keys.ENTER)