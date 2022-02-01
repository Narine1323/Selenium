import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
'''from Locators.Locators import locators
from Common.CustomFindElement.CustomFindElement import CustomFindElement'''
from Pages.Common.baseClass import BaseClass


class ProductPage(BaseClass):
    def __init__(self, driver):
        BaseClass.__init__(self, driver)

    def selectedPrice(self):
        click_on_selected_price = self.custom.custom_find_element(self.locators.selected_price)
        click_on_selected_price.click

    def customer_review_click(self):
            click_on_Customer_review = self.custom.custom_find_element(self.locators.reviews)
            click_on_Customer_review.click()


    def click_on_my_choice(self):
        myChoice = self.custom.custom_find_element(self.locators.myChoice)
        myChoice.click()




