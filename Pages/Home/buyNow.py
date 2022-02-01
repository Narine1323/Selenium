import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Pages.Common.baseClass import BaseClass

class Buy_Now(BaseClass):
    def __init__ (self, driver):
        BaseClass.__init__(self, driver)

    def click_on_buy_now_button(self):
        buy_now = self.custom.custom_find_element(self.locators.buy_now)
        buy_now.click()
