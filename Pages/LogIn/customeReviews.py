import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Locators.Locators import Locators
from Common.CustomFindElement.CustomFindElement import CustomFindElement
from Pages.Common.baseClass import BaseClass

class Customers_Review_Filter(BaseClass):
    def __init__(self, driver):
        BaseClass.__init__(self, driver)

    def customer_review_click(self):
        click_on_Customer_review = self.driver.find_element(By.ID, "p_72/1248963011")
        click_on_Customer_review.click()

