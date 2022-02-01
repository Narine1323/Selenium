import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Pages.Common.baseClass import BaseClass

class ProductDetails(BaseClass):
    def __init__ (self, driver):
        BaseClass.__init__(self, driver)

    def select_quantity_of_product(self):
        select_quantity_of_my_product = self.custom.custom_find_element(self.locators.select_quantity)
        select_quantity_of_my_product.click()

    def click_on_selected_quantity(self):
        click_on_selected_quantity_of_the_product = self.custom.custom_find_element(self.locators.selected_quantity)
        click_on_selected_quantity_of_the_product.click()



