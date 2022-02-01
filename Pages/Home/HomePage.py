import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
'''from Locators.Locators import locators
from Common.CustomFindElement.CustomFindElement import CustomFindElement'''
from Pages.Common.baseClass import BaseClass

class HomePage(BaseClass):
    def __init__(self, driver):
        BaseClass.__init__(self, driver)

    def search_field(self):
        search_field = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_field.send_keys("jenga")
        search_field.send_keys(Keys.ENTER)


    def selectedPrice(self):
        click_on_selected_price = self.custom.custom_find_element(self.locators.selected_price)
        click_on_selected_price.click

    def customer_review_click(self):
            click_on_Customer_review = self.custom.custom_find_element(self.locators.reviews)
            click_on_Customer_review.click()


    def click_on_my_choice(self):
        myChoice = self.custom.custom_find_element(self.locators.myChoice)
        myChoice.click()



    def click_on_selected_quantity(self):
        click_on_selected_quantity_of_the_product = self.custom.custom_find_element(self.locators.selected_quantity)
        click_on_selected_quantity_of_the_product.click()

    def click_on_add_to_cart_button(self):
        add_to_cart = self.custom.custom_find_element(self.locators.add_to_cart_button)
        add_to_cart.click()

    #def click_on_buy_now_button(self):
        #buy_now = self.custom.custom_find_element(self.locators.buy_now_button)
        #buy_now.click()











